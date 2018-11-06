# Calculate length of Longest subarray with maximum goodness value.
# The goodness of a subarray is defined as difference between number of 1's  and number of 0's  present in the subarray.


def Goodness(arr_num):
    goodness_list = list()
    count = 0
    max_element = 0
    flag = 1
    for num in range(len(arr_num)):
        if arr_num[num] == 1:
            count += 1
        else:
            count -= 1
        goodness_list.append(count)
    #print goodness_list
    max_element = max(goodness_list)
    #print "Max element is: " + str(max_element)
    occurances = goodness_list.count(max_element)
    #print "No of times Max element occurs: " + str(occurances)

    if occurances == 1:
        return str(goodness_list.index(max_element)+flag)
    else:
        while occurances > 1:
            goodness_list.remove(max_element)
            occurances -= 1
            flag += 1
        return (goodness_list.index(max_element) + flag)


number = input()
number_array = list()
number_array = [int(n) for n in raw_input().split()]
# for num in range(int(number)):
#     n = input()
#     number_array.append(int(n))
print number_array

print Goodness(number_array)
