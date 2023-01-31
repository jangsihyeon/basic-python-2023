# 연산자
# 할당 연산 assignment
# 2 = 1 (x)
val=1 

# equal 연산자 
print(1==1)

# 사칙연산
print(1+1)
print(1-1)
print(10*10)
print(1024/2)   # 소수 나누기 
print(1024//2)  # 정수 나누기 
print(6//3)
print(6%3)      # 나머지 

# print(6/0)    # 무한대를 인식 못함    
# print(6//0)            "

print(2**10) # 2의 10승

#문자열 연산 
first='Hello'
second='World'
print(first+second)
print(first+' '+second)
print(first, second)

print(first*4)

# 문자열 길이 
print(len(first))
print(first[0])
print(first[1])
print(first[2])
print(first[3])
print(first[4])
# print(first[5]) # IndexError  

# 파이썬에서 인덱스를 찾는 특이한 방법 
print(first[-1])
print(first[-2])
print(first[-3])
print(first[-4])
print(first[-5])

# 리스트 자르기 
current = '2023-01-31 15:14:02' # 현재시간
print(len(current))
print(current[0:4])
print(current[5:7])
print(current[8:10])
print(current[11:13])
print(current[14:16])
print(current[17:])

print(current[-19:-15])
print(current[-19:4])   # 위랑 똑같음 

# 리스트 연산 
que=[1,2,3,4,5]
que[0]=7

print(que)

# que[5]=10      # 리스트는 이런 방식으로 값 추가 불가 
que.append(10)   # append로 맨 마지막 변수 추가 가능 
print(que)     

que.insert(3, 99)  #insert 는 내가 원하는 자리에 변수 추가 가능 
print(que)

que.remove(10)    # 해당 값 삭제 
print(que)
que.remove(99)
print(que)

# tup= (1,2,3,4,5)
# tup[1]=9          # 튜플은 한번 만들면 연산 불가 

# 문자열 리스트 
title = 'python'
print(title[0])

# title[0]='P'     # 문자열에서는 값 변경 x
print('P'+title[1:])

text = ['p', 'y','t','h', 'o','n']
print(text)
text[0]='P'
print(text)

# 문자열 포맷팅
print("I'm so happy {0} you, {1}!!".format(2, 'Hey'))
# 최신식 문자열 포맷팅 
preword=2
sayHello= 'Hey'
print(f"I'm so happy {preword} you, {sayHello}!!")

pi=3.141592
print(f'파이는 {pi}입니다.')
print(f'파이는 {pi:0.2f}입니다.')
print(f'파이는 {pi:10.3f}입니다.')

# 문자열을 특정 문자로 자르기 
full_name='Jang S.i Hyeon'
vals=full_name.split()   # 스페이스
print(type(vals))
print(vals)

vals=full_name.split('.') # . 으로 지정 
print(vals)

print(full_name.replace('jang', 'kim'))

# 문자열 공백 없애기 
hi= '          Hello~ Bye~          '
print(hi.lstrip()+'|')
print(hi.rstrip()+'|')
print(hi.strip()+'|')

print(full_name.index('H'))

print(full_name.find('z'))  # index는 없는 값은 안나옴(error), find는 없으면 -1 출력 
print(full_name.find('H'))

# 찾는 단어의 개수를 알려줌
print(full_name.count('n'))

# 모든 단어 대문자/소문자로 변경
print(full_name.upper())
print(full_name.lower())

# 연산자 우선순위 
print(3+4*2)
print((3+4)*2)

