# https://www.hackerrank.com/challenges/python-tuples/problem

number = int(raw_input())
my_tuple = ()
for num in range(number):
    line = raw_input().split(" ")
    my_tuple = map(int, line)
print my_tuple
