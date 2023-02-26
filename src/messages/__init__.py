import locale

from .English import English
from .Francais import Francais
from .LangInterface import LangInterface
from .LangSelector import LangSelector

langue, formatting = locale.getlocale()
