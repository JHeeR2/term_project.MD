# term_project.MD
최종 파일인 project_code.py에 대한 설명이다. 
request와 encoding을 이용해 링크의 연표 데이터를 가져온다.
데이터를 원하는 부분만 슬라이싱을 이용해 자르고 필요없는 분은 지운다.
그 후 split을 이용해 데이터를 리스트 형식으로 저장한다.
데이터에는 아무 정보 없이 년도만 써저있는 정보가 있는데 이것은 필요하지 않은 부분이므로 이것을 trash라는 리스트에 저장한 후, remove를 이용해서 trash에 들어가 있는 요소들을 데이터에서 지운다.
프로그램에 대해 설명하는 문구를 맨 처음에 한번 출력한다.
년도 input을 받으면 input받은 내용과 그것의 길이를 조사한다. 길이를 조사해야 하는 이유는 이렇다.
예를 들어 800년에 어떤 사건이 일어났는지 검색을 한다 하자.만약 프로그램에서 길이를 조사하지 않고 숫자가 리스트의 원소 안에 포함되면 그것을 출력하도록 하면 800을 쳤을 때  800년에 일어난 사건뿐만 아니라 1800년대에 일어난 사건이 같이 출력이 된다. 그러므로 원하는 정보만 얻기 위해 input받은 것의 길이를 조사한다.
데이터는 [0000년 무슨 사건발생] 이런 형식으로 되어 있으므로 입력을 [0000년]으로 받아서 찾아야 한다. input받은 것에는 끝에 '년'이 꼭 들어가 있어야 한다. 그 이유는 앞서서 길이를 조사해야 하는 이유랑 비슷하다. 프로그램이 '년'을 입력하지 않아도 검색을 허용하면 다음과 같은 문제가 생긴다. 예를 들어 3년에 일어난 사건을 검색하고 싶을 때 '3'만 입력하면 3년에 일어난 사건 뿐만 아니라 300년대의 사건들이 모두 출력이 되어 버린다. 따라서 이 문제를 해결 하기 위해 input받은 내용에는 끝에 '년'이 꼭 붙어야 하고, 이것은 맨 처음에 프로그램에 대해 설명하는 문구에도 공지를 했다.
input 받은 것이 [0000년] 형식이 아니면 형식이 잘못되었다는 문구를 보낸다.
input 받은 것이 올바른 형식이면 리스트 원소들 중에 input 받은 정보가 포함된 것을 찾아서 있으면 그것을 프린트 하고 없으면 해당 년도에 일어난 사건이 없다고 프린트한다.
검색을 한번 했으면 계속 검색할지 여부를 묻고 'n'을 입력하면 프로그램을 끝내고 '이용해주셔서 감사합니다'를 출력하고 , 그 이외 아무 키를 입력받으면 계속 프로그램을 구동한다.
