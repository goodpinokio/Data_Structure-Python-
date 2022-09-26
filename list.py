#리스트 자료형

a=[7,3,2,5,9]
#  0 1 2 3 4

print(a)

a[4] = 4
print(a)

a=[1,2,3,4,5,6,7,8,9]

# 네 번째 원소만 출력
print(a[3])

#두 번째 원소부터 네 번째 원소까지
print(a[1:4])

#0부터 9까지의 수를 포함하는 리스트
array = [i for i in range(10)]
print(array)

#리스트 컴프리헨션
#N * M 크기의 2차원 리스트 초기화
n=4
m=3
array = [[0]*m for _ in range(n)]
print(array)

#파이썬에서는 반복을 수행하되 반복을 위한 변수의 값을 무시하고자
#할 때 언더바(_) 자주사용
# EX
summary = 0
for _ in range(5):
    print("Hello World")

a = [1,4,3]
print("기본 리스트:",a)

# 리스트에 원소 삽입
a.append(2)
print("삽입:",a)

# 오름차순 정렬
a.sort()
print("오름차순 정렬:",a)

# 내림차순 정렬
a.sort(reverse=True)
print("내림 차순 정렬:",a)

a = [4,3,2,1]

#리스트 원소 뒤집기
a.reverse()
print("원소 뒤집기:",a)

#특정 인덱스에 데이터 추가
a.insert(2, 3)
print("인덱스 2에 3추가:",a)

#특정 값인 데이터 개수 세기
print("값이 3인 데이터 개수:",a.count(3))

#특정 값 데이터 삭제
a.remove(1)
print("값이 1인 데이터 삭제:",a)
