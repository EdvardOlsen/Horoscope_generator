# Horoscope generator
This is a horoscope generating code \
This code was made by EdvardOlsen  \
The generator is based on fine-tuning model GPT-2 from OpenAI ([HuggingFace realization](https://github.com/huggingface/transformers/)) library  \
The dataset was taken from [here](https://github.com/dsnam/markovscope/) 


## Installation

To install clone this repo and run `chmod 777 setup.sh && ./setup.sh`

## Training

To train the model run `chmod 777 train.sh && ./train.sh`  \
Make sure to clone the transformers repo

## Inference

[Demo](https://colab.research.google.com/drive/1NMZAtj7wPU5hb4F1ruT5RZUj2KMzOzAA?usp=sharing)

if you want to run python script, `run generate.py` or use `telegram_bot.py`

``` python
>>> def generateHoro(raw_text):
>>>  context_tokens = tokenizer.encode(raw_text, add_special_tokens=False)
>>>  out = sample_sequence(
...      model=model,
...      context=context_tokens,
...      num_samples=1,
...      length=50,
...      device=device)
>>>  out = out[:, len(context_tokens):].tolist()[0]
>>>  text = raw_text + tokenizer.decode(out, clean_up_tokenization_spaces=True)
>>>  text = text.replace('\n', '').replace('\xa0', '')
>>>  return text
```

You can download pretrained weights from [here](https://drive.google.com/drive/folders/1X6et5EGgHrMmCl6lGemluaV-NOoK3cEH?usp=sharing)
