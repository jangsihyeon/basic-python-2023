# 클래스 
class Person:
    name = '익명'
    height= ''
    gender= ''
    bloodtype='A'

    # 1. 생성자 추가  
    # def __init__(self):
    #     self.name='홍길동'
    #     self.height='169'
    #     self.gender='male'
    #     self.bloodtype='AB'

    def __init__(self, name='홍길동', height=169, gender='male') -> None:
        self.name = name
        self.height = height 
        self.gender = gender
    
    def walk(self): 
        print(f'{self.name}이(가) 걷습니다.')

    def run(self, option): 
        if option == 'Fast' :
            self.walk()
            print(f'{self.name}이(가) 빨리 뜁니다.')
        else:
            print(f'{self.name}이(가) 천천히 뜁니다.')

    def stop(self):
        print(f'{self.name}이(가) 멈춥니다.')

     # 2. 생성자 외 매직메서드(펑션) __str__
    def __str__(self) -> str:
         return f'출력 : 이름은 {self.name} 입니다.'

sihyeon = Person('시현', 170, 'female')   # 객체 생성 instance 
#sihyeon.name='시현'
#sihyeon.height='170'
#sihyeon.gender='female'
#sihyeon.bloodtype='RH+ AB'

print(f'{sihyeon.name}의 혈액형은 {sihyeon.bloodtype} 입니다.')

sihyeon.run('Fast')
print(sihyeon)

# 1. 초기화 후 객체 생성 
hong=Person('홍길동', 169, 'male')
hong.run('Slow')
print(hong)

print('=========================')
# 2.  파라미터를 받는 생성자 실행
ashely=Person('애슐리', 165, 'Female')
print(ashely.name)
print(ashely.height)
print(ashely.gender)
print(ashely)

