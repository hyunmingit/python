"""
날짜 : 2022/01/04
이름 : 장현민
내용 : 파이썬 조건문 연습문제
"""
count = 0
for i in range(1, 10):

    if i <= 5:
        count += 1
    else:
        count -= 1
    for j in range(5-count):
        print(' ', end='')

    for k in range(count*2 -1):
        print('*', end='')

    print()

