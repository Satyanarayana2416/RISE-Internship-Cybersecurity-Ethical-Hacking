import subprocess
import re

def scan_networks():
    try:
        # Run the netsh command to get Wi-Fi networks
        output = subprocess.check_output(["netsh", "wlan", "show", "networks", "mode=bssid"], shell=True)
        output = output.decode("utf-8", errors="ignore")

        networks = re.findall(r"SSID \d+ : (.+)", output)
        signals = re.findall(r"Signal\s*:\s*(\d+)%", output)

        print("📶 Available Wi-Fi Networks:\n")
        for ssid, signal in zip(networks, signals):
            print(f"🔸 SSID: {ssid.strip():<30} Signal Strength: {signal}%")

    except Exception as e:
        print(f"⚠️ Error occurred: {e}")

if __name__ == "__main__":
    scan_networks()
