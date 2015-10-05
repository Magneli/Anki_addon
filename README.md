# Anki plugin using jisho.org

# Description

   * Plugin for anki that implements a dictionary lookup that can import results as cards into anki.
   * Primarily made for my own needs, no intentions to actively distribute.

# Status

   * UI pending rework, otherwise functional.
   * Comes with a default setting for deck and template.
   * UI might display incorrectly on unix systems.

# Todo

   * Rework the UI so that it displays properly on unix systems.


## Resources

   * [Anki](http://ankisrs.net/)
   * [Jisho](http://classic.jisho.org/)

## Extra requirements

   * [bs4 (BeutifulSoup 4)](https://pypi.python.org/pypi/beautifulsoup4/)


## Install instructions

### Debian

    $ apt-get install python-bs4
    $ git clone https://github.com/Magneli/Anki-japanese-dictionary-plugin---WIP.git ~/Documents/Anki/addons

### Ubuntu

    $ apt-get install python-bs4
    $ git clone https://github.com/Magneli/Anki-japanese-dictionary-plugin---WIP.git ~/Anki/addons

### Windows

    * Download all files and put the contents in the anki addon folder.
    * Download bs4 for python 2.7, unzip it and put the bs4 folder in the anki addon folder.
