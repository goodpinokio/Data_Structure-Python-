#함수
#더하기 예제1
def add(a,b):
    return a+b

print(add(3,7))

#더하기 예제2
def add(a,b):
    print('함수의 결과:',a+b)

add(3, 7)

#global 키워드
a=0

def func():
    global a
    a+=1

for i in range(10):
    func()

print(a)

#배열 함수

array = [1,2,3,4,5]

def func():
    array = [3,4,5]
    array.append(6)
    print(array)

func()
print(array)

#여러 개의 반환 값
def operator(a,b):
    add_var = a+b
    subtract_var = a-b
    multiply_var = a*b
    divide_var = a/b
    return add_var,subtract_var,multiply_var,divide_var

a,b,c,d = operator(7, 3)
print(a,b,c,d)

#람다 표현식
def add(a,b):
    return a+b

#일반적인 add() 메서드 사용
print(add(3, 7))

#람다 표현식으로 구현한 add() 메서드
print((lambda a,b:a+b)(3,7))

array = [('홍길동',50),('이순신',32),('아무개',74)]

def my_key(x):
    return x[1]

print(sorted(array,key=my_key))
print(sorted(array, key=lambda x:x[1]))

#여러 개의 리스트에 람다 표현식
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

result = map(lambda a, b: a+b,list1,list2)

print(list(result))