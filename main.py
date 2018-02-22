#!/usr/bin/env python

import sys
import numpy as np
from argparse import ArgumentParser
import tensorflow as tf

from model import VOModel
from utils import DataManager

from matplotlib import pyplot as plt


def main():
    parser = ArgumentParser('Test')
    parser.add_argument('-d', '--dataset', type=str, required=True, help='Path to dataset folder')
    args = parser.parse_args()

    sequence_length = 10
    batch_size      = 5
    memory_size     = 1000

    dm = DataManager(
                dataset_path=args.dataset,
                batch_size=batch_size,
                sequence_length=sequence_length,
                debug=True)

    image_shape = dm.getImageShape()

    # create model
    model = VOModel(image_shape, memory_size, sequence_length)

    with tf.Session() as session:
        for images, poses in dm.batches():
            session.run(tf.global_variables_initializer())
            model.get_rnn_output(session, images, poses)


if __name__ == '__main__':
    main()
