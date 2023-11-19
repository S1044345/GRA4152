# FullyConNN class
from tensorflow.keras import layers, Sequential
from NeuralNetwork import NeuralNetwork


# FullyConNN class
class FullyConNN(NeuralNetwork):
    def __init__(self, input_shape=(28 * 28), neurons=50, y_dim=10):
        """
        Initializes a FullyConNN object.

        Args:
            input_shape (int): The shape of the input data. Defaults to 28 * 28.
            neurons (int): The number of neurons in the hidden layers. Defaults to 50.
            y_dim (int): The dimension of the output. Defaults to 10.
        """
        super(FullyConNN, self).__init__(neurons, y_dim)
        self.initialize_layers(input_shape)

    def __repr__(self):
        """
        Returns a string representation of the FullyConNN object.

        Returns:
            str: A string representation of the FullyConNN object.
        """
        return f"FullyConNN(hidden={self.hidden}, classifier={self.cls})"

    def hidden_layers(self, input_shape, neurons):
        """
        Creates the fully connected hidden layers.

        Args:
            input_shape (int): The shape of the input data.
            neurons (int): The number of neurons in the hidden layers.

        Returns:
            Sequential: The fully connected hidden layers.
        """
        hidden = Sequential(
            [
                layers.InputLayer(input_shape=(input_shape,)),
                layers.Dense(neurons, activation="relu"),
                layers.Dense(neurons, activation="relu"),
            ]
        )
        return hidden
