# 💣 Project 5: Simple Ransomware Simulator (Educational Use Only)

## 📌 Problem Statement
Ransomware attacks are increasingly disrupting individuals and organizations by encrypting valuable data and demanding ransom for recovery. Understanding how such attacks work is essential to defend against them.

## 🎯 Objective
Create a simulation that mimics basic ransomware behavior by encrypting files in a folder and decrypting them using a key—purely for **educational and awareness** purposes. This tool should highlight risks and teach mitigation strategies.

## 🛠️ Requirements

- Python 3.x  
- `cryptography` library (specifically `Fernet`)  
- A folder with sample files  
- Awareness of safe coding and ethical guidelines

## ⚙️ Installation Steps

1. Clone or download the repository.
2. Install the required library:

   ```bash
   pip install cryptography
3. - Place sample text/image/doc files into a folder named (e.g., target_folder).
## 🚀 How to Run
# 🔐 Encryption Phase
python encryptor.py
- Encrypts all files inside target_folder
- Saves the encryption key in a secure location (or displays it to the user)
# 🔓 Decryption Phase
python decryptor.py
- Prompts for the encryption key
- Decrypts all previously encrypted files if the correct key is provided
## 📂 Features
- Recursively encrypts all files within a directory
- Simple symmetric encryption using Fernet
- Clear separation of encryption and decryption logic
- Ideal for demonstrating security risks and defenses
## ✅ Expected Outcome
- Understand how ransomware encrypts user data
- Learn the importance of securing file systems and preventing unauthorized access
- Gain hands-on experience with cryptography modules
## 📚 Further Learning
- Implement GUI interface for user-friendly simulation
- Use logging to record encrypted files and events
- Explore real ransomware mitigation strategies (backups, antivirus, monitoring)
⚠️ Ethical Disclaimer
This project is intended exclusively for educational purposes. Do not deploy it on real systems or use it against personal devices. Always seek permission before testing any security-related tool, and never exploit vulnerabilities unethically.
Encrypt to educate, not exploit. 🔐

