from aqt import mw
from aqt.qt import QAction, SIGNAL

from old_user_interface import runOldUi
import Gui.NewUi


newgui = QAction("JP-ENG dictionary new interface", mw)
mw.connect(newgui, SIGNAL("triggered()"), Gui.NewUi.runInterface)
mw.form.menuTools.addAction(newgui)

action = QAction("JP-ENG Dictionary", mw)
mw.connect(action, SIGNAL("triggered()"), runOldUi)
mw.form.menuTools.addAction(action)
