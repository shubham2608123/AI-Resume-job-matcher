# AI Resume Job Matching System

## 📌 Overview

The **AI Resume Job Matching System** is an intelligent application that analyzes resumes and predicts the most suitable job category using Machine Learning.

The system allows users to **upload a resume image**, extracts text using OCR, and predicts the **job role/category** using a trained machine learning model.

This project demonstrates the integration of **Machine Learning, OCR, API development, and frontend UI** in a complete end-to-end AI application.

---

## 🚀 Features

* Upload resume images
* OCR-based text extraction
* Machine learning job category prediction
* Interactive web interface
* REST API backend
* End-to-end AI pipeline

---

## 🧠 System Architecture

User Upload Resume
↓
OCR Text Extraction
↓
Text Preprocessing
↓
TF-IDF Vectorization
↓
Machine Learning Model
↓
Predicted Job Category

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### Backend

* FastAPI
* Uvicorn

### Machine Learning

* Scikit-learn
* Logistic Regression
* TF-IDF Vectorizer

### OCR

* Tesseract OCR
* pytesseract

### Other Libraries

* pandas
* joblib
* Pillow
* requests

---

## 📂 Project Structure

```
Resume-job-matching-system
│
├── backend
│   ├── main.py
│   ├── ocr_utils.py
│
├── frontend
│   ├── app.py
│
├── model
│   ├── model.pkl
│   ├── vectorizer.pkl
│
├── dataset
│
├── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```
git clone https://github.com/yourusername/resume-job-matching-system.git
cd resume-job-matching-system
```

---

### 2️⃣ Create Virtual Environment

```
python -m venv venv
```

Activate environment

Windows:

```
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```
pip install fastapi uvicorn streamlit scikit-learn pandas pytesseract pillow joblib requests
```

---

### 4️⃣ Install Tesseract OCR

Download and install:

https://github.com/UB-Mannheim/tesseract/wiki

After installing, set path in Python:

```
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

---

## ▶️ Running the Application

### Start Backend Server

```
cd backend
python -m uvicorn main:app --reload
```

Backend runs on:

```
http://127.0.0.1:8000
```

API Documentation:

```
http://127.0.0.1:8000/docs
```

---

### Start Frontend

Open another terminal:

```
cd frontend
streamlit run app.py
```

Frontend runs on:

```
http://localhost:8501
```

---

## 📊 Machine Learning Model

The model is trained using:

* TF-IDF Vectorization
* Logistic Regression Classifier

Dataset used:

* Resume Dataset (Kaggle)

The model predicts job categories such as:

* Data Scientist
* Web Developer
* Python Developer
* Java Developer
* DevOps Engineer
* Data Analyst

---

## 🔄 Application Workflow

1. User uploads resume image
2. OCR extracts text from resume
3. Text is cleaned and processed
4. TF-IDF vectorizer converts text to numerical features
5. Machine learning model predicts job category
6. Result is displayed in the Streamlit interface

---

## 🧪 Future Improvements

* Resume skill extraction using NLP
* Job description matching
* Resume ATS scoring
* Top job recommendations
* Support for PDF resumes
* Deep learning models (BERT)

---

## 👨‍💻 Author

Developed by **Shubham Dalvi**

---

## 📜 License

This project is open-source and available under the MIT License.
