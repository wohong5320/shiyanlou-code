for i in range(1,101):
    if i % 7 == 0: # 能被7整除的数
        pass
    elif i % 10 == 7: # 个位数是7
        pass
    elif i // 10 == 7: # 十位数是7
        pass
    else:
        print(i,end=",")
