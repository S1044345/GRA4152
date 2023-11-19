# DataLoader class for loading data

import tensorflow as tf
from tensorflow.keras.utils import to_categorical

class DataLoader:
    """
    A class for loading and preprocessing data.

    Attributes:
        _x_tr (numpy.ndarray): Training input data.
        _y_tr (numpy.ndarray): Training target data.
        _x_te (numpy.ndarray): Testing input data.
        _y_te (numpy.ndarray): Testing target data.

    Methods:
        load_data(): Abstract method to be implemented in subclasses for loading specific datasets.
        preprocess_data(): Preprocesses the data by normalizing and one-hot encoding.
        loader(batch_size): Creates a TensorFlow data loader object.

    """

    def __init__(self):
        """
        Initializes the DataLoader object.

        Loads the training and testing data using the `load_data` method and assigns them to instance variables.

        Parameters:
        None

        Returns:
        None
        """
        (self._x_tr, self._y_tr), (self._x_te, self._y_te) = self.load_data()
    
    @property
    def x_tr(self):
        return self._x_tr
    
    @x_tr.setter
    def x_tr(self,value):
        self._x_tr = value

    @property
    def y_tr(self):
        return self._y_tr
    
    @y_tr.setter
    def y_tr(self,value):
        self._y_tr = value

    @property
    def x_te(self):
        return self._x_te
    
    @x_te.setter
    def x_te(self,value):
        self._x_te = value

    @property
    def y_te(self):
        return self._y_te
    
    @y_te.setter
    def y_te(self,value):
        self._y_te = value

    def load_data(self):
        """
        Abstract method to be implemented in subclasses for loading specific datasets.

        Raises:
            NotImplementedError: This method should be implemented in subclasses.

        """
        raise NotImplementedError("This method should be implemented in subclasses")

    def preprocess_data(self):
        """
        Preprocesses the data by normalizing and one-hot encoding.

        Returns:
            tuple: A tuple containing the preprocessed training and testing data.

        """
        self.x_tr = self.x_tr.astype('float32') / 255.0
        self.x_te = self.x_te.astype('float32') / 255.0
        self.y_tr = to_categorical(self.y_tr)
        self.y_te = to_categorical(self.y_te)

        return (self.x_tr, self.y_tr), (self.x_te, self.y_te)
    
    def loader(self, batch_size):
        """
        Creates a TensorFlow data loader object.

        Args:
            batch_size (int): The batch size for the data loader.

        Returns:
            tf.data.Dataset: A TensorFlow data loader object.

        """
        tf_dl = tf.data.Dataset.from_tensor_slices((self.x_tr, self.y_tr)).shuffle(self.x_tr.shape[0]).batch(batch_size)
        return tf_dl
    