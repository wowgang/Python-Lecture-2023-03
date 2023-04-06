'''
sys는 파이썬 표준 라이브러리에 포함된 모듈 중 하나로, 
파이썬 인터프리터의 동작과 관련된 정보를 제공합니다. 
sys 모듈은 파이썬 스크립트에서 인수(argument)를 읽어오거나, 
파이썬 인터프리터의 종료(exit) 등과 같은 동작을 수행할 수 있습니다.
'''

''' 
# sys 모듈의 주요 기능

sys.argv: 명령행 인수(argument)를 읽어올 수 있는 리스트입니다.
sys.exit(): 프로그램을 강제 종료합니다.
sys.path: 모듈을 찾을 때 검색할 경로(path)를 담고 있는 리스트입니다.
sys.stdin, sys.stdout, sys.stderr: 각각 표준 입력(stdin), 표준 출력(stdout), 표준 오류(stderr)에 대한 파일 객체입니다.

또한 sys 모듈을 사용하여 현재 실행 중인 파이썬 버전 정보나 운영체제 정보를 확인할 수 있습니다. 
이러한 정보는 프로그램이 실행되는 환경을 파악하는 데 유용합니다.
'''
import sys


print(sys.getwindowsversion)


print(len(sys.argv))
print(sys.argv)

while True:
    cmd = input('Prompt> ')
    if cmd == 'exit': # exit입력하면 빠져나간다
        sys.exit()      # 빠져나간다
    print(cmd)