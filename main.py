from tkinter import *

import history
import tkWelcome as ta
import newEntry as ne
from history import walletCoinListBuilder, runWallets


def main():
    root = Tk()
    ta.startApp(root)


if __name__ == '__main__':
    main()
