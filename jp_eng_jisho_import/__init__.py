from aqt import mw
from aqt.qt import QAction, SIGNAL
from user_interface import testFunction

action = QAction("JP-ENG Dictionary", mw)
mw.connect(action, SIGNAL("triggered()"), testFunction)
mw.form.menuTools.addAction(action)
