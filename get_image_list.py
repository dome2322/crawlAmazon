#coding=utf-8
#!/usr/bin/python

from bs4 import BeautifulSoup

def parserImageList(data,Enconding,limitation):
    soup = BeautifulSoup(data,fromEncoding=Enconding)
    images_item=soup.findAll('img',attrs={'alt':'Product Details','class':'s-access-image cfMarker'},limit=limitation)

    print 'number of images in this page is '+ str(len(images_item))
    return images_item
