import os
import unittest

from parameterized import parameterized

from src.messages import Francais, LangSelector, English
from utilities.OHCE_Builder import OHCEBuilder


class TestOHCE(unittest.TestCase):

    def test_01_bonjour(self):
        """ Par défaut, la langue francaise est selectionnee """
        ohce = OHCEBuilder().set_langue(Francais).set_time(8).build()
        lang = LangSelector(Francais)
        self.assertEqual(lang.bonjour, ohce.bonjour)
        lang = LangSelector(English)
        self.assertNotEqual(lang.bonjour, ohce.bonjour)

    def test_02_au_revoir(self):
        """ Par défaut, la langue anglaise est sélectionné """
        ohce = OHCEBuilder().set_langue(Francais).set_time(8).build()
        lang = LangSelector(Francais)
        self.assertEqual(ohce.manage_au_revoir, lang.bonne_journee)
        lang = LangSelector(English)
        self.assertNotEqual(ohce.manage_au_revoir, lang.bonne_journee)

    def test_02_palindrome(self):
        """ Quand on saisit un palindrome, alors, on renvoie le palindrome, ET "Bien dit!"  """
        # Etant donné l'OHCE
        ohce = OHCEBuilder().set_langue(Francais).set_time(8).build()
        lang = ohce._lang

        # quand on saisit une chaine,
        _in = "toot"
        val = ohce.execute(_in)

        # Alors celle-ci est renvoyée en miroir
        self.assertEqual(lang.bonjour + "\n" + "toot" + "\n" + lang.bien_dit +
                         "\n" + lang.bonne_journee, val)

    def test_03_radar(self):
        # THEORY
        """ Test que OHCE renvoi radar """
        ohce = OHCEBuilder().set_langue(Francais).set_time(8).build()
        lang = ohce._lang

        _in = "radar"
        self.assertEqual(lang.bonjour + "\n" + "radar" + "\n" + lang.bien_dit
                         + "\n" + lang.bonne_journee, ohce.execute(_in))
        _in = "Radar"
        self.assertEqual(lang.bonjour + "\n" + "radaR" + "\n" + lang.bien_dit
                         + "\n" + lang.bonne_journee, ohce.execute(_in))

    def test_04_chaine_complete(self):  # T.A.F
        """ renvoie au revoir """
        ohce = OHCEBuilder().set_langue(Francais).set_time(8).build()
        lang = ohce._lang
        _in = "tEstS"
        self.assertEqual(lang.bonjour + "\n" + "StsEt" + "\n" + lang.bonne_journee, ohce.execute(_in))

    def test_05_invalid_in(self):
        """ Test des entrés invalide """
        ohce = OHCEBuilder().set_langue(Francais).set_time(8).build()

        self.assertRaises(ValueError, ohce.execute, 42)
        self.assertRaises(ValueError, ohce.execute, self)
        self.assertRaises(ValueError, ohce.execute, 1.42)
        self.assertRaises(ValueError, ohce.execute, os)

    def test_06_multilingual_english(self, lang=English):
        """ Test que le paramètre English est bien appliqué"""
        ohce = OHCEBuilder().set_langue(lang).set_time(8).build()
        self.assertEqual(lang.bonjour + "\n" + "YEH!" + "\n" + lang.bonne_journee, ohce.execute("!HEY"))
        self.assertEqual(lang.bonjour + "\n" + "YEY" + "\n" + lang.bien_dit + "\n" + lang.bonne_journee,
                         ohce.execute("YEY"))

    def test_07_multilingual_french(self, lang=Francais):
        """ Test que le paramètre français est bien appliqué"""
        ohce = OHCEBuilder().set_langue(lang).set_time(8).build()

        self.assertEqual(lang.bonjour + "\n" + "YEH!" + "\n" + lang.bonne_journee, ohce.execute("!HEY"))
        self.assertEqual(lang.bonjour + "\n" + "YEY" + "\n" + lang.bien_dit + "\n" + lang.bonne_journee,
                         ohce.execute("YEY"))

    @parameterized.expand([
        [0, Francais.late_nighter],
        [1, Francais.late_nighter],
        [6, Francais.bonjour],
        [8, Francais.bonjour],
        [12, Francais.bonjour],
        [16, Francais.bon_apres_midi],
        [20, Francais.bonsoir],
        [23, Francais.bonsoir],
    ])
    def test_08_bonjour_multiple_times_fr(self, _time, _expected):
        ohce = OHCEBuilder().set_langue(Francais).set_time(_time).build()
        self.assertEqual(_expected, ohce.bonjour)

    @parameterized.expand([
        [0, English.late_nighter],
        [1, English.late_nighter],
        [6, English.bonjour],
        [8, English.bonjour],
        [12, English.bonjour],
        [16, English.bon_apres_midi],
        [20, English.bonsoir],
        [23, English.bonsoir],
    ])
    def test_09_bonjour_multiple_times_en(self, _time, _expected):
        ohce = OHCEBuilder().set_langue(English).set_time(_time).build()
        self.assertEqual(_expected, ohce.bonjour)
