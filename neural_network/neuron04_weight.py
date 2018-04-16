# coding: UTF-8
import math

# シグモイド関数
def sigmoid(a):
    return 1.0 / (1.0 + math.exp(-a))


# ニューロン
class Neuron:
    input_sum = 0.0
    output = 0.0
    def setInput(self, inp):
        self.input_sum += inp
        # print self.input_sum


    def getOutput(self):
        self.output = sigmoid(self.input_sum)
        return self.output


# ニューラルネットワーク
class NeuralNetwork:
    # 重み
    w = [1.5, -2.5, -0.5]
    # ニューロンのインスタンス
    neuron = Neuron()
    # 実行
    def commit(self, input_data):
        self.neuron.setInput(input_data[0] * self.w[0])
        self.neuron.setInput(input_data[1] * self.w[1])
        self.neuron.setInput(input_data[2] * self.w[2])
        return self.neuron.getOutput()

# ニューラルネットワークのインスタンス
neural_network = NeuralNetwork()

# 実行
trial_data = [1.0, 2.0, 3.0]
print neural_network.commit(trial_data)

