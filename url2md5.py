#coding=utf-8
#!/usr/bin/python

import hashlib

#md5
def getMD5(url):
    myMd5=hashlib.md5()
    myMd5.update(url)
    myMd5_Digest=myMd5.hexdigest()
    return myMd5_Digest
