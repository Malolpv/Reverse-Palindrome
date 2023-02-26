from abc import ABC


class LangInterface(ABC):
    # BONJOUR
    bonjour: str
    bonsoir: str
    late_nighter: str

    # AU REVOIR
    de_bon_matin: str
    au_revoir: str
    bonne_journee: str
    bonne_soiree: str
    bonne_nuit: str
    vas_te_coucher: str
    bon_apres_midi: str

    # OHCE
    bien_dit: str
    OHCE_INPUT: str
    rien_fourni: str
    impossible_reverse: str
