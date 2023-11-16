import numpy as np
class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        # Initialize the weights and biases for the neural network
        self.weights_input_hidden = np.random.rand(input_size, hidden_size)
        self.bias_hidden = np.zeros((1, hidden_size))
        self.weights_hidden_output = np.random.rand(hidden_size, output_size)
        self.bias_output = np.zeros((1, output_size))
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    def sigmoid_derivative(self, x):
        return x * (1 - x)
    def forward(self, X):
        self.hidden_input = np.dot(X, self.weights_input_hidden) + self.bias_hidden
        self.hidden_output = self.sigmoid(self.hidden_input)
        self.output_input = np.dot(self.hidden_output, self.weights_hidden_output) + self.bias_output
        self.output = self.sigmoid(self.output_input)
        return self.output
    def backward(self, X, y, learning_rate):
        loss = y - self.output
        output_delta = loss * self.sigmoid_derivative(self.output)
        hidden_output_error = output_delta.dot(self.weights_hidden_output.T)
        self.weights_hidden_output += self.hidden_output.T.dot(output_delta) * learning_rate
        self.weights_input_hidden += X.T.dot(hidden_output_error * self.sigmoid_derivative(self.hidden_output)) * learning_rate
        self.bias_output += np.sum(output_delta, axis=0, keepdims=True) * learning_rate
        self.bias_hidden += np.sum(hidden_output_error * self.sigmoid_derivative(self.hidden_output), axis=0, keepdims=True) * learning_rate
    def train(self, X, y, epochs, learning_rate):
        for _ in range(epochs):
            self.forward(X)
            self.backward(X, y, learning_rate)
    def predict(self, X):
        return self.forward(X)
if __name__ == "__main__":
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([[0], [1], [1], [0]])
    neural_net = NeuralNetwork(input_size=2, hidden_size=2, output_size=1)
    neural_net.train(X, y, epochs=10000, learning_rate=0.1)
    for input_data in X:
        prediction = neural_net.predict(input_data)
        print(f"Input: {input_data}, Predicted Output: {prediction}")
