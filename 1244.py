num_sw = int(input())
sw_list = list(map(int, input().split()))
num_st = int(input())
st_list = []
for i in range(num_st):
    student = list(map(int, input().split()))
    st_list.append(student)

for i in range(num_st):
    if st_list[i][0] == 1:
        for i in range(st_list[i][1] - 1, num_sw, st_list[i][1]):
            if sw_list[i] == 0:
                sw_list[i] = 1
            else:
                sw_list[i] = 0
    else:
        n = 0
        while (st_list[i][1] - n - 1 >= 0) and (st_list[i][1] + n - 1 < num_sw) and (sw_list[st_list[i][1] - n - 1] == sw_list[st_list[i][1] + n - 1]):
            if sw_list[st_list[i][1] - n - 1] == 0:
                sw_list[st_list[i][1] - n - 1] = 1
                sw_list[st_list[i][1] + n - 1] = 1
            else:
                sw_list[st_list[i][1] - n - 1] = 0
                sw_list[st_list[i][1] + n - 1] = 0
            n += 1
            

for i in range(num_sw):
    print(sw_list[i], end='')
    if (i != num_sw - 1) and (i % 20 != 19):
        print(' ', end = '')
    elif i == 0:
        print(' ', end = '')
    elif ((i % 20) == 19):
        print()