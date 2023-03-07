from src.messages import LangSelector
from src.models.Clock import Clock


class OHCE:
    _lang: LangSelector
    _time: int

    def __init__(self, lang=None, time=None):
        self._lang = LangSelector(lang=lang)
        self._time = Clock.time if time is None else time

    @property
    def bonjour(self):
        """
            Renvoie le message de bienvenue adapté en fonction du moment de la journée
        """
        if self._time < 6:
            msg_bonjour = self._lang.late_nighter
        elif self._time < 12:
            msg_bonjour = self._lang.bonjour
        elif self._time < 16:
            msg_bonjour = self._lang.bonjour
        elif self._time < 20:
            msg_bonjour = self._lang.bon_apres_midi
        elif self._time < 24:
            msg_bonjour = self._lang.bonsoir
        else:
            # if self._time >= 24 or self._time < 0:
            raise ValueError("Invalid Time")
        return msg_bonjour

    @property
    def manage_au_revoir(self) -> str:
        """
            Renvoie le message d'au revoir adapté en fonction du moment de la journée
        """
        if self._time < 6:
            msg_au_revoir = self._lang.de_bon_matin
        elif self._time < 12:
            msg_au_revoir = self._lang.bonne_journee
        elif self._time < 16:
            msg_au_revoir = self._lang.bon_apres_midi
        elif self._time < 20:
            msg_au_revoir = self._lang.bonne_soiree
        elif self._time < 22:
            msg_au_revoir = self._lang.bonne_nuit
        elif self._time < 24:
            msg_au_revoir = self._lang.vas_te_coucher
        else:
            # if _time >= 24 or _time < 0:
            raise ValueError("Invalid Time")
        return msg_au_revoir

    @staticmethod
    def to_palindrome(param: str) -> str:
        """
        Renvoie l'inverse de la chaine donnée
        :param param: La chaine à inverser
        """
        return param[::-1]

    def is_palindrome(self, param: str):
        """
        Vérifie que la chaine donnée est un palindrome
        :param param: chaine à comparer
        :return: true si c'est un palindrome faux sinon
        """
        return param.lower() == self.to_palindrome(param).lower()

    def valid_param(self, given_param, expected_type: type):
        """
        Permet de vérifier que le paramètre passé correspond au type attendu
        :param given_param: parametre dont on est pas sur du type
        :param expected_type: type attendu
        """
        if not isinstance(given_param, expected_type):
            raise ValueError

    def execute(self, string: str):
        """
        Analyse la chaine donnée et et construit une réponse en fonction de l'heure et du language système
        :param string: Chaine/palindrome potentiel
        :return : renvoie la réponse construite en fonction de l'heure et du language système
        """
        self.valid_param(string, str)

        bien_dit = self._lang.bien_dit + '\n' if self.is_palindrome(string) else ''
        return f"{self.bonjour}\n{self.to_palindrome(string)}\n{bien_dit}{self.manage_au_revoir}"
