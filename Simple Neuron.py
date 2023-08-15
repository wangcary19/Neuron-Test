#Idea for the simplest neuron, capable of adjusting only to purely linear data without any bias offset (i.e. goes through the origin).
#A driver function should repeatedly activate the neuron until it fits the data.

data = [1, 2, 3, 4, 5]
expected_output = [6, 12, 18, 24, 30]


class SimpleNeuron:
    def __init__(self):
        self.weight = 0
        self.increment = 1

    def predict(self, datapoint):
        return datapoint * self.weight

    def increase_weight(self):
        self.weight = self.weight + self.increment

    def decrease_weight(self):
        self.weight = self.weight - self.increment

    def __del__(self):
        print("Neuron instance" + str(self) + "destroyed.")
        return


# A driver function for neuron learning that assumes a perfect dataset (i.e. training will finish right at the end of the data).
neuron_instance  = SimpleNeuron()
def learn(data, expected_output, neuron):

    i = 0
    prediction = neuron.predict(data[i])

    while i <= len(data) - 1 and prediction != expected_output[i]:
        prediction = neuron.predict(data[i])
        if prediction == expected_output[i]:
            print("Data learned.  Neuron weight is " + str(neuron.weight))
            return
        elif prediction < expected_output[i]:
            neuron.increase_weight()
            i += 1
            print("Learning.  Neuron weight is " + str(neuron.weight))
            continue
        elif prediction > expected_output[i]:
            neuron.decrease_weight()
            i += 1
            print("Learning.  Neuron weight is " + str(neuron.weight))
            continue

    print("Data exhausted.  Current neuron weight is " + str(neuron.weight))
    return


# Calling
learn(data, expected_output, neuron_instance)
