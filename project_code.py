import os
os.chdir('C:\\Users\\LG\\Desktop')

import requests 
import re
r=requests.get('https://ko.wikipedia.org/wiki/%ED%95%9C%EA%B5%AD%EC%82%AC_%EC%97%B0%ED%91%9C')
r.encoding='utf-8'
data=str(r.text)
begin=data.find('3년 고구려가')
end=data.find('1943년 카이로 선언 발표')
end=end+len('1943년 카이로 선언 발표')
d=data[begin:end]    
d=re.sub('<.+?>','',d,0)
data1=d.split('\n')
trash=['50년','100년','150년','200년','250년','300년','350년','400년','450년','500년','550년','600년','650년','700년',
       '750년','800년','850년','900년','936년','950년','1000년','1050년','1100년','1150년','1200년','1250년','1300년',
       '1350년','1392년','1400년','1450년','1500년','1550년','1600년','1650년','1700년','1750년','1800년','1850년',
       '1875년','1897년','1900년','1910년','1920년','1930년','1940년']
for x in trash:
    data1.remove(x)

with open('eastern_history.txt','r') as f:
    second=f.read()
    
data2=second.split('\n')    

with open ('world_history.txt', 'r') as f:
    third=f.read()
    
data3=third.split('\n')

    
print('''이 프로그램에는 한국사, 동양사, 세계사 연표가 저장되어 있고, 년도를 입력하면 어떤 사건이 일어났는지 알려주는 프로그램 입니다.
3년 부터 1943년 사이의 연도를 검색할 수 있으며 [0000년]형식으로  입력해 주세요 \n예)1592년\n 만일 검색을 그만두고 싶으면 'n'을 입력하세요. ''')
while True:
    user=input('년도 입력:')
    l= len(user)
    num1=0
    num2=0
    num3=0
    if user=='n':
        break
    elif '년' not in user:
        print('형식을 잘못 입력하셨습니다.')
        continue
    else:    
        for i in data1:
            if user == i[0:l]:
                korea=i
                num1+=1
            if num1==0:    
                korea='해당 년도에 일어난 사건이 없습니다.'
            
        for x in data2:
            if user == x[0:l]:
                east=x
                num2+=1
            if num2==0:    
                east='해당 년도에 일어난 사건이 없습니다.'
            
        for a in data3:
            if user == a[0:l]:
                world=a
                num3+=1
            if num3==0:    
                world='해당 년도에 일어난 사건이 없습니다.'
        print('한국사:', korea)
        print('동양사:', east)
        print('세계사:', world)
        continue

    
print('이용해주셔서 감사합니다.')
