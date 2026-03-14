print("START")

from chemdataextractor.doc.text import Sentence
from chemdataextractor.parse.voc_parser import DegradationEfficiencyParser

text = "95 % degradation efficiency was achieved."

sent = Sentence(text)
parser = DegradationEfficiencyParser()

# pass token sequence, not Sentence object
results = list(parser.parse(sent.tokens))

print("RESULTS:", results)

for r in results:
    try:
        print(r.serialize())
    except Exception:
        print(r)

print("END")
