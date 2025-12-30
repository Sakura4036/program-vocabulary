# Program Vocabulary (计算机术语词典)

这是一个专注于计算机科学与编程领域的术语词典项目。旨在收集、整理常用的编程与计算机专业词汇，并提供中英文对照。

## 项目简介

本项目维护了一个高质量的计算机术语库，源码格式为 JSON，方便程序读取和处理。同时提供了 Python 脚本工具，可自动生成纯英文单词列表和中英文对照列表，便于用户进行背诵、检索或其他用途。

## 核心功能

- **结构化数据**: 核心词汇存储在 `vocabulary.json` 中，按字母分类，结构清晰。
- **自动生成**: 提供 `convert.py` 脚本，可一键生成易于阅读的文本文件。
- **中英对照**: 生成的文件包含纯英文列表 (`vocabulary_english.txt`) 和中英对照列表 (`vocabulary_mixed.txt`)。
- **自动排序**: 脚本生成时会自动按字母顺序（不区分大小写）对词汇进行排序。

## 文件结构

```text
.
├── vocabulary.json         # [核心] 词汇数据源文件 (JSON 格式)
├── convert.py              # [工具] 数据转换与生成脚本 (Python)
├── vocabulary_english.txt  # [产物] 纯英文单词列表 (自动生成)
├── vocabulary_mixed.txt    # [产物] 中英文对照列表 (自动生成)
└── README.md               # 项目说明文档
```

## 数据格式说明 (`vocabulary.json`)

词库按首字母进行分类存储，格式如下：

```json
{
  "a": {
    "algorithm": ["算法"],
    "array": ["数组"]
  },
  "b": {
    "boolean": ["布尔值"]
  }
}
```

- **Keys (a, b, ...)**: 单词首小写字母。
- **Word Keys ("algorithm")**: 具体的英文单词或短语。
- **Values (["算法"])**: 对应的中文翻译（数组格式，支持多义词，但目前主要使用第一个释义）。

## 如何使用

### 1. 运行环境
确保您的系统中已安装 Python 3.x。

### 2. 生成/更新词汇表
当您修改了 `vocabulary.json` 后，运行以下命令来更新文本文件：

```bash
python convert.py
```

脚本运行成功后，会输出以下提示，并覆盖更新 `vocabulary_english.txt` 和 `vocabulary_mixed.txt`：

```text
Successfully converted to:
1. .../vocabulary_english.txt
2. .../vocabulary_mixed.txt
```

### 3. 查看结果
- **vocabulary_english.txt**: 仅包含英文单词，适合听写或自我测试。
- **vocabulary_mixed.txt**: 包含“单词 + 换行 + 翻译”的格式，适合对照学习。

## 贡献指南

欢迎提交 Pull Request 来扩充词库！请确保：
1. 在 `vocabulary.json` 中找到对应的首字母分类。
2. 按照 JSON 格式添加新的单词和翻译。
3. 提交前请运行 `python convert.py` 确保 JSON 格式正确且能正常生成文件。
