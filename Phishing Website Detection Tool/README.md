# 🛡️ Project 1: Phishing Website Detection Tool

## 📌 Problem Statement
Phishing websites are malicious sites that trick users into entering sensitive information such as usernames, passwords, or banking details. These attacks result in identity theft, financial loss, and compromised accounts.

## 🎯 Objective
Develop a Python-based tool that detects potentially harmful URLs using either:
- Rule-based filtering techniques  
- Machine learning models

This project aims to improve digital security awareness and help users avoid falling victim to phishing attacks.

## 🛠️ Requirements

### 🧰 For Rule-Based Detection
- Python 3.x  
- `pandas` – for data manipulation  
- `re` (Regex) – for URL pattern analysis

### 🧠 For Machine Learning Detection
- Python 3.x  
- `scikit-learn` – for training and evaluating ML models  
- `pandas` – for handling datasets  
- A labeled dataset of legitimate and phishing URLs

### 🖼️ (Optional) GUI
- `tkinter` – for building a simple graphical interface

## ⚙️ Installation Steps

1. Clone or download the project repository.
2. Make sure Python is installed on your system.
3. Install necessary libraries using pip:

   ```bash
   pip install pandas scikit-learn
## 🚀 How to Run
Rule-Based Version
Bash :- python rule_based_detector.py

## Machine Learning Version
bash :- python ml_detector.py

- Provide a URL input via command line or GUI.
- The tool returns whether the URL is potentially safe or a phishing attempt.
## 📂 Features
- Lightweight and easy to deploy
- Two detection options (rule-based or ML)
- Provides actionable feedback to users
- Simple codebase for learning and customization
## ✅ Expected Outcome
Users should be able to input a URL and receive a warning if the website is likely to be malicious. You'll also gain insight into URL characteristics commonly used in phishing attacks and how to identify them programmatically.
