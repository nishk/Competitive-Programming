var = input()
def_str = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
for number in range(0, var):
    UserStr = raw_input()
    NewStr = list(UserStr)
    new_list = []
    for element in NewStr:
        if element in def_str:
            new_list.append(element)
    print len(new_list)
