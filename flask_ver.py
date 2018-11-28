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
    trash=['50년','100년','150년','200년','250년','300년','350년','400년','450년','500년','550년','600년','650년','700년',
       '750년','800년','850년','900년','936년','950년','1000년','1050년','1100년','1150년','1200년','1250년','1300년',
       '1350년','1392년','1400년','1450년','1500년','1550년','1600년','1650년','1700년','1750년','1800년','1850년',
       '1875년','1897년','1900년','1910년','1920년','1930년','1940년']
    for x in trash:
        k.remove(x)
    name=request.args.get('name')
    num=0 
    for i in k:
        if name in i:
            return i
            num+=1
        if num==0:    
            return '해당 년도에 일어난 사건이 없습니다.'
