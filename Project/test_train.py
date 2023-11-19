import tensorflow as tf
from sklearn.metrics import roc_auc_score

from NeuralNetwork import NeuralNetwork
from ConvNN import ConvNN
from FullyConNN import FullyConNN

from DataLoader import DataLoader
from MNIST import MNIST
from CIFAR10 import CIFAR10

# this file was used to test the training of the model
# see train.py for the proper training script

epochs = 10
batch_size = 256

# load the CIFAR10 dataset
data_loader = CIFAR10()
# data_loader = MNIST()
data_loader.preprocess_data()

# get the Tensorflow loader
tr_data = data_loader.loader(batch_size)

# initialise model
model = ConvNN()
# model = FullyConNN()

# set the optimiser
optimizer = tf.keras.optimizers.Adam(learning_rate=5e-4)

# train the model
step = 0
while step < epochs:
    for i, data_batch in enumerate(tr_data):
        losses = model.train(data_batch, optimizer=optimizer)
    step += 1

# calculate AUC
pi_hat = model.test(data_loader.x_te)
pi_hat = tf.reshape(pi_hat, [-1, 1])
auc = roc_auc_score(data_loader.y_te, pi_hat)
print("final auc %0.4f" % (auc))
