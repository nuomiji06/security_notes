#弄一个 word.txt，里面塞一段英文，用 Python 读出来，用字典统计每个单词出现的次数，然后打印出来。（提示：用到 split() 和 dict.get(word, 0)）。
with open("word.txt","r",encoding="utf-8") as f:
    text = f.read()

text = text.replace(".","").replace(",","").replace("!","").replace("?","")  # 去掉标点符号
words = text.split()

freq = {}  # 按空格分割单词
for word in words:
    freq[word] = freq.get(word, 0) + 1  # 统计单词出现次数
print(freq)  # 打印单词统计结果