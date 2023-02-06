# 콘솔 출력 보충 
# 이스케이프 캐릭터(탈출 문자)
print('1. Hello. \r\n World')
print('2. Hello. \n World')    # 이걸 권장 

print('3. Hello. \n\t World')    # t 탭 
print('4. Hello. \n\t\b World')    # b 백스페이스 (한칸 앞으로)

print('5. Hello. \n\'World\'')    # \' 문자열 내 홑따옴표
print('6. Hello. \n"World"')    
print('7. Hello. \"World\"')

print('8. Hello. \\ World')    # \\ => \를 문자열에 표현하고 싶을때 (python만 \ 하나로 표현 가능)

print('9. Hello.\0')

# 문자열 포맷팅 - 구닥다리 
# %로 포맷코드를 시작
me='저'
name='장시현'
age=24
print('%s는 %s입니다. %d살 입니다.' %(me, name, age))

print( f'{254.112233:.2f}')    # 최신 방식 
print('%4.4f' %(254.112233))   # 구식 전체자리수.소수점자리수



