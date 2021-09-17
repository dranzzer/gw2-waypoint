import pywin32


window = win32gui.FindWindow("Notepad", None)
if window:
    tup = win32gui.GetWindowPlacement(window)
    if tup[1] == win32con.SW_SHOWMAXIMIZED:
        print("maximized")
    elif tup[1] == win32con.SW_SHOWMINIMIZED:
        print("minimized")
    elif tup[1] == win32con.SW_SHOWNORMAL:
        print("normal")