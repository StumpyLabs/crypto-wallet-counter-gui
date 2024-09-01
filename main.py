from tkinter import *

import history
import tkWelcome as ta
import newEntry as ne
from history import walletCoinListBuilder, runWallets


def main():
    root = Tk()
    ta.startApp(root)
    # ne.newEntry()
    # history.nameListBuilder()
    #history.runNames()
    #history.searchDB()
    #history.nameListApp()
    #print(type("QWERTY", "Dvorak", "Colemak", "Workman"))
    # runWallets("Casey Stumpf", "Big Money")


if __name__ == '__main__':
    main()
