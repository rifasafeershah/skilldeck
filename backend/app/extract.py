import re

KEYWORDS = {
    "sql": "SQL",
    "machine learning": "Machine Learning",
    "data visualization": "Data Visualization",
    "ai ethics": "AI Ethics",
    "product launch": "Product Management",
    "agile": "Agile",
    "cryptography": "Cryptography",
    "patent": "IP Literacy",
    "artificial intelligence": "AI Fundamentals"
}

def extract_skills(text: str):
    text = text.lower()
    found = set()
    for k, v in KEYWORDS.items():
        if re.search(k, text):
            found.add(v)
    return list(found)
