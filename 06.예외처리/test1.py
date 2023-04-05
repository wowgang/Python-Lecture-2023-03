'''
for i in range(1, 101):
    sum += i
    print(sum)
TypeError: unsupported operand type(s) for +=: 'builtin_function_or_method' and 'int'
'''


sum = 0
for i in range(1, 101):
    sum += i
print(sum)


'''
fruits = ['감','밤','배']
print(fruits[3])
IndexError: list index out of range 
0,1,2 까지 있어서
'''
# 예외처리

fruits = ['감','밤','배']
try:
    print(fruits[3])
except:
    print('IndextError 예외 발생')
