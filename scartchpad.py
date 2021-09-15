from win32gui import GetWindowText, GetForegroundWindow

#i=1
#while i==1:
#    print(GetWindowText(GetForegroundWindow()))

print(type(GetWindowText(GetForegroundWindow())))