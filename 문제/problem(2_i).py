#정수 N이 입력되면 00시 00분 00초 부터 N시 59분 59초까지 3이 포함 되는 경우의 수 구하기

#h 입력받기
h= int(input())

count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            #매 시간 안에 3 이 포함되ㅏ어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count+=1


print(count)
