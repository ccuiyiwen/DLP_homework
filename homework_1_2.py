import re
import collections
import jieba
import matplotlib.pyplot as plt
import os

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
    # 加载停用词列表
    stopwords_file = 'stop_words.txt'
    stopwords = load_stopwords(stopwords_file)

    plt.figure(figsize=(10, 5))

    for i in range(1, 17):  # 假设有16个文件，文件名从1.txt到16.txt
        file_name = f'{i}.txt'
        if os.path.exists(file_name):
            with open(file_name, 'r', encoding='GBK', errors='ignore') as file:
                text = file.read()

            # 数据清洗
            cleaned_text = clean_text(text)

            # 计算词频
            word_counts = calculate_word_frequencies(cleaned_text, stopwords)

            # 获取频率并排序
            frequencies = sorted(list(word_counts.values()), reverse=True)

            # 绘制齐夫定律的图表
            ranks = range(1, len(frequencies) + 1)
            plt.plot(ranks, frequencies, linestyle='-', label=f'文件 {i}')

    plt.rcParams['font.sans-serif'] = ['SimSun']  # 指定要使用的中文字体为宋体
    plt.xscale('log')
    plt.yscale('log')
    plt.xlim(1, 1000)  # 设置x轴范围
    plt.ylim(1, 1e5)  # 设置y轴范围
    plt.title("齐夫定律")
    plt.xlabel('排名')
    plt.ylabel('词频')
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=8)  # 将图例放置在整个图的下方间
    plt.show()
