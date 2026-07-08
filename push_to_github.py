"""通过 GitHub API 上传所有项目文件（绕过 git push 网络问题）"""
import json
import os
import base64
import urllib.request
import urllib.error

TOKEN = os.environ["GH_TOKEN"]
OWNER = "NikolasCao"
REPO = "german-listening"
API = f"https://api.github.com/repos/{OWNER}/{REPO}"
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json",
    "Content-Type": "application/json",
}

# 要上传的文件列表（相对于项目根目录）
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def get_files_to_upload():
    """收集所有需要上传的文件"""
    files = []
    skip_dirs = {".git", ".workbuddy", "output", "__pycache__", "temp"}
    skip_files = {".env", "test_fix.py", "check_format.py"}
    
    for root, dirs, filenames in os.walk(BASE_DIR):
        # 过滤目录
        dirs[:] = [d for d in dirs if d not in skip_dirs]
        for fname in filenames:
            if fname in skip_files:
                continue
            if fname.endswith(".pyc"):
                continue
            fpath = os.path.join(root, fname)
            relpath = os.path.relpath(fpath, BASE_DIR).replace("\\", "/")
            files.append((relpath, fpath))
    
    return sorted(files)

def api_request(url, data=None, method="GET"):
    """发送 GitHub API 请求"""
    body = json.dumps(data).encode() if data else None
    req = urllib.request.Request(url, data=body, headers=HEADERS, method=method)
    try:
        resp = urllib.request.urlopen(req)
        return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        err_body = e.read().decode()
        print(f"  API Error {e.code}: {err_body[:200]}")
        raise

def create_blob(filepath):
    """上传文件内容为 Git blob，返回 blob SHA"""
    with open(filepath, "rb") as f:
        content = base64.b64encode(f.read()).decode()
    result = api_request(f"{API}/git/blobs", {"content": content, "encoding": "base64"}, "POST")
    return result["sha"]

def main():
    files = get_files_to_upload()
    print(f"Found {len(files)} files to upload:")
    for relpath, _ in files:
        print(f"  {relpath}")
    print()
    
    # 1. 获取当前 HEAD commit (如果仓库为空则跳过)
    try:
        ref = api_request(f"{API}/git/refs/heads/main")
        parent_sha = ref["object"]["sha"]
        print(f"Parent commit: {parent_sha}")
        # 获取 parent commit 的 tree
        parent_commit = api_request(f"{API}/git/commits/{parent_sha}")
        base_tree = parent_commit["tree"]["sha"]
    except urllib.error.HTTPError:
        print("Repo is empty, creating first commit")
        parent_sha = None
        base_tree = None
    
    # 2. 为每个文件创建 blob
    tree_items = []
    for i, (relpath, fpath) in enumerate(files):
        print(f"  [{i+1}/{len(files)}] Creating blob: {relpath}", end=" ... ")
        blob_sha = create_blob(fpath)
        print(f"OK ({blob_sha[:8]})")
        tree_items.append({
            "path": relpath,
            "mode": "100644",
            "type": "blob",
            "sha": blob_sha,
        })
    
    # 3. 创建 tree
    print("\nCreating tree...")
    tree_data = {"tree": tree_items}
    if base_tree:
        tree_data["base_tree"] = base_tree
    tree = api_request(f"{API}/git/trees", tree_data, "POST")
    tree_sha = tree["sha"]
    print(f"Tree created: {tree_sha}")
    
    # 4. 创建 commit
    print("Creating commit...")
    commit_data = {
        "message": "德语听力生成器 - 完整版本\n\n- 德语TTS引擎 (edge-tts, 10个德语神经语音)\n- 多角色音频合成 (MP3拼接)\n- 内容生成 (LLM API + 18套CEFR分级Demo)\n- 海洋主题前端 (老师/学生双模式)\n- 云部署配置 (Render/Docker)",
        "tree": tree_sha,
    }
    if parent_sha:
        commit_data["parents"] = [parent_sha]
    commit = api_request(f"{API}/git/commits", commit_data, "POST")
    commit_sha = commit["sha"]
    print(f"Commit created: {commit_sha}")
    
    # 5. 更新 ref
    print("Updating main branch...")
    api_request(f"{API}/git/refs/heads/main", {"sha": commit_sha, "force": True}, "PATCH")
    
    print(f"\n✅ All done! Repo: https://github.com/{OWNER}/{REPO}")

if __name__ == "__main__":
    main()
