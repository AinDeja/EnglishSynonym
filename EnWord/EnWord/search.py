# -- coding: utf-8 --
from django.shortcuts import render
from django.views.decorators import csrf
from . import get_word_by_youdao
import json


# 接收POST请求数据
def search_post(request):
    root_word=request.POST['input_word']
    json_word=json.loads(get_word_by_youdao.get_word_about(request.POST['input_word']))
    syno_chinese=json_word[0]
    #print(syno_chinese)
    syno_word=json_word[1]
    root_word_chinese=json_word[2]
    syno_word_dict={'id':'','pid':'','topic':''}
    syno_word_json_list=[]
    child_chinese_num=1
    child_word_num=1
    for child_chinese in syno_chinese:
        if(child_chinese=="|"):
            child_chinese_num+=1
        else:
            syno_word_dict['id']='c'+str(child_chinese_num)
            syno_word_dict['pid']='root'
            syno_word_dict['topic']=child_chinese
            #print(syno_word_dict)
            syno_word_json_list.append(json.dumps(syno_word_dict, ensure_ascii=False)) #ensure_ascii=False解决中文乱码
        syno_word_dict.clear()
    child_chinese_num = 1
    for child_word in syno_word:
        if(child_word=="|"):
            child_chinese_num+=1

        else:
            syno_word_dict['pid'] = 'c' + str(child_chinese_num)
            syno_word_dict['id']=syno_word_dict['pid']+'w'+str(child_word_num)
            syno_word_dict['topic']=child_word
            child_word_num += 1
            #print(syno_word_dict)
            syno_word_json_list.append(json.dumps(syno_word_dict, ensure_ascii=False))
        syno_word_dict.clear()
    #print(syno_word_json_list)
    ctx = {}
    if request.POST:
        #ctx['rlt'] = request.POST['input_word']
        ctx['root_word']=root_word
        ctx['root_word_chinese']=root_word_chinese
        ctx['rlt']=json.loads(get_word_by_youdao.get_word_about(request.POST['input_word']))
        ctx['list']=syno_word
        ctx['mind_map_data']=syno_word_json_list
    return render(request, "index.html", ctx)