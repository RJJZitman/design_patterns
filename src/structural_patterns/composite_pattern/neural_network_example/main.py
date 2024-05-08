from neurons import Neuron, NeuronLayer


if __name__ == '__main__':
    base = Neuron(name="base")
    hidden1 = NeuronLayer('L1', 3)
    hidden2 = NeuronLayer('L2', 4)
    out = Neuron(name="out")

    base.connect_to(hidden1)
    hidden1.connect_to(hidden2)
    hidden2.connect_to(out)

    print(base)
    print(hidden1)
    print(hidden2)
    print(out)
