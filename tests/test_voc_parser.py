from chemdataextractor import Document

text = """
95 % degradation efficiency was achieved under visible light.
"""

doc = Document(text)

for record in doc.records:
    print(record.serialize())
