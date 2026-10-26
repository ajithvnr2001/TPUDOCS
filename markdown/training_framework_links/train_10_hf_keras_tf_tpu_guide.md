---
id: "train_10_hf_keras_tf_tpu_guide"
title: "Hugging Face Keras/TF TPU guide"
url: "https://huggingface.co/docs/transformers/main/en/perf_train_tpu_tf"
category: "Training framework links"
description: "Usable Keras sequence-classification example: initialize TPUClusterResolver, TPUStrategy, load/tokenize data, create the model inside strategy.scope(), and call model.fit()."
crawled_at: "2026-10-26T12:45:46.944214+00:00"
crawler_engine: "Crawl4AI"
---

[![Hugging Face's logo](https://huggingface.co/front/assets/huggingface_logo-noborder.svg) Hugging Face](https://huggingface.co/)
  * [ Models ](https://huggingface.co/models)
  * [ Datasets ](https://huggingface.co/datasets)
  * [ Spaces ](https://huggingface.co/spaces)
  * [ Buckets new](https://huggingface.co/storage)
  * [ Docs ](https://huggingface.co/docs)
  * [ Enterprise ](https://huggingface.co/enterprise)
  * [Pricing](https://huggingface.co/pricing)
  *     * Website
      * [ Tasks](https://huggingface.co/tasks)
      * [ HuggingChat](https://huggingface.co/chat)
      * [ Collections](https://huggingface.co/collections)
      * [ Languages](https://huggingface.co/languages)
      * [ Organizations](https://huggingface.co/organizations)
    * Community
      * [ Blog](https://huggingface.co/blog)
      * [ Posts](https://huggingface.co/posts)
      * [ Daily Papers](https://huggingface.co/papers)
      * [ Hardware](https://huggingface.co/hardware)
      * [ Learn](https://huggingface.co/learn)
      * [ Discord](https://huggingface.co/join/discord)
      * [ Forum](https://discuss.huggingface.co/)
      * [ GitHub](https://github.com/huggingface)
    * Solutions
      * [ Team & Enterprise](https://huggingface.co/enterprise)
      * [ Hugging Face PRO](https://huggingface.co/pro)
      * [ Enterprise Support](https://huggingface.co/support)
      * [ Inference Providers](https://huggingface.co/inference/models)
      * [ Inference Endpoints](https://huggingface.co/inference-endpoints)
      * [ Storage Buckets](https://huggingface.co/storage)
  * * * *
  * [Log In](https://huggingface.co/login)
  * [Sign Up](https://huggingface.co/join)


Transformers documentation
TPU
# Transformers
🏡 View all docs AWS Trainium & Inferentia Accelerate Argilla AutoTrain Bitsandbytes CLI Chat UI Dataset viewer Datasets Deploying on AWS Diffusers Distilabel Evaluate Google Cloud Google TPUs Gradio Hub Hub Python Library Huggingface.js Inference Endpoints (dedicated) Inference Providers Kernels LeRobot Leaderboards Lighteval Microsoft Azure OpenEnv Optimum PEFT Reachy Mini Safetensors Sentence Transformers TRL Tasks Text Embeddings Inference Text Generation Inference Tokenizers Trackio Transformers Transformers.js Xet smolagents timm
Search documentation
`Ctrl+K`
main v5.20.2 v5.19.0 v5.17.0 v5.15.1 v5.14.0 v5.13.1 v5.12.0 v5.11.0 v5.10.4 v5.9.0 v5.8.1 v5.7.0 v5.6.2 v5.5.4 v5.4.0 v5.3.0 v5.2.0 v5.1.0 v5.0.0 v4.57.6 v4.56.2 v4.55.4 v4.53.3 v4.52.3 v4.51.3 v4.50.0 v4.49.0 v4.48.2 v4.47.1 v4.46.3 v4.45.2 v4.44.2 v4.43.4 v4.42.4 v4.41.2 v4.40.2 v4.39.3 v4.38.2 v4.37.2 v4.36.1 v4.35.2 v4.34.1 v4.33.3 v4.32.1 v4.31.0 v4.30.0 v4.29.1 v4.28.1 v4.27.2 v4.26.1 v4.25.1 v4.24.0 v4.23.1 v4.22.2 v4.21.3 v4.20.1 v4.19.4 v4.18.0 v4.17.0 v4.16.2 v4.15.0 v4.14.1 v4.13.0 v4.12.5 v4.11.3 v4.10.1 v4.9.2 v4.8.2 v4.7.0 v4.6.0 v4.5.1 v4.4.2 v4.3.3 v4.2.2 v4.1.1 v4.0.1 v3.5.1 v3.4.0 v3.3.1 v3.2.0 v3.1.0 v3.0.2 v2.11.0 v2.10.0 v2.9.1 v2.8.0 v2.7.0 v2.6.0 v2.5.1 v2.4.1 v2.3.0 v2.2.2 v2.1.1 v2.0.0 v1.2.0 v1.1.0 v1.0.0 doc-builder-html AR DE EN ES FR HI IT JA KO PT RO TE TR ZH
[ ](https://github.com/huggingface/transformers)
Get started
[Transformers](https://huggingface.co/docs/transformers/main/en/index)[Installation](https://huggingface.co/docs/transformers/main/en/installation)[Quickstart](https://huggingface.co/docs/transformers/main/en/quicktour)
Base classes
Models
Preprocessors
Inference
Pipeline API
Generate API
Optimization
Chat with models
Serving
Training
Get started
Customization
[Parameter-efficient fine-tuning](https://huggingface.co/docs/transformers/main/en/peft)
Performance
Distributed training
Hardware
Quantization
Ecosystem integrations
Resources
API
You are viewing main version, which requires [installation from source](https://huggingface.co/docs/transformers/installation#install-from-source). If you'd like regular pip install, checkout the latest stable version ([v5.20.2](https://huggingface.co/docs/transformers/v5.20.2/perf_train_tpu_tf)).
![Hugging Face's logo](https://huggingface.co/front/assets/huggingface_logo-noborder.svg)
Join the Hugging Face community
and get access to the augmented documentation experience
Collaborate on models, datasets and Spaces
Faster examples with accelerated inference
Switch between documentation themes
[Sign Up](https://huggingface.co/join)
to get started
#  [](https://huggingface.co/docs/transformers/main/en/perf_train_tpu_tf#tpu) TPU
TPU (Tensor Processing Unit) is a type of hardware designed to accelerate tensor computations for training and inference. TPUs are generally accessed through Google cloud services, but smaller TPUs are also available for free from [Google Colab](https://colab.research.google.com/notebooks/tpu.ipynb) or [Kaggle](https://www.kaggle.com/docs/tpu).
This guide focuses on training a Keras model for sequence classification on a TPU from Google Colab. Make sure the TPU runtime is enabled by going to **Runtime > Change runtime type** and selecting a TPU.
Run the command below to install the latest version of Transformers and [Datasets](https://huggingface.co/docs/datasets).
Copied

```
!pip install --U transformers datasets
```

Create an instance of [tf.distribute.cluster_resolver.TPUClusterResolver](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/TPUClusterResolver), and then connect to the remote cluster and initialize the TPUs.
Copied

```
import tensorflow as tf

resolver = tf.distribute.cluster_resolver.TPUClusterResolver()
tf.config.experimental_connect_to_cluster(resolver)
tf.tpu.experimental.initialize_tpu_system(resolver)
```

There are various distribution strategies for running your model on multiple TPUs. The [tpu.distribute.TPUStrategy](https://www.tensorflow.org/api_docs/python/tf/distribute/TPUStrategy) offers synchronized distributed training.
Copied

```
strategy = tf.distribute.TPUStrategy(resolver)
```

Load and tokenize a dataset - this example uses [CoLA](https://huggingface.co/datasets/nyu-mll/glue/viewer/cola) from the GLUE benchmark - and pad all samples to the maximum length so it is easier to load as an array and to avoid [XLA compilation issues](https://huggingface.co/docs/transformers/main/en/perf_train_tpu_tf#xla).
Copied

```
from transformers import AutoTokenizer
from datasets import load_dataset
import numpy as np

dataset = load_dataset("glue", "cola")["train"]
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-cased")

train_data = tokenizer(
    dataset["sentence"],
    padding="max_length",
    truncation=True,
    max_length=128,
    return_tensors="np",
)
train_data = dict(train_data)
train_labels = np.array(dataset["label"])
```

The model **must** be created inside [Strategy.scope](https://www.tensorflow.org/api_docs/python/tf/distribute/MirroredStrategy#scope) in order to replicate the model layers on each TPU device.
Copied

```
from transformers import TFAutoModelForSequenceClassification

with strategy.scope():
    model = TFAutoModelForSequenceClassification.from_pretrained(model_checkpoint)
    model.compile(optimizer="adam")
```

TPUs only accept [tf.data.Dataset](https://www.tensorflow.org/api_docs/python/tf/data/Dataset) inputs unlike the Keras [fit](https://keras.io/api/models/model_training_apis/#fit-method) method which accepts a broader range of inputs.
Copied

```
BATCH_SIZE = 8 * strategy.num_replicas_in_sync

tf_dataset = tf.data.Dataset.from_tensor_slices((train_data, train_labels))
tf_dataset = tf_dataset.shuffle(len(tf_dataset))
tf_dataset = tf_dataset.batch(BATCH_SIZE, drop_remainder=True)
```

Finally, call [fit](https://keras.io/api/models/model_training_apis/#fit-method) to start training.
Copied

```
model.fit(tf_dataset)
```

##  [](https://huggingface.co/docs/transformers/main/en/perf_train_tpu_tf#large-datasets) Large datasets
The dataset created above pads every sample to the maximum length and loads the whole dataset into memory. This may not be possible if you’re working with larger datasets. When training on large datasets, you may want to create a [tf.TFRecord](https://www.tensorflow.org/tutorials/load_data/tfrecord) or stream the data.
###  [](https://huggingface.co/docs/transformers/main/en/perf_train_tpu_tf#tftfrecord) tf.TFRecord
[tf.TFRecord](https://www.tensorflow.org/tutorials/load_data/tfrecord) is the standard [tf.data](https://www.tensorflow.org/guide/data) format for storing training data. For very large training jobs, it’s worth preprocessing your data and storing it in the `tf.TFRecord` format and building a `tf.data` pipeline on top. Refer to the table below to help you decide whether `tf.TFRecord` is helpful for you.  
| pros  | cons  |  
| --- | --- |  
| works on all TPU instances  | costs associated with cloud storage  |  
| supports huge datasets and massive throughput  | some data types (images) can take a lot of space to store  |  
| suitable for training on entire TPU pods  |   |  
| preprocessing is done in advance, maximizing training speed  |   |  
Preprocess and tokenize the dataset before writing it to a `tf.TFRecord` to avoid writing every time the data is loaded.
An exception is made for _train-time augmentations_ , because augmentations applied after writing to a `tf.TFRecord` results in the same augmentation for each epoch. Instead, apply augmentations in the `tf.data` pipeline that loads the data.
In practice, you probably won’t be able to load the entire dataset in memory. Load a chunk of the dataset at a time and convert it to `TFRecord`, and repeat until the entire dataset is in the `TFRecord` format. Then you can use a list of all the files to create a `TFRecordDataset`. The example below demonstrates a single file for simplicity.
Copied

```
tokenized_data = tokenizer(
    dataset["sentence"],
    padding="max_length",
    truncation=True,
    max_length=128,
    return_tensors="np",
)
labels = dataset["label"]

with tf.io.TFRecordWriter("dataset.tfrecords") as file_writer:
    for i in range(len(labels)):
        features = {
            "input_ids": tf.train.Feature(
                int64_list=tf.train.Int64List(value=tokenized_data["input_ids"][i])
            ),
            "attention_mask": tf.train.Feature(
                int64_list=tf.train.Int64List(value=tokenized_data["attention_mask"][i])
            ),
            "labels": tf.train.Feature(
                int64_list=tf.train.Int64List(value=[labels[i]])
            ),
        }
        features = tf.train.Features(feature=features)
        example = tf.train.Example(features=features)
        record_bytes = example.SerializeToString()
        file_writer.write(record_bytes)
```

Build a [TFRecordDataset](https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset) using the saved filename to load it.
Copied

```
def decode_fn(sample):
    features = {
        "input_ids": tf.io.FixedLenFeature((128,), dtype=tf.int64),
        "attention_mask": tf.io.FixedLenFeature((128,), dtype=tf.int64),
        "labels": tf.io.FixedLenFeature((1,), dtype=tf.int64),
    }
    return tf.io.parse_example(sample, features)

# TFRecordDataset can handle gs:// paths
tf_dataset = tf.data.TFRecordDataset(["gs://matt-tf-tpu-tutorial-datasets/cola/dataset.tfrecords"])
tf_dataset = tf_dataset.map(decode_fn)
tf_dataset = tf_dataset.shuffle(len(dataset)).batch(BATCH_SIZE, drop_remainder=True)
tf_dataset = tf_dataset.apply(
    tf.data.experimental.assert_cardinality(len(labels) // BATCH_SIZE)
)
```

The dataset can now be passed to the [fit](https://keras.io/api/models/model_training_apis/#fit-method) method.
Copied

```
model.fit(tf_dataset)
```

###  [](https://huggingface.co/docs/transformers/main/en/perf_train_tpu_tf#stream-from-raw-data) Stream from raw data
Data can be stored in its native format and preprocessed in a [tf.data](https://www.tensorflow.org/guide/data) pipeline as the data is loaded. This approach isn’t supported for many models with complex tokenization schemes, but some models like BERT are supported because their tokenization can be compiled. Refer to the table below to help you decide whether this approach is helpful for you.  
| pros  | cons  |  
| --- | --- |  
| suitable for highly compressed big data in native format (images, audio)  | requires writing a full preprocessing pipeline  |  
| convenient if raw data is available in a public cloud bucket  | complex preprocessing on-the-fly can hurt throughput  |  
| works on all TPU instances if data is stored in Google Cloud  | must place data in cloud storage if not already there  |  
|   | not as suitable for text data because writing a tokenization pipeline is hard (use `TFRecord` for text)  |  
The example below demonstrates streaming data for an image model.
Load an image dataset and get a list of the underlying image file paths and labels.
Copied

```
from datasets import load_dataset

image_dataset = load_dataset("beans", split="train")
filenames = image_dataset["image_file_path"]
labels = image_dataset["labels"]
```

Convert the local filenames in the dataset into `gs://` paths in Google Cloud Storage.
Copied

```
# strip everything but the category directory and filenames
base_filenames = ['/'.join(filename.split('/')[-2:]) for filename in filenames]
# prepend the Google Cloud base path to everything instead
gs_paths = ["gs://matt-tf-tpu-tutorial-datasets/beans/"+filename for filename in base_filenames]

# create tf_dataset
tf_dataset = tf.data.Dataset.from_tensor_slices(
    {"filename": gs_paths, "labels": labels}
)
tf_dataset = tf_dataset.shuffle(len(tf_dataset))
```

Transformers preprocessing classes like [AutoImageProcessor](https://huggingface.co/docs/transformers/main/en/model_doc/auto#transformers.AutoImageProcessor) are framework-agnostic and can’t be compiled into a pipeline by `tf.data`. To get around this, get the normalization values (`mean` and `std`) from the [AutoImageProcessor](https://huggingface.co/docs/transformers/main/en/model_doc/auto#transformers.AutoImageProcessor) and use them in the `tf.data` pipeline.
Copied

```
from transformers import AutoImageProcessor

processor = AutoImageProcessor.from_pretrained("google/vit-base-patch16-224")
image_size = (processor.size["height"], processor.size["width"])
image_mean = processor.image_mean
image_std = processor.image_std
```

Use these normalization values to create a function to load and preprocess the images.
Copied

```
BATCH_SIZE = 8 * strategy.num_replicas_in_sync

def decode_fn(sample):
    image_data = tf.io.read_file(sample["filename"])
    image = tf.io.decode_jpeg(image_data, channels=3)
    image = tf.image.resize(image, image_size)
    array = tf.cast(image, tf.float32)
    array /= 255.0
    array = (array - image_mean) / image_std
    array = tf.transpose(array, perm=[2, 0, 1])
    return {"pixel_values": array, "labels": sample["labels"]}

tf_dataset = tf_dataset.map(decode_fn)
tf_dataset = tf_dataset.batch(BATCH_SIZE, drop_remainder=True)
print(tf_dataset.element_spec)
```

The dataset can now be passed to the [fit](https://keras.io/api/models/model_training_apis/#fit-method) method.
Copied

```
from transformers import TFAutoModelForImageClassification

with strategy.scope():
    model = TFAutoModelForImageClassification.from_pretrained(image_model_checkpoint)
    model.compile(optimizer="adam")

model.fit(tf_dataset)
```

###  [](https://huggingface.co/docs/transformers/main/en/perf_train_tpu_tf#stream-with-preparetfdataset) Stream with prepare_tf_dataset
[prepare_tf_dataset()](https://huggingface.co/docs/transformers/main/en/main_classes/model#transformers.TFPreTrainedModel.prepare_tf_dataset) creates a `tf.data` pipeline that loads samples from [tf.data.Dataset](https://www.tensorflow.org/api_docs/python/tf/data/Dataset). The pipeline uses [tf.numpy_function](https://huggingface.co/docs/transformers/main/en/perf_train_tpu_tf) or [from_generator](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.Dataset.from_generator), which can’t be compiled by TensorFlow, to access the underlying `tf.data.Dataset`. It also won’t work on a Colab TPU or TPU Nodes because the pipeline streams data from a local disk. Refer to the table below to help you decide whether this approach is helpful for you.  
| pros  | cons  |  
| --- | --- |  
| simple code  | only works on TPU VM  |  
| same approach on TPU/GPU  | data must be available as a Hugging Face Dataset  |  
| dataset doesn’t have to fit in memory  | data must fit on local storage  |  
| supports variable padding  | data loading may be a bottleneck on a big TPU pod slice  |  
[prepare_tf_dataset()](https://huggingface.co/docs/transformers/main/en/main_classes/model#transformers.TFPreTrainedModel.prepare_tf_dataset) only works on [TPU VM](https://huggingface.co/docs/transformers/main/en/perf_train_tpu_tf#tpu-types). Add the tokenizer output as columns in the dataset since the dataset is stored on disk, which means it can handle data larger than the available memory. Use [prepare_tf_dataset()](https://huggingface.co/docs/transformers/main/en/main_classes/model#transformers.TFPreTrainedModel.prepare_tf_dataset) to stream data from the dataset by wrapping it with a `tf.data` pipeline.
Copied

```
def tokenize_function(examples):
    return tokenizer(
        examples["sentence"], padding="max_length", truncation=True, max_length=128
    )
# add the tokenizer output to the dataset as new columns
dataset = dataset.map(tokenize_function)

# prepare_tf_dataset() chooses columns that match the models input names
tf_dataset = model.prepare_tf_dataset(
    dataset, batch_size=BATCH_SIZE, shuffle=True, tokenizer=tokenizer
)
```

The dataset can now be passed to the [fit](https://keras.io/api/models/model_training_apis/#fit-method) method.
Copied

```
from transformers import AutoTokenizer, TFAutoModelForSequenceClassification

with strategy.scope():
    model = TFAutoModelForSequenceClassification.from_pretrained(model_checkpoint)
    model.compile(optimizer="adam")

model.fit(tf_dataset)
```

##  [](https://huggingface.co/docs/transformers/main/en/perf_train_tpu_tf#tpu-types) TPU types
There are two types of TPUs, a TPU Node and a TPU VM.
A TPU Node indirectly accesses a remote TPU. It requires a separate VM to initialize your network and data pipeline, and then forwards it to the remote node. Google Colab TPUs are an example of a TPU Node. You can’t use local data because the TPU is remotely located, and data must be stored in Google Cloud Storage where the data pipeline can access it.
TPU VM are connected directly to the machine the TPU is located on, and they are generally easier to work with, especially when it comes to your data pipeline.
We recommend avoiding TPU Nodes if possible because it is more difficult to debug than TPU VMs. TPU Nodes may also be unsupported in the future and become a legacy access method.
A single TPU (v2-8, v3-8, v4-8) runs 8 replicas. TPUs can exist in **pods** which run hundreds or even thousands of replicas simultaneously. When you only use a portion of a pod, it is referred to as a **pod slice**. On Google Colab, you’ll typically get a single v2-8 TPU.
##  [](https://huggingface.co/docs/transformers/main/en/perf_train_tpu_tf#xla) XLA
[XLA](https://openxla.org/xla) is a linear algebra compiler for high-performance execution and it is used by default to improve performance on TPUs.
Before executing your code on a TPU, it’s a good idea to try it first on a CPU or GPU because it is easier to debug. You can train for a few steps to make sure the model and data pipeline work as expected. Set `jit_compile=True` in the [compile](https://keras.io/api/models/model_training_apis/#compile-method) method to enable XLA compilation (but remember to remove this line of code before running on a TPU).
The section below outlines three rules for making your code XLA-compatible. Transformers enforce the first two rules for models and loss functions by default, but don’t forget about them if you’re writing your own models and loss functions.
###  [](https://huggingface.co/docs/transformers/main/en/perf_train_tpu_tf#data-dependent-conditionals) Data dependent conditionals
Any `if` statements cannot depend on values inside a [tf.Tensor](https://www.tensorflow.org/api_docs/python/tf/Tensor). The code below can’t be compiled by XLA.
Copied

```
if tf.reduce_sum(tensor) > 10:
    tensor = tensor / 2.0
```

To compile with XLA, use [tf.cond](https://www.tensorflow.org/api_docs/python/tf/cond) or remove the conditional and use indicator variables instead as shown below.
Copied

```
sum_over_10 = tf.cast(tf.reduce_sum(tensor) > 10, tf.float32)
tensor = tensor / (1.0 + sum_over_10)
```

###  [](https://huggingface.co/docs/transformers/main/en/perf_train_tpu_tf#data-dependent-shapes) Data dependent shapes
The shape of a [tf.Tensor](https://www.tensorflow.org/api_docs/python/tf/Tensor) cannot depend on their values. For example, [tf.unique](https://www.tensorflow.org/api_docs/python/tf/unique) can’t be compiled because it returns a tensor containing an instance of each unique value in the input. The shape of this output depends on how repetitive the input [tf.Tensor](https://www.tensorflow.org/api_docs/python/tf/Tensor) is.
This is an issue during **label masking** , where labels are set to a negative value to indicate they should be ignored when computing the loss. The code below can’t be compiled by XLA because the shape of `masked_outputs` and `masked_labels` depend on how many positions are masked.
Copied

```
label_mask = labels >= 0
masked_outputs = outputs[label_mask]
masked_labels = labels[label_mask]
loss = compute_loss(masked_outputs, masked_labels)
mean_loss = torch.mean(loss)
```

To compile with XLA, avoid the data-dependent shapes by computing the loss for every position and zeroing out the masked positions in both the numerator and denominator when calculating the mean. Convert `tf.bool` to `tf.float32` as an indicator variable to make your code XLA-compatible.
Copied

```
label_mask = tf.cast(labels >= 0, tf.float32)
loss = compute_loss(outputs, labels)
loss = loss * label_mask
mean_loss = tf.reduce_sum(loss) / tf.reduce_sum(label_mask)
```

###  [](https://huggingface.co/docs/transformers/main/en/perf_train_tpu_tf#recompile-different-input-shapes) Recompile different input shapes
XLA recompiles your model if input shapes are variable which create huge performance problems. It is especially common in text models because input texts have variable lengths after tokenization.
Execessive padding can also severely slow down training because requires more compute and memory to process.
To avoid different shapes, use padding to pad all your inputs to the same length and use an `attention_mask`. Try padding batches of samples to a multiple of 32 or 64 tokens. Use the parameters `padding="max_length"`, `padding="longest"`, or `pad_to_multiple_of` to help with padding. This often increases the number of tokens by a small amount, but it significantly reduces the number of unique input shapes because every input shape is a multiple of 32 or 64. Fewer unique input shapes requires fewer recompilation.
[< > Update on GitHub](https://github.com/huggingface/transformers/blob/main/docs/source/en/perf_train_tpu_tf.md)
[Transformers→](https://huggingface.co/docs/transformers/main/en/index)
[TPU](https://huggingface.co/docs/transformers/main/en/perf_train_tpu_tf#tpu)[Large datasets](https://huggingface.co/docs/transformers/main/en/perf_train_tpu_tf#large-datasets)[tf.TFRecord](https://huggingface.co/docs/transformers/main/en/perf_train_tpu_tf#tftfrecord)[Stream from raw data](https://huggingface.co/docs/transformers/main/en/perf_train_tpu_tf#stream-from-raw-data)[Stream with prepare_tf_dataset](https://huggingface.co/docs/transformers/main/en/perf_train_tpu_tf#stream-with-preparetfdataset)[TPU types](https://huggingface.co/docs/transformers/main/en/perf_train_tpu_tf#tpu-types)[XLA](https://huggingface.co/docs/transformers/main/en/perf_train_tpu_tf#xla)[Data dependent conditionals](https://huggingface.co/docs/transformers/main/en/perf_train_tpu_tf#data-dependent-conditionals)[Data dependent shapes](https://huggingface.co/docs/transformers/main/en/perf_train_tpu_tf#data-dependent-shapes)[Recompile different input shapes](https://huggingface.co/docs/transformers/main/en/perf_train_tpu_tf#recompile-different-input-shapes)