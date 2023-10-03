import streamlit as st
import pickle

# Load the saved model
with open('/content/drive/MyDrive/Colab Notebooks/model.pkl', 'rb') as f:
    best_model = pickle.load(f)

# Example new texts
new_texts = [
    "I love this product! It exceeded my expectations.",
    "The customer service was terrible. I would not recommend this company.",
    "This movie was just average. Nothing special.",
    "The quality of the product is really poor."
]

# Streamlit app
def main():
    st.title("Sentiment Analysis")
    st.write("Enter a text to predict its sentiment:")

    # User input text
    text = st.text_input("Text")

    # Make a prediction when the user submits the input
    if st.button("Predict"):
        if text:
            # Use the model to predict sentiment on the user input
            prediction = best_model.predict([text])[0]

            # Display the predicted sentiment
            if prediction == 1:
                st.write("Sentiment: Positive")
            else:
                st.write("Sentiment: Negative")
        else:
            st.write("Please enter a text.")

if __name__ == "__main__":
    main()
   


       
