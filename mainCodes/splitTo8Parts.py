import os
import os.path


# 读取目录下的所有文件，包括嵌套的文件夹
def GetFileList(dir, fileList):
    newDir = dir
    if os.path.isfile(dir):
        fileList.append(dir)
    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            # 如果需要忽略某些文件夹，使用以下代码
            # if s == "xxx":
            # continue
            newDir = os.path.join(dir, s)
            GetFileList(newDir, fileList)
    return fileList


# 循环处理文件
fileDir = "/Users/mac/Desktop/语料处理2/语料3输出"
list = GetFileList(fileDir, [])

# for i in range(len(list)):
#     print(list[i])

# # 先去除所有文件中空行：
# numOfEmpty = 0
# totalLine = 0
# for i in list:
#     print(i)
#     fileName = os.path.split(i)[-1]
#     outputPath3 = os.path.join(fileDir, fileName)
#     if os.path.split(i)[-1].startswith('.'):
#         continue
#     with open(fileName, 'r', encoding='utf-8') as f:
#         for line in f.readlines():
#             if line == '\n':
#                 line = line.strip("\n")
#                 # numOfEmpty = numOfEmpty + 1
#             with open(outputPath3, 'a', encoding='utf-8') as wf:
#                 wf.write(line)
#                 # totalLine = totalLine + 1

# 统计多少行
totalLine = 0

# for i in list:
#     print(i)
#     fileName = os.path.split(i)[-1]
#     path = os.path.join(fileDir, fileName)
#     if os.path.split(i)[-1].startswith('.'):
#         continue
#     with open(path, encoding='GBK') as f:
#         totalLine = totalLine + len(f.readlines())
#         # text = f.read()
#         # for j in range(len(text)):
#         #     if text[j] == '\n':
#         #         totalLine = totalLine + 1


# 空行......
# print("\n")
# print(totalLine)
# 总行数为603221

# def splitTo8Parts(text):

# 分成8个文件 : 527 x 8 = 4216  out8则为529行
count = 0  # counter of lines

out1 = '/Users/mac/Desktop/语料处理2/语料三输出/part1.txt'
out2 = '/Users/mac/Desktop/语料处理2/语料三输出/part2.txt'
out3 = '/Users/mac/Desktop/语料处理2/语料三输出/part3.txt'
out4 = '/Users/mac/Desktop/语料处理2/语料三输出/part4.txt'
out5 = '/Users/mac/Desktop/语料处理2/语料三输出/part5.txt'
out6 = '/Users/mac/Desktop/语料处理2/语料三输出/part6.txt'
out7 = '/Users/mac/Desktop/语料处理2/语料三输出/part7.txt'
out8 = '/Users/mac/Desktop/语料处理2/语料三输出/part8.txt'
totalLine = 603221   # 需要统计处理过后的所有txt总共多少行
row = int(totalLine / 8)
for i in list:
    fileName = os.path.split(i)[-1]
    path = os.path.join(fileDir, fileName)
    if os.path.split(i)[-1].startswith('.'):
        continue
    print(i)
    with open(path, encoding='GBK') as f:
        for line in f.readlines():
            count = count + 1
            if 1 <= count <= row:
                with open(out1, 'a', encoding='utf-8') as wf:
                    wf.write(line)
            if row + 1 <= count <= row * 2:
                with open(out2, 'a', encoding='utf-8') as wf:
                    wf.write(line)
            if row * 2 + 1 <= count <= row * 3:
                with open(out3, 'a', encoding='utf-8') as wf:
                    wf.write(line)
            if row * 3 + 1 <= count <= row * 4:
                with open(out4, 'a', encoding='utf-8') as wf:
                    wf.write(line)
            if row * 4 + 1 <= count <= row * 5:
                with open(out5, 'a', encoding='utf-8') as wf:
                    wf.write(line)
            if row * 5 + 1 <= count <= row * 6:
                with open(out6, 'a', encoding='utf-8') as wf:
                    wf.write(line)
            if row * 6 + 1 <= count <= row * 7:
                with open(out7, 'a', encoding='utf-8') as wf:
                    wf.write(line)
            if row * 7 + 1 <= count <= row * 8:
                with open(out8, 'a', encoding='utf-8') as wf:
                    wf.write(line)

        # 每换一个文件，都要在前面加一个换行符
        if 1 <= count <= row:
            with open(out1, 'a', encoding='utf-8') as wf:
                wf.write('\n')
        if row + 1 <= count <= row * 2:
            with open(out2, 'a', encoding='utf-8') as wf:
                wf.write('\n')
        if row * 2 + 1 <= count <= row * 3:
            with open(out3, 'a', encoding='utf-8') as wf:
                wf.write('\n')
        if row * 3 + 1 <= count <= row * 4:
            with open(out4, 'a', encoding='utf-8') as wf:
                wf.write('\n')
        if row * 4 + 1 <= count <= row * 5:
            with open(out5, 'a', encoding='utf-8') as wf:
                wf.write('\n')
        if row * 5 + 1 <= count <= row * 6:
            with open(out6, 'a', encoding='utf-8') as wf:
                wf.write('\n')
        if row * 6 + 1 <= count <= row * 7:
            with open(out7, 'a', encoding='utf-8') as wf:
                wf.write('\n')
        if row * 7 + 1 <= count <= row * 8:
            with open(out8, 'a', encoding='utf-8') as wf:
               wf.write('\n')