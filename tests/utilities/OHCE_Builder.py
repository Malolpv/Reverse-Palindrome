from src.messages import Francais
from src.models import OHCE


class OHCEBuilder:
    _lang = Francais
    _time: int

    def __init__(self):
        pass

    def build(self) -> OHCE.__class__:
        return OHCE(lang=self._lang, time=self._time)

    def set_langue(self, lang):
        """
        Assigner une langue pour bypass la langue système
        :param lang: la langue a assigner
        :return: self
        """
        self._lang = lang
        return self

    def set_time(self, time: int):
        """
        Assigner une heure pour bypass l'heure système
        :param time : Heure à assigner
        :return : self
        """
        self._time = time
        return self
