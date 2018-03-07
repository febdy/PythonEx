1-1.
river_in_bracket = re.findall('[(].*[)]', river)
river_remove_bracket = []

for line in river_in_bracket:
    line = line.split(" ")

    for word in line:
        word = ''.join(re.findall('[a-zA-Z]', word))
        river_remove_bracket.append(word)

river_in_bracket = ' '.join(river_remove_bracket)

river_word_cnt = {word: river_in_bracket.count(word) for word in set(river_remove_bracket)}

river_keys = river_word_cnt.keys()

max = 0
max_key = ""
for key in river_keys:
    if river_word_cnt[key] >= max:
        max_key = key
        max = river_word_cnt[key]

print(max_key, " : ", max)



1-2.
river_in_bracket = re.findall('[(].*[)]', river)
river_remove_bracket = []

for line in river_in_bracket:
    line = line.split(" ")

    for word in line:
        word = ''.join(re.findall('[a-zA-Z]', word))
        river_remove_bracket.append(word)

river_in_bracket = ' '.join(river_remove_bracket)

river_word_cnt = {word: river_in_bracket.count(word) for word in set(river_remove_bracket) if 'v' in word}

print(river_word_cnt)



1-3.
river_list = river.split("\n")
river_even_list = []

flag = 1
for line in river_list:
    if flag == 0:
        river_even_list.append(line.upper())
        flag += 1
    else:
        flag -= 1

dict_keys = dic.keys()
dict_values = dic.values()

dict_list = list(zip(dict_keys, dict_values))

river_morse = []

for line in river_even_list:
    for character in line:
        for i in range(0, 26):
            if character == dict_list[i][1]:
                river_morse.append(dict_list[i][0])


river_morse = ''.join(river_morse)
print(river_morse)



2번
# 2조 문제 


#영단어 , 영단어 외 가사에서 각각 몇퍼 차지하는지 (소숫점 자리 제외)

str_re = str.replace('\n', ' ')

str_split = str_re.split()

str_len = len(str_split) - 1

# print('전체 단어 리스트 : ' , str_len)

eng_wordsList = []

for eng_words in str_split:

    if re.findall('[a-zA-Z]', eng_words):

        eng_wordsList.append(eng_words)

 

# print('영단어 리스트 : ', eng_wordsList)

eng_wordsListLen = len(eng_wordsList) - 1

eng_wordsListSize = ("%.2f%%" % (eng_wordsListLen / str_len * 100.0))

eng_wordsListSizeNum = eng_wordsListSize.find('.')

eng_wordsListInt = int(eng_wordsListSize[0:eng_wordsListSizeNum])

 

kor_wordsListInt = 100 - eng_wordsListInt;

print('==================1번 문제 정답==================')

print('kor_wordsListInt 비율 : ' , kor_wordsListInt)

print('eng_wordsListInt 비율 : ' , eng_wordsListInt)

 

# 'Beverly ills' 몇번 반복 횟수

word_loopCnt = len(re.findall('Beverly ills', str))

print('==================2번 문제 정답==================')

print('Beverly ills 반복 횟수 : ' , word_loopCnt)

 

# 가사에 등장한 숫자 다 더하기

str_re = str.replace('\n', ' ')

str_split = str_re.split()

# print('전체 단어 리스트 : ' , str_len)

num_wordsList = []

sum = 0

for num_words in str_split:

    # print(num_words)

    m = re.findall('\d+', num_words)

    # num_wordsList.append(

    if len(m) != 0 :

        # print(m)

        sum+=int(m[0])

print('==================3번 문제 정답==================')

 

print('sum 값 : ' , sum)


3-1.
>>> num = re.findall('[1-4].*', '\n'.join(str), re.MULTILINE)  //리스트형태를 다시 문자열로 바꾸는것
 ( 이렇게 해도됨 > 원래문자열 형태만 넣은것  :    num = re.findall('[1-4].*', song)   )
>>> num
['1 초라도 안 보이면 ', '2 이렇게 초조한데', '3 삼초는 어떻게 기다려 이야이야이야이야', '4 사랑해 널 사랑해 ', '10 십년이 가도 너를 사랑해']
>>> del num[-1]
>>> num
['1 초라도 안 보이면 ', '2 이렇게 초조한데', '3 삼초는 어떻게 기다려 이야이야이야이야', '4 사랑해 널 사랑해 ']



4-1.
import re
import string

so_hot = '''I'm so hot 난 너무 예뻐요
I'm so fine 난 너무 매력 있어 
I'm so cool 난 너무 멋져
'''

eng = re.findall('[a-zA-Z].*[a-zA-Z]', so_hot, re.MULTILINE)
kor = re.findall('[가-힣].*[가-힣]', so_hot, re.MULTILINE)

for eng_ly, kor_ly in set(zip(eng, kor)):
    print(eng_ly, kor_ly)


4-2.



4-3.


