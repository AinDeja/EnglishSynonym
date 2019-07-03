import requests,json
from bs4 import BeautifulSoup

def get_word_about(word):
    #part_of_speech list词性
    part_of_speech_list=[]
    #part_of_speech chinese_list词义
    part_of_speech_chinese_list=[]
    #syno_word_chinese_list词性+词义
    syno_word_chinese_list=[]
    #syno_word_list同义词
    syno_word_list=[]
    #root_chinese
    root_chinese=''
    # main body
    #while word != 'q': # 'q' to exit
    try:
        # 利用GET获取输入单词的网页信息
        r = requests.get(url='http://dict.youdao.com/w/%s/#keyfrom=dict2.top'%word)
        # 利用BeautifulSoup将获取到的文本解析成HTML
        soup = BeautifulSoup(r.text, "lxml")
        # 获取字典的标签内容
        s = soup.find(class_='trans-container')('ul')[0]('li')
        #获取同近义词标签内容[词性和汉语解释]
        syno_chinese_and_sp=soup.find(id='synonyms')('ul')[0]('li')
        # 获取同近义词标签内容[相近单词]
        syno_words = soup.find(id='synonyms')('ul')[0].find_all('p')
        #(id='synonyms')('ul')[0]('li')[0]('p')('span')[0]('a')
        # 输出字典的具体内容
        for item in s:
            if item.text:
                root_chinese=root_chinese+item.text+"   "
        #        print(item.text)
        #print('='*40+'\n')
        for item in syno_chinese_and_sp:
            if item.text:
                #print(item.text)
                #part_of_speech_list.append(item.text.split('.')[0]) #分割词性
                #part_of_speech_chinese_list.append(item.text.split('.')[1].strip()) #分割同义词释义
                syno_word_chinese_list.append(item.text.split('.')[0]+item.text.split('.')[1].strip())
            #part_of_speech_list.append("|")
            #part_of_speech_chinese_list.append("|")
            syno_word_chinese_list.append("|")
        #print('='*40+'\n')
        for item in syno_words:
            spanlist=item.find_all('span')
            for wordlist in spanlist:
                word_=wordlist.find_all('a')[0]
                if word_.text:
                    #print(word_.text)
                    syno_word_list.append(word_.text)
            syno_word_list.append("|")
        #print(part_of_speech_list)
        #print(part_of_speech_chinese_list)
        #print(syno_word_chinese_list)
        #print(syno_word_list)
        #part_of_speech_list.clear()
        #part_of_speech_chinese_list.clear()
        #syno_word_list.clear()
        # part_of_speech_list.pop()
        # part_of_speech_chinese_list.pop()
        syno_word_chinese_list.pop()
        syno_word_list.pop()

        all_list = [syno_word_chinese_list, syno_word_list, root_chinese]
        json_list = json.dumps(all_list)
        return json_list
    except Exception:
        print("Sorry, there is a error!\n")


