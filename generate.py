import torch
from utils import sample_sequence
from transformers import GPT2LMHeadModel, GPT2Tokenizer


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model_class, tokenizer_class = (GPT2LMHeadModel, GPT2Tokenizer)
tokenizer = tokenizer_class.from_pretrained('output')
model = model_class.from_pretrained('output')
model.to(device)
model.eval()

def generateHoro(raw_text):
  context_tokens = tokenizer.encode(raw_text, add_special_tokens=False)
  out = sample_sequence(
      model=model,
      context=context_tokens,
      num_samples=1,
      length=50,
      device=device)
  out = out[:, len(context_tokens):].tolist()[0]
  text = raw_text + tokenizer.decode(out, clean_up_tokenization_spaces=True)
  text = text.replace('\n', '').replace('\xa0', '')
  return text

def main():
  text = 'today '
  print(generateHoro(text))
  
if __name__ == '__main__':
  main()
