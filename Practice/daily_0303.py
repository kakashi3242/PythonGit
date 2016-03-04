# 第 0004 题：任一个英文的纯文本文件，统计其中的单词出现的个数。
import re

file_name= '/Users/wuyong/Desktop/english.txt'
word_dict = {}
line_list = []
with open(file_name) as f:
    for line in f:
        r = re.compile(r'[^a-zA-Z0-9]+')
        match = re.findall(r, line)
        for i in match:
            line = line.replace(i, ' ')
        line_list = line.split()
        for i in line_list:
            if i not in word_dict:
                word_dict[i] = 1
            else:
                word_dict[i] += 1

print(len(word_dict))






