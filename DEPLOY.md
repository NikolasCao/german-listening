# 德语听力生成器 — 免费部署到 Render 完整指南

## 概览

| 项目 | 说明 |
|------|------|
| 平台 | Render.com（免费版） |
| 费用 | 0 元 |
| 访问地址 | https://你的应用名.onrender.com |
| 限制 | 15分钟无访问会休眠，下次访问需等待约30秒唤醒 |
| 解决休眠 | 配合 UptimeRobot 免费保活（见第5步） |

---

## 第1步：注册 GitHub 账号（已有可跳过）

1. 打开 https://github.com/signup
2. 填写用户名、邮箱、密码
3. 验证邮箱

---

## 第2步：上传代码到 GitHub

### 方法A：网页上传（简单，推荐非技术用户）

1. 打开 https://github.com/new
2. Repository name 填 `german-listening`
3. 选择 **Public**
4. 点击 **Create repository**
5. 在新页面点击 **uploading an existing file**
6. 打开项目文件夹 `C:\Users\18767\WorkBuddy\2026-07-08-11-17-54`
7. 将以下文件/文件夹拖入上传区域：

   ```
   backend/        （整个文件夹）
   static/         （整个文件夹）
   .env.example
   .gitignore
   Dockerfile
   Procfile
   render.yaml
   requirements.txt
   runtime.txt
   start.bat
   ```

   > 注意：不要上传 `.env`（含密钥）、`output/`（音频文件）、`.workbuddy/`

8. 点击 **Commit changes**

### 方法B：Git 命令推送（技术用户）

```bash
cd C:\Users\18767\WorkBuddy\2026-07-08-11-17-54

# 已初始化 git，直接添加远程并推送
git remote add origin https://github.com/你的用户名/german-listening.git
git branch -M main
git push -u origin main
```

---

## 第3步：注册 Render 账号

1. 打开 https://render.com
2. 点击 **Get Started** 或 **Sign Up**
3. 选择 **Sign up with GitHub**（用 GitHub 账号直接登录）
4. 授权 Render 访问你的 GitHub

---

## 第4步：部署应用

1. 登录 Render 后，点击右上角 **New +** → **Web Service**

2. 找到 `german-listening` 仓库，点击 **Connect**

3. 填写配置：
   - **Name**: `german-listening`（或任意名称）
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python -m backend.main`
   - **Instance Type**: `Free`

4. 点击 **Create Web Service**

5. 等待 2-3 分钟，Render 会自动安装依赖并启动

6. 部署完成后，页面顶部会显示你的公网地址：
   ```
   https://german-listening.onrender.com
   ```

7. 点击地址即可访问！任何人都能用这个链接。

---

## 第5步：配置 UptimeRobot 保活（重要！）

> 没有这一步，15分钟没人用就会休眠，下次访问要等30秒。

1. 打开 https://uptimerobot.com
2. 注册免费账号
3. 点击 **Add New Monitor**
4. 配置：
   - **Monitor Type**: HTTP(s)
   - **Friendly Name**: `German Listening`
   - **URL**: `https://german-listening.onrender.com/api/status`
   - **Monitoring Interval**: `5 minutes`

5. 点击 **Create Monitor**

从此 UptimeRobot 每5分钟访问一次你的应用，保持它永不休眠。

---

## 第6步（可选）：配置 LLM API Key

配了 Key 之后可以动态生成任意主题的听力内容，不配则用内置18套Demo。

### 在 Render 上配置：

1. 进入你的 Web Service 页面
2. 点击左侧 **Environment**
3. 添加环境变量：

   | Key | Value |
   |-----|-------|
   | LLM_API_KEY | sk-你的密钥 |
   | LLM_BASE_URL | https://api.deepseek.com/v1 |
   | LLM_MODEL | deepseek-chat |

4. 点击 **Save Changes**，Render 会自动重新部署

> 推荐用 DeepSeek API（便宜，中文理解好）：https://platform.deepseek.com

---

## 验证清单

部署完成后检查：
- [ ] 打开 `https://你的应用名.onrender.com` 能看到海洋主题页面
- [ ] 选择 A1 + 选择题 + Begrüßung，点击生成，能听到音频
- [ ] 音频完整播放（不会3-4秒就停）
- [ ] 老师模式能看到原文+答案
- [ ] 学生模式有"对答案"按钮
- [ ] UptimeRobot 显示状态为 Up

---

## 常见问题

**Q: 部署失败怎么办？**
A: 检查 Render 的 Logs 页面，最常见原因是 requirements.txt 缺少依赖。

**Q: 首次访问很慢？**
A: 正常，Render 免费版冷启动需要30秒左右。配了 UptimeRobot 后就不会再冷启动。

**Q: 音频生成失败？**
A: edge-tts 需要访问微软服务器，Render 的网络环境支持。如果偶尔失败，重试即可。

**Q: 能绑定自己的域名吗？**
A: Render 免费版不支持自定义域名。需要域名的话升级到付费版（$7/月）或用其他方案。
