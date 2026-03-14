print("START TEST")

from chemdataextractor.doc import Paragraph
from chemdataextractor.model.voc_photocatalysis import VOCPhotocatalysis
from chemdataextractor.parse.voc_parser import DegradationEfficiencyParser

text = "95 % degradation efficiency was achieved."
print("TEXT:", text)

p = Paragraph(text)
print("PARAGRAPH CREATED")

print("Number of sentences:", len(p.sentences))
print("Sentence text:", p.sentences[0].text)

parser = DegradationEfficiencyParser()
print("PARSER:", parser)

try:
    results = list(parser.parse(p.sentences[0]))
    print("RAW PARSE RESULTS:", results)
except Exception as e:
    print("PARSER ERROR:", repr(e))

print("MODEL PARSERS:", VOCPhotocatalysis.parsers)

try:
    for parser in VOCPhotocatalysis.parsers:
        results = list(parser.parse(p.sentences[0]))
        print("MODEL PARSER RESULTS:", results)
except Exception as e:
    print("MODEL PARSER ERROR:", repr(e))

print("END TEST")
