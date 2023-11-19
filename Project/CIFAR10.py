# CIFAR10 class for loading CIFAR10 data
from DataLoader import DataLoader
from tensorflow.keras.datasets import cifar10


class CIFAR10(DataLoader):
    def __init__(self):
        """
        Initializes an instance of the CIFAR10 class.
        """
        super().__init__()

    def load_data(self):
        """
        Loads the CIFAR10 dataset.

        Returns:
            Tuple: A tuple containing the training and testing data, in the format (x_tr, y_tr), (x_te, y_te).
                   x_tr: numpy.ndarray - Training images.
                   y_tr: numpy.ndarray - Training labels.
                   x_te: numpy.ndarray - Testing images.
                   y_te: numpy.ndarray - Testing labels.
        """
        (x_tr, y_tr), (x_te, y_te) = cifar10.load_data()

        # Reshape is not required for CIFAR10 as it's already in the shape of (32, 32, 3)

        return (x_tr, y_tr), (x_te, y_te)

    # Note: The loader method are inherited from DataLoader and will be used as is.
