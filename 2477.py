melon = int(input())
area = []
for i in range(0, 6):
    area.append(list(map(int, input().split())))

area += area

for i in range(len(area) - 2):
    if area[i][0] == area[i + 2][0]:
        if area[i + 1][0] == area[i + 3][0]:
            area = area[i:i+6]
            break

max_area = area[4][1] * area[5][1]
min_area = area[1][1] * area[2][1]

print((max_area - min_area) * melon)