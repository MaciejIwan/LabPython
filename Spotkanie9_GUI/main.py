try:
    from Spotkanie9_GUI.appJar import gui
except:
    from appJar import gui

def press(button):
    if button == "Cancel":
        app.stop()
    else:
        usr = app.getEntry("Username")
        pwd = app.getEntry("Password")
        print("User: {0} \n Pass: {1}".format(usr, pwd))

#Create GUI
app = gui("Kalkulator", "400x550")
app.setBg("darkgray")
app.setFont(20)






app.go()
