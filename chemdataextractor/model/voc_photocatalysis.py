from chemdataextractor.model.base import BaseModel
from chemdataextractor.model.base import StringType


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
