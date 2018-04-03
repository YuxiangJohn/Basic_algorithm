# -*- coding: utf-8 -*-
import sys

if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    sum1=0
    sum2=0
    
    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    values = map(int, line.split())
    for i in range(n):
        sum2+=values[i]/2
        if values[i]%2==1:
            sum1+=1

    if sum1==0:
        print sum2*2
    else:
        print sum2/sum1*2+1

