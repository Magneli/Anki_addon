# Anki plugin using jisho.org

# Description

   * Plugin for anki that implements a dictionary lookup that can import results as cards into anki.
   * Primarily made for my own needs, no intentions to actively distribute.

# Status

   * UI pending rework, otherwise functional.
   * Comes with a default setting for deck and template.
   * UI might display incorrectly on unix systems.

# Todo

   * Add config parser
   * Rework the UI so that it displays properly on unix systems.
   * Better option to change deck and template, currently requires renaming in source code.

## Resources

   * [Anki](http://ankisrs.net/)
   * [Jisho](http://classic.jisho.org/)

## Extra requirements

   * bs4 (BeutifulSoup 4)


## Install instructions

### Debian

    $ apt-get install python-bs4
    $ git clone git@github.com:magneli/Anki_dictionary_plugin_WIP.git ~/Documents/Anki/addons

### Windows

    * Download all files and put them in the anki addon folder.
    * Download bs4 for python 2.7 and put the bs4 folder in the anki addon folder.
