# Program Vocabulary (计算机术语词典)

这是一个专注于计算机科学与编程领域的术语词典项目。旨在收集、整理常用的编程与计算机专业词汇，并提供中英文对照。

## 项目简介

本项目维护了一个高质量的、按领域分类的计算机术语库。项目结构分为两部分：
1. **vocabulary/**: 包含原始全量数据（JSON 格式）和核心处理脚本。
2. **words/**: 包含经过精简处理后的数据，按领域分类，可直接用于背诵或集成。

## 核心功能

- **多维分类**: 涵盖 AI、云原生/后端、前端/Web、计算机基础四大领域。
- **结构化数据**: 核心词汇存储在 `vocabulary.json` 中，支持多义词翻译。
- **精简易用**: `words/` 目录下的文本文件经过清洗，剔除了通用简单词汇，保留专业核心术语。
- **自动化工具**: 
  - 支持一键生成纯英文和中英对照列表。
  - 支持自动提取缩写词并合并到主库。

## 文件结构

```text
.
├── LICENSE                     # 项目许可证 (MIT)
├── README.md                   # 项目说明文档
├── vocabulary/                 # [核心] 原始词汇资源与处理工具
│   ├── vocabulary.json         # 全量词汇原始数据 (JSON)
│   ├── vocabulary_english.txt  # [产物] 全量纯英文单词列表
│   ├── vocabulary_mixed.txt    # [产物] 全量中英文对照列表
│   ├── convert.py              # [工具] 数据转换生成脚本
│   ├── extract_abbreviations.py # [工具] 提取全大写缩写词
│   └── merge_vocabularies.py    # [工具] 合并缩写词到主库
└── words/                      # [精简] 处理后的精简数据 (推荐直接使用)
    ├── ai_words.txt            # 人工智能领域精简词汇
    ├── cloud_backend_words.txt  # 云计算/后端领域精简词汇
    ├── frontend_web_words.txt   # 前端/Web 领域精简词汇
    ├── computer_science_words.txt # 计算机基础领域精简词汇
    └── all_words.txt           # 汇总精简词汇 (按领域排序)
```

## 数据说明

### 领域分类
- **AI/LLM**: 深度学习、自然语言处理、神经网络等。
- **Cloud/Backend**: 微服务、Docker/K8s、数据库、系统架构。
- **Frontend/Web**: 浏览器引擎、框架（React/Vue）、CSS、Web 标准。
- **CS Fundamentals**: 数据结构、算法、计算机网络、操作系统。

### 数据版本
- **vocabulary**: 包含全量词库，适合程序化、结构化查询。
- **words**: 已剔除 high-frequency (高频) 简单词（如 "if", "get", "set" 等），专注于专业核心术语，适合人工记忆。

## 如何使用

### 1. 使用精简数据
直接访问 `words/` 目录下的相应文件。这些文件已按“英文一行、中文一行”的格式排版。

### 2. 更新全量原始列表
在 `vocabulary` 目录下运行 `convert.py`：
```bash
python vocabulary/convert.py
```

### 3. 处理缩写词
- **提取**: `python vocabulary/extract_abbreviations.py`（从 `vocabulary.json` 中自动识别）。
- **合并**: `python vocabulary/merge_vocabularies.py`（将更新后的缩写词写回主库）。

## 贡献指南

欢迎参与词库扩充！您可以：
1. 直接在 `vocabulary/vocabulary.json` 中添加词条。
2. 完善 `words/` 目录下的分类词库内容。
3. 提交 PR 前请运行 `convert.py` 以确保同步。
