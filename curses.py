import curses


window = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)


def init_panes():
    height, width = window.getmaxyx()
    half_width = width // 2
    left_pane = curses.newwin(height, half_width)
    right_pane = curses.newwin(height, half_width, half_width, 0)
    curses.raw()

    def set_options(left, right):
        def set_text(pane, text):
            pane.clear()
            pane.box()
            pane.addstr(height // 2, (half_width - len(text)) // 2, text)
            pane.refresh()
        # window.clear()
        set_text(left_pane, left)
        set_text(right_pane, right)
        # window.refresh()
    return set_options


display_options = init_panes()


display_options(options[0], options[1])

import time

time.sleep(3)

curses.nocbreak()
window.keypad(False)
curses.echo()
curses.endwin()
