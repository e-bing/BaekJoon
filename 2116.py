def biggest(dice, down): # 옆면 중에서 가장 큰 값, down은 0~5까지 인덱스
    max = 0
    for i in range(6):
        if (i != down) and (i != 5 - down):
            if max < dice[i]:
                max = dice[i]
    return max

def cal_tot(dices, down_num, count): # count로 점검
    sum = 0
    for i in range(count):
        for j in range(6):
            if (down_num == dices[-count][j]):
                down_idx = j
        sum += biggest(dices[i], down_idx)
        down_num = dices[i][5 - down_idx]
    return sum

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
