# 京东2018第一题
判断一个数是否由一个奇数和一个偶数相乘，并输出组合中最大的偶数，和奇数

```Python
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
```
