# NeuralNetwork class
import tensorflow as tf
from tensorflow.keras import layers, Sequential


class NeuralNetwork(tf.keras.Model):
    """
    A class representing a neural network model.

    Args:
        neurons (int): Number of neurons in the hidden layer.
        y_dim (int): Dimension of the output.

    Attributes:
        neurons (int): Number of neurons in the hidden layer.
        y_dim (int): Dimension of the output.
        params (list): List of trainable parameters in the model.

    Methods:
        initialize_layers(input_shape): Initializes the hidden layers and classifier.
        hidden_layers(input_shape, neurons): Creates the hidden layers of the model.
        classifier(neurons, y_dim): Creates the classifier layer of the model.
        call(inputs): Performs a forward pass through the model.
        test(x): Performs inference on the input data.
        train(inputs, optimizer): Performs a training step on the model.

    """

    def __init__(self, neurons=50, y_dim=10):
        """
        Initializes a NeuralNetwork object.

        Parameters:
        - neurons (int): The number of neurons in the network. Default is 50.
        - y_dim (int): The dimension of the output. Default is 10.
        """
        super(NeuralNetwork, self).__init__()
        self.neurons = neurons
        self.y_dim = y_dim
        self.params = []

    def initialize_layers(self, input_shape):
            """
            Initializes the hidden layers and classifier layers of the neural network.

            Args:
                input_shape: The shape of the input data.

            Returns:
                None
            """
            self.hidden = self.hidden_layers(input_shape, self.neurons)
            self.cls = self.classifier(self.neurons, self.y_dim)
            self.params = self.cls.trainable_variables + self.hidden.trainable_variables

    def __repr__(self):
        """
        Returns a string representation of the NeuralNetwork object.
        
        The string representation includes the values of the 'hidden' and 'classifier' attributes.
        """
        return f"NeuralNetwork(hidden={self.hidden}, classifier={self.cls})"

    def hidden_layers(self, input_shape, neurons):
            """
            This method should be implemented in subclasses.
            
            Args:
                input_shape (tuple): The shape of the input data.
                neurons (int): The number of neurons in each hidden layer.
            
            Raises:
                NotImplementedError: This method should be implemented in subclasses.
            """
            raise NotImplementedError("This method should be implemented in subclasses")

    def classifier(self, neurons, y_dim):
        """
        Creates a classifier neural network model.

        Parameters:
        neurons (tuple): The shape of the input layer.
        y_dim (int): The number of classes in the output layer.

        Returns:
        Sequential: The classifier neural network model.
        """
        cls = Sequential(
            [
                layers.InputLayer(input_shape=neurons),
                layers.Dense(y_dim, activation="softmax"),
            ]
        )
        return cls

    def call(self, inputs):
        """
        Calculates the loss for the given inputs.

        Args:
            inputs: A tuple containing the input data (x) and the target labels (y).

        Returns:
            loss: The calculated loss value.
        """
        x, y = inputs
        out = self.hidden(x)
        out = self.cls(out)
        loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(y, out))
        return loss

    def test(self, x):
        """
        Perform a forward pass through the neural network to make predictions.

        Args:
            x (tf.Tensor): Input data.

        Returns:
            tf.Tensor: Predicted class labels.
        """
        out = self.hidden(x)
        out = self.cls(out)
        y_hat = tf.math.argmax(out, axis=1)
        return y_hat

    def train(self, inputs, optimizer):
        """
        Trains the neural network using the given inputs and optimizer.

        Args:
            inputs: The input data for training.
            optimizer: The optimizer used for updating the network's parameters.

        Returns:
            The loss value after training.
        """
        with tf.GradientTape() as tape:
            loss = self.call(inputs)
        gradients = tape.gradient(loss, self.params)
        optimizer.apply_gradients(zip(gradients, self.params))
        return loss
