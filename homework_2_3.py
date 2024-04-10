import math
import jieba
import collections
import pandas as pd
import os

def calculate_entropy(text):
    # 使用jieba进行分词
    words = jieba.lcut(text)

    # 构建三元模型
    tri_grams = [(words[i], words[i+1], words[i+2]) for i in range(len(words)-2)]

    # 统计三元词组频率
    tri_gram_counts = collections.Counter(tri_grams)

    # 总三元词组数
    total_tri_grams = sum(tri_gram_counts.values())

    # 计算每个三元词组的概率
    tri_gram_probabilities = {tri_gram: count / total_tri_grams for tri_gram, count in tri_gram_counts.items()}

    # 计算信息熵
    entropy = -sum(prob * math.log(prob, 2) for prob in tri_gram_probabilities.values())

    return round(entropy, 3)  # 保留3位小数

def calculate_char_entropy(text):
    # 构建三元模型
    tri_grams = [(text[i], text[i+1], text[i+2]) for i in range(len(text)-2)]

    # 统计三元字组频率
    tri_gram_counts = collections.Counter(tri_grams)

    # 总三元字组数
    total_tri_grams = sum(tri_gram_counts.values())

    # 计算每个三元字组的概率
    tri_gram_probabilities = {tri_gram: count / total_tri_grams for tri_gram, count in tri_gram_counts.items()}

    # 计算信息熵
    entropy = -sum(prob * math.log(prob, 2) for prob in tri_gram_probabilities.values())

    return round(entropy, 3)  # 保留3位小数

if __name__ == "__main__":
    # 创建一个空的DataFrame来存储结果
    result_df = pd.DataFrame(columns=['文件名', '三元词级别信息熵', '三元字级别信息熵'])

    for i in range(1, 17):  # 假设有16个文件，文件名从1.txt到16.txt
        file_name = f'{i}.txt'
        if os.path.exists(file_name):
            with open(file_name, 'r', encoding='GBK', errors='ignore') as file:
                text = file.read()

            # 计算三元词级别的信息熵
            tri_word_entropy = calculate_entropy(text)

            # 计算三元字级别的信息熵
            tri_char_entropy = calculate_char_entropy(text)

            # 将结果添加到DataFrame中
            result_df = pd.concat([result_df, pd.DataFrame({'文件名': [file_name], '三元词级别信息熵': [tri_word_entropy], '三元字级别信息熵': [tri_char_entropy]})], ignore_index=True)

    # 打印结果
    print(result_df)

    # 将结果保存为CSV文件
    result_df.to_csv('tri_gram_entropy_results.csv', index=False)
