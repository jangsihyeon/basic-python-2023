# # 다중 입력 
# x, y =input('두 영단어를 입력하세요. > ').split()

# print(x)
# print(y)

# 완전 다중입력(개수 상관 없음)
# 중요 !!
inputs = list(map(str, input('단어를 입력하세요(개수 상관 없음) > ').split()))

print(inputs)

inputs = list(map(int, input('정수를 입력하세요(개수 상관 없음) > ').split()))

print(inputs)