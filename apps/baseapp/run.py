try:
    from app import Application as Appl
except ImportError:
    class Appl(): pass
import sys
sys.path.append('/apps/baseapp')
from application import BaseApplication
from browser import window
app = {}
class App(Appl, BaseApplication):
    pass
Application = App()