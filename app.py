import streamlit as st
import pickle

# Load files
model = pickle.load(open("spam_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

st.title("📧 Spam Mail Detection App")
st.write("Enter an email message below:")

message = st.text_area("Email text", height=200)

if st.button("Predict"):
    if message.strip() == "":
        st.warning("Please type an email to check.")
    else:
        # Transform text
        data = vectorizer.transform([message])
        
        # Predict
        result = model.predict(data)[0]

        if result == 0:
            st.error("🚫 Spam")
        else:
            st.success("✔️ Not Spam")
