class Godbigs_area:

    def __init__(self):
        self.god = list(map(int, input("god : ").split()))
        self.bai = list(map(int, input("bai : ").split()))
        self.bay = list(map(int, input("bay : ").split()))

    def Area(self, cor):
        return (cor[2] - cor[0]) * (cor[3] - cor[1])

    def section(self, cor):
        return list(range(cor[0], cor[2] + 1)), list(range(cor[1], cor[3] + 1))

    # def overlap(self, x, y):
    #     for x in god_x:
    #         if x in bai_x:
    #             god_bai_x += 1
    #     print(god_bai_x)
    #
    #     god_bai_y = 0
    #     for x in god_y:
    #         if x in bai_y:
    #             god_bai_y += 1
    #     print(god_bai_y)


    #하다 말았음 