---
id: "legacy_03_hf_training_scripts_legacy"
title: "Hugging Face training scripts — legacy TPU instructions"
url: "https://huggingface.co/docs/transformers/run_scripts"
category: "Legacy docs"
description: "The TPU section uses PyTorch/XLA and xla_spawn.py; do not treat it as the current TorchTPU setup."
crawled_at: "2026-10-26T12:44:53.045494+00:00"
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
Fine-tuning
# Transformers
🏡 View all docs AWS Trainium & Inferentia Accelerate Argilla AutoTrain Bitsandbytes CLI Chat UI Dataset viewer Datasets Deploying on AWS Diffusers Distilabel Evaluate Google Cloud Google TPUs Gradio Hub Hub Python Library Huggingface.js Inference Endpoints (dedicated) Inference Providers Kernels LeRobot Leaderboards Lighteval Microsoft Azure OpenEnv Optimum PEFT Reachy Mini Safetensors Sentence Transformers TRL Tasks Text Embeddings Inference Text Generation Inference Tokenizers Trackio Transformers Transformers.js Xet smolagents timm
Search documentation
`Ctrl+K`
main v5.20.2 v5.19.0 v5.17.0 v5.15.1 v5.14.0 v5.13.1 v5.12.0 v5.11.0 v5.10.4 v5.9.0 v5.8.1 v5.7.0 v5.6.2 v5.5.4 v5.4.0 v5.3.0 v5.2.0 v5.1.0 v5.0.0 v4.57.6 v4.56.2 v4.55.4 v4.53.3 v4.52.3 v4.51.3 v4.50.0 v4.49.0 v4.48.2 v4.47.1 v4.46.3 v4.45.2 v4.44.2 v4.43.4 v4.42.4 v4.41.2 v4.40.2 v4.39.3 v4.38.2 v4.37.2 v4.36.1 v4.35.2 v4.34.1 v4.33.3 v4.32.1 v4.31.0 v4.30.0 v4.29.1 v4.28.1 v4.27.2 v4.26.1 v4.25.1 v4.24.0 v4.23.1 v4.22.2 v4.21.3 v4.20.1 v4.19.4 v4.18.0 v4.17.0 v4.16.2 v4.15.0 v4.14.1 v4.13.0 v4.12.5 v4.11.3 v4.10.1 v4.9.2 v4.8.2 v4.7.0 v4.6.0 v4.5.1 v4.4.2 v4.3.3 v4.2.2 v4.1.1 v4.0.1 v3.5.1 v3.4.0 v3.3.1 v3.2.0 v3.1.0 v3.0.2 v2.11.0 v2.10.0 v2.9.1 v2.8.0 v2.7.0 v2.6.0 v2.5.1 v2.4.1 v2.3.0 v2.2.2 v2.1.1 v2.0.0 v1.2.0 v1.1.0 v1.0.0 doc-builder-html AR DE EN ES FR HI IT JA KO PT RO TR ZH
[ 168,185](https://github.com/huggingface/transformers)
Get started
[Transformers](https://huggingface.co/docs/transformers/v5.20.2/index)[Installation](https://huggingface.co/docs/transformers/v5.20.2/installation)[Quickstart](https://huggingface.co/docs/transformers/v5.20.2/quicktour)
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
[Trainer overview](https://huggingface.co/docs/transformers/v5.20.2/trainer)[Fine-tuning](https://huggingface.co/docs/transformers/v5.20.2/training)
Customization
[Parameter-efficient fine-tuning](https://huggingface.co/docs/transformers/v5.20.2/peft)
Performance
Distributed training
Hardware
Quantization
Ecosystem integrations
Resources
API
![Hugging Face's logo](https://huggingface.co/front/assets/huggingface_logo-noborder.svg)
Join the Hugging Face community
and get access to the augmented documentation experience
Collaborate on models, datasets and Spaces
Faster examples with accelerated inference
Switch between documentation themes
[Sign Up](https://huggingface.co/join)
to get started
Copy page
#  [](https://huggingface.co/docs/transformers/v5.20.2/training#fine-tuning) Fine-tuning
Fine-tuning continues training a large pretrained model on a smaller dataset specific to a task or domain. For example, fine-tuning on a dataset of coding examples helps the model get better at coding. Fine-tuning is identical to pretraining except you don’t start with random weights. It also requires far less compute, data, and time.
The tutorial below walks through fine-tuning a large language model with [Trainer](https://huggingface.co/docs/transformers/v5.20.2/en/main_classes/trainer#transformers.Trainer).
Log in to your Hugging Face account with your user token to push your fine-tuned model to the Hub.
Copied

```
from huggingface_hub import login

login()
```

##  [](https://huggingface.co/docs/transformers/v5.20.2/training#tokenization) Tokenization
Load a dataset and [tokenize](https://huggingface.co/docs/transformers/v5.20.2/fast_tokenizers) the text column the model trains on (`horoscope` in the dataset below).
The tokenizer creates the model inputs, `input_ids` and `attention_mask`. The model’s forward method only accepts `input_ids` and `attention_mask`, so set `remove_columns` to drop columns like `horoscope` after tokenization.
  * Set `truncation=True` and a `max_length` to truncate longer sequences to a specified maximum length.
  * Use the `train_test_split` method to create a test split for evaluating the model.


Copied

```
from datasets import load_dataset
from transformers import AutoTokenizer, DataCollatorForLanguageModeling

model_name = "Qwen/Qwen3-0.6B"
tokenizer = AutoTokenizer.from_pretrained(model_name)
dataset = load_dataset("karthiksagarn/astro_horoscope", split="train")

def tokenize(batch):
    return tokenizer(
        batch["horoscope"],
        truncation=True,
        max_length=512,
    )

dataset = dataset.map(tokenize, batched=True, remove_columns=dataset.column_names)
dataset = dataset.train_test_split(test_size=0.1)
```

A data collator assembles dataset samples into batches for the model to process. [DataCollatorForLanguageModeling](https://huggingface.co/docs/transformers/v5.20.2/en/main_classes/data_collator#transformers.DataCollatorForLanguageModeling) _dynamically_ pads each batch to the longest sequence in that batch rather than padding every sequence in the dataset to the same length. This saves compute and memory by avoiding computing unnecessary padding tokens.
  * Set `mlm=False` to avoid randomly masking tokens.


Copied

```
data_collator = DataCollatorForLanguageModeling(tokenizer, mlm=False)
```

##  [](https://huggingface.co/docs/transformers/v5.20.2/training#loading-a-model) Loading a model
Load a pretrained checkpoint to fine-tune (see the [Loading models](https://huggingface.co/docs/transformers/v5.20.2/models) guide for more details about loading models).
  * Set `dtype="auto"` to load the weights in their saved dtype. Without it, PyTorch loads weights in `torch.float32`, which doubles memory usage if the weights are originally `torch.bfloat16`.


Copied

```
from transformers import AutoModelForCausalLM, TrainingArguments, Trainer

model_name = "Qwen/Qwen3-0.6B"
model = AutoModelForCausalLM.from_pretrained(model_name, dtype="auto")
```

##  [](https://huggingface.co/docs/transformers/v5.20.2/training#training-configuration) Training configuration
[TrainingArguments](https://huggingface.co/docs/transformers/v5.20.2/en/main_classes/trainer#transformers.TrainingArguments) provides all the options for customizing a training run. Only the most common arguments are covered here. Everything else has reasonable defaults or is only relevant to specific scenarios like distributed training. See the [TrainingArguments](https://huggingface.co/docs/transformers/v5.20.2/en/main_classes/trainer#transformers.TrainingArguments) API docs for a complete list of arguments.
training duration
training optimizations
evaluation and checkpointing
logging
  * `num_train_epochs` and `per_device_train_batch_size` control training duration and batch size. `learning_rate` sets the initial learning rate for the optimizer.


Copied

```
training_args = TrainingArguments(
    output_dir="qwen3-finetuned",
    num_train_epochs=3,
    per_device_train_batch_size=2,
    gradient_accumulation_steps=8,
    gradient_checkpointing=True,
    gradient_checkpointing_kwargs={"every_n_layers": 4},
    bf16=True,
    learning_rate=2e-5,
    logging_steps=10,
    eval_strategy="epoch",
    save_strategy="epoch",
    load_best_model_at_end=True,
)
```

##  [](https://huggingface.co/docs/transformers/v5.20.2/training#training) Training
Create a [Trainer](https://huggingface.co/docs/transformers/v5.20.2/en/main_classes/trainer#transformers.Trainer) instance with all the necessary components, then call [train()](https://huggingface.co/docs/transformers/v5.20.2/en/main_classes/trainer#transformers.Trainer.train) to begin.
Copied

```
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset["train"],
    eval_dataset=dataset["test"],
    processing_class=tokenizer,
    data_collator=DataCollatorForLanguageModeling(tokenizer, mlm=False),
)

trainer.train()
trainer.push_to_hub()
```

[push_to_hub()](https://huggingface.co/docs/transformers/v5.20.2/en/main_classes/trainer#transformers.Trainer.push_to_hub) uploads the fine-tuned weights, generation config, tokenizer, and model config to the Hub.
##  [](https://huggingface.co/docs/transformers/v5.20.2/training#next-steps) Next steps
  * Read the [Trainer features](https://huggingface.co/docs/transformers/v5.20.2/trainer_recipes) guide for minimal working examples of common Trainer features like custom loss functions, memory-efficient evaluation, checkpointing, and more.
  * Read the [Subclassing Trainer methods](https://huggingface.co/docs/transformers/v5.20.2/trainer_customize) guide to learn how to subclass [Trainer](https://huggingface.co/docs/transformers/v5.20.2/en/main_classes/trainer#transformers.Trainer) methods to support new and custom functionalities.
  * Read the [Callbacks](https://huggingface.co/docs/transformers/v5.20.2/trainer_callbacks) guide to learn how to hook into training events for logging, early stopping, and other custom behavior.
  * Read the [Data collators](https://huggingface.co/docs/transformers/v5.20.2/data_collators) guide to learn how to customize how samples are assembled into batches.
  * Run a training script on a rented GPU with [Hugging Face Jobs](https://huggingface.co/docs/hub/jobs-training).
  * Browse [notebooks](https://huggingface.co/docs/transformers/v5.20.2/notebooks) or the **Resources > Task Recipes** section for additional training examples on different text, audio, vision, and multimodal tasks.

[ Update on GitHub](https://github.com/huggingface/transformers/blob/main/docs/source/en/training.md)
[←Trainer overview](https://huggingface.co/docs/transformers/v5.20.2/trainer) [Subclassing Trainer methods→](https://huggingface.co/docs/transformers/v5.20.2/trainer_customize)
[Fine-tuning](https://huggingface.co/docs/transformers/v5.20.2/training#fine-tuning)[Tokenization](https://huggingface.co/docs/transformers/v5.20.2/training#tokenization)[Loading a model](https://huggingface.co/docs/transformers/v5.20.2/training#loading-a-model)[Training configuration](https://huggingface.co/docs/transformers/v5.20.2/training#training-configuration)[Training](https://huggingface.co/docs/transformers/v5.20.2/training#training)[Next steps](https://huggingface.co/docs/transformers/v5.20.2/training#next-steps)