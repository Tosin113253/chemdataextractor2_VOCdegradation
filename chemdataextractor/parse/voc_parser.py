from chemdataextractor.parse.elements import W, I, R, Optional
from chemdataextractor.parse.base import BaseParser


class DegradationEfficiencyParser(BaseParser):

    number = R(r'^\d+(\.\d+)?$')
    percent = W('%')

    degradation_words = (
        I('degradation') |
        I('removal') |
        I('conversion')
    )

    efficiency_word = Optional(I('efficiency'))

    root = (
        number('value') + percent + degradation_words + efficiency_word
    ) | (
        degradation_words + efficiency_word + Optional(I('of')) + number('value') + percent
    )

    def interpret(self, result, start, end):
        from chemdataextractor.model.voc_photocatalysis import VOCPhotocatalysis

        record = VOCPhotocatalysis()
        record.degradation_efficiency = f"{result.value.text}%"
        yield record
