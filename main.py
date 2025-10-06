import json
import os
from datetime import datetime, timezone
import curl_cffi

r = curl_cffi.get("https://truthsocial.com/api/v1/accounts/107780257626128497/statuses", impersonate="chrome_android")
print(r.text)
data = r.json()

os.makedirs("./statuses", exist_ok=True)
timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
file_path = f"./statuses/{timestamp}.json"
with open(file_path, "w", encoding="utf-8") as f:
  json.dump(data, f, ensure_ascii=False, indent=4)