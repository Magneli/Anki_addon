from aqt.qt import *


def makeAreas(widget):
    make_upper_area(widget)
    make_html_area(widget)

    layout = QVBoxLayout(widget)
    layout.addWidget(widget.textboxarea)
    layout.addWidget(widget.htmlarea)


def make_html_area(widget):
    widget.htmlarea = QWebView(widget)
    widget.htmlarea.move(0, 40)


def make_upper_area(widget):
    widget.textboxarea = QWidget(widget)
    widget.textboxarea.setMinimumSize(QSize(100, 35))
    widget.textboxarea.setMaximumSize(QSize(400, 35))

    widget.textbox = QLineEdit(widget.textboxarea)
    widget.textbox.setMinimumHeight(25)

    widget.setDeck = QLineEdit(widget.textboxarea)
    widget.setDeck.setMinimumHeight(25)
    widget.setDeck.setMinimumWidth(80)
    widget.setDeck.setMaximumWidth(80)

    textboxareaLayout = QHBoxLayout(widget.textboxarea)
    textboxareaLayout.addSpacing(20)
    textboxareaLayout.addWidget(widget.textbox)
    textboxareaLayout.addSpacing(70)
    textboxareaLayout.addWidget(widget.setDeck)
