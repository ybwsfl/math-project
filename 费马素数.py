print(2**32+1)
print(6700417*641)

def feimashu(n):
    print(2**n+1)
    return 2**n+1

for i in range(100):
    num = feimashu(i)

    # 质数大于 1
    if num > 1:
        # 查看因子
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "不是质数")
                print(i, "乘于", num // i, "是", num)
                break
        else:
            print(num, "是质数")

    # 如果输入的数字小于或等于 1，不是质数
    else:
        print(num, "不是质数")


