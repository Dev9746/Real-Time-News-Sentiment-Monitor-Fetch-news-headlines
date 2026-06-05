# 🛒 Amazon Review Sentiment Analysis using NLP

## 📌 Project Overview

This project performs **Sentiment Analysis** on Amazon product reviews using **Natural Language Processing (NLP)** and **Machine Learning**.

The system classifies customer reviews into:

* 😊 Positive Review
* 😞 Negative Review

A Streamlit web application is included for real-time sentiment prediction.

---

## 🚀 Features

* Text Preprocessing
* TF-IDF Vectorization
* Linear Support Vector Machine (LinearSVC)
* Positive & Negative Sentiment Classification
* Confidence Score
* Happy & Unhappy Feedback Messages
* Confusion Matrix Visualization
* Model Saving using Pickle
* Streamlit Web Application

---

## 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Streamlit
* Matplotlib
* Seaborn
* NLP

---

## 📂 Dataset

Dataset Used:

Amazon Polarity Dataset

Labels:

| Label | Meaning         |
| ----- | --------------- |
| 0     | Negative Review |
| 1     | Positive Review |

The dataset contains millions of Amazon product reviews for sentiment classification.

---

## 🧠 Machine Learning Pipeline

1. Load Dataset
2. Text Cleaning
3. TF-IDF Feature Extraction
4. Train LinearSVC Model
5. Evaluate Performance
6. Save Model
7. Deploy with Streamlit

---

## 📊 Model Evaluation

Metrics Used:

* Accuracy Score
* Precision
* Recall
* F1 Score
* Confusion Matrix

Target Accuracy:

90%+ (depending on dataset size and training configuration)

---

## 📁 Project Structure

amazon-review-sentiment-analysis/

├── app.py

├── requirements.txt

├── README.md

├── sentiment_model.pkl

├── vectorizer.pkl

├── notebook.ipynb

└── sample_output.png

---

## ▶️ Installation

Clone the repository:

git clone https://github.com/your-username/amazon-review-sentiment-analysis.git

Move into the project directory:

cd amazon-review-sentiment-analysis

Install dependencies:

pip install -r requirements.txt

---

## ▶️ Run the Application

Start the Streamlit application:

streamlit run app.py

The application will open automatically in your browser.

---

## 💡 Sample Positive Reviews

This product is amazing and works perfectly.

Excellent quality and worth every penny.

Fantastic purchase. Highly recommended.

The battery life is excellent and performance is great.

I am very satisfied with this product.

---

## 💡 Sample Negative Reviews

Worst product ever. Waste of money.

Very disappointed with the quality.

The item stopped working after one day.

Poor performance and bad customer support.

I would not recommend this product.

---

## 🎯 Output

The system displays:

* Positive Review or Negative Review
* Confidence Score
* Customer Feedback Message

Example:

Positive Review 😊

Confidence Score: 95%

Great choice! Customers seem very happy with this product.

---

## 💾 Saved Files

The project saves:

* sentiment_model.pkl
* vectorizer.pkl

These files are used for prediction without retraining the model.

---

## 📈 Future Improvements

* BERT-based Sentiment Analysis
* Aspect-Based Sentiment Analysis
* Review Summarization
* Word Cloud Visualization
* Cloud Deployment
* Multi-Language Support

---

## 👨‍💻 Author

Amazon Review Sentiment Analysis Project

Built using Python, NLP, TF-IDF, Linear SVM, and Streamlit.
