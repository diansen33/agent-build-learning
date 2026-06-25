# 研究助手 Agent 项目 Roadmap

> 技术路线：先做一个单 Agent，再给它加工具、检索、记忆，最后再做工作流编排。
> 每一步都能单独产出结果，每一步都能为下一步提供基础。

---

## 一、Roadmap 六阶段

### 第 1 阶段：最小可用研究助手

```text
用户问题 → 搜索论文 → 抽取标题/摘要/作者 → 生成简要总结
```

核心知识点（4 个）：
1. 输入输出设计：把用户问题变成结构化任务。
2. 搜索接口：从 arXiv / Semantic Scholar 获取论文。
3. 摘要抽取：拿到标题、摘要、作者、年份。
4. 固定模板总结：让模型稳定输出"解决了什么、方法是什么、优缺点是什么"。

产物：CLI 或简单网页，输入关键词后返回前 5 篇论文的卡片式总结。

---

### 第 2 阶段：结构化检索

补的知识点：
- 查询改写：把一个主题改写成多个可检索 query。
- 结果排序：按相关性、年份、引用信息、摘要匹配度排序。
- 过滤规则：年份、领域、作者、会议/期刊。
- 去重：同一论文不同来源不重复。

产物：输入一个主题，返回"相关论文列表 + 排名理由 + 标签"。

---

### 第 3 阶段：工具调用

至少让模型会调用这些工具：
- `search_papers(query)`
- `fetch_paper(paper_id)`
- `summarize_text(text)`
- `save_note(title, content)`

要学的不是"会不会写 prompt"，而是：
- 什么时候该调用工具
- 工具返回结果后怎么继续思考
- 怎么限制模型乱编工具参数
- 怎么让输出稳定成 JSON 或固定 schema

产物：用户输入"帮我找 2023 年以后关于某方向的综述"，Agent 能自己拆任务、查资料、再汇总。

---

### 第 4 阶段：短期记忆 + 长期记忆

短期记忆：
- 当前会话里用户问过什么
- 现在正在研究的子问题
- 当前已经筛过哪些论文

长期记忆：
- 关注的方向
- 常用的关键词
- 偏好的输出格式
- 看过的论文和笔记

产物：第二次问同一方向时，能主动接着上次的上下文继续。

---

### 第 5 阶段：工作流编排

```text
Query Planner
 → Search Node
 → Filter Node
 → Reader Node
 → Summarizer Node
 → Memory Writer
 → Report Generator
```

会真正理解：
- 为什么 agent 要拆节点
- 为什么中间状态要落盘
- 为什么"工作流"和"Agent"不是一回事
- 为什么可观测性很重要

产物：一个稳定的研究流水线，而不是容易跑偏的聊天机器人。

---

### 第 6 阶段：评估

建立一个小型评测集（约 30 个问题）：
- 搜索类：是否找对论文
- 总结类：是否抓住论文核心贡献
- 可靠性类：是否编造不存在的信息
- 一致性类：同一个问题多次回答是否稳定
- 可用性类：输出是否清晰、可读、可复用

产物：能回答"这个研究助手到底比普通聊天强在哪"。

---

## 二、三个里程碑（落地优先级）

```text
里程碑 A：能搜论文
里程碑 B：能读并总结论文
里程碑 C：能记住并形成研究笔记
```

先做 A，再做 B，再做 C。C 跑通后再用 LangGraph 之类把整个流程正规化。

---

## 三、推荐学习顺序

```text
1. Python + 数据结构
2. LLM 调用 / Structured Output
3. 工具调用
4. 检索与排序
5. 文本抽取与总结
6. 记忆系统
7. 工作流编排
8. 评估与部署
```

---

## 四、第一版目标

```text
输入：MRAM CIM 的综述论文
输出：
- 相关论文 5 篇
- 每篇 5 行总结
- 1 段整体趋势分析
- 1 个可保存的研究笔记
```

覆盖核心链路：检索、阅读、总结、记忆、输出。

---

## 五、项目目录结构

下面这份结构是按"分层 + 渐进式"设计的：每一阶段只需新增或填充对应的目录，
不需要提前把所有空文件建出来。

```text
research-agent/
├── README.md                      # 项目说明 + 快速开始
├── ROADMAP.md                     # 本文件：路线图 + 目录说明 + 实现顺序
├── pyproject.toml                 # 依赖与项目元信息（用 uv / poetry 管理）
├── .env.example                   # 环境变量模板（API key 等），真 key 放 .env
├── .gitignore
│
├── config/                        # 配置层
│   ├── __init__.py
│   ├── settings.py                # 读取 .env、模型名、检索参数等全局配置
│   └── prompts.py                 # 所有 prompt 模板集中放这里（阶段 1 就开始用）
│
├── src/                           # 核心代码
│   ├── __init__.py
│   │
│   ├── llm/                       # LLM 调用层（阶段 1）
│   │   ├── __init__.py
│   │   ├── client.py              # 封装 LLM 客户端：chat / structured output
│   │   └── schemas.py             # Pydantic 模型：PaperSummary / Note / Report 等
│   │
│   ├── search/                    # 检索层（阶段 1 起步，阶段 2 完善）
│   │   ├── __init__.py
│   │   ├── arxiv.py               # arXiv API 客户端
│   │   ├── semantic_scholar.py    # Semantic Scholar API 客户端（阶段 2 加入）
│   │   ├── reranker.py            # 结果排序/打分（阶段 2）
│   │   ├── filters.py             # 年份/领域/作者过滤与去重（阶段 2）
│   │   └── query_rewriter.py      # 查询改写（阶段 2）
│   │
│   ├── reader/                    # 论文阅读层（阶段 1 简版，阶段 3 完善）
│   │   ├── __init__.py
│   │   ├── extractor.py           # 从论文 metadata / 全文里抽取关键字段
│   │   └── summarizer.py          # 单篇论文总结器
│   │
│   ├── tools/                     # 工具层（阶段 3）
│   │   ├── __init__.py
│   │   ├── registry.py            # 工具注册表 + schema 描述
│   │   ├── search_papers.py       # 工具：search_papers(query)
│   │   ├── fetch_paper.py         # 工具：fetch_paper(paper_id)
│   │   ├── summarize_text.py      # 工具：summarize_text(text)
│   │   └── save_note.py           # 工具：save_note(title, content)
│   │
│   ├── memory/                    # 记忆层（阶段 4）
│   │   ├── __init__.py
│   │   ├── short_term.py          # 短期记忆：会话级上下文
│   │   ├── long_term.py           # 长期记忆：偏好/已读论文/笔记
│   │   └── store.py               # 持久化后端（SQLite / JSON 文件起步）
│   │
│   ├── agent/                     # Agent 层（阶段 3 起步，阶段 5 重构）
│   │   ├── __init__.py
│   │   ├── simple_agent.py        # 阶段 3：单 Agent + tool calling 循环
│   │   └── graph.py               # 阶段 5：LangGraph 工作流定义
│   │
│   ├── nodes/                     # 工作流节点（阶段 5）
│   │   ├── __init__.py
│   │   ├── planner.py             # Query Planner
│   │   ├── search_node.py
│   │   ├── filter_node.py
│   │   ├── reader_node.py
│   │   ├── summarizer_node.py
│   │   ├── memory_writer.py
│   │   └── report_generator.py
│   │
│   └── utils/                     # 工具函数
│       ├── __init__.py
│       ├── logging.py             # 统一日志
│       ├── http.py                # 重试、超时、限流
│       └── text.py                # 文本清洗、截断、token 估算
│
├── cli/                           # 命令行入口（阶段 1 就有简版）
│   ├── __init__.py
│   └── main.py                    # argparse / typer 入口
│
├── tests/                         # 测试（每个阶段都要补）
│   ├── __init__.py
│   ├── test_search.py
│   ├── test_summarizer.py
│   ├── test_tools.py
│   ├── test_memory.py
│   └── test_agent.py
│
├── eval/                          # 评估（阶段 6）
│   ├── __init__.py
│   ├── datasets/                  # 评测集（30 个问题）
│   │   └── questions.yaml
│   ├── runners/                   # 评测执行器
│   │   └── run_eval.py
│   └── metrics.py                 # 指标：命中率、忠实度、一致性等
│
├── data/                          # 运行时产生的数据
│   ├── notes/                     # save_note 保存的笔记
│   ├── cache/                     # API 响应缓存
│   └── memory.db                  # 长期记忆 SQLite（阶段 4）
│
├── notebooks/                     # 探索性分析
│   └── 01_arxiv_api_demo.ipynb
│
└── docs/                          # 设计文档（按需写）
    ├── architecture.md
    └── decisions.md               # ADR：关键技术选型记录
```

---

## 六、每一层该写哪些文件（按阶段对齐）

### 阶段 1：最小可用研究助手
只需要这些文件就能跑通最小闭环：

| 文件 | 作用 |
|------|------|
| `pyproject.toml` | 依赖：httpx、pydantic、openai（或同类）、typer |
| `.env.example` | `OPENAI_API_KEY=`、`ARXIV_MAX_RESULTS=5` |
| `config/settings.py` | 读取配置，导出 `settings` 单例 |
| `config/prompts.py` | `SUMMARY_TEMPLATE`：固定模板总结 |
| `src/llm/client.py` | `chat()` 与 `summarize()` 两个函数 |
| `src/llm/schemas.py` | `PaperSummary(BaseModel)` |
| `src/search/arxiv.py` | `search_arxiv(query, max_results)` 返回标准化论文列表 |
| `src/reader/summarizer.py` | 调用 LLM 生成单篇卡片总结 |
| `cli/main.py` | `python -m cli.main "MRAM CIM"` 输出 5 篇卡片 |
| `src/utils/text.py` | 摘要清洗、超长截断 |

### 阶段 2：结构化检索
新增 / 完善：

| 文件 | 作用 |
|------|------|
| `src/search/query_rewriter.py` | LLM 把一个主题改写成 3~5 个 query |
| `src/search/reranker.py` | 多维打分：年份、引用、摘要相似度 |
| `src/search/filters.py` | 年份/领域过滤 + 按 id 去重 |
| `src/search/semantic_scholar.py` | 引入第二个数据源做交叉补充 |
| `src/llm/schemas.py` | 新增 `RankedPaper`、`SearchResult` |

### 阶段 3：工具调用
把前面的能力包装成工具：

| 文件 | 作用 |
|------|------|
| `src/tools/registry.py` | 工具注册 + JSON schema 生成 |
| `src/tools/search_papers.py` | 包装 `src/search` |
| `src/tools/fetch_paper.py` | 按 id 拉单篇详情 |
| `src/tools/summarize_text.py` | 包装 `src/reader/summarizer.py` |
| `src/tools/save_note.py` | 写入 `data/notes/` |
| `src/agent/simple_agent.py` | tool-calling 循环：思考 → 调工具 → 观察 → 再思考 |
| `cli/main.py` | 增加 `agent` 子命令进入交互式 Agent |

### 阶段 4：记忆
| 文件 | 作用 |
|------|------|
| `src/memory/store.py` | SQLite 后端：notes、seen_papers、preferences 三张表 |
| `src/memory/short_term.py` | 维护当前会话上下文窗口 |
| `src/memory/long_term.py` | 读写用户偏好 / 已读论文 / 笔记 |
| `src/tools/save_note.py` | 改为写入长期记忆 store |
| `src/agent/simple_agent.py` | 注入短期记忆到 system prompt |

### 阶段 5：工作流编排
| 文件 | 作用 |
|------|------|
| `src/agent/graph.py` | 用 LangGraph 定义工作流图 + State |
| `src/nodes/planner.py` | 拆解用户问题为子任务 |
| `src/nodes/search_node.py` | 调检索层 |
| `src/nodes/filter_node.py` | 排序、去重、截断到 Top N |
| `src/nodes/reader_node.py` | 抓全文/详情 |
| `src/nodes/summarizer_node.py` | 批量总结 |
| `src/nodes/memory_writer.py` | 落盘到记忆层 |
| `src/nodes/report_generator.py` | 汇总成最终报告 |
| `cli/main.py` | 新增 `pipeline` 子命令跑完整工作流 |

### 阶段 6：评估
| 文件 | 作用 |
|------|------|
| `eval/datasets/questions.yaml` | 30 个评测问题 + 期望 |
| `eval/runners/run_eval.py` | 跑全量评测、产出报告 |
| `eval/metrics.py` | 命中率、忠实度、一致性、延迟、成本 |

---

## 七、实现顺序（逐步落地）

> 原则：每一步结束都要能 `python -m cli.main ...` 跑出可见结果。

### Step 0 — 项目骨架（半天）
1. 初始化 `pyproject.toml`，装依赖。
2. 建 `config/`、`src/`、`cli/`、`tests/` 目录与 `__init__.py`。
3. 写 `.env.example` 和 `.gitignore`。
4. 跑通 `cli/main.py` 输出 "hello"。

### Step 1 — arXiv 检索（里程碑 A 的核心）
5. `src/search/arxiv.py`：用 httpx 调 arXiv API，返回标准化 dict。
6. `src/utils/text.py`：清洗摘要里的换行、LaTeX 残留。
7. `tests/test_search.py`：mock 一次响应做单测。
8. `cli/main.py`：`search <query>` 子命令，打印前 5 篇标题。

### Step 2 — LLM 总结（里程碑 B 的核心）
9. `src/llm/client.py`：封装 chat + structured output。
10. `src/llm/schemas.py`：`PaperSummary`（problem/method/pros/cons）。
11. `config/prompts.py`：固定模板，强约束输出。
12. `src/reader/summarizer.py`：输入论文 → 输出 `PaperSummary`。
13. `cli/main.py`：`summarize <query>` 打印 5 张卡片。

### Step 3 — 结构化检索（阶段 2）
14. `src/search/query_rewriter.py`：主题 → 多 query。
15. `src/search/reranker.py` + `filters.py`：打分、过滤、去重。
16. `src/search/semantic_scholar.py`：第二数据源。
17. CLI 增加 `--year`、`--field`、`--top` 参数。

### Step 4 — 工具调用（阶段 3）
18. `src/tools/registry.py`：定义工具 schema。
19. 把 search / fetch / summarize / save_note 包装成工具。
20. `src/agent/simple_agent.py`：ReAct 式 tool loop。
21. CLI 增加 `agent` 子命令进入交互模式。

### Step 5 — 记忆（阶段 4，里程碑 C）
22. `src/memory/store.py`：SQLite 建表。
23. `src/memory/short_term.py` + `long_term.py`。
24. Agent 注入记忆，`save_note` 写入 store。
25. 验证：同一主题第二次问能接着上次。

### Step 6 — 工作流编排（阶段 5）
26. 定义 `State`（query、papers、summaries、notes、report）。
27. 逐个实现 `src/nodes/`。
28. `src/agent/graph.py` 串成 LangGraph 图。
29. CLI 增加 `pipeline <topic>` 跑完整流水线。

### Step 7 — 评估（阶段 6）
30. 整理 30 个评测问题。
31. `eval/runners/run_eval.py` + `eval/metrics.py`。
32. 跑一轮基线评测，记录结果到 `docs/`。

---

## 八、第一版验收标准

跑这条命令能拿到下面格式的输出即视为第一版完成：

```bash
python -m cli.main summarize "MRAM CIM survey" --top 5
```

输出包含：
- 5 篇相关论文
- 每篇 5 行总结
- 1 段整体趋势分析
- 1 个可保存的研究笔记（写入 `data/notes/`）

覆盖链路：**检索 → 阅读 → 总结 → 记忆 → 输出**。
