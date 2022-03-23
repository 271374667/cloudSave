# 由A经过B到C
def hanoi(n,a,b,c):
    #把上面n-1个盘子全部挪到B
    if n > 0:
        hanoi(n-1,a,c,b)
        print(f'把[{a}]最上面的盘子移动到[{c}]')
        hanoi(n-1,b,a,c)
hanoi(3,'A','B','C')