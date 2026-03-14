from chemdataextractor.parse.elements import W, I, R
from chemdataextractor.parse.actions import merge
from chemdataextractor.parse.base import BaseParser
from chemdataextractor.model.voc_photocatalysis import VOCPhotocatalysis


class DegradationEfficiencyParser(BaseParser):

    # match numbers like 95%
    efficiency_value = R(r'^\d+(\.\d+)?$') + W('%')

    # keywords around degradation
    degradation_words = (
        I('degradation') |
        I('removal') |
        I('conversion')
    )

    root = efficiency_value('degradation_efficiency') + degradation_words

    def interpret(self, result, start, end):

        record = VOCPhotocatalysis()

        record.degradation_efficiency = " ".join(result.degradation_efficiency)

        yield record
