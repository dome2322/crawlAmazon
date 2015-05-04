#coding=utf-8
#!/usr/bin/python

import os

from bs4 import BeautifulSoup
import cookielib,hashlib
import urllib2,urllib,os,time,random
import socket

import url2md5
import get_page_content as getPage
import get_image_list as getImageList
import write_image2folder as saveImage
import check_folder_exists as checkPath
import get_text_content as getText
import write_text2file as saveText

current_path=os.getcwd()

# set parameters
limitation=50
classlabel='amazon'
image_folder_path=current_path+'/'+classlabel+'/'
word_text_path=image_folder_path
amazon_url='http://www.amazon.com/s/ref=sr_pg_'+str(pageNumber)+'?fst=as%3Aoff&rh=n%3A172282%2Cn%3A541966%2Cn%3A193870011%2Cn%3A572238%2Ck%3Acomputer&page='+str(pageNumber)+'&keywords=computer&ie=UTF8&qid=1430636803&spIA=B00PWMQKXC,B00PJ6OQWI,B00PJ6ZDS4'
amazonEnconding='iso-8859-1'

Enconding=amazonEnconding
failUrl=[]

for pageNumber in range(1,61):
    socket.setdefaulttimeout(120)
    print '=============================='
    try:        
        print 'the number of page is '+str(pageNumber)
        userid=str(random.randint(1000,9999))
        url=amazon_url
        print url
        page=getPage.getPageContent(url)
        image_list=getImageList.parserImageList(page,Enconding,limitation)
        checkPath.checkFolderExists(image_folder_path)
        if len(image_list)==0:
            failUrl.append(url)
        else:
            for i in range(0,len(image_list)):
                try:
                    # get images
                    try:
                        image_url=image_list[i].get('src')
                        saveImage.saveImage2folder(image_url,image_folder_path)
                        print 'first crawl image ok'
                    except:
                        print 'first crawl image error'

                    # get words
                    try:
                        pageUrl=image_list[i].parent.get('href')
                        if pageUrl==None:
                            pageUrl=image_list[i].parent.parent.get('href')
                        else:
                            pass                            
                        page_product=getPage.getPageContent(pageUrl)
                        (title,description_meta,title_meta,keywords_meta)=getText.parserTextPage(page_product,Enconding)
                        saveText.writeTextToFile(word_text_path,classlabel,image_url,title,description_meta,title_meta,keywords_meta)
                        print 'first crawl text ok'
                        # print pageUrl
                    except:
                        print 'first crawl text error'
                        print pageUrl

                    # os.system('pause')
                    print '+++++++++++++++++first crawl +++++++++++++++++++'
                    
                except:
                    print "+++++++++++++++++first time to crawl error+++++++++++++++++"
                    print pageUrl
    except:
        print 'first time to crawl exception'

while len(failUrl)>0:
    for num in range(0,len(failUrl)):
        try:
            finalTargetURL=failUrl[num]
            print '%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
            print finalTargetURL
            print '%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
            page=getPage.getPageContent(finalTargetURL)
            image_list=getImageList.parserImageList(page,Enconding,limitation)
            if len(image_list)>0:
                failUrl.remove(finalTargetURL)
                for i in range(0,len(image_list)):
                    try:
                        # get images
                        try:
                            image_url=image_list[i].get('src')
                            saveImage.saveImage2folder(image_url,image_folder_path)
                            print 'try to crawl image ok'
                        except:
                            print 'try to crawl image error'

                        # get words
                        try:
                            pageUrl=image_list[i].parent.get('href')
                            if pageUrl==None:
                                pageUrl=image_list[i].parent.parent.get('href')
                            else:
                                pass
                            page_product=getPage.getPageContent(pageUrl)
                            (title,description_meta,title_meta,keywords_meta)=getText.parserTextPage(page_product,Enconding)
                            saveText.writeTextToFile(word_text_path,classlabel,image_url,title,description_meta,title_meta,keywords_meta)
                            print 'try to crawl text ok'
                            # print pageUrl
                        except:
                            print 'try to crawl text error'
                            print pageUrl
                        # os.system('pause')
                        print '**********************try to crawl***********************'
                    except:
                        print '**********************try to crawl error**********************'
            else:
                pass
        except:
            print 'fail to crawling '
print 'crawler ok'
