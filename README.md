# Language Identification System (NLP Project)

## Overview

This project is a Natural Language Processing (NLP) application that automatically identifies the language of short text inputs.
It supports multiple languages commonly used in Kenya:

* English
* Swahili
* Sheng
* Kikuyu

The system was developed as part of an academic project to demonstrate text classification using machine learning techniques.

---

## Objectives

* Build a model that can classify short text into different languages
* Apply NLP preprocessing and feature extraction techniques
* Compare multiple machine learning models
* Deploy the model as an interactive application

---

## Technologies Used

* Python
* Scikit-learn
* Pandas / NumPy
* Streamlit

---

## Methodology

### 1. Data Collection

A balanced dataset was created with text samples from four languages:

* English
* Swahili
* Sheng
* Kikuyu

Each class contains an equal number of samples.

---

### 2. Data Preprocessing

Text data was cleaned using:

* Lowercasing
* Removal of extra whitespace
* Preservation of special characters (important for Kikuyu)

---

### 3. Feature Extraction

Text was converted into numerical features using:

* TF-IDF Vectorization
* Character n-grams (1–5 range)

This approach captures language-specific character patterns.

---

### 4. Model Training

Two models were trained and compared:

* Multinomial Naive Bayes
* Logistic Regression

---

### 5. Model Evaluation

Performance was evaluated using:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix

#### Results:

* Naive Bayes Accuracy: 100%
* Logistic Regression Accuracy: 97.92%

Naive Bayes was selected as the final model due to its superior performance.

---

### 6. Deployment

The model was deployed using Streamlit, allowing users to:

* Enter text
* Click a button
* Receive an instant language prediction

---

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/amandatheuri/language-identification-nlp.git
cd language-identification-nlp
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
streamlit run app.py
```

---

## Example Usage

| Input Text                 | Predicted Language |
| -------------------------- | ------------------ |
| I am going to school       | English            |
| Ninaenda soko leo          | Swahili            |
| Wacha tuende base          | Sheng              |
| Thimo cia Gîkûyû nî nyingî | Kikuyu             |

---

## Limitations

* The model is trained on a relatively small dataset
* It assumes one language per input
* Code-mixed text (e.g., Swahili + Kikuyu) may reduce accuracy

---

## Future Improvements

* Handle code-mixed text
* Expand dataset for better generalization
* Use deep learning models (e.g., LSTM, BERT)
* Deploy the app online

---

## Author

Developed by Amanda Theuri

---

## License

This project is for educational purposes.
