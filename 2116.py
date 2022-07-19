def biggest(dice, down): # 옆면 중에서 가장 큰 값
    max = 0
    for i in range(6):
        if (i != down) and (i != 5 - down):
            if max < dice[i]:
                max = dice[i]
    return max


    


num_dc = int(input())
dices = []
for i in range(num_dc):
    dice = list(map(int, input().split()))
    dices.append(dice)

result = 0
for down in range(6):
    total = 0
    up = 5 - down
    total += biggest(dices[0], down)
    total += calculate_tot(dices, down, num_dc-1)
    if total > result:
        result = total


