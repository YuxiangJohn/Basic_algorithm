#coding=utf-8
import sys

if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())

    for i in range(n):
        # 读取每一行
        value = int(sys.stdin.readline().strip())
        if (value % 2) != 0:
            print "No"
        else:
            y = 0
            while value % 2 == 0 and value !=1:
                value =value/2
                y += 1

            print value,pow(2,y)
