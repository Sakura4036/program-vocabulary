import json

# 读取原始 JSON 文件
with open('vocabulary.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 创建新的字典用于存储简写词
abbreviations = {}

# 遍历每个字母分组
for letter, words in data.items():
    abbreviations[letter] = {}
    
    # 遍历每个单词
    for word, translations in words.items():
        # 检查是否为全大写单词（简写）
        # 注意：需要确保单词中至少有一个字母，且所有字母都是大写
        if word.isupper() and any(c.isalpha() for c in word):
            abbreviations[letter][word] = translations
    
    # 如果该字母下没有简写词，删除该键
    if not abbreviations[letter]:
        del abbreviations[letter]

# 将结果保存到新的 JSON 文件
with open('vocabulary_abbreviations.json', 'w', encoding='utf-8') as f:
    json.dump(abbreviations, f, ensure_ascii=False, indent=2)

print(f"提取完成！共提取 {sum(len(words) for words in abbreviations.values())} 个简写词。")
print(f"结果已保存到 vocabulary_abbreviations.json")
