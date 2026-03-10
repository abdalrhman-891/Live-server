import requests
import json
from datetime import datetime
import os

def update_github_link():
    url = "https://iptv-org.github.io/iptv/countries/eg.m3u"
    try:
        response = requests.get(url, timeout=10)
        lines = response.text.split('\n')
        new_link = ""
        
        for i, line in enumerate(lines):
            if "MBC" in line and "Masr" in line and "2" in line:
                if i + 1 < len(lines):
                    new_link = lines[i+1].strip()
                    break
        
        if new_link:
            data = {
                "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "mbc_masr_2": new_link
            }
            # حفظ الملف محلياً
            with open("link.json", "w") as f:
                json.dump(data, f, indent=4)
            print("Link updated in link.json")
            return True
    except Exception as e:
        print(f"Error: {e}")
    return False

update_github_link()