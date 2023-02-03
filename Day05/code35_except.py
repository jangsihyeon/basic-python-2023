# 예외 처리 

def add (a, b):
    return a + b

def mul (a, b):
    return a * b
    
def div (a, b):
    return a / b

try:    
    x, y = (input('두 수를 입력하세요 > ').split())
    x=int(x)
    y=int(y)
except Exception as e:
    print(e)
    exit()
finally:
    print('계속되나요?!')  

# 원시적인 예외처리 
# if y == 0:
#     print('0을 넣지 마세요.')
#     exit()

print('계산 테스트')

try:
    print(div(x,y))  
except ZeroDivisionError as e:
    print('0으로 놔두면 안됩니다.')    
except Exception as e:              # 예외 처리 문장에서 제일 마지막에 있어야함 ..! 
    print(e) 
    exit()
finally:
    print('계산은 계속됩니다!')   

print(add(x,y))  
print(mul(x,y))  

