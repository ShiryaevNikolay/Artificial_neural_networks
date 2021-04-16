from lab_4.comparison import Comparison
from lab_4.receiver_1 import Receiver1
from lab_4.reset_block import ResetBlock


class ART:
    def __init__(self):

        # Слой распознавания
        self.layer_recognition = []

        # Слой сравнения
        self.layer_comparison = [Comparison() for i in range(8**2)]

        # Блок сброса
        self.reset_bloc = ResetBlock()

        # Приемник 1
        self.receiver_1 = Receiver1()

    def work(self, input_x):
        pass
