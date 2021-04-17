
# Приемник 1
class Receiver1:
    def __init__(self):
        self.g1 = 0

    def get_g1(self):
        return self.g1

    def calculate_result(self, input_x, input_r):
        result_x = 0
        result_r = 0
        for x in input_x:
            if x == 1:
                result_x = 1
                break
        for r in input_r:
            if r == 1:
                result_r = 1
                break
        if result_x == 1 and result_r == 0:
            self.g1 = 1
        else:
            self.g1 = 0
