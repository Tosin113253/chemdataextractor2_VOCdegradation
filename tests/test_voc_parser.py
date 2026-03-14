from chemdataextractor import Document
from chemdataextractor.model.voc_photocatalysis import VOCPhotocatalysis

text = "95 % degradation efficiency was achieved."

doc = Document(text)

records = doc.records.serialize()

print(records)
