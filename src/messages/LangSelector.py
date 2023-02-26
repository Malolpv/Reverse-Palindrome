import locale

from src.messages import LangInterface
from src.messages.English import English
from src.messages.Francais import Francais


class LangSelector:
    __lang = None
    _msgs: LangInterface = None

    def __init__(self, lang=None):
        if lang:
            self._msgs = lang() or lang
        else:
            lang, formatting = locale.getlocale()
            try:
                self.__lang = lang.split('_')[0]
            except:
                self.__lang = None

            match self.__lang:
                case "English":
                    self._msgs = English()
                case _:  # Défaut
                    self._msgs = Francais()

    def __getattr__(self, item):
        if self._msgs:
            return self._msgs.__getattribute__(item)
        raise AttributeError
