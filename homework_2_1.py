import math
import jieba
import collections
import pandas as pd
import os

def calculate_entropy(text):
    # 使用jieba进行分词
    words = jieba.lcut(text)

    # 统计词频
    word_counts = collections.Counter(words)

    # 总词数
    total_words = sum(word_counts.values())

    # 计算每个词的概率
    word_probabilities = {word: count / total_words for word, count in word_counts.items()}

    # 计算信息熵
    entropy = -sum(prob * math.log(prob, 2) for prob in word_probabilities.values())

    return round(entropy, 3)  # 保留3位小数

def calculate_char_entropy(text):
    # 统计每个字的出现次数
    char_counts = collections.Counter(text)

    # 总字数
    total_chars = sum(char_counts.values())

    # 计算每个字的概率
    char_probabilities = {char: count / total_chars for char, count in char_counts.items()}

    # 计算信息熵
    entropy = -sum(prob * math.log(prob, 2) for prob in char_probabilities.values())

    return round(entropy, 3)  # 保留3位小数

if __name__ == "__main__":
    # 创建一个空的DataFrame来存储结果
    result_df = pd.DataFrame(columns=['文件名', '词级别信息熵', '字级别信息熵'])

    for i in range(1, 17):  # 假设有16个文件，文件名从1.txt到16.txt
        file_name = f'{i}.txt'
        if os.path.exists(file_name):
            with open(file_name, 'r', encoding='GBK', errors='ignore') as file:
                text = file.read()

            # 计算词级别的信息熵
            word_entropy = calculate_entropy(text)

            # 计算字级别的信息熵
            char_entropy = calculate_char_entropy(text)

            # 将结果添加到DataFrame中
            result_df = pd.concat([result_df, pd.DataFrame({'文件名': [file_name], '词级别信息熵': [word_entropy], '字级别信息熵': [char_entropy]})], ignore_index=True)

    # 打印结果
    print(result_df)

    # 将结果保存为CSV文件
    result_df.to_csv('entropy_results.csv', index=False)
