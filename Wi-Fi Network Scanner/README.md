# 📡 Project 8: Wi-Fi Network Scanner

## 📌 Problem Statement
Choosing the right Wi-Fi network is essential for strong and reliable connectivity. Users often need to compare available networks based on factors like signal strength—but manual inspection can be frustrating and inefficient.

## 🎯 Objective
Create a Python-based tool that scans nearby Wi-Fi networks and displays useful details including:
- Network names (SSID)
- Signal strength (RSSI)
- Security status
This helps users make informed decisions about which network to join.

## 🛠️ Requirements

### 🧰 Libraries & Modules
- Python 3.x  
- `subprocess` or `os` for command execution  
- `wifi` or `pywifi` module (depends on operating system)  

### 💡 Platform-Specific Notes
- **Linux/macOS**: Can use `iwlist`, `nmcli`, or similar CLI tools  
- **Windows**: Prefer `pywifi` or PowerShell commands  

## ⚙️ Installation Steps

1. Make sure Python is installed on your system.
2. Install `pywifi` (for Windows or cross-platform support):

   ```bash
   pip install pywifi
3. (Optional) On Linux, ensure you have wireless-tools or similar packages installed.
## 🚀 How to Run
- Clone or download the project directory.
- Navigate to the folder in your terminal.
- Run the script:
python wifi_scanner.py
- - The tool will list available Wi-Fi networks with relevant data such as:
- SSID (network name)
- Signal strength (in dBm or percent)
- Security type (e.g., WPA2, Open)
## 📂 Features
- Scans available Wi-Fi networks in real-time
- Displays sorte- d results based on signal quality
- Works across Windows/Linux with modular backend
- Easily expandable with GUI (Tkinter or PyQt)
## ✅ Expected Outcome
By the end of this project, you'll be able to:
- Detect nearby Wi-Fi networks and evaluate their strength
- Understand how OS tools and Python interact for network tasks
- Build on this foundation to create monito- ring or optimization tools
## 📚 Further Learning
- Integrate with map visualization to show signal zones
- Add periodic scanning and signal tracking
- Combine with network performance tests (ping, bandwidth)
## ⚠️ Disclaimer
This tool is for educational and personal use only. Ensure that you have permission to scan and analyze any networks you don’t own.






