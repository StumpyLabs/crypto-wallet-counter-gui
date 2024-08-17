from tkinter import *

import history
import tkinterApp as ta
import newEntry as ne


def main():
    # root = Tk()
    # ta.startApp(root)
    # ne.newEntry()
    history.nameListBuilder()
    history.searchDB()


if __name__ == '__main__':
    main()
