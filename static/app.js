/**
 * 德语听力生成器 —— 前端交互逻辑
 */

// ==================== 状态管理 ====================
const state = {
    identity: "student",
    difficulty: "A1",
    questionType: "选择题",
    theme: "",
};

// ==================== DOM 元素 ====================
const $ = (sel) => document.querySelector(sel);
const $$ = (sel) => document.querySelectorAll(sel);

// ==================== 初始化按钮组 ====================
function initButtonGroups() {
    // 身份切换
    $$("#identity-group .toggle-btn").forEach((btn) => {
        btn.addEventListener("click", () => {
            $$("#identity-group .toggle-btn").forEach((b) => b.classList.remove("active"));
            btn.classList.add("active");
            state.identity = btn.dataset.value;
        });
    });

    // 难度切换
    $$("#difficulty-group .pill-btn").forEach((btn) => {
        btn.addEventListener("click", () => {
            $$("#difficulty-group .pill-btn").forEach((b) => b.classList.remove("active"));
            btn.classList.add("active");
            state.difficulty = btn.dataset.value;
        });
    });

    // 题型切换
    $$("#qtype-group .pill-btn").forEach((btn) => {
        btn.addEventListener("click", () => {
            $$("#qtype-group .pill-btn").forEach((b) => b.classList.remove("active"));
            btn.classList.add("active");
            state.questionType = btn.dataset.value;
        });
    });
}

// ==================== 生成请求 ====================
async function generate() {
    const theme = $("#theme-input").value.trim() || "Begrüßung";
    state.theme = theme;

    // 显示加载
    $("#loading").style.display = "block";
    $("#error-card").style.display = "none";
    $("#results").style.display = "none";
    $("#generate-btn").disabled = true;
    $("#generate-btn .btn-text").textContent = "生成中...";

    // 更新加载提示
    const loadingTexts = [
        "正在生成德语听力原文...",
        "正在合成德语语音...",
        "正在拼接多角色音频...",
        "即将完成...",
    ];
    let textIdx = 0;
    const loadingInterval = setInterval(() => {
        if (textIdx < loadingTexts.length) {
            $("#loading-text").textContent = loadingTexts[textIdx];
            textIdx++;
        }
    }, 2000);

    try {
        const response = await fetch("/api/generate", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                identity: state.identity,
                difficulty: state.difficulty,
                question_type: state.questionType,
                theme: theme,
            }),
        });

        const data = await response.json();

        if (!response.ok || !data.success) {
            throw new Error(data.error || "生成失败，请重试");
        }

        displayResults(data);
    } catch (err) {
        showError(err.message);
    } finally {
        clearInterval(loadingInterval);
        $("#loading").style.display = "none";
        $("#generate-btn").disabled = false;
        $("#generate-btn .btn-text").textContent = "生成听力练习";
    }
}

// ==================== 显示结果 ====================
function displayResults(data) {
    const content = data.content;
    const isTeacher = data.identity === "teacher";

    // 元信息
    const sourceLabel = data.source === "demo" ? "Demo 内容" : "AI 生成";
    $("#result-meta").innerHTML = `
        <strong>${content.title}</strong>
        &nbsp;·&nbsp; ${data.difficulty} · ${data.question_type} · ${data.theme}
        &nbsp;·&nbsp; ${sourceLabel}
    `;

    // 音频
    if (data.audio_url) {
        $("#audio-player").src = data.audio_url;
        $("#audio-card").style.display = "block";

        // 声线信息
        const voiceMap = data.voice_map || {};
        const voiceTags = Object.entries(voiceMap)
            .map(([speaker, voice]) => `<span class="voice-tag">${speaker} → ${voice}</span>`)
            .join("");
        $("#voice-info").innerHTML = voiceTags ? `声线分配：${voiceTags}` : "";
    } else {
        $("#audio-card").style.display = "none";
    }

    // 题目
    $("#questions-content").innerHTML = renderQuestions(content.questions);

    // 听力原文
    $("#transcript-content").innerHTML = renderTranscript(content.text_segments, content.text_type);

    // 答案
    $("#answers-content").innerHTML = renderAnswers(content.questions);

    // 老师模式：直接显示所有内容
    // 学生模式：隐藏原文和答案，显示"对答案"按钮
    if (isTeacher) {
        $("#reveal-section").style.display = "none";
        $("#transcript-card").classList.add("revealed");
        $("#answers-card").classList.add("revealed");
    } else {
        $("#reveal-section").style.display = "block";
        $("#transcript-card").classList.remove("revealed");
        $("#answers-card").classList.remove("revealed");
    }

    // 重置对答案按钮
    const revealBtn = $("#reveal-btn");
    revealBtn.style.display = isTeacher ? "none" : "inline-flex";
    revealBtn.onclick = revealAnswers;

    // 显示结果区
    $("#results").style.display = "block";

    // 绑定复制按钮
    initCopyButtons();

    // 滚动到结果
    setTimeout(() => {
        $("#results").scrollIntoView({ behavior: "smooth", block: "start" });
    }, 100);
}

// ==================== 渲染题目 ====================
function renderQuestions(questions) {
    if (!questions || questions.length === 0) return "<p>暂无题目</p>";

    return questions
        .map((q) => {
            let html = `<div class="question-item">`;
            html += `<span class="question-num">${q.id}.</span>`;
            html += `<span class="question-text">${escapeHtml(q.question)}</span>`;

            if (q.type === "multiple_choice" && q.options) {
                html += `<div class="question-options">`;
                q.options.forEach((opt) => {
                    html += `<div class="question-option">${escapeHtml(opt)}</div>`;
                });
                html += `</div>`;
            }

            html += `</div>`;
            return html;
        })
        .join("");
}

// ==================== 渲染听力原文 ====================
function renderTranscript(segments, textType) {
    if (!segments || segments.length === 0) return "<p>暂无原文</p>";

    if (textType === "monologue" || segments.length === 1) {
        return segments
            .map((seg) => {
                if (seg.speaker && textType === "dialogue") {
                    return `<div class="transcript-line"><span class="transcript-speaker">${escapeHtml(seg.speaker)}:</span>${escapeHtml(seg.text)}</div>`;
                }
                return `<div class="transcript-line">${escapeHtml(seg.text)}</div>`;
            })
            .join("");
    }

    return segments
        .map(
            (seg) =>
                `<div class="transcript-line"><span class="transcript-speaker">${escapeHtml(seg.speaker || "")}:</span>${escapeHtml(seg.text)}</div>`
        )
        .join("");
}

// ==================== 渲染答案 ====================
function renderAnswers(questions) {
    if (!questions || questions.length === 0) return "<p>暂无答案</p>";

    return questions
        .map((q) => {
            return `<div class="answer-item">
                <span class="answer-num">${q.id}.</span>
                <span class="answer-text">${escapeHtml(q.answer)}</span>
            </div>`;
        })
        .join("");
}

// ==================== 对答案 ====================
function revealAnswers() {
    $("#transcript-card").classList.add("revealed");
    $("#answers-card").classList.add("revealed");
    $("#reveal-section").style.display = "none";

    // 平滑滚动到原文
    setTimeout(() => {
        $("#transcript-card").scrollIntoView({ behavior: "smooth", block: "start" });
    }, 200);
}

// ==================== 复制功能 ====================
function initCopyButtons() {
    $$(".copy-btn").forEach((btn) => {
        btn.onclick = () => {
            const targetId = btn.dataset.target;
            const targetEl = $("#" + targetId);
            if (!targetEl) return;

            const text = targetEl.innerText || targetEl.textContent;

            navigator.clipboard
                .writeText(text)
                .then(() => {
                    const label = btn.querySelector(".copy-label");
                    const originalText = label.textContent;
                    label.textContent = "已复制!";
                    btn.classList.add("copied");

                    setTimeout(() => {
                        label.textContent = originalText;
                        btn.classList.remove("copied");
                    }, 2000);
                })
                .catch(() => {
                    // 降级方案
                    const textarea = document.createElement("textarea");
                    textarea.value = text;
                    textarea.style.position = "fixed";
                    textarea.style.opacity = "0";
                    document.body.appendChild(textarea);
                    textarea.select();
                    document.execCommand("copy");
                    document.body.removeChild(textarea);

                    const label = btn.querySelector(".copy-label");
                    label.textContent = "已复制!";
                    btn.classList.add("copied");
                    setTimeout(() => {
                        label.textContent = "复制";
                        btn.classList.remove("copied");
                    }, 2000);
                });
        };
    });
}

// ==================== 错误提示 ====================
function showError(msg) {
    $("#error-text").textContent = "❌ " + msg;
    $("#error-card").style.display = "block";
    $("#error-card").scrollIntoView({ behavior: "smooth", block: "center" });
}

// ==================== HTML 转义 ====================
function escapeHtml(text) {
    if (!text) return "";
    const map = {
        "&": "&amp;",
        "<": "&lt;",
        ">": "&gt;",
        '"': "&quot;",
        "'": "&#039;",
    };
    return String(text).replace(/[&<>"']/g, (m) => map[m]);
}

// ==================== 启动 ====================
document.addEventListener("DOMContentLoaded", () => {
    initButtonGroups();
    $("#generate-btn").addEventListener("click", generate);

    // 回车提交
    $("#theme-input").addEventListener("keydown", (e) => {
        if (e.key === "Enter") generate();
    });
});
