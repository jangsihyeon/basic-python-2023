# if 문을 배워요
name = '시현'
state= '안아픔'

if name == '시현':
    print('진료실에서 담당의사를 만납니다.')
    if state == '아픔':
        print('선생님, 배가 아파요.')
        print('배 어디가 어떻게 아프십니까?')
    else:
        print('어디가 아프세요?')
        print('안아파요')
        print('그럼 왜 오신건가요?')
elif name == '다원':
    print('주사실로 가세요.')
else:
    print('조용히 기다립니다.')    