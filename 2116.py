import sys
sys.setrecursionlimit(10**6) # recursion error

def biggest(dice, down): # 옆면 중에서 가장 큰 값, down은 0~5까지 인덱스
    max = 0
    for i in range(6):
        if (i != down) and (i != 5 - down):
            if max < dice[i]:
                max = dice[i]
    return max

def cal_tot(dices, down_num, count): # 재귀, count로 점검
    if count == 0:
        return 0
    else:
        for i in range(6):
            if (down_num == dices[-count][i]):
                down_idx = i
        return biggest(dices[-count], down_idx) + cal_tot(dices, dices[-count][5-i], count-1)

num_dc = int(input())
dices = []
for i in range(num_dc):
    dice = list(map(int, input().split()))
    dices.append(dice)

result = 0

for idx in range(6): # 여기서 idx는 첫번째 주사위의 면 idx
    sum = cal_tot(dices, dices[0][idx], num_dc)
    if result < sum:
        result = sum

print(result)
