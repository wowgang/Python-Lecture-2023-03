PI = 3.1415926535

def number_input():
    return float(input('숫자 입력> '))

def get_circumference(radius): # 원둘레
    return 2 * PI * radius

def get_area(radius): # 면적
    return PI * radius

def print_name():
    print(__name__)

# python test_module.py 와 같이 돌릴 경우에는 아래 코드가 실행됨
if __name__ == '__main__':
    print(f'원의 반지름: 10'), 
    print(f'원 둘레: {get_circumference(10)}, 원 면적: {get_area(10):.4f}')