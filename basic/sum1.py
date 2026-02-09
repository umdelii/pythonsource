def add(a, b):
    return a + b


PI = 3.141592


def number_input():
    output = input("숫자 입력")
    return float(output)


def get_circ(radius):
    return 2 * PI * radius


def get_area(radius):
    return PI * (radius**2)


# 함수 확인
if __name__ == "__main__":
    print("module 내부", get_circ(4))
    print("module 내부", get_area(4))
