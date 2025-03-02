# A simple Python program to measure network download and upload speed in Mbps.

import speedtest

st = speedtest.Speedtest()

print("\n=== Network Speed Test Results ===\n")
print("Testing your connection...\n")
print("🌐 Analyzing download and upload speeds...\n")

st.get_best_server()

download_speed = st.download() / 1_000_000
upload_speed = st.upload() / 1_000_000

def get_speed_rating(speed):
    if speed > 100:
        return "🚀 Excellent"
    elif speed > 50:
        return "✨ Very Good" 
    elif speed > 25:
        return "👍 Good"
    elif speed > 10:
        return "🆗 Fair"
    else:
        return "⚠️ Poor"

download_rating = get_speed_rating(download_speed)
upload_rating = get_speed_rating(upload_speed)

print(f"Download Speed: {download_speed:.2f} Mbps ({download_rating})\n")
print(f"Upload Speed: {upload_speed:.2f} Mbps ({upload_rating})\n")
