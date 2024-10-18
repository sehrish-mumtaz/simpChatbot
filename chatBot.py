# ai_chatbot.py

import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Step 1: Load the model and tokenizer from Hugging Face
model_name = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Step 2: Initialize chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Step 3: Define a function to generate responses
def generate_response(user_input):
    # Encode the new user input and append to chat history
    new_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors="pt")

    # Concatenate the chat history with the new input
    if st.session_state.chat_history:
        bot_input_ids = torch.cat([torch.tensor(st.session_state.chat_history), new_input_ids], dim=-1)
    else:
        bot_input_ids = new_input_ids

    # Generate the model's response
    chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)

    # Decode and return the bot response
    bot_response = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
    
    # Update the chat history
    st.session_state.chat_history.append(new_input_ids)
    
    return bot_response

# Step 4: Create the Streamlit app layout
st.title("AI Education Chatbot")
st.write("Ask me anything about Artificial Intelligence!")

# User input field
user_input = st.text_input("You:", "")

# When the user submits a question
if st.button("Send"):
    if user_input:
        response = generate_response(user_input)
        st.session_state.chat_history.append(user_input)
        
        # Display the chatbot's response
        st.text_area("Chatbot:", value=response, height=150, max_chars=None, key="response", disabled=True)

# Step 5: Display previous conversation history
if st.session_state.chat_history:
    st.write("### Conversation History:")
    for idx, entry in enumerate(st.session_state.chat_history):
        st.write(f"You: {entry}")
        if idx < len(st.session_state.chat_history) - 1:
            st.write(f"Chatbot: {tokenizer.decode(st.session_state.chat_history[idx + 1][0], skip_special_tokens=True)}")
