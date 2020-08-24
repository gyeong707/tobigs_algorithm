import numpy as np


# 임시 좌표 설정
# god = list(map(int, input("god : ").split()))
# bai = list(map(int, input("bai : ").split()))
# bay = list(map(int, input("bay : ").split()))
god = [1, 2, 3, 5]
bai = [6, 0, 10, 4]
bay = [2, 1, 8, 3]

# 갓빅스 광고판 넓이 계산
god_area = (god[2] - god[0]) * (god[3] - god[1])
print(god_area)

#god 사각형과 bai 사각형이 겹치는지 확인하기 (가로)
if god[0] <= bai[0] <= god[2]:
    if god[0] <= bai[2] <= god[2]:
        bai_width = bai[2]-bai[0]
    bai_width = god[2] - bai[0]

elif god[0] <= bai[2] <= god[2]:
    bai_width = bai[2] - god[0]

else:
    bai_width = 0

print(bai_width)


#god 사각형과 bai 사각형이 겹치는지 확인하기 (세로)
if god[1] <= bai[1] <= god[3]:
    if god[1] <= bai[3] <= god[3]:
        bai_height = bai[3]-bai[1]
    bai_height = god[3] - bai[1]

elif god[1] <= bai[3] <= god[3]:
    bai_height = bai[3] - god[1]

else:
    bai_height = 0

print(bai_height)


#god 사각형과 bay 사각형이 겹치는지 확인하기 (가로)
if god[0] <= bay[0] <= god[2]:
    if god[0] <= bay[2] <= god[2]:
        bay_width = bay[2]-bay[0]
    bay_width = god[2] - bay[0]

elif god[0] <= bay[2] <= god[2]:
    bay_width = bay[2] - god[0]

else:
    bay_width = 0

print(bay_width)


#god 사각형과 bay 사각형이 겹치는지 확인하기 (세로)
if god[1] <= bay[1] <= god[3]:
    if god[1] <= bay[3] <= god[3]:
        bay_height = bay[3]-bay[1]
    bay_height = god[3] - bay[1]

elif god[1] <= bay[3] <= god[3]:
    bay_height = bay[3] - god[1]

else:
    bay_height = 0

print(bay_height)

# 값을 바탕으로 넓이 계산
result_area = god_area - (bai_width*bai_height) - (bay_width*bay_height)
print(result_area)

