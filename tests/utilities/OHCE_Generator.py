from src.messages import LangSelector
from tests.utilities.OHCE_Builder import OHCEBuilder


class OHCEGenerator:
    def __init__(self):
        pass

    def generate(self, nb_wanted: int):
        """
        Generate nb_wanted OHCEBuilders
        :param nb_wanted: Number of OHCEBuilders to generate
        """
        for i in range(nb_wanted):
            yield OHCEBuilder
