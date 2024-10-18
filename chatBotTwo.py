import streamlit as st
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration

# Load the pre-trained BlenderBot model and tokenizer
model_name = "facebook/blenderbot-400M-distill"
tokenizer = BlenderbotTokenizer.from_pretrained(model_name)
model = BlenderbotForConditionalGeneration.from_pretrained(model_name)

# Function to generate chatbot responses
def chatbot_response(user_input):
    # Encode user input and add EOS token
    inputs = tokenizer([user_input], return_tensors="pt")

    # Generate chatbot response
    reply_ids = model.generate(**inputs)

    # Decode and return the response
    bot_reply = tokenizer.decode(reply_ids[0], skip_special_tokens=True)
    return bot_reply

# Streamlit app layout
st.title("BlenderBot AI Chatbot")
st.write("Type your message and interact with the AI chatbot!")

# Input field for user message
user_input = st.text_input("You: ", "")

# Chat history to keep track of the conversation
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# If the user enters a message, generate a response
if st.button("Send"):
    if user_input:
        # Get chatbot response
        bot_response = chatbot_response(user_input)
        
        # Update the chat history
        st.session_state.chat_history.append(f"You: {user_input}")
        st.session_state.chat_history.append(f"Chatbot: {bot_response}")

# Display the conversation history
if st.session_state.chat_history:
    st.write("### Conversation History")
    for message in st.session_state.chat_history:
        st.write(message)
