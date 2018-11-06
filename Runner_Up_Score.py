# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem


def Runner_Up(num_arr):
    copy_array = list()
    copy_array = num_arr

    winner = max(copy_array)
    occurances = copy_array.count(winner)
    #print "No of times Max element occurs: " + str(occurances)

    if occurances == 1:
        copy_array.remove(winner)
        return max(copy_array)
    else:
        while occurances > 0:
            copy_array.remove(winner)
            occurances -= 1
        return max(copy_array)


number = input()
number_array = list()
number_array = [int(n) for n in raw_input().split()]
#print number_array
print Runner_Up(number_array)
