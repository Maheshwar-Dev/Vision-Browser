import images as img                    #For UI Icon Paths
import preferences as pref              #Contains Browser Preferences
import themes                           #Contains Colors And Themes For UI
import screen                           #Contains Screen Dimensions


from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *  #Contains the web engine
from PyQt5.QtGui import QIcon           #For UI Icons




#Class Containing The Main Window
class MainWindow(QMainWindow):


    #Navigates To The Home Menu
    def Goto_Home(self):
        self.browser.setUrl(QUrl(pref.app_defaultURL))


    def Nav_To_Url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def UpdateURL(self, q):
        self.url_bar.setText(q.toString())

    def add_new_tab(self):
        new_tab = QWidget()  # Create a new QWidget for the tab
        self.tabs.addTab(new_tab, "New Tab")

        # Create a new instance of QWebEngineView and set it as the central widget for the tab
        web_view = QWebEngineView(new_tab)
        new_tab.layout = QVBoxLayout()
        new_tab.layout.addWidget(web_view)
        new_tab.setLayout(new_tab.layout)

        # Set up context menu for the web view
        self.setup_tab_context_menu(web_view)

        # Load a default URL or perform any other initialization for the web view here
        web_view.setUrl(QUrl(pref.app_defaultURL))

    def setup_tab_context_menu(self, tab):
        # Create a context menu for each tab with a "Close Tab" action
        close_tab_action = QAction("Close Tab", tab)
        close_tab_action.triggered.connect(self.close_tab)
        tab.setContextMenuPolicy(3)  # 3 represents ActionsContextMenu
        tab.addAction(close_tab_action)

    def close_tab(self):
        # Get the index of the current tab
        current_tab_index = self.tabs.currentIndex()
        if current_tab_index != -1:  # Ensure a tab is open
            # Remove the current tab
            self.tabs.removeTab(current_tab_index)

    #Constructor
    def __init__(self):

        #Setting Up The App Window
        super(MainWindow, self).__init__()

        #Enabling The Web Engine View Eg The Search Engine
        self.browser = QWebEngineView()

        #Setting Up the Default URL that the browser will load On Start
        #self.browser.setUrl(QUrl(pref.app_defaultURL))



        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        # Create a new tab and add a WebView to it

        #Add Tab Button
        self.addTab_btn = QAction("Add Tab", self)
        self.addTab_btn.setIcon(QIcon(img.AddTab_Btn_Icon_Path))
        self.addTab_btn.triggered.connect(self.add_new_tab)
        self.add_new_tab()

        #Close Tab Button
        self.closeTab_btn = QAction("Close Tab", self)
        self.closeTab_btn.setIcon(QIcon(img.CloseTab_Btn_Icon_Path))
        self.closeTab_btn.triggered.connect(self.close_tab)

        self.menuBar().addAction(self.addTab_btn)
        self.menuBar().addAction(self.closeTab_btn)


        #This Will Allow Us To See The Google WebEngine
        #self.setCentralWidget(self.browser)

        #Checks Whether App Should Be Opened In Full Screen Or Not
        if(pref.fullScreen == True):
            self.showMaximized()

        else:
            self.setGeometry(100, 100, screen.width, screen.height)
            self.show()  #ERR CHK

        #This the the navigation bar located at the top of browser, it contains reload, forward and back btns
        navbar = QToolBar()
        navbar.setStyleSheet("background-color: " + themes.navBar_color)

        #Adding The Toolbar To The Browser
        self.addToolBar(navbar)


        #Back Button
        back_btn = QAction("Back", self) #Creating A Button
        back_btn.setIcon(QIcon(img.Back_Btn_Icon_Path)) #Setting Icon For Button
        back_btn.triggered.connect(self.browser.back) #Logic To Be Performed Upon Clicking the Button
        navbar.addAction(back_btn)  #Add The Button To The Toolbar

        #Forward Button
        forward_btn = QAction("Forward", self) #Creating A Button
        forward_btn.setIcon(QIcon(img.Forward_Btn_Icon_Path)) #Setting Icon For Button
        forward_btn.triggered.connect(self.browser.forward) #Logic To Be Performed Upon Clicking the Button
        navbar.addAction(forward_btn)  #Add The Button To The Toolbar

        #Reload Button
        reload_btn = QAction("Reload", self) #Creating A Button
        reload_btn.setIcon(QIcon(img.Reload_Btn_Icon_Path)) #Setting Icon For Button
        reload_btn.triggered.connect(self.browser.reload) #Logic To Be Performed Upon Clicking the Button
        navbar.addAction(reload_btn)  #Add The Button To The Toolbar

        #Home Button
        home_btn = QAction("Home", self) #Creating A Button
        home_btn.setIcon(QIcon(img.Home_Btn_Icon_Path)) #Setting Icon For Button
        home_btn.triggered.connect(self.Goto_Home) #Logic To Be Performed Upon Clicking the Button
        navbar.addAction(home_btn)  #Add The Button To The Toolbar


        #URL Bar
        self.url_bar = QLineEdit()
        self.url_bar.setText("Enter A URL")
        self.url_bar.returnPressed.connect(self.Nav_To_Url)
        navbar.addWidget(self.url_bar)

        #Seperating The Navbar So That Buttons Can Go On Right Side
        #navbar.addSeparator()


        #Search Btn
        search_btn = QAction("Search", self) #Creating A Button
        search_btn.setIcon(QIcon(img.Search_Btn_Icon_Path)) #Setting Icon For Button
        #settings_btn.triggered.connect() #Logic To Be Performed Upon Clicking the Button TODO
        navbar.addAction(search_btn)  #Add The Button To The Toolbar


        #Voice Btn
        voice_btn = QAction("Voice", self) #Creating A Button
        voice_btn.setIcon(QIcon(img.Voice_Btn_Icon_Path)) #Setting Icon For Button
        #settings_btn.triggered.connect() #Logic To Be Performed Upon Clicking the Button TODO
        navbar.addAction(voice_btn)  #Add The Button To The Toolbar


        #Settings Btn
        settings_btn = QAction("Settings", self) #Creating A Button
        settings_btn.setIcon(QIcon(img.Settings_Btn_Icon_Path)) #Setting Icon For Button
        settings_btn.triggered.connect(self.Goto_Home) #Logic To Be Performed Upon Clicking the Button
        navbar.addAction(settings_btn)  #Add The Button To The Toolbar


       #On Url Change
        self.browser.urlChanged.connect(self.UpdateURL)
