1. 키보드로 정수를 입력받아 그것이 3의 배수인지 판단하세요.
-1 들어오면 끝.
while True:
    input_num = input("수를 입력하세요(종료 : -1) : ")

    if input_num.isdigit():
        input_num = int(input_num)

        if input_num % 3 == 0:
            print("3의 배수입니다.")
        else:
            print("3의 배수가 아닙니다.")
    else:
        print(input_num)
        if input_num == '-1':
            break

        print("정수가 아닙니다.")



2. 키보드로 정수 수치를 입력받아 짝수인지 홀수인지 판별하는 코드를 작성하세요.
while True:
    input_num = input("수를 입력하세요 : ")

    input_num = int(input_num)

    if input_num % 2 == 0:
        print("짝수")
    else:
        print("홀수")



3. 파이썬 경로명 s = '/usr/local/bin/python'에서 각각의 디렉토리 경로명을 분리하여 출력하세요.
s = '/usr/local/bin/python'

print(s[1:].split("/"))



3-1. 디렉토리 경로명과 파일명을 분리하여 출력하세요.
s = '/usr/local/bin/python'

file_name = s.find('python')

print(s[:file_name], s[file_name:])



4. 다음과 같은 텍스트에서 모든 태그를 제외한 텍스트만 출력하세요.
s = """
<html>
    <body style='background-color:#ffff'>
        <h4>Click</h4>
        <a href='http://www.python.org'>Here</a>
        <p>
        	To connect to the most powerful tools in the world.
        </p>
    </body>
</html>"""


flag = 0
s_list=[]

for s_letter in s :
    if s_letter is "<":
        flag = 1
        continue
    elif s_letter is ">":
        flag = 0
        continue

    if flag == 0:
        s_list.append(s_letter)

print(''.join(s_list))



5.1)다음 문자열을 모든 소문자를 대문자로 변환하고, 문자 ',', '.','\n'를 없앤 후에 중복없이 각 단어를 순서대로 출력하세요.
s = """We encourage everyone to contribute to Python. If you still have questions after reviewing the material
in this guide, then the Python Mentors group is available to help guide new contributors through the process."""

s = s.upper()
s = s.replace(",", "")
s = s.replace(".", "")
s = s.replace("\n", "")

s_list = s.split(" ")
sorted_s_set = sorted(set(s_list))

for s_word in sorted_s_set:
    print(s_word)



2)각 단어의 빈도수도 함께 출력해 보세요.
s = """We encourage everyone to contribute to Python. If you still have questions after reviewing the material
in this guide, then the Python Mentors group is available to help guide new contributors through the process."""

s = s.upper()
s = s.replace(",", "")
s = s.replace(".", "")
s = s.replace("\n", "")

s_list = s.split(" ")
sorted_s_set = sorted(set(s_list))

s_word_cnt = {s_word: s.count(s_word) for s_word in sorted_s_set}

for word_cnt in s_word_cnt:
    print(word_cnt, s_word_cnt[word_cnt])



6. 100까지 3의 배수의 개수와 배수의 합을 구하여 출력형태와 같이 출력하세요.
cnt = 0
sum = 0

for i in range(1, 101):
    if i % 3 == 0:
        cnt += 1
        sum += i

print("100까지의 3의 배수의 개수 -> ", cnt)
print("100까지의 3의 배수이ㅡ 합 ->", sum)



7. 키보드에서 정수로 된 돈의 액수를 입력 받아 오만 원권, 만원 권, 오천 원권, 천원 권, 500원짜리 동전, 100원짜리 동전, 50원짜리 동전, 10원짜리 동전, 1원짜리 동전 각 몇 개로 변환 되는지 작성하시오.
money = int(input("금액 : "))

unit_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10, 5, 1]
i = 0

while i < len(unit_list):
    if money >= unit_list[i]:
        unit_cnt = money // unit_list[i]
        print(unit_list[i], '원 : ', unit_cnt, '개')

        money -= unit_list[i] * unit_cnt

    else:
        print(unit_list[i], '원 : 0개')
    i += 1



8.키보드에서 5개의 정수를 입력 받아 리스트에 저장하고 평균을 구하는 프로그램을 작성하시오.
input_sum = 0

for i in range(1, 6):
    input_num = int(input("수 입력 : "))
    input_sum += input_num


print("평균 : ", input_sum / 5)



9.문자열을 입력 받아, 해당 문자열을 문자 순서를 뒤집어서 반환하는 함수 reverse(s)을 작성하세요.
def reverse(s):
    return s[::-1]

input_str = input("입력>")

print("출력>" , reverse(input_str))



10. 주어진 if 문을 dict를 사용해서 수정하세요.

11. 함수 sum 을 만드세요. 이 함수는 임의의 개수의 인수를 받아서 그 합을 계산합니다.

12. 반복문을 이용하여 369게임에서 박수를 쳐야 하는 경우의 수를 순서대로 화면에 출력해보세요. 1부터 99까지만 실행하세요.

13. 숫자를 입력 받아서 아래와 같은 실행결과가 나타나도록 코드를 완성하세요.

14. 숨겨진 카드의 수를 맞추는 게임입니다. 1-100까지의 임의의 수를 가진 카드를 한 장 숨기고 이 카드의 수를 맞추는 게임입니다. 아래의 화면과 같이 카드 속의 수가 57인 경우를 보면 수를 맞추는 사람이 40이라고 입력하면 "더 높게", 다시 75이라고 입력하면 "더 낮게" 라는 식으로 범위를 좁혀가며 수를 맞추고 있습니다. 게임을 반복하기 위해 y/n이라고 묻고 n인 경우 종료됩니다.

