import pandas as pd
import re
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import tkinter as tk
from tkinter import messagebox
import os

# === 1. Feature Extraction ===
def extract_features(url):
    return {
        'url_length': len(url),
        'has_ip': 1 if re.search(r'\d{1,3}(\.\d{1,3}){3}', url) else 0,
        'count_dots': url.count('.'),
        'has_at': 1 if '@' in url else 0,
        'has_hyphen': 1 if '-' in url else 0,
        'has_https': 1 if url.lower().startswith("https") else 0,
        'has_login': 1 if 'login' in url.lower() else 0,
        'has_verify': 1 if 'verify' in url.lower() else 0,
        'has_update': 1 if 'update' in url.lower() else 0,
        'digit_count': sum(char.isdigit() for char in url)
    }

# === 2. Load Dataset and Train Model ===
def train_model():
    if not os.path.exists("phishing_dataset.csv"):
        raise FileNotFoundError("⚠️ Missing 'phishing_dataset.csv'. Make sure your dataset is in the same folder.")

    df = pd.read_csv("phishing_dataset.csv")
    df.dropna(inplace=True)

    features = df["URL"].apply(lambda url: pd.Series(extract_features(url)))
    X = features
    y = df["Label"]  # Ensure Label is 0 (legit) or 1 (phishing)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Optional evaluation
    print("\n📊 Model Evaluation:\n")
    print(classification_report(y_test, model.predict(X_test)))

    return model

# === 3. GUI ===
class DetectorGUI:
    def __init__(self, model):
        self.model = model
        self.root = tk.Tk()
        self.root.title("🔍 Phishing URL Detector")

        tk.Label(self.root, text="Enter a URL:").pack(pady=5)

        self.entry = tk.Entry(self.root, width=60)
        self.entry.pack(pady=5)

        tk.Button(self.root, text="Check URL", command=self.check_url).pack(pady=10)

        self.root.mainloop()

    def check_url(self):
        url = self.entry.get().strip()

        if not url:
            messagebox.showwarning("Input Error", "Please enter a URL.")
            return

        features = pd.DataFrame([extract_features(url)])
        prediction = self.model.predict(features)[0]

        if prediction == 1:
            messagebox.showerror("⚠️ Phishing Detected", "🚨 This URL appears to be a PHISHING site!")
        else:
            messagebox.showinfo("✅ Legitimate", "This URL appears safe.")

# === 4. Entry Point ===
if __name__ == "__main__":
    try:
        clf = train_model()
        DetectorGUI(clf)
    except Exception as e:
        print(f"❌ Error: {e}")
