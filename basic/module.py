# 모듈
# 함수, 변수, 클래스를 모아 놓은 파이썬 파일

# math 모듈 전체 import
# import math
# import sys

# print(math.sqrt(16))
# print(sys.builtin_module_names)

# 부분 import : 바로 메소드 호출 가능
from math import sin, cos, floor, ceil

print(sin(1))
print(cos(1))
print(floor(1))
print(ceil(1))

from random import random, uniform, randrange, choice, shuffle, sample

print(random())  # 0 ~ 1미만 random 난수 생성
print(uniform(10, 20))  # 범위 내 난수(float) 생성
print(randrange(10, 21))  # 범위 내 정수
print(choice([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # 하나 골라
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
shuffle(list1)  # 섞기
print(list1)
print(sample(list1, 2))  # 샘플 안에서 ?개 골라

# 별칭
import math as m

print(m.ceil(m.pi))

# 커스텀 모듈 호출
import prt

prt.prt1()
prt.prt2()

import sum1

print(sum1.add(8, 2))

num1 = sum1.number_input()
print(sum1.get_circ(num1))
print(sum1.get_area(num1))

# import calc
from calc import Calc

# calc1 = calc.Calc(5, 8)
calc1 = Calc(59, 2)
print(calc1.add())
print(calc1.sub())
print(calc1.mul())
print(calc1.div())
