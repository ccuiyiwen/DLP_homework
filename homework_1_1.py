import re
import collections
import jieba
import matplotlib.pyplot as plt


def clean_text(text):
    # 去除标点符号和特殊字符
    text = re.sub(r'[^\u4e00-\u9fa5]', '', text)
    return text


def load_stopwords(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        stopwords = [line.strip() for line in file]
    return stopwords


def calculate_word_frequencies(text, stopwords):
    # 使用jieba进行分词
    words = jieba.lcut(text)
    # 去除停用词
    words = [word for word in words if word not in stopwords]
    word_counts = collections.Counter(words)
    return word_counts


if __name__ == "__main__":
    # 读取中文文本数据，可以替换成您自己的文本数据
    with open('1.txt', 'r', encoding='GBK',errors = 'ignore') as file:
        text = file.read()

    # 加载停用词列表
    stopwords_file = 'stop_words.txt'
    stopwords = load_stopwords(stopwords_file)

    # 数据清洗
    cleaned_text = clean_text(text)

    # 计算词频
    word_counts = calculate_word_frequencies(cleaned_text, stopwords)

    # 取词频最高的前 n 个单词
    n = 50
    top_words = word_counts.most_common(n)

    # 获取频率并排序
    frequencies = sorted([count for _, count in top_words], reverse=True)

    # 绘制齐夫定律的图表
    ranks = range(1, len(frequencies) + 1)

    plt.figure(figsize=(10, 5))
    plt.plot(ranks, frequencies, marker='o', linestyle='-')
    plt.xscale('log')
    plt.yscale('log')
    plt.title("Zipf's Law")
    plt.xlabel('Rank')
    plt.ylabel('Frequency')
    plt.show()