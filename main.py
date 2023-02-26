import datetime
import locale

lng_fra = {
    "Welcome": "Bienvenue",
    "Good morning": "Bonjour",
    "Good evening": "Bonsoir",
    "Good Night": "Bonne soirée",
    "Goodbye": "Au revoir",
    "Input something": "Entrez quelque chose",
    "Well said!": "Bien dit!",
    "Nothing was provided": "Rien n'a été fourni.",
}

lang, formatting = locale.getlocale()


def lng_(sentence):
    """ returns the actual lang value of the given text """
    return sentence if lang == "English_United States" or lang == "English_Great Britain" else lng_fra[sentence]


def current_time():
    time = datetime.time().hour
    val = None
    if 8 > time >= 0:
        val = lng_("All Nighter")
    if 12 > time >= 8:
        val = lng_("Good morning")
    if 16 > time >= 12:
        val = lng_("Good evening")
    if 24 > time >= 16:
        val = lng_("Goodbye")
    return val


if __name__ == '__main__':
    print(lng_("Welcome"))
    user_input = input(lng_("Input something"))
    if not user_input:
        raise IOError(lng_("Nothing was provided"))
    reversed_input = user_input[::-1]
    if user_input == reversed_input:
        print(lng_("Well said!"))
    else:
        print(reversed_input)
    print(lng_("Goodbye"))
