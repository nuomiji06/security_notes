#Python：把你写好的 notes.txt 读出来，用 strip() 去除换行符，用 for 循环逐行打印。
with open("notes.txt","r",encoding="utf-8") as f:
    for line in f:
        print(line.strip())#自带换行，会隔一行（双倍换行）
    f.seek(0)#回到文件开头
    for line in f:
        print(line)#去掉首尾空白，再正常换行
    f.seek(0)#回到文件开头  
    for line in f:
        print(line,end="")#原汁原味，保留原换行、空格