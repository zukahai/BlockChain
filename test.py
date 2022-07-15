import json

data = {"Eleven": "Millie","Mike": "Finn", "Will": "Noah"}

print(data)

with open('blocks.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)