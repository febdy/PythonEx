1. 가사 지우고 원하는 곳에 집어넣기
a = '''It’s 11:11
오늘이 한 칸이 채 안 남은 그런 시간
우리 소원을 빌며 웃던 그 시간
별 게 다 널 떠오르게 하지'''

# 첫 줄 '시간', 둘째 줄 '며 웃' 삭제
alist = list(a.split('\n'))
alist[1] = alist[1][ : -3]

str = '며 웃'
alist[2] = alist[2].replace(str, '')


# 붙이기
temp = [alist[1], ' 시간']
temp = ''.join(temp)
alist[1] = temp
del alist[2]

temp = alist[2]
temp = list(temp)
temp.insert(8, str)
temp = ''.join(temp)
alist[2] = temp

alist ='\n'.join(alist)
print(alist)

alist = '\n'.join(alist)
print(alist)

2. 나머지 소절 합치기
alist.append('''네 맘 끝자락처럼 차가운 바람
창을 열면 온통 네가 불어와
이 시간이 전부 지나고 나면
이별이 끝나 있을까 Yeah
널 다 잊었을까
모든 게 자릴 찾아서 떠나가고
넌 내 모든 걸 갖고서 떠나도
내 맘은 시계 속의 두 바늘처럼
같은 곳을 두고 맴돌기만 해
Na na na na na na na na
na na na na na oh
Na na na na na na na na
I believe I will be over you''')


3. things 리스트를 만들고 "mozzarella", "cinderella", "salmonella" 세 개의 문자열을 요소로 만들기
things = ["mozzarella", "cinderella", "salmonella"]

things
things.append('mozzarella')
things.append('cinderella')
things.insert(2, 'salmonella')


4. thins 리스트에서 사람 이름의 첫 글자를 대문자로 바꿔서 출력하기
things[0].capitalize()
things[1].capitalize()


5. things 리스트에서 salmonella 삭제하기
things.remove('salmonella')