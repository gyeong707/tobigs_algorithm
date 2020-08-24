# 임시 좌표 설정
god = list(map(int, input().split()))
bai = list(map(int, input().split()))
bay = list(map(int, input().split()))

# 갓빅스 광고판 넓이 계산
god_area = (god[2] - god[0]) * (god[3] - god[1])

# 각 광고판의 좌표 구간 계산
square_list = []
god_x = list(range(god[0], god[2] + 1))
square_list.append(list(range(god[0], god[2] + 1)))
god_y = list(range(god[1], god[3] + 1))
square_list.append(list(range(god[1], god[3] + 1)))

bai_x = list(range(bai[0], bai[2] + 1))
square_list.append(list(range(bai[0], bai[2] + 1)))
bai_y = list(range(bai[1], bai[3] + 1))
square_list.append(list(range(bai[1], bai[3] + 1)))

bay_x = list(range(bay[0], bay[2] + 1))
square_list.append(list(range(bay[0], bay[2] + 1)))
bay_y = list(range(bay[1], bay[3] + 1))
square_list.append(list(range(bay[1], bay[3] + 1)))


# 겹치는 구간 계산
god_bai_x = 0
for x in god_x:
    if x in bai_x:
        god_bai_x += 1

god_bai_y = 0
for x in god_y:
    if x in bai_y:
        god_bai_y += 1

god_bay_x = 0
for x in god_x:
    if x in bay_x:
        god_bay_x += 1

god_bay_y = 0
for x in god_y:
    if x in bay_y:
        god_bay_y += 1

bai_bay_x = 0
bai_bay_x_list = []
for x in bai_x:
    if x in bay_x:
        bai_bay_x_list.append(x)
        bai_bay_x += 1

bai_bay_y = 0
bai_bay_y_list = []
for x in bai_y:
    if x in bay_y:
        bai_bay_y_list.append(x)
        bai_bay_y += 1

#두 사각형이 겹치는지 계산
god_bai_bay_x = 0
god_bai_bay_x_list = []
for x in god_x:
    if x in bai_bay_x_list:
        god_bai_bay_x_list.append(x)
        god_bai_bay_x += 1

god_bai_bay_y = 0
god_bai_bay_y_list = []
for x in god_y:
    if x in bai_bay_y_list:
        god_bai_bay_y_list.append(x)
        god_bai_bay_y += 1

#겹치는 구간
god_bai_area = (god_bai_x-1)*(god_bai_y-1)
god_bay_area = (god_bay_x-1)*(god_bay_y-1)
bai_bay_area = (bai_bay_x-1)*(bai_bay_y-1)
god_bai_bay_area = (god_bai_bay_x-1)*(god_bai_bay_y-1)

#계산
if god_bai_area > 0:
    result_area = god_area - god_bai_area
    if god_bay_area > 0:
        result_area -= god_bay_area
        if god_bai_bay_area > 0:
            result_area += god_bai_bay_area
elif god_bay_area > 0:
        result_area = god_area - god_bay_area
else:
    result_area = god_area


#예외처리
for l in square_list:
    if len(l) == 0:
        result_area = 0

print(result_area)

