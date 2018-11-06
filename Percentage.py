# https://www.hackerrank.com/challenges/finding-the-percentage/problem

number = int(raw_input())
student_marks = {}
for _ in range(number):
    line = raw_input().split(" ")
    name, scores = line[0], line[1:]
    scores = map(float, scores)
    student_marks[name] = scores
print student_marks

query_name = raw_input()

if query_name in student_marks:
    total = 0
    for num in student_marks[query_name]:
        total += num
    print '{:.2f}'.format(total/3)
