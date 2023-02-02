import os
import code

# 자동차 클래스 
class Car:
    __number = '54라9538'

    def get_number(self):
        return self.__number

    # 클래서 외부에서는 변경 x , 멤버 함수로는 내부를 조작 o
    def set_number(self, number):
        self.__number = number

    def __init__(self, number='54라9538') -> None:
        print('__init__')
        self.__number=number

    # def __new__(cls): 
    #     print('__new__')
    #     return super().__new__(cls)  # 부모 클래스 (상속)     # ctrl+k+c 전부 다 주석처리

    def __str__(self) -> str:
        return f'차 번호는 {self.__number}'

yourcar = Car(number='88호7645')
print(yourcar)
yourcar.__number='54라9999'   # ※ 외부에서는 멤버 변수에 접근 불가 ※
print(yourcar)    # <내가따로> 차번호 안바뀜 -> 함부로 바꿀수 없음(=캡슐화 / 돈 안넣고 자판기에서 음료뽑을수? -> no )
print('클래스 내부 함수 사용 !')
yourcar.set_number('55오5555')  
print(yourcar)    # <내가따로> 차번호 바뀜 

mycar = Car()
print(mycar)
print(f'제 차는 아이오닉에 번호가 {mycar.get_number()} 예요.')

mycar.__number='132거8874'
print(mycar.get_number())
print(mycar)




