num_pillar = int(input())
pillar_list = []
for i in range(num_pillar):
    pillar_list.append(list(map(int, input().split())))

pillar_list.sort()

max = 0 # 가장 높은 기둥의 길이
max_idx = 0 # 가장 높은 기둥 번호
length = 0 # 기둥의 전체 개수
for i in pillar_list:
    if max < i[1]:
        max = i[1]
        max_idx = length
    length += 1

local_max = 0
sum = 0
for i in range(max_idx):
    if local_max < pillar_list[i][1]:
        local_max = pillar_list[i][1]
    sum += (pillar_list[i + 1][0] - pillar_list[i][0]) * local_max

sum += max

local_max = 0
for i in range(length - 1, max_idx, -1):
    if local_max < pillar_list[i][1]:
        local_max = pillar_list[i][1]
    sum += (pillar_list[i][0] - pillar_list[i - 1][0]) * local_max

print(sum)