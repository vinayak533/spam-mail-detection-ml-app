```
spam-mail-detection-ml-app/
│── app.py                # Streamlit Web App
│── spam_model.pkl        # Trained Naive Bayes model
│── vectorizer.pkl        # TF-IDF Vectorizer
│── requirements.txt      # Package dependencies
│── README.md             # Documentation
│── notebook/ (optional)  # Jupyter notebook for training
    └── spam_mail_detection.ipynb
```

---

# 🧠 Machine Learning Pipeline

## 1️⃣ Data Preprocessing
- Lowercasing  
- Punctuation removal  
- Removing numbers  
- Removing stopwords  
- Tokenization  
- Lemmatization (optional)

## 2️⃣ Feature Extraction
- TF-IDF Vectorizer  
- Converts text to numerical representation  
- Controls frequent-word importance  

## 3️⃣ Model Used
- **Multinomial Naive Bayes**
- Works best for text classification  
- Fast, simple, and accurate  
- Great baseline for spam detection tasks  

## 4️⃣ Evaluation Metrics
- Accuracy  
- Precision  
- Recall  
- F1 Score  
- Confusion Matrix  

---
