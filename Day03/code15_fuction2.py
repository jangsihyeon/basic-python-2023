# 함수 
# 함수 정의 - 이건 실행이 아님 
# 함수 만드는 방법 4가지 
# 1. 파라미터 0 리턴 0
# 2. 파라미터 0 리턴 x
# 3. 파라미터 x 리턴 0
# 4. 파라미터 x 리턴 x

def add(x, y):
    result = x + y
    print(result)
    #return    # 생략가능한 return : 값을 return 안해서 

def sub(x, y):
    result= x-y
    print(result)
    

def mul(x, y):
    result=x*y
    print(result)
    

def div(x,y):
    result=x//y
    print(result)
    

def hello():
    print('Hello~!!')
    

def hello2():
    msg='hello, hello'
    return  msg

#함수 호출
hello()

print(hello2())

add(1024, 5)

sub(1024, 1000)

mul(512, 2)

div(108, 10)

