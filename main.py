import os, shutil, docx, sys
txt_file = open('script.txt', 'r', encoding='utf-8')
title =''
temp = []

def get_script(txt_file):
    lines = txt_file.read().splitlines()
    for line in lines:
        if line == '':
            lines.pop(lines.index(line))
    return lines



def format_txt(line):
    global title, temp
    keyword = {'标题':'script_title', '作者':'author', '日期' : 'date1', '简介标题':'abstract_title', '简介内容':'description', '人物名称':'character_title', '注释':'notes'}
    if "：" in line:
        temp_list = line.split('：')
        if temp_list[0] in keyword.keys():
            if temp_list[0] == '标题':
                title = temp_list[1]
            return temp_list[1], keyword[temp_list[0]]
        else:
            temp = [(temp_list[0], 'character'), (temp_list[1], 'dialogue')]
            return 0
    else:
        if line[0] in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            return line, 'scene'
        elif line[0] == '第' and line[2] == '章':
            return line, 'chapter_title'

        return line, 'action_description'

def write_dial():
    global temp
    for i in temp:
        print(i)
        write_docx(i, doc)

def prepare_docx():
    base_dir = os.path.dirname(__file__)  # 获取当前文件目录
    outfile = 'temp.docx'
    path = os.path.join(base_dir, outfile)  # path是需要把文件复制到的指定位置
    new_path = r'%s' % path  # 文件新名字
    origin_path = r'%s\format.docx' %(base_dir) # 原始文件完整目录
    shutil.copyfile(origin_path, new_path)

prepare_docx()
doc = docx.Document('temp.docx')


def write_docx(list, doc):
    doc.add_paragraph(list[0], style=list[1])



for line in get_script(txt_file):
    f = format_txt(line)
    if f == 0:
        write_dial()
    else:
        write_docx(f, doc)

doc.save("%s.docx" % title)