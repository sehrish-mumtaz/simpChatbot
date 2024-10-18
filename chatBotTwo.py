import streamlit as st

# Function to generate chatbot responses
def chatbot_response(user_input):
    # Dictionary of predefined responses
    responses = {
        "what is ai": "AI stands for Artificial Intelligence. It refers to the simulation of human intelligence in machines that are programmed to think and learn like humans.",
        "what are the types of ai": "There are three main types of AI: Narrow AI, General AI, and Superintelligent AI. Narrow AI is designed to perform specific tasks, General AI can perform any intellectual task that a human can do, and Superintelligent AI surpasses human intelligence.",
        "what is machine learning": "Machine learning is a subset of AI that focuses on developing algorithms that allow computers to learn and make decisions from data without being explicitly programmed.",
        "what is deep learning": "Deep learning is a subset of machine learning that uses neural networks with many layers (deep networks) to model and understand complex patterns in data.",
        "what is natural language processing": "Natural Language Processing (NLP) is a branch of AI that focuses on the interaction between computers and humans using natural language. NLP allows machines to read, understand, and respond to human language.",
        "quit": "Goodbye! I hope you learned something about AI."
    }

    # Lowercase the user input to handle variations
    user_input = user_input.lower()

    # Provide a default response if the input is not recognized
    return responses.get(user_input, "I'm sorry, I don't understand that question. Can you ask something else about AI?")

# Streamlit app layout
st.title("AI Chatbot - Learn about Artificial Intelligence")
st.write("Ask me anything about AI, and I'll do my best to help!")

# Input field for user message
user_input = st.text_input("You: ", "")

# Chat history to keep track of the conversation
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Generate a response when the user clicks the "Send" button
if st.button("Send"):
    if user_input:
        # Get chatbot response
        bot_response = chatbot_response(user_input)
        
        # Update chat history
        st.session_state.chat_history.append(f"You: {user_input}")
        st.session_state.chat_history.append(f"Chatbot: {bot_response}")

# Display the conversation history
if st.session_state.chat_history:
    st.write("### Conversation History")
    for message in st.session_state.chat_history:
        st.write(message)
