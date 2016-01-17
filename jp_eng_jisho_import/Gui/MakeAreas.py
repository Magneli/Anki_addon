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
    widget.textboxarea.setMaximumHeight(35)

    widget.search_box = QLineEdit(widget.textboxarea)
    widget.search_box.setMinimumHeight(23)

    widget.setDeck = QLineEdit(widget.textboxarea)
    widget.setDeck.setMinimumHeight(23)
    widget.setDeck.setMinimumWidth(80)
    widget.setDeck.setMaximumWidth(80)

    font = QFont()
    font.setPixelSize(14)

    widget.current_deck_label = QLabel(widget.textboxarea)
    widget.current_deck_label.setText("Current: yay")
    widget.current_deck_label.setFont(font)

    widget.search_label = QLabel(widget.textboxarea)
    widget.search_label.setText("Search:")
    widget.search_label.setFont(font)

    widget.set_deck_label = QLabel(widget.textboxarea)
    widget.set_deck_label.setText("Set Deck:")
    widget.set_deck_label.setFont(font)

    textboxareaLayout = QHBoxLayout(widget.textboxarea)
    textboxareaLayout.addWidget(widget.search_label)
    textboxareaLayout.addWidget(widget.search_box)
    textboxareaLayout.addSpacing(40)

    textboxareaLayout.addWidget(widget.set_deck_label)
    textboxareaLayout.addWidget(widget.setDeck)
    textboxareaLayout.addWidget(widget.current_deck_label)
    textboxareaLayout.setAlignment(widget.current_deck_label, Qt.AlignRight)
    textboxareaLayout.setAlignment(widget.setDeck, Qt.AlignRight)
    textboxareaLayout.setAlignment(widget.set_deck_label, Qt.AlignRight)
    textboxareaLayout.addSpacing(20)
