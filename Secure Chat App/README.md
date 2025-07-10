# 🔐 Project 6: Secure Chat App

## 📌 Problem Statement
Most chat applications lack robust default security, leaving messages vulnerable to interception. This project focuses on solving this problem by enabling secure, encrypted communication between users.

## 🎯 Objective
Develop a secure messaging application with real-time, encrypted text exchange between two users using Python. The app ensures **end-to-end encryption**, so that only the sender and receiver can read the messages.

## 🛠️ Requirements

### ⚙️ Programming & Security
- Python 3.x  
- Socket programming (for real-time connection)  
- `PyCryptodome` or built-in `RSA` module (for message encryption and decryption)

### 🖥️ Optional UI
- `Tkinter` or `PyQt5` (for graphical interface)

## 📂 Installation Steps

1. Clone or download the project repository.
2. Install required libraries:

   ```bash
   pip install pycryptodome
3. (Optional) Install PyQt5 or use Tkinter for GUI:
   bash:- pip install pyqt5
## 🚀 How to Run
- Start the server script:
bash:- python server.py
- Launch the client script (on same or different machine):
python client.py
- Begin secure messaging! All messages are encrypted before sending and decrypted upon receipt.
## 🔐 Encryption Features
- Generates asymmetric key pairs (RSA) for each session
- Encrypts messages using public key, decrypts with private key
- Prevents man-in-the-middle attacks via secure message passing
## ✅ Expected Outcome
You’ll end up with a secure chat tool that:
- Sends and receives encrypted messages over sockets
- Demonstrates key encryption techniques
- Can be used for learning, internal communication, or showcasing cybersecurity principles
## 📚 Further Learning
- Implement key exchange protocols like Diffie-Hellman
- Upgrade to AES encryption with symmetric keys
- Add user authentication and message integrity checks
## ⚠️ Disclaimer
This project is for educational use only. Avoid deploying it in production environments without additional security measures like SSL/TLS and secure key storage.


Talk securely. Learn deeply. Code ethically. 🔐


