# 🚗 Car Price Prediction & 📰 Hamshahri Newspaper Analysis & 🧑‍💻 Face Recognition Projects

This repository contains a series of three machine learning and data science mini-projects designed to showcase practical applications in web scraping, NLP, and computer vision using traditional algorithms.

---

## 📁 Project 1: Car Price Prediction (Peugeot 206 Type 2)

### 🔧 Description
A complete pipeline to **scrape**, **preprocess**, and **train a machine learning model** to predict the price of used Peugeot 206 Type 2 cars from Divar.

### 🧪 Technologies
- `Selenium`, `requests`, `BeautifulSoup`
- `pandas`, `scikit-learn`, `joblib`
- `termcolor` for CLI output

### ⚙️ Features
- Extracts car data using Divar API and web scraping
- Handles 100k+ tokens and parses individual car details
- Trains a `LinearRegression` model with preprocessing
- Saves model and provides a CLI prediction interface

---

## 📁 Project 2: Hamshahri Newspaper

### 📄 Dataset
The [Hamshahri Corpus](https://dbrg.ut.ac.ir/hamshahri) — one of the largest Persian news datasets with over **160,000 articles** across 82 categories from 1996–2002.

### 🔍 Tasks
- Data cleaning using `hazm` (normalization, stemming, lemmatization)
- Visualization: Bar chart, Line plot, WordCloud
- TF-IDF vectorization
- Frequency analysis of the word "ناتو" over time
- Dimensionality reduction (2D and 5D)
- Clustering (Unsupervised Learning)
- Classification using:
  - KNN
  - Logistic Regression
  - Naive Bayes
  - Random Forest
  - Ensemble Voting Model

---

## 📁 Project 3: Face Recognition Without Deep Learning

### 🎯 Goal
Use traditional CV techniques to **detect and recognize a single user's face** through webcam using **SSIM (Structural Similarity Index)**.

### 🧠 Method
- Capture 60 grayscale images as reference dataset
- Compare incoming frames from webcam using SSIM
- Accept or reject based on a similarity threshold
- No deep learning allowed — uses only OpenCV and image similarity



