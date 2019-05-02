import random
import os

# write_root=r'/Users/mac/Desktop/语料处理2/语料三'
# doc_list=os.listdir(r'/Users/mac/Desktop/语料处理2/jjynb/语料/语料3：裁定书/裁定书txt/desc')
# root=r'/Users/mac/Desktop/语料处理2/jjynb/语料/语料3：裁定书/裁定书txt/desc'

write_root=r'/Users/mac/Desktop/语料处理2/语料三2'
doc_list=os.listdir(r'/Users/mac/Desktop/语料处理2/jjynb-1/语料/语料3：裁定书/裁定书txt/desc')
root=r'/Users/mac/Desktop/语料处理2/jjynb-1/语料/语料3：裁定书/裁定书txt/desc'
for i in doc_list:
    fileName = os.path.split(i)[-1]  # 去掉macbook中.DS的无用文件
    new_root=os.path.join(root,fileName)
    if os.path.split(i)[-1].startswith('.'):
        continue
    new_list=os.listdir(new_root)
    for j in new_list:
        fileName2 = os.path.split(j)[-1]  # 去掉macbook中.DS的无用文件
        read_path=os.path.join(new_root,fileName2)
        if os.path.split(j)[-1].startswith('.'):
            continue
        with open(read_path,encoding='GBK') as f:
            write_path=os.path.join(write_root,fileName2)
            with open(write_path,mode='w',encoding='GBK') as wf:
                wf.write(f.read())
