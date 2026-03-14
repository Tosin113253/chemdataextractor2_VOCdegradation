from chemdataextractor.parse.elements import W, I, R, Optional
from chemdataextractor.parse.base import BaseParser


class DegradationEfficiencyParser(BaseParser):
    tag_type = "pos_tag"

    root = (
        R(r'^\d+(\.\d+)?$')('value')
        + W('%')
        + Optional(I('photocatalytic'))
        + (I('degradation') | I('removal') | I('conversion'))
        + Optional(I('efficiency'))
    )

    def interpret(self, result, start, end):
        from chemdataextractor.model.voc_photocatalysis import VOCPhotocatalysis

        record = VOCPhotocatalysis()
        record.degradation_efficiency = f"{result.value.text}%"
        yield record
