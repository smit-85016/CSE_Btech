import os
from transformers import AutoModelForCausalLM, AutoTokenizer
from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Load pre-trained transformer model and tokenizer
MODEL_NAME = "gpt2"
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("input")
    if not user_input:
        return jsonify({"error": "Invalid input"}), 400

    # Tokenize user input
    input_ids = tokenizer.encode(user_input, return_tensors="pt")

    # Generate response
    response_ids = model.generate(
        input_ids, 
        max_length=150, 
        num_return_sequences=1, 
        no_repeat_ngram_size=2, 
        top_p=0.95, 
        top_k=50
    )
    
    # Decode the response
    response = tokenizer.decode(response_ids[0], skip_special_tokens=True)
    
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ.get("PORT", 5000)))
