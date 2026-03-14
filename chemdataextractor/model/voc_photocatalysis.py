from .base import BaseModel, StringType
from ..parse.voc_parser import DegradationEfficiencyParser

class VOCPhotocatalysis(BaseModel):

    pollutant = StringType()

    catalyst = StringType()

    initial_concentration = StringType()

    wavelength = StringType()

    dosage = StringType()

    reactor_volume = StringType()

    light_intensity = StringType()

    reaction_time = StringType()

    degradation_efficiency = StringType()

    temperature = StringType()

    humidity = StringType()

    k_rate_constant = StringType()

    parsers = [DegradationEfficiencyParser()]
