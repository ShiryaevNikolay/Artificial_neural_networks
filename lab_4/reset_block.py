class ResetBlock:
    def __init__(self):
        self.p = 0.5

    def reset_result(self, input_c):
        sum_c = sum(input_c)
        if sum_c <= self.p:
            return 1
        else:
            return 0
