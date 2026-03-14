from chemdataextractor import Document

def test_voc_efficiency():
    text = """
    The photocatalytic degradation efficiency reached 95 % under visible light irradiation.
    """
    doc = Document(text)

    for record in doc.records:
        print(record.serialize())

test_voc_efficiency()
