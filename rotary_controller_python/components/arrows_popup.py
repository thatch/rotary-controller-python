import os

from kivy.app import App
from kivy.core.window import Window
from kivy.logger import Logger
from kivy.properties import NumericProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.modalview import ModalView
from kivy.uix.popup import Popup
from kivy.lang import Builder
from kivy.uix.relativelayout import RelativeLayout

log = Logger.getChild(__name__)

kv_file = os.path.join(os.path.dirname(__file__), __file__.replace(".py", ".kv"))
if os.path.exists(kv_file):
    log.info(f"Loading KV file: {kv_file}")
    Builder.load_file(kv_file)


class ArrowsPopup(RelativeLayout):
    pass
