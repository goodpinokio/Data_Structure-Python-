#문자열 자료형

data = 'Hello World'
print(data)

data = "Don't you know \"Python\"?"
print(data)

#문자열 연산

a="Hello"
b="World"
print(a+" "+b)

a="String"
print(a*3)

a="ABCDEF"
print(a[2:4])

#튜플 자료형
#튜플은 한 번 선언된 값을 변경할 수 없다
#리스트는 대괄호([])를 이용하지만, 튜플은 소괄호()를 이용한다
#튜플은 리스트에 비해 상대적으로 공간 효율적이다

a=(1,2,3,4,5,6,7,8,9)

#네 번째 원소만 출력
print(a[3])

#두 번째 원소부터 네 번째 원소까지
print(a[1:4])

