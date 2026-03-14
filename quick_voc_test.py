import re

text = "The photocatalytic degradation efficiency reached 95 % under visible light irradiation."

patterns = [
    r'(\d+(?:\.\d+)?)\s*%\s*(?:photocatalytic\s+)?(?:degradation|removal|conversion)(?:\s+efficiency)?',
    r'(?:degradation|removal|conversion)(?:\s+efficiency)?(?:\s+of)?\s*(\d+(?:\.\d+)?)\s*%'
]

match_value = None
for pattern in patterns:
    m = re.search(pattern, text, flags=re.IGNORECASE)
    if m:
        match_value = m.group(1) + "%"
        break

print("TEXT:", text)
print("DEGRADATION_EFFICIENCY:", match_value)
