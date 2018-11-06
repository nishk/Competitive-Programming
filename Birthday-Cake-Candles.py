# Problem - https://www.hackerrank.com/challenges/birthday-cake-candles/problem

# Example of how O(n)=n^2 v/s O(n)=n


def birthdaycakecandles(ar):
    flag = 0
    count = 0
    for i in ar:
        if i > flag:
            flag = i
            count = 1
        elif i == flag:
            count = count+1
    print flag
    print count
    # print flag
    # for i in ar:
    #     if i == flag:
    #         count = count+1
    # print count


x = [10, 20, 30, 40]
birthdaycakecandles(x)
