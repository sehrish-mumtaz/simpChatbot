import streamlit as st

# Predefined responses for questions about AI
responses = {
    "What is Artificial Intelligence?": "Artificial Intelligence (AI) is the simulation of human intelligence in machines designed to think and act like humans.",
    "What are the types of AI?": "The main types of AI are Narrow AI, General AI, and Superintelligent AI.",
    "What is Machine Learning?": "Machine Learning is a subset of AI that enables machines to learn from data and improve their performance over time.",
    "What is Deep Learning?": "Deep Learning is a subset of Machine Learning that uses neural networks with many layers.",
    "What are neural networks?": "Neural networks are computing systems inspired by the biological neural networks that constitute animal brains.",
    "What is Natural Language Processing?": "Natural Language Processing (NLP) is a field of AI that focuses on the interaction between computers and humans through natural language.",
    "What are the applications of AI?": "AI has applications in various fields, including healthcare, finance, education, transportation, and entertainment.",
    "What is supervised learning?": "Supervised learning is a type of machine learning where a model is trained on labeled data to make predictions.",
    "What is unsupervised learning?": "Unsupervised learning is a type of machine learning where a model is trained on unlabeled data to find patterns.",
    "What is reinforcement learning?": "Reinforcement learning is a type of machine learning where an agent learns to make decisions by receiving rewards or penalties.",
    "What is computer vision?": "Computer vision is a field of AI that enables machines to interpret and understand visual information from the world.",
    "What is the Turing Test?": "The Turing Test is a measure of a machine's ability to exhibit intelligent behavior equivalent to, or indistinguishable from, that of a human.",
    "What is bias in AI?": "Bias in AI refers to the presence of systematic errors in the algorithms that lead to unfair outcomes or reinforce stereotypes.",
    "What are chatbots?": "Chatbots are AI programs that simulate human conversation through voice or text interactions.",
    "What is the future of AI?": "The future of AI includes advancements in general intelligence, ethical considerations, and improved human-AI collaboration."
}

# Streamlit app layout
st.title("AI Chatbot")
st.write("Ask me anything about Artificial Intelligence!")

# Input field for user message
user_input = st.text_input("You: ")

# When the user clicks the "Send" button
if st.button("Send"):
    # Check if the user input matches any predefined questions
    response = responses.get(user_input, "Sorry, I don't have an answer for that.")
    
    # Display the chatbot response
    st.write(f"Chatbot: {response}")
