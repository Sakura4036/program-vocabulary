import json
import os

def update_vocabulary():
    file_path = r'd:\Code\sakura4036\program-vocabulary\v3\vocabulary.json'
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    new_words = {
        "A": {
            "Auto-GPT": "一个能自主实现目标的 AI 智能体实验原型",
            "Anthropic": "开发了 Claude 系列模型的 AI 安全与研究公司",
            "AutoGen": "Microsoft 开发的多智能体应用框架",
        },
        "B": {
            "Bias": "偏见，特指 AI 模型中的算法偏见",
            "Benchmark": "基准测试，用于评估硬件或软件性能的标准化测试",
        },
        "C": {
            "Claude": "由 Anthropic 开发的高性能大语言模型系列",
            "Compute": "算力，进行计算处理的能力",
            "CUDA": "由 NVIDIA 推出的并行计算平台和编程模型",
            "Constitutional AI": "宪法 AI，一种通过预设原则引导模型行为的对齐技术",
        },
        "D": {
            "Deepfake": "深度伪造，利用 AI 生成的虚假音视频内容",
            "Distillation": "知识蒸馏，将大型模型的能力转移到较小模型的技术",
        },
        "E": {
            "Embodied AI": "具身智能，使 AI 能够通过机器人在物理世界中感知和互动",
            "Emergence": "涌现，模型规模达到一定程度时表现出的复杂新能力",
        },
        "F": {
            "Few-shot": "少样本学习，模型仅需少量示例即可学习新任务",
            "Foundation Model": "基础模型，在海量数据上预训练且可适配多种任务的模型",
        },
        "G": {
            "Gemini": "Google 开发的多模态大模型系统",
            "GGUF": "针对 LLM 推理优化的模型量化存储文件格式",
            "GPU": "图形处理器，广泛用于 AI 计算加速",
            "Generative AI": "生成式人工智能，能够创作新内容（文本、图像等）的 AI",
        },
        "H": {
            "Hyperparameter": "超参数，在模型训练前手动设置的参数",
        },
        "I": {
            "In-context Learning": "上下文学习，模型通过输入示例直接学习任务的能力",
            "Instruct": "指令微调，使模型能够遵循人类指令的技术",
        },
        "L": {
            "LangGraph": "用于构建复杂、循环的多智能体系统的开发框架",
            "LMM": "大视觉语言模型 (Large Multimodal Model)",
        },
        "M": {
            "Mistral": "高性能开源大模型系列及其背后的法国 AI 公司",
            "Multi-agent": "多智能体系统，多个 AI 智能体协作解决问题的架构",
            "Modality": "模态，指不同类型的信息输入（如文本、图像、音频）",
        },
        "N": {
            "NPU": "神经网络处理器，专门为加速神经网络运算设计的微处理器",
        },
        "O": {
            "Ollama": "支持在本地轻松部署和运行 LLM 的开源工具",
            "ONNX": "开放神经网络交换格式，用于不同深度学习框架间的模型转换",
        },
        "P": {
            "Prompt Engineering": "提示工程，通过优化输入来引导 AI 生成更优结果的技术",
            "Perplexity": "困惑度，衡量语言模型预测文本质量的常用指标",
            "Pre-training": "预训练，在海量数据上进行初始模型训练的过程",
        },
        "Q": {
            "Quantization": "量化，压缩模型权重精度以降低显存占用并提速的技术",
            "QLoRA": "量化低秩自适应，一种极高显存效率的模型微调技术",
        },
        "R": {
            "Reasoning": "推理，模型通过逻辑步骤解决问题的思维过程",
        },
        "S": {
            "Scaling Law": "缩放法则，描述模型性能随计算量、参数量和数据量增加而提升的规律",
            "Synthetic Data": "合成数据，由算法或 AI 生成的训练数据",
            "Stable Diffusion": "一种流行的开源潜在扩散模型，常用于 AI 图像生成",
        },
        "T": {
            "Temperature": "温度参数，控制 LLM 输出随机性和多样性的超参数",
            "Tokenization": "分词，将文本转换为模型可处理的 Token 序列的过程",
            "TPU": "张量处理器，Google 开发的专门用于机器学习加速的硬件",
        },
        "V": {
            "Vector Database": "向量数据库，专为高维向量搜索和存储设计的数据库",
            "VLM": "视觉语言模型，可同时理解并处理图像和文本信息",
        }
    }

    for letter, words in new_words.items():
        if letter not in data:
            data[letter] = {}
        data[letter].update(words)
        # Sort words within alphabet
        data[letter] = dict(sorted(data[letter].items(), key=lambda x: x[0].lower()))

    # Sort alphabet keys
    data = dict(sorted(data.items()))

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    update_vocabulary()
