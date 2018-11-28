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
k=d.split('\n')
trash=['50년','100년','150년','200년','250년','300년','350년','400년','450년','500년','550년','600년','650년','700년',
       '750년','800년','850년','900년','936년','950년','1000년','1050년','1100년','1150년','1200년','1250년','1300년',
       '1350년','1392년','1400년','1450년','1500년','1550년','1600년','1650년','1700년','1750년','1800년','1850년',
       '1875년','1897년','1900년','1910년','1920년','1930년','1940년']
for x in trash:
    k.remove(x)
    
print('''이 프로그램에는 한국사 연표가 저장되어 있고, 년도를 입력하면 어떤 사건이 일어났는지 알려주는 프로그램 입니다.
3년 부터 1943년 사이의 연도를 검색할 수 있으며 [0000년]형식으로  입력해 주세요 \n예)1592년''')
while True:
    user=input('년도 입력:')
    l= len(user)
    num=0
    if '년' not in user:
        print('형식을 잘못 입력하셨습니다.')
    else:    
        for i in k:
            if user == i[0:l]:
                print(i)
                num+=1
        if num==0:    
            print('해당 년도에 일어난 사건이 없습니다.')
    question=input('계속 검색하시겠습니까? 계속 검색을 원하면 n을  아무 키를 입력해주시고 그렇지 않으면 n을  눌러주세요.')
    if question=='n':
        break
    else:
        continue
print('이용해주셔서 감사합니다.')