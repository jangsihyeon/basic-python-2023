# 글자 인코딩 
# ASCII -> 한 단어를 표헌하는 체계(영어)
# Unicode(UTF-8)-> 모든 나라 언어 표현 가능  

# 파일 만들기 
file = open('../sample07.txt', 'w', encoding='UTF-8')  # 파일쓰기로 만듦

file.write('안녕하세요~ \n')
file.write('와~두번째 파일입니다\n')
file.write('절대경로에 파일이 생성 될겁니다.\n')

file.close()
print('sample07.txt 가 생성되었습니다.')

# 파일 / 폴더 경로 
