import streamlit as st
import joblib

# Load the trained model
model = joblib.load('/content/drive/MyDrive/Colab Notebooks/m
# Define the preprocess_text function
def preprocess_text(text):
    # Perform preprocessing steps on the text
    preprocessed_text = text.lower()  # Example preprocessing step: convert to lowercase

    # Return the preprocessed text
    return preprocessed_text
# Define the Streamlit app
def main():
    st.title("Sentiment Analysis")
    st.write("Enter a text to predict its sentiment:")

    # User input text
    text = st.text_input("Text")

    # Preprocess the text (similar to the preprocessing done during training)
    preprocessed_text = preprocess_text(text)

    # Make a prediction
    if st.button("Predict"):
        prediction = model.predict([preprocessed_text])[0]

        # Display the predicted sentiment
        if prediction == 1:
            st.write("Sentiment: Positive")
        else:
            st.write("Sentiment: Negative")

if __name__ == "__main__":
    main()

  
