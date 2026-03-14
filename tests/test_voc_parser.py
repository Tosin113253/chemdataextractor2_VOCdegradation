from chemdataextractor import Document

text = "95 % degradation efficiency was achieved."

doc = Document(text)

for record in doc.records:
    print(record.serialize())
