class ResetBlock:
    def __init__(self):
        self.p = 0.95
        self.c = [0 for i in range(8**2)]

    def get_c(self):
        return self.c

    def reset_result(self, input_x, input_c):
        self.c = input_c
        sum_c = sum(input_c)
        sum_x = sum(input_x)
        s = sum_c / sum_x
        if s > self.p:
            return False
        else:
            return True
