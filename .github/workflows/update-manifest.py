import json
import sys
from datetime import datetime

json_file_path = sys.argv[1]
version = sys.argv[2]
url = sys.argv[3]

with open(json_file_path, 'r') as file:
    data = json.load(file)

new_entry = {
    "name": "hello-sh",
    "binaryName": "symctl-hello-sh",
    "version": version,
    "description": "Shell Hello World plugin.",
    "urls": [
        {
            "platform": "any",
            "os": "any",
            "url": url,
        }
    ],
    "created": datetime.utcnow().isoformat() + 'Z'
}

data.append(new_entry)

with open(json_file_path, 'w') as file:
    json.dump(data, file, indent=2)

print("New entry added successfully.")
