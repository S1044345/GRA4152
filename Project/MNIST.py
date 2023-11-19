# MNIST class for loading MNIST data
from DataLoader import DataLoader
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical


class MNIST(DataLoader):
    def __init__(self):
        super().__init__()  # Call the constructor of the parent class (DataLoader)
        # Reshape MNIST data from (N, 28, 28) to (N, 784)

    def load_data(self):
        """
        Load and reshape the MNIST dataset.

        Returns:
            Tuple: A tuple containing the training and testing data and labels.
        """
        (x_tr, y_tr), (x_te, y_te) = mnist.load_data()
        return (x_tr, y_tr), (x_te, y_te)

    def preprocess_data(self):
        """
        Perform preprocessing steps on the MNIST data.

        Returns:
            Tuple: A tuple containing the preprocessed training and testing data and labels.
        """
        self.x_tr = self.x_tr.astype('float32') / 255.0
        self.x_te = self.x_te.astype('float32') / 255.0
        self.y_tr = to_categorical(self.y_tr)
        self.y_te = to_categorical(self.y_te)

        self.x_tr = self.x_tr.reshape((-1, 28 * 28))
        self.x_te = self.x_te.reshape((-1, 28 * 28))

        return (self.x_tr, self.y_tr), (self.x_te, self.y_te)