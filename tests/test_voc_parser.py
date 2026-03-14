print("START")

from chemdataextractor import Document

text = "95 % degradation efficiency was achieved."
print("TEXT LOADED")

doc = Document(text)
print("DOC CREATED")

for record in doc.records:
    print(record.serialize())

print("END")
