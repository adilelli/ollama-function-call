from transformers import AutoTokenizer, AutoModelForCausalLM

# Load model and tokenizer
model_name = "huggingface/smolvlm-256m"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Generate text
prompt = "What is the capital of France?"
inputs = tokenizer(prompt, return_tensors="pt")
output = model.generate(**inputs, max_length=50)

# Decode and print the response
response = tokenizer.decode(output[0], skip_special_tokens=True)
print(response)
