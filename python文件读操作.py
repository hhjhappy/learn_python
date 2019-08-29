from sys import argv

script,filename = argv

#readline()每次读取一行，节省内存    每次只读取一行，通常比 .readlines() 慢得多。仅当没有足够内存可以一次读取整个文件时，才应该使用 .readline()
with open(filename,'r') as f:
    while True:
        txt_line = f.readline()
        if txt_line:
            print(txt_line.strip('\n'))
            # if '那到底是一个什么地方' in txt_line:
                # print(txt_line.strip('\n'))
        else:
            break

#read() 每次读取整个文件，它通常用于将文件内容放到一个字符串变量中，不适用于大文件
with open(filename,'r') as f:
    print(f.read())


#readlines() 自动将文件内容分析成一个行的列表，该列表可以由 Python 的 for ... in ... 结构进行处理。
with open(filename,'r') as f:
    for i in f.readlines():
        print(i)
