#coding=utf-8
#!/usr/bin/python

import os
import url2md5
import time

def writeTextToFile(word_text_path,classlabel,image_url,title,description_meta,title_meta,keywords_meta):

    creat_time=time.strftime('%Y-%m-%d',time.localtime(time.time()))
    word_txt_file = open(word_text_path+creat_time+classlabel+".txt",'a')

    #write text into .txt file
    word_id=url2md5.getMD5(image_url)
    word_txt_file.write(word_id+'\n')

    word_txt_file.write('title'+'\t'+title.get_text()+'\n')

    if len(description_meta)==0:
    	pass
    else:
    	word_txt_file.write('description_meta'+'\t'+description_meta[0].get('content')+'\n')

    if len(title_meta)==0:
    	pass
    else:
    	word_txt_file.write('title_meta'+'\t'+title_meta[0].get('content')+'\n')

    if len(keywords_meta)==0:
    	pass
    else:
    	word_txt_file.write('keywords_meta'+'\t'+keywords_meta[0].get('content')+'\n')

    word_txt_file.close()
