#coding=utf-8
#!/usr/bin/python

import os
import url2md5
import cookielib
import urllib2,urllib

#writeImageToFile
def saveImage2folder(image_url,image_folder_path):
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    opener.addheaders = [('Host',"amazon.com"),('User-agent','Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)'),('Connection','Keep-Alive'),] 
    image_content = opener.open(image_url).read()
    image_name=url2md5.getMD5(image_url)
    home_path=unicode(image_folder_path,'ascii')
    with open(home_path+'/'+str(image_name)+'.jpg','wb') as code:
        code.write(image_content)
