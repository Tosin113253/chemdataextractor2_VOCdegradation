from chemdataextractor import Document

print("START")

text = """
The photocatalytic degradation efficiency reached 95 % under visible light irradiation.
"""

doc = Document(text)

for record in doc.records:
    print(record.serialize())

print("END")
