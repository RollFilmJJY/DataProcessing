import os
import Levenshtein as L
import random
import re

# 二字三字四字姓名所占比例：     3：3：4
with open(r'/Users/mac/Desktop/语料处理2/jjynb/name_语料/letter2_uncommon_name.txt',encoding='UTF-8') as f:
    names2=f.read().split('\n')

with open(r'/Users/mac/Desktop/语料处理2/jjynb/name_语料/letter3_uncommon_name.txt',encoding='UTF-8') as f:
    names3=f.read().split('\n')

with open(r'/Users/mac/Desktop/语料处理2/jjynb/name_语料/compound_name.txt', encoding='UTF-8') as f:
    names_complex = f.read().split('\n')

with open(r'/Users/mac/Desktop/语料处理2/jjynb/name.txt', encoding='UTF-8') as f:
    names_com = f.read().split('\n')

number=['1','2','3','4','5','6','7','8','9','0']

def get_number():
    return random.choice(number)

def get_set():
    s={'张'}
    for i in names2:
        s.add(i[0])
    for i in names3:
        s.add(i[0])
    for i in names_com:
        if i != '':
            s.add(i[0])
    return s

set=get_set()

def get_name():
    # 按照比例生成姓名
    a=random.randint(1,10)
    if a<=3:
        return random.choice(names2)
    elif a<=6:
        return random.choice(names3)
    else:
        return random.choice(names_complex)

def txt_strip(text):
    # 删除“被告”以前的字以及“本院认为”以后的字
    # 输入：文本text
    # 返回：修改后的text
    index1 = text.find("被告")
    index2 = text.find("本院认为")
    if (index1 > 0 and index2 > 0):
        return text[index1 : index2]
    return text

def partition(text):
    # 一句话一行，计算相似度(ratio>0.75)去重
    list=text.split('。')
    res=''
    length=len(list)
    for i in range(length):
        list[i]=list[i]+'。'
    for i in range(0,length):
        for j in range(i+1,length):
            sim=L.ratio(list[i],list[j])
            if sim>0.75:
                list[i]=''
                break
    res=res.join(list)
    return res

def replace2(text,char):
    index = text.find(char)
    while (index > 0):
        if text[index - 1] in set:
            if text[index + 1] == char:
                name = get_name()
                text = text[0:index - 1] + name + text[index + 2:]
            else:
                name = get_name()
                text = text[0:index - 1] + name + text[index + 1:]
        else:
            text=text[:index]+get_number()+text[index+1:]
        index = text.find(char)
    return text

def replace(text):

    index=text.find('某某')
    while index>0:
        name=get_name()
        text=text[0:index-1]+name+text[index+2:]
        index = text.find('某某')

    text=replace2(text,'X')
    text =replace2(text, 'x')
    text =replace2(text, '×')

    index = text.find('某')
    while (index > 0):
        if text[index + 1] in number:
            name = get_name()
            text = text[0:index - 1] + name + text[index + 2:]
        else:
            name = get_name()
            text = text[0:index - 1] + name + text[index + 1:]
        index = text.find('某')
    return text


def splitSeqNum(text):
    s1 = re.sub(r'\d+\u3001', r'', text)  # 去除每行有"1、"类的问题
    s2 = re.sub(r'[一二三四五六七八九十]\u3001', r'', s1)  # 去除每行有"一、"类的问题
    s3 = re.sub(r'(^\d+\.)|(\d+\.(?!\d+))', r'', s2)  # 去除"1. "类的问题
    s4 = re.sub(r'\uFF08[一二三四五六七八九十]+\uFF09', r'', s3)  # 删除（ 与 ）(中文括号)包含的序号
    s5 = re.sub(r'\(\d+\)', r'', s4)  # 删除每行有"(1)"(英文类括号)类的问题
    s6 = re.sub(r'[①②③④⑤⑥⑦⑧⑨⑩]', r'', s5)  # 删除①等类的序号，但是文中的还没解决
    s7 = re.sub(r'\uFF08[12345678910]+\uFF09', r'', s6)  # 删除每行有"（1）"(中文类括号)类的问题
    # s8 = re.sub(r'物证', r'', s7)  # 删除"物证"
    # s9 = re.sub(r'书证', r'', s8)  # 删除"书证"
    # s10 = re.sub(r'证言', r'', s9)  # 删除"证言" ps上述删除三个词是文本内所有的词语
    s11 = re.sub(r'\n\d+\uff09', r'\n', s7)  # 去除开头2）这类的序号
    s12 = re.sub(r'\d+\.2016', r'2016', s11)  # 去除开头为2.2016...这类的序号
    s13 = re.sub(r'\n\uff09', r'\n', s12)  # 去除开头有）的
    s14 = re.sub(r'\n\)', r'\n', s13)  # 去除掉开头有英文)的
    s15 = re.sub(r'\n[\u2475\u2476\u2477]\u3001', '\n', s14)
    s16 = re.sub(r'\n\u2474\u3001', '\n', s15)
    s17 = re.sub(r'\n[\u2474\u2475\u2476\u2477\u2478\u2479\u247a]', '\n', s16)

    return s17


def smallerThan256(text):
    # 将一篇txt中处理到一行尽量小于256个字符，并且以句号分隔，返回一个重组的文本buffer
    s = text.replace('\n', '')
    sentence = re.split('。', s)
    sizeOfSen = len(sentence)  # number of sentences
    buffer = []
    new_content = ''
    for j in range(sizeOfSen):
        if len(sentence[j]) >= 256:
            new_content = '\n' + sentence[j] + '。' + '\n'
            buffer.append(new_content)
            new_content = ''
        else:
            if len(new_content) + len(sentence[j]) < 256:
                new_content = new_content + sentence[j] + '。'
                if j == sizeOfSen - 1:
                    buffer.append(new_content)
            else:
                buffer.append(new_content)
                new_content = '\n' + sentence[j] + '。'

    # 去除尾部两个句号
    buffer[len(buffer) - 1] = buffer[len(buffer) - 1][:-2]
    res=''
    res = res.join(buffer)

    return res


def process(text):
    # text1 =txt_strip(text)
    # text2 =partition(text1)
    # text3 =replace(text2)
    # text4 =splitSeqNum(text3)
    # print("success splitSeqNum？")
    # text5 =smallerThan256(text4)

    text = txt_strip(text)
    text = partition(text)
    text = replace(text)
    text = splitSeqNum(text)
    print("success splitSeqNum？")
    text = smallerThan256(text)
    return text



root=r'/Users/mac/Desktop/语料处理2/语料三'
write_root=r'/Users/mac/Desktop/语料处理2/语料3输出'

file_list=os.listdir(root)
print("总数：",len(file_list))
count=1
for i in file_list:
    fileName = os.path.split(i)[-1] # 去掉macbook中.DS的无用文件
    path=os.path.join(root,fileName)
    if os.path.split(i)[-1].startswith('.'):
        continue
    with open(path,encoding='GBK') as f:
        print(count)
        count+=1
        text=f.read()
        # 处理
        text = process(text)
        write_path = os.path.join(write_root,fileName)
        with open(write_path,mode='w',encoding='GBK') as wf:
            wf.write(text)



