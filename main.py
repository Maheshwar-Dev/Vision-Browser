import sys
import windowClass as win

#-------------------------------------------------------------Program-----------------------------------------------------------------------------------------------

#This is The Main Function Of The Program

def main():
    #Setting Up A QT Application
    app = win.QApplication(sys.argv)

    print("Browser Started")

    #Setting the name of the app
    app.setApplicationName(win.pref.app_name)


    #Setting The Default Icon Of App
    app.setWindowIcon(win.QIcon(win.img.Browser_Icon_Path))

    #Instantiaing an Object out of MainWindow Class
    window = win.MainWindow()


    #Contains the Main Loop/ Executes The App
    sys.exit(app.exec_())



if __name__ == "__main__":
    main()







