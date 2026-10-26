---
name: train-11-mnist-tf2-keras
description: "Cloud TPU MNIST with TensorFlow 2.x/Keras \u2014 Official end-to-end TensorFlow/Keras training recipe using TPU distribution; useful as a small migration smoke test before a larger workload."
source_url: "https://cloud.google.com/tpu/docs/tutorials/mnist-2.x"
category: "training_framework_links"
---

# Agent Skill: Cloud TPU MNIST with TensorFlow 2.x/Keras

- **Official Source**: [https://cloud.google.com/tpu/docs/tutorials/mnist-2.x](https://cloud.google.com/tpu/docs/tutorials/mnist-2.x)
- **Category**: `training_framework_links`
- **Resource ID**: `train_11_mnist_tf2_keras`
- **When to Activate**: Official end-to-end TensorFlow/Keras training recipe using TPU distribution; useful as a small migration smoke test before a larger workload.

## Document Sections

- **Cloud TPU MNIST with TensorFlow 2.x and Keras (`mnist-2.x`)**
  - **1. Overview & Architecture**
  - **2. Provision a Cloud TPU VM & Install TensorFlow**
- **Create a TPU VM using Compute Engine**
- **SSH into the TPU VM**
  - **3. Initialize `TPUClusterResolver` and `TPUStrategy`**
  - **4. Official `tensorflow/tpu` Keras MNIST Script (`models/experimental/mnist_keras/mnist.py`)**
- **Copyright 2018 The TensorFlow Authors. All Rights Reserved.**
- **Licensed under the Apache License, Version 2.0 (the "License");**
- **you may not use this file except in compliance with the License.**
- **You may obtain a copy of the License at**
- **http://www.apache.org/licenses/LICENSE-2.0**
- **Unless required by applicable law or agreed to in writing, software**
- **distributed under the License is distributed on an "AS IS" BASIS,**
- **WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.**
- **See the License for the specific language governing permissions and**
- **limitations under the License.**
- **==============================================================================**
- **Standard Imports**
- **TODO(sourabhbajaj): Remove the need for this flag.**
- **Batch size should satify two properties to be able to run in cloud:**
- **num_eval_samples % batch_size == 0**
- **batch_size % 8 == 0**
- **input image dimensions**
  - **5. Official `tensorflow/tpu` TensorFlow 2.x MNIST with TensorBoard Summary (`mnist_tf2_with_summary.py`)**
- **Copyright 2019 The TensorFlow Authors. All Rights Reserved.**
- **Licensed under the Apache License, Version 2.0 (the "License");**
- **you may not use this file except in compliance with the License.**
- **You may obtain a copy of the License at**
- **http://www.apache.org/licenses/LICENSE-2.0**
- **Unless required by applicable law or agreed to in writing, software**
- **distributed under the License is distributed on an "AS IS" BASIS,**
- **WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.**
- **See the License for the specific language governing permissions and**
- **limitations under the License.**
- **==============================================================================**
- **Standard Imports**
- **Batch size should satify two properties to be able to run in cloud:**
- **num_eval_samples % batch_size == 0**
- **batch_size % 8 == 0**
- **input image dimensions**

## Key CLI Commands & Invocations

```bash
gcloud compute tpus tpu-vm create mnist-tpu-vm \
gcloud compute tpus tpu-vm ssh mnist-tpu-vm --zone=us-central1-a
python mnist.py --use_tpu=False [--fake_data=true]
python mnist.py --use_tpu=True [--tpu=$TPU_NAME]
python mnist_tf2_with_summary.py --use_tpu=True [--tpu=$TPU_NAME]
```

## Complete Technical Reference

# Cloud TPU MNIST with TensorFlow 2.x and Keras (`mnist-2.x`)

> **URL Redirect Note**: On `cloud.google.com/tpu/docs/tutorials/mnist-2.x`, Google Cloud now HTTP 301 redirects to `/tpu/docs/pytorch-on-tpu`. Below is the complete end-to-end TensorFlow 2.x / Keras Cloud TPU MNIST training guide and the official `tensorflow/tpu` reference scripts (`mnist.py` and `mnist_tf2_with_summary.py`).

## 1. Overview & Architecture

This recipe demonstrates synchronous distributed training on a Cloud TPU VM using TensorFlow 2.x, Keras (`tf.keras`), `tf.data`, and `tf.distribute.TPUStrategy`. It serves as a fast migration smoke test before running larger TensorFlow/Keras workloads on Cloud TPU.

## 2. Provision a Cloud TPU VM & Install TensorFlow

```bash
# Create a TPU VM using Compute Engine
gcloud compute tpus tpu-vm create mnist-tpu-vm \
  --zone=us-central1-a \
  --accelerator-type=v5litepod-8 \
  --version=tpu-ubuntu2204-base

# SSH into the TPU VM
gcloud compute tpus tpu-vm ssh mnist-tpu-vm --zone=us-central1-a
```

## 3. Initialize `TPUClusterResolver` and `TPUStrategy`

```python
import tensorflow as tf
import tensorflow_datasets as tfds

resolver = tf.distribute.cluster_resolver.TPUClusterResolver(tpu='local')
tf.config.experimental_connect_to_cluster(resolver)
tf.tpu.experimental.initialize_tpu_system(resolver)
strategy = tf.distribute.TPUStrategy(resolver)
print('Number of accelerators: ', strategy.num_replicas_in_sync)
```

## 4. Official `tensorflow/tpu` Keras MNIST Script (`models/experimental/mnist_keras/mnist.py`)

```python
# Copyright 2018 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
r"""Experimental Keras MNIST Example.

To test on CPU:
    python mnist.py --use_tpu=False [--fake_data=true]

To test on TPU:
    python mnist.py --use_tpu=True [--tpu=$TPU_NAME]
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Standard Imports
from absl import app
from absl import flags
import numpy as np
import tensorflow.compat.v1 as tf
from tensorflow.contrib import cluster_resolver as contrib_cluster_resolver
from tensorflow.contrib import distribute as contrib_distribute

# TODO(sourabhbajaj): Remove the need for this flag.
flags.DEFINE_bool('use_tpu', True,
                  'Ignored: preserved for backward compatibility.')
flags.DEFINE_string('tpu', '', 'Name of the TPU to use.')
flags.DEFINE_string(
    'model_dir', None,
    ('The directory where the model and training/evaluation summaries '
     'are stored. If unset, no summaries will be stored.'))

flags.DEFINE_bool('fake_data', False, 'Use fake data to test functionality.')

# Batch size should satify two properties to be able to run in cloud:
# num_eval_samples % batch_size == 0
# batch_size % 8 == 0
BATCH_SIZE = 200
NUM_CLASSES = 10
EPOCHS = 15

# input image dimensions
IMG_ROWS, IMG_COLS = 28, 28

FLAGS = flags.FLAGS


def mnist_model(input_shape):
  """Creates a MNIST model."""
  model = tf.keras.models.Sequential()
  model.add(
      tf.keras.layers.Conv2D(
          32, kernel_size=(3, 3), activation='relu', input_shape=input_shape))
  model.add(tf.keras.layers.Conv2D(64, (3, 3), activation='relu'))
  model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2)))
  model.add(tf.keras.layers.Dropout(0.25))
  model.add(tf.keras.layers.Flatten())
  model.add(tf.keras.layers.Dense(128, activation='relu'))
  model.add(tf.keras.layers.Dropout(0.5))
  model.add(tf.keras.layers.Dense(NUM_CLASSES, activation='softmax'))
  return model


def run():
  """Run the model training and return evaluation output."""
  resolver = contrib_cluster_resolver.TPUClusterResolver(tpu=FLAGS.tpu)
  contrib_distribute.initialize_tpu_system(resolver)
  strategy = contrib_distribute.TPUStrategy(resolver, steps_per_run=100)

  if FLAGS.fake_data:
    print('Using fake data')
    x_train = np.random.random((BATCH_SIZE, IMG_ROWS, IMG_COLS))
    y_train = np.zeros([BATCH_SIZE, 1], dtype=np.int32)
    x_test, y_test = x_train, y_train
  else:
    # the data, split between train and test sets
    print('Using real data')
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

  x_train = x_train.reshape(x_train.shape[0], IMG_ROWS, IMG_COLS, 1)
  x_test = x_test.reshape(x_test.shape[0], IMG_ROWS, IMG_COLS, 1)
  input_shape = (IMG_ROWS, IMG_COLS, 1)

  x_train = x_train.astype('float32')
  x_test = x_test.astype('float32')
  x_train /= 255
  x_test /= 255
  print('x_train shape:', x_train.shape)
  print(x_train.shape[0], 'train samples')
  print(x_test.shape[0], 'test samples')

  # convert class vectors to binary class matrices
  y_train = tf.keras.utils.to_categorical(y_train, NUM_CLASSES)
  y_test = tf.keras.utils.to_categorical(y_test, NUM_CLASSES)
  with strategy.scope():
    model = mnist_model(input_shape)
    model.compile(
        loss=tf.keras.losses.categorical_crossentropy,
        optimizer=tf.train.GradientDescentOptimizer(learning_rate=0.05),
        metrics=['accuracy'])

  callbacks = []
  if FLAGS.model_dir:
    callbacks = [tf.keras.callbacks.TensorBoard(log_dir=FLAGS.model_dir)]

  model.fit(
      x_train,
      y_train,
      batch_size=BATCH_SIZE,
      callbacks=callbacks,
      epochs=EPOCHS,
      verbose=1,
      validation_data=(x_test, y_test))
  return model.evaluate(x_test, y_test, batch_size=BATCH_SIZE, verbose=1)


def main(unused_dev):
  score = run()
  print('Loss for final step: %s;' % score[0])
  print('Accuracy: %s;' % score[1])


if __name__ == '__main__':
  tf.logging.set_verbosity(tf.logging.INFO)
  app.run(main)
```

## 5. Official `tensorflow/tpu` TensorFlow 2.x MNIST with TensorBoard Summary (`mnist_tf2_with_summary.py`)

```python
# Copyright 2019 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
r"""Keras MNIST Example with tf.summary usage.

Passing Keras Tensorboard callback to Keras fit() API parameter writes
metrics and losses as well as model weights to summary event files for
visualization. However, for advanced use cases, users may wish to write
aribitrary intermediate tensors to summary event files. This example
shows how to write intermediate tensors in model definition while running
a model on TPU's.

To test on TPU:
    python mnist_tf2_with_summary.py --use_tpu=True [--tpu=$TPU_NAME]
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Standard Imports

from absl import app
from absl import flags
from absl import logging

import tensorflow.compat.v2 as tf

flags.DEFINE_bool('use_tpu', True,
                  'Ignored: preserved for backward compatibility.')
flags.DEFINE_string('tpu', '', 'Name of the TPU to use.')
flags.DEFINE_string(
    'model_dir', '',
    ('The directory where the model and training/evaluation summaries '
     'are stored. If unset, no summaries will be stored.'))
flags.DEFINE_string(
    'protocol', None,
    'Ex: "grpc". Overrides the communication protocol for the '
    'cluster.')

flags.DEFINE_bool('fake_data', False, 'Use fake data to test functionality.')

# Batch size should satify two properties to be able to run in cloud:
# num_eval_samples % batch_size == 0
# batch_size % 8 == 0
BATCH_SIZE = 200
NUM_CLASSES = 10
_EPOCHS = 15

# input image dimensions
IMG_ROWS, IMG_COLS = 28, 28

FLAGS = flags.FLAGS


class LayerForWritingHistogramSummary(tf.keras.layers.Layer):
  """A pass-through layer that only records values to summary."""

  def call(self, x):
    tf.summary.histogram('custom_histogram_summary', x)
    return x


class LayerForWritingImageSummary(tf.keras.layers.Layer):
  """A pass-through layer that only records image values to summary."""

  def call(self, x):
    tf.summary.image('custom_image_summary', x)
    return x


def mnist_model(input_shape):
  """Creates a MNIST model."""
  model = tf.keras.models.Sequential()

  # Adding custom pass-through layer to visualize input images.
  model.add(LayerForWritingImageSummary())

  model.add(
      tf.keras.layers.Conv2D(
          32, kernel_size=(3, 3), activation='relu', input_shape=input_shape))
  model.add(tf.keras.layers.Conv2D(64, (3, 3), activation='relu'))
  model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2)))
  model.add(tf.keras.layers.Dropout(0.25))
  model.add(tf.keras.layers.Flatten())
  model.add(tf.keras.layers.Dense(128, activation='relu'))
  model.add(tf.keras.layers.Dropout(0.5))
  model.add(tf.keras.layers.Dense(NUM_CLASSES, activation='softmax'))

  # Adding custom pass-through layer for summary recording.
  model.add(LayerForWritingHistogramSummary())
  return model


def run():
  """Run the model training and return evaluation output."""
  resolver = tf.distribute.cluster_resolver.TPUClusterResolver(tpu=FLAGS.tpu)
  tf.config.experimental_connect_to_cluster(resolver, protocol=FLAGS.protocol)
  logging.info('Remote eager configured')
  tf.tpu.experimental.initialize_tpu_system(resolver)
  strategy = tf.distribute.experimental.TPUStrategy(resolver)

  (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

  x_train = x_train.reshape(x_train.shape[0], IMG_ROWS, IMG_COLS, 1)
  x_test = x_test.reshape(x_test.shape[0], IMG_ROWS, IMG_COLS, 1)
  input_shape = (IMG_ROWS, IMG_COLS, 1)

  x_train = x_train.astype('float32')
  x_test = x_test.astype('float32')
  x_train /= 255
  x_test /= 255
  print('x_train shape:', x_train.shape)
  print(x_train.shape[0], 'train samples')
  print(x_test.shape[0], 'test samples')
  steps_per_epoch = int(x_train.shape[0] / BATCH_SIZE)
  steps_per_eval = int(x_test.shape[0] / BATCH_SIZE)

  # convert class vectors to binary class matrices
  y_train = tf.keras.utils.to_categorical(y_train, NUM_CLASSES)
  y_test = tf.keras.utils.to_categorical(y_test, NUM_CLASSES)

  train_dataset = tf.data.Dataset.from_tensor_slices((x_train, y_train))
  train_dataset = train_dataset.batch(BATCH_SIZE, drop_remainder=True).repeat()
  test_dataset = tf.data.Dataset.from_tensor_slices((x_test, y_test))
  test_dataset = test_dataset.batch(BATCH_SIZE, drop_remainder=True).repeat()

  with strategy.scope():
    model = mnist_model(input_shape)
    optimizer = tf.keras.optimizers.SGD(learning_rate=0.05)
    logging.info('Finished building Keras MNIST model')
    model.compile(optimizer, loss=tf.keras.losses.categorical_crossentropy)

    # Writing summary logs to file may have performance impact. Therefore, we
    # only write summary events every 100th steps.
    tensorboard_callback = tf.keras.callbacks.TensorBoard(
        FLAGS.model_dir, update_freq=100)
    model.fit(
        x=train_dataset,
        epochs=_EPOCHS,
        steps_per_epoch=steps_per_epoch,
        validation_steps=steps_per_eval,
        validation_data=test_dataset,
        callbacks=[tensorboard_callback])


def main(unused_dev):
  run()


if __name__ == '__main__':
  logging.set_verbosity(logging.INFO)
  tf.enable_v2_behavior()

  # Soft device placement should be enabled to automatically place
  # summary ops to CPU.
  tf.config.set_soft_device_placement(True)

  app.run(main)
```
