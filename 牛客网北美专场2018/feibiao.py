# -*- coding: utf-8 -*-
import sys

if __name__ == "__main__":

    # 读取第一行的n
    n = int(sys.stdin.readline().strip())  #同心圆数

    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    values = list(map(int, line.split()))
    area=[]
    area.append(0)
    for i in range(0, n):
        area.append(values[i]*values[i])
    x = int(sys.stdin.readline().strip())

    ans = 0
    for i in range(1, n+1):
        ans += (n-i+1) * (area[i] - area[i-1])

    score = ans * x / area[-1]
    print("%.3f" % score)





