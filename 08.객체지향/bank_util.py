import datetime as dt
from account import Account
# 이름과 금액을 입력으로 받아서 account에 새로운 항목을 추가

def create_account(acc_list):
    try:   
        cmd = input('이름 금액> ').split()
        name, amount = cmd[0], int(cmd[1])
    except:
        print('입력이 잘못되었습니다.')
        return   
    now = dt.datetime.now()
    ano = now.strftime('%H%M%S')
    account = Account(ano, name, amount) # 객체만들기
    acc_list.append(account) # 객체 집어넣기
    return


# 계좌번호와 금액을 입력으로 받아서 계좌의 금액을 추가
def deposit(acc_list):
    try:
        cmd = input('계좌번호 금액> ').split()
        ano, amount = cmd[0], int(cmd[1])
    except:
        print('입력이 잘못되었습니다.')
        return   
    for acc in acc_list: # acc는 딕셔너리 {'계좌번호': '142603', '소유주':' 홍길동', '잔액': 10000 }
        if ano == acc.ano: # acc는 -Account의 인스턴스
            acc.deposit(amount)
            return 

#  계좌번호와 금액을 입력으로 받아서 계좌의 금액을 인출
def withdraw(acc_list):
    try:
        cmd = input('계좌번호 금액> ').split()
        ano, amount = cmd[0], int(cmd[1])
    except:
        print('입력이 잘못되었습니다.')
        return   
    for acc in acc_list:
        if ano == acc.ano:
            acc.withdraw(amount)
            return
        
        

            