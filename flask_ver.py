from flask import Flask, request
import requests 
import re
app=Flask(__name__)

@app.route("/")


def timeline():
    r=requests.get('https://ko.wikipedia.org/wiki/%ED%95%9C%EA%B5%AD%EC%82%AC_%EC%97%B0%ED%91%9C')
    r.encoding='utf-8'
    data=str(r.text)
    begin=data.find('3년 고구려가')
    end=data.find('1943년 카이로 선언 발표')
    end=end+len('1943년 카이로 선언 발표')
    d=data[begin:end]    
    d=re.sub('<.+?>','',d,0)
    k=d.split('\n')
    k.remove('50년')
    k.remove('100년')
    k.remove('150년')
    k.remove('200년')
    k.remove('250년')
    k.remove('300년')
    k.remove('350년')
    k.remove('400년')
    k.remove('450년')
    k.remove('500년')
    k.remove('550년')
    k.remove('600년')
    k.remove('650년')
    k.remove('700년')
    k.remove('750년')
    k.remove('800년')
    k.remove('850년')
    k.remove('900년')
    k.remove('936년')
    k.remove('950년')
    k.remove('1000년')
    k.remove('1050년')
    k.remove('1100년')
    k.remove('1150년')
    k.remove('1200년')
    k.remove('1250년')
    k.remove('1300년')
    k.remove('1350년')
    k.remove('1392년')
    k.remove('1400년')
    k.remove('1450년')
    k.remove('1500년')
    k.remove('1550년')
    k.remove('1600년')
    k.remove('1650년')
    k.remove('1700년')
    k.remove('1750년')
    k.remove('1800년')
    k.remove('1850년')
    k.remove('1875년')
    k.remove('1897년')
    k.remove('1900년')
    k.remove('1910년')
    k.remove('1920년')
    k.remove('1930년')
    k.remove('1940년')
    data=tuple(k)
    name=request.args.get('name')
    num=0
    l=len(str(name))
    for i in data:
        if str(name) in i[0:l]:
            num+=1
            return print (str(i))
    if num==0:
        return '해당 년도에 일어난 사건이 없습니다.'
print('start', flush=True)
