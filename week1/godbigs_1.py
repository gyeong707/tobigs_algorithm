# 임시 좌표 설정
# god = list(map(int, input("god : ").split()))
# bai = list(map(int, input("bai : ").split()))
# bay = list(map(int, input("bay : ").split()))
god = [1, 2, 3, 5]
bai = [6, 0, 10, 4]
bay = [2, 1, 8, 3]

# 갓빅스 광고판 넓이 계산
god_area = (god[2] - god[0]) * (god[3] - god[1])
print("갓빅스 면적 : " , god_area)

# 각 광고판의 좌표 구간 계산
square_list = []
god_x = list(range(god[0], god[2] + 1))
square_list.append(list(range(god[0], god[2] + 1)))
print(god_x)
god_y = list(range(god[1], god[3] + 1))
square_list.append(list(range(god[1], god[3] + 1)))
print(god_y)

bai_x = list(range(bai[0], bai[2] + 1))
square_list.append(list(range(bai[0], bai[2] + 1)))
print(bai_x)
bai_y = list(range(bai[1], bai[3] + 1))
square_list.append(list(range(bai[1], bai[3] + 1)))
print(bai_y)

bay_x = list(range(bay[0], bay[2] + 1))
square_list.append(list(range(bay[0], bay[2] + 1)))
print(bay_x)
bay_y = list(range(bay[1], bay[3] + 1))
square_list.append(list(range(bay[1], bay[3] + 1)))
print(bay_y)

print("Square_list : ", square_list)

print('\n')

# 겹치는 구간 계산
god_bai_x = 0
for x in god_x:
    if x in bai_x:
        god_bai_x += 1
print(god_bai_x)

god_bai_y = 0
for x in god_y:
    if x in bai_y:
        god_bai_y += 1
print(god_bai_y)

god_bay_x = 0
for x in god_x:
    if x in bay_x:
        god_bay_x += 1
print(god_bay_x)

god_bay_y = 0
for x in god_y:
    if x in bay_y:
        god_bay_y += 1
print(god_bay_y)

print('\n')
print('비교군끼리 비교')

bai_bay_x = 0
bai_bay_x_list = []
for x in bai_x:
    if x in bay_x:
        bai_bay_x_list.append(x)
        bai_bay_x += 1
print(bai_bay_x)
print(bai_bay_x_list)

bai_bay_y = 0
bai_bay_y_list = []
for x in bai_y:
    if x in bay_y:
        bai_bay_y_list.append(x)
        bai_bay_y += 1
print(bai_bay_y)
print(bai_bay_y_list)

print('\n')

#두 사각형이 겹치는지 계산
print("\n세 사각형이 겹치는가?")
god_bai_bay_x = 0
god_bai_bay_x_list = []
for x in god_x:
    if x in bai_bay_x_list:
        god_bai_bay_x_list.append(x)
        god_bai_bay_x += 1
print(god_bai_bay_x)
print(god_bai_bay_x_list)

god_bai_bay_y = 0
god_bai_bay_y_list = []
for x in god_y:
    if x in bai_bay_y_list:
        god_bai_bay_y_list.append(x)
        god_bai_bay_y += 1
print(god_bai_bay_y)
print(god_bai_bay_y_list)


#겹치는 구간
god_bai_area = (god_bai_x-1)*(god_bai_y-1)
print("bai 면적 : ", god_bai_area)

god_bay_area = (god_bay_x-1)*(god_bay_y-1)
print("bay 면적 : ", god_bay_area)

bai_bay_area = (bai_bay_x-1)*(bai_bay_y-1)
print("bai_bay 면적 : ", bai_bay_area)

god_bai_bay_area = (god_bai_bay_x-1)*(god_bai_bay_y-1)
print("god_bai_bay 면적 : ", god_bai_bay_area)



print("\n")
#계산
if god_bai_area > 0:
    result_area = god_area - god_bai_area
    print(result_area)
    if god_bay_area > 0:
        result_area -= god_bay_area
        print(result_area)
        if god_bai_bay_area > 0:
            result_area += god_bai_bay_area

elif god_bay_area > 0:
        result_area = god_area - god_bay_area
        print(result_area)

else:
    result_area = god_area

print("결과 : " ,result_area)

#예외처리
for l in square_list:
    if len(l) == 0:
        print(l)
        result_area = 0

print("결과 : " ,result_area)


