1. ���� ����� ���ϴ� ���� ����ֱ�
a = '''It��s 11:11
������ �� ĭ�� ä �� ���� �׷� �ð�
�츮 �ҿ��� ���� ���� �� �ð�
�� �� �� �� �������� ����'''

# ù �� '�ð�', ��° �� '�� ��' ����
alist = list(a.split('\n'))
alist[1] = alist[1][ : -3]

str = '�� ��'
alist[2] = alist[2].replace(str, '')


# ���̱�
temp = [alist[1], ' �ð�']
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

2. ������ ���� ��ġ��
alist.append('''�� �� ���ڶ�ó�� ������ �ٶ�
â�� ���� ���� �װ� �Ҿ��
�� �ð��� ���� ������ ����
�̺��� ���� ������ Yeah
�� �� �ؾ�����
��� �� �ڸ� ã�Ƽ� ��������
�� �� ��� �� ���� ������
�� ���� �ð� ���� �� �ٴ�ó��
���� ���� �ΰ� �ɵ��⸸ ��
Na na na na na na na na
na na na na na oh
Na na na na na na na na
I believe I will be over you''')


3. things ����Ʈ�� ����� "mozzarella", "cinderella", "salmonella" �� ���� ���ڿ��� ��ҷ� �����
things = ["mozzarella", "cinderella", "salmonella"]

things
things.append('mozzarella')
things.append('cinderella')
things.insert(2, 'salmonella')


4. thins ����Ʈ���� ��� �̸��� ù ���ڸ� �빮�ڷ� �ٲ㼭 ����ϱ�
things[0].capitalize()
things[1].capitalize()


5. things ����Ʈ���� salmonella �����ϱ�
things.remove('salmonella')