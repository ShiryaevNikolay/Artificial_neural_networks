
# Приемник 1
class Receiver1:
    def __init__(self):
        self.g1 = 1

    def get_g1(self):
        return self.g1

    def calculate_g1(self, input_x, input_r):
        if sum(input_x) != 0 and sum(input_r) == 0:
            self.g1 = 1
        else:
            self.g1 = 0
