# 📧 Spam Mail Detection ML App

## 📌 Summary

This project is a machine learning-based web application that classifies emails or messages as **Spam** or **Not Spam** using Natural Language Processing (NLP) techniques and a Multinomial Naive Bayes model. The application is built with Streamlit and uses TF-IDF vectorization for text feature extraction.

---

## 🛠️ Technologies Used

* Python
* Scikit-learn
* Natural Language Processing (NLP)
* TF-IDF Vectorizer
* Multinomial Naive Bayes
* Streamlit
* Pandas & NumPy

---

## ✨ Features

* Classifies messages as Spam or Not Spam
* Text preprocessing pipeline (cleaning, tokenization)
* TF-IDF feature extraction
* Fast and accurate Naive Bayes model
* Interactive Streamlit web interface
* Real-time predictions from user input
* Lightweight and easy to deploy

---

## ⌨️ Keyboard Shortcuts

```
Ctrl + C   → Stop application
Enter      → Submit command
Up Arrow   → Reuse previous command
```

---

## ⚙️ Process

```
1. User enters email or message text
2. Text is preprocessed (cleaning and tokenization)
3. TF-IDF converts text into numerical features
4. Model predicts Spam or Not Spam
5. Result is displayed to the user
```

---

## 🏗️ How I Built It

```
- Collected and prepared spam dataset
- Performed text preprocessing and cleaning
- Extracted features using TF-IDF vectorizer
- Trained Multinomial Naive Bayes classifier
- Saved model and vectorizer using pickle
- Built Streamlit interface for predictions
```

---

## 📚 What I Learned

```
- Natural Language Processing fundamentals
- Text preprocessing techniques
- Feature extraction using TF-IDF
- Naive Bayes classification
- Model deployment using Streamlit
- End-to-end ML workflow
```

---

## 🚀 How It Could Be Improved

```
- Use deep learning models (LSTM / BERT)
- Add email dataset integration
- Deploy to cloud platforms
- Improve UI/UX design
- Add confidence score visualization
- Support multiple languages
```

---

## ▶️ How to Run the Project

### Clone Repository

```bash
git clone https://github.com/yourusername/spam-mail-detection-ml-app.git
cd spam-mail-detection-ml-app
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Streamlit Application

```bash
streamlit run streamlit_app.py
```

Open in browser:

```
http://localhost:8501
```

---

## 📂 Project Structure

```
spam-mail-detection-ml-app/
│
├── streamlit_app.py
├── spam_model.pkl
├── vectorizer.pkl
├── requirements.txt
└── README.md
```

---

## ⭐ About

A machine learning-based spam mail detection web application built using Python, Scikit-learn, and Streamlit that classifies messages as Spam or Not Spam using NLP techniques.
