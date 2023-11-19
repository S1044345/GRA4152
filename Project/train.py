import argparse
import tensorflow as tf
from sklearn.metrics import roc_auc_score

from NeuralNetwork import NeuralNetwork
from ConvNN import ConvNN
from FullyConNN import FullyConNN

from DataLoader import DataLoader
from MNIST import MNIST
from CIFAR10 import CIFAR10

def parse_args():
    parser = argparse.ArgumentParser(description='Train a neural network on MNIST or CIFAR10. Example usage: python train.py --dset cifar10 --nn_type conv --epochs 10')
    parser.add_argument('--nn_type', type=str, default='fully_con', choices=['fully_con', 'conv'],
                        help='Type of neural network (fully connected or convolutional).')
    parser.add_argument('--epochs', type=int, default=10, help='Number of epochs for training.')
    parser.add_argument('--batch_size', type=int, default=256, help='Batch size for training.')
    parser.add_argument('--dset', type=str, default='mnist', choices=['mnist', 'cifar10'],
                        help='Dataset to use (MNIST or CIFAR10).')
    return parser.parse_args()

def main():
    args = parse_args()

    # Input validation
    assert args.epochs > 0, "Number of epochs must be positive"
    assert args.batch_size > 0, "Batch size must be positive"
    assert args.dset in ['mnist', 'cifar10'], "Dataset must be either MNIST or CIFAR10"
    assert args.nn_type in ['fully_con', 'conv'], "Neural network type must be either fully_con or conv"

    # Initialize data loader for the chosen dataset
    if args.dset == 'mnist':
        data_loader = MNIST()
        data_loader.preprocess_data()
    elif args.dset == 'cifar10':
        data_loader = CIFAR10()
        data_loader.preprocess_data()

    # get the Tensorflow loader
    tr_data = data_loader.loader(args.batch_size)

    # Initialize the neural network
    if args.nn_type == 'fully_con':
        model = FullyConNN()
    elif args.nn_type == 'conv':
        model = ConvNN()

    # set the optimiser
    optimizer = tf.keras.optimizers.Adam(learning_rate=5e-4)

    # train the model
    step = 0
    while step < args.epochs:
        for i, data_batch in enumerate(tr_data):
            losses = model.train(data_batch, optimizer=optimizer)
        step += 1

    # calculate AUC
    pi_hat = model.test(data_loader.x_te)
    pi_hat = tf.reshape(pi_hat, [-1, 1])
    auc = roc_auc_score(data_loader.y_te, pi_hat)
    print("final auc %0.4f" % (auc))

if __name__ == '__main__':
    main()