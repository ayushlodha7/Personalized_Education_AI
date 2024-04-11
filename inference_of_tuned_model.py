import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

def load_model_and_tokenizer(model_name):
    """
    Load the fine-tuned model and tokenizer from Hugging Face.
    
    Args:
    model_name (str): The model repository on Hugging Face.
    
    Returns:
    model: The loaded model.
    tokenizer: The loaded tokenizer.
    """
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    model.eval()  # Set the model to evaluation mode
    if torch.cuda.is_available():
        model.to('cuda')  # Move model to GPU if available
    return model, tokenizer

def generate_response(model, tokenizer, input_text):
    """
    Generate a response from the model based on the input text.
    
    Args:
    model: The loaded model.
    tokenizer: The loaded tokenizer.
    input_text (str): Input text to generate a response for.
    
    Returns:
    str: The generated text response from the model.
    """
    # Encode the input text
    inputs = tokenizer(input_text, return_tensors='pt', max_length=512, truncation=True)
    if torch.cuda.is_available():
        inputs = {k: v.to('cuda') for k, v in inputs.items()}
    
    # Generate a response
    with torch.no_grad():
        outputs = model.generate(**inputs, max_length=1024, num_beams=5, early_stopping=True)
    
    # Decode and return the response
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

# Example usage
if __name__ == "__main__":
    model_name = 'your_hf_username/your_repo_name'  # Replace with your actual model repo
    model, tokenizer = load_model_and_tokenizer(model_name)
    
    # Example input text
    input_text = "Explain the theory of relativity"
    response = generate_response(model, tokenizer, input_text)
    print("Generated Response:", response)
