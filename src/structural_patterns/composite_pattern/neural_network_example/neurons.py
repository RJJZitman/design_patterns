from connectable import Connectable


class Neuron(Connectable):
    def __init__(self, name: str, inputs: int = 1, outputs: int = 1):
        self.name = name
        self.inputs = [None] * inputs
        self.outputs = [None] * outputs

    def __iter__(self):
        yield self

    def __str__(self):
        return f'Neuron {self.name}, {len(self.inputs)} inputs, {len(self.outputs)} outputs'


class NeuronLayer(list, Connectable):
    def __init__(self, name: str, count: int):
        super().__init__()
        self.name = name
        for x in range(0, count):
            self.append(Neuron(f'{name}-{x}'))

    def __str__(self):
        return f'Layer {self.name} with {len(self)} neurons: {[str(neuron) for neuron in self]}'
