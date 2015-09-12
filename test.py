# import the main window object (mw) from ankiqt
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import showInfo
# import all of the Qt GUI library
from aqt.qt import *
from anki import Collection
import Searchthing





def testFunction():
    card = mw.col.sched.getCard()
    cardCount = mw.col.cardCount()
    # show a message box


    search_term = "かも".decode(encoding='UTF-8',errors='strict')

    ids = mw.col.findCards(search_term)
    #showInfo(search_term)
    card = mw.col.getCard(ids[0])


    note = card.note()
    taberu = Searchthing.Ducks("taberu")
    showInfo(taberu.get_kanji(0))
    for id in ids:
        result =""
        card = mw.col.getCard(id)
        note = card.note()

        for (name, value) in note.items():
            result+=value

        showInfo(result)





action = QAction("test", mw)
mw.connect(action, SIGNAL("triggered()"), testFunction)
mw.form.menuTools.addAction(action)