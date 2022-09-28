#조건문
#조건문 예제

x = 15

if x>=10:
    print("x>=10")

if x>=0:
    print("x>=0")

if x>=30:
    print("x>=30")

#반복문
i=1
result = 0

#i가 9보다 작거나 같을 때 아래 코드를 반복적으로 실행
while i<=9:
    result += i
    i+=1

print(result)

i=1
result = 0
#i가 9보다 작거나 같을 때 아래 코드를 반복적으로 실행
while i<=9:
    if i % 2 ==1:
        result+=i
    i+=1

print(result)

#range()함수 예제
result = 0

for i in range(1,10):
    result += i

print(result)

#파이썬의 continue 키워드

result = 0

for i in range(1,10):
    if i % 2 ==0:
        continue
    result += i

print(result)

#파이썬 break 키워드
i=1

while True:
    print("현재 i의 값:",i)
    if i == 5:
        break
    i+=1

#예제 학생들의 합격 여부 판단
scores = [90,85,77,65,97]
cheating_student_list = {2,4}

for i in range(5):
    if i+1 in cheating_student_list:
        continue
    if scores[i]>=80:
        print(i+1,"번 학생은 합격입니다")

#구구단 예제
for i in range(2,10):
    for j in range(1,10):
        print(i,"X",j,"=",i*j)
    print()