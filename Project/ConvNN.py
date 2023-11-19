# ConvNN class
from tensorflow.keras import layers, Sequential
from NeuralNetwork import NeuralNetwork


class ConvNN(NeuralNetwork):
    def __init__(self, input_shape=(32, 32, 3), neurons=50, y_dim=10):
        """
        Initializes a Convolutional Neural Network.

        Args:
            input_shape (tuple): The shape of the input data. Default is (32, 32, 3).
            neurons (int): The number of neurons in the hidden layer. Default is 50.
            y_dim (int): The number of output classes. Default is 10.
        """
        super().__init__(neurons, y_dim)
        self.initialize_layers(input_shape)

    def __repr__(self):
        """
        Returns a string representation of the ConvNN object.
        
        The string representation includes the values of the 'hidden' and 'classifier' attributes.
        """
        return f"ConvNN(hidden={self.hidden}, classifier={self.cls})"

    def hidden_layers(
        self, input_shape, neurons, filters=32, kernel_size=3, strides=(2, 2)
    ):
        """
        Creates the convolutional hidden layers of the Convolutional Neural Network.

        Args:
            input_shape (tuple): The shape of the input data.
            neurons (int): The number of neurons in the hidden layer.
            filters (int): The number of filters in the convolutional layers. Default is 32.
            kernel_size (int or tuple): The size of the convolutional kernel. Default is 3.
            strides (int or tuple): The stride of the convolution. Default is (2, 2).

        Returns:
            Sequential: The convolutional hidden layers.
        """
        # Defining the convolutional hidden layers
        # Note: The architecture can be more complex, with more convolutional layers, pooling layers, etc.
        hidden = Sequential(
            [
                layers.InputLayer(input_shape=input_shape),
                layers.Conv2D(
                    filters=filters, kernel_size=kernel_size, strides=strides
                ),
                layers.Conv2D(
                    filters=2 * filters, kernel_size=kernel_size, strides=strides
                ),
                layers.Conv2D(filters=neurons, kernel_size=kernel_size, strides=(5, 5)),
                layers.Flatten(),
            ]
        )
        return hidden
