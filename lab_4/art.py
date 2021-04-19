from lab_4.comparison import Comparison
from lab_4.receiver_1 import Receiver1
from lab_4.recognition import Recognition
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

        self.init_state = True

    def work(self, input_x):

        new_image = True

        blocked_neurons = []

        while len(blocked_neurons) < len(self.layer_recognition):

            # Фаза распознавания
            recognition_win = self.phase_recognition(input_x, blocked_neurons)

            # Фаза сравнения
            self.receiver_1.calculate_g1(input_x, self.layer_recognition[recognition_win].get_t())

            output_c = self.calculate_c(input_x, recognition_win)

            reset = self.reset_bloc.reset_result(input_x, output_c)

            if reset:
                blocked_neurons.append(recognition_win)
                continue

            self.layer_recognition[recognition_win].learn(output_c)
            new_image = False
            return new_image, self.layer_recognition[recognition_win].get_t(), recognition_win

        self.layer_recognition.append(Recognition())
        self.layer_recognition[len(self.layer_recognition) - 1].learn(input_x)
        return new_image, self.layer_recognition[len(self.layer_recognition) - 1].get_t(), len(self.layer_recognition) - 1

    def phase_recognition(self, input_c, blocked_neurons=[]):
        recognition_win = 0
        net_win = 0
        for i, recognition in enumerate(self.layer_recognition):

            next_step = False
            for j in blocked_neurons:
                if j == i:
                    next_step = True
                    break
            if next_step:
                continue

            net = recognition.calculate_r(input_c)
            if net > net_win:
                net_win = net
                recognition_win = i
        return recognition_win

    def calculate_c(self, input_x, recognition_win):
        output_c = []
        for i, comparison in enumerate(self.layer_comparison):
            output_c.append(
                comparison.result(self.receiver_1.get_g1(), self.layer_recognition[recognition_win].get_t()[i],
                                  input_x[i]))
        return output_c
