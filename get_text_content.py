#coding=utf-8
#!/usr/bin/python

from bs4 import BeautifulSoup

def parserTextPage(data,Enconding):
    soup = BeautifulSoup(data,fromEncoding=Enconding)

    #text_page    
    title=soup.find('title')
    description_meta=soup.findAll('meta',attrs={'name':'description'})
    title_meta=soup.findAll('meta',attrs={'name':'title'})
    keywords_meta=soup.findAll('meta',attrs={'name':'keywords'}) 
    return (title,description_meta,title_meta,keywords_meta)
