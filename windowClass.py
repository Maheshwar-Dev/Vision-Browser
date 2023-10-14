import SystemTheme
import images as img                    #For UI Icon Paths
import preferences as pref              #Contains Browser Preferences
import themes                           #Contains Colors And Themes For UI
import screen                           #Contains Screen Dimensions
import chatGPT

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *  #Contains the web engine
from PyQt5.QtGui import QIcon ,QPixmap, QImage         #For UI Icons

import time

class CustomTabWidget(QTabWidget):

    def __init__(self):
        super().__init__()


        self.add_new_tab()
        self.setTabsClosable(True)
        self.tabCloseRequested.connect(self.close_tab)
        self.currentChanged.connect(self.on_current_tab_changed)

    def on_current_tab_changed(self, index):
        pass

    def add_new_tab(self):
        new_tab = QWidget()
        layout = QVBoxLayout()

        #Can Define Background Color Of Browser
        #self.setStyleSheet("background-color: " + themes.theme_color_orange_background[0] + ";")#+ "; color: " + themes.theme_color_orange[0] +  ";")
        # URL bar for the tab
        url_bar = QLineEdit()
        url_bar.setText("Enter A URL")
        url_bar.returnPressed.connect(self.navigate_to_url)

        web_view = QWebEngineView()
        layout.addWidget(web_view)



        new_tab.setLayout(layout)
        self.addTab(new_tab, "New Tab")
        self.setCurrentWidget(new_tab)

        if pref.shouldLoadSearchEngine:
            # Set the default URL for the new tab
            web_view.setUrl(QUrl(pref.app_defaultURL))

        else:
            # Set the default HTML Webpage for the new tab
            web_view.setUrl(QUrl.fromLocalFile(pref.app_defaultHTMLWebpage))

    def navigate_to_url(self):
        current_tab = self.currentWidget()
        if current_tab:
            url_bar = current_tab.findChild(QLineEdit)
            web_view = current_tab.findChild(QWebEngineView)
            if url_bar and web_view:
                url = url_bar.text()
                web_view.setUrl(QUrl(url))

    def close_tab(self, index):
        self.removeTab(index)




#Class Containing The Main Window
class MainWindow(QMainWindow):

    #Navigates To The Home Menu
    def Goto_Home(self):
        current_index = self.tabs.currentIndex()
        current_tab = self.tabs.widget(current_index)
        if current_tab:
            web_view = current_tab.findChild(QWebEngineView)
            if web_view:
                web_view.setUrl(QUrl(pref.app_defaultURL))

    def back_button_logic(self):
        current_index = self.tabs.currentIndex()
        current_tab = self.tabs.widget(current_index)
        if current_tab:
            web_view = current_tab.findChild(QWebEngineView)
            if web_view:
                web_view.back()

    def forward_button_logic(self):
        current_index = self.tabs.currentIndex()
        current_tab = self.tabs.widget(current_index)
        if current_tab:
            web_view = current_tab.findChild(QWebEngineView)
            if web_view:
                web_view.forward()

    def reload_button_logic(self):
        current_index = self.tabs.currentIndex()
        current_tab = self.tabs.widget(current_index)
        if current_tab:
            web_view = current_tab.findChild(QWebEngineView)
            if web_view:
                web_view.reload()

    def Nav_To_Url(self):
        current_index = self.tabs.currentIndex()
        current_tab = self.tabs.widget(current_index)
        if current_tab:
            web_view = current_tab.findChild(QWebEngineView)
            if web_view:
                url = self.url_bar.text()
                web_view.setUrl(QUrl(url))

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
        if pref.shouldLoadSearchEngine:
            web_view.setUrl(QUrl(pref.app_defaultURL))

        else:
            web_view.setUrl(QUrl.fromLocalFile(pref.app_defaultHTMLWebpage))

    def add_about_tab(self):
        new_tab = QWidget()  # Create a new QWidget for the tab
        self.tabs.addTab(new_tab, "About")

        # Create a new instance of QWebEngineView and set it as the central widget for the tab
        web_view = QWebEngineView(new_tab)
        new_tab.layout = QVBoxLayout()
        new_tab.layout.addWidget(web_view)
        new_tab.setLayout(new_tab.layout)

        # Set up context menu for the web view
        self.setup_tab_context_menu(web_view)

        # Loading a default HTML Webpage
        web_view.setUrl(QUrl.fromLocalFile(pref.app_defaultHTMLWebpage))

    def show_chat_dialog(self):
        chat_dialog = QDialog(self)
        chat_dialog.setWindowTitle("Chat with ChatGPT")

        chat_history = QTextEdit()
        chat_input = QTextEdit()

        send_button = QPushButton("Send")

        layout = QVBoxLayout()
        layout.addWidget(chat_history)
        layout.addWidget(chat_input)
        layout.addWidget(send_button)

        chat_dialog.setLayout(layout)

        # Connect the send button to a function to process the chat message
        send_button.clicked.connect(lambda: self.process_chat_message(chat_input, chat_history))

        chat_dialog.exec_()

    def process_chat_message(self, chat_input, chat_history):
        message = chat_input.toPlainText()
        # Here, you can process the message and send it to ChatGPT.
        # You can update the chat history display with responses.

    def add_settings_tab(self):
        new_tab = QWidget()  # Create a new QWidget for the tab
        self.tabs.addTab(new_tab, "Settings")

        #Dialog BOX SET HERE TODO

        #------------------END

        # Create a new layout for the tab
        tab_layout = QVBoxLayout()
        # Create a new instance of QWebEngineView
        web_view = QWebEngineView()



        # Loading a default HTML Webpage
        if pref.settingsTabFromHTML:
            web_view.setUrl(QUrl.fromLocalFile(pref.settingsTabHTMLFile_Path)) #Load The HTML File
            tab_layout.addWidget(web_view) # Add the web view to the layout below the buttons
            new_tab.setLayout(tab_layout)  # Set the tab's layout

        # Rendering Settings Tab From Browser Side
        else:
            #Themes Menu
            themeButtons_layout  = QHBoxLayout() #Create a horizontal layout for the theme selecting buttons
            themesTextLabel = QLabel("Themes")

            orangeColor_Btn = QPushButton("Orange")
            voiletColor_Btn = QPushButton("Voilet")
            pinkColor_Btn = QPushButton("Pink")
            cyanColor_Btn = QPushButton("Cyan")
            limeColor_Btn = QPushButton("Lime")
            lightColor_Btn = QPushButton("Light")
            darkColor_Btn = QPushButton("Dark")
            systemColor_Btn = QPushButton("System")


            themeButtons_layout.addWidget(themesTextLabel)

            # Create and add five buttons to the horizontal layout

            themeButtons_layout.addWidget(orangeColor_Btn)
            themeButtons_layout.addWidget(voiletColor_Btn)
            themeButtons_layout.addWidget(pinkColor_Btn)
            themeButtons_layout.addWidget(cyanColor_Btn)
            themeButtons_layout.addWidget(limeColor_Btn)
            themeButtons_layout.addWidget(lightColor_Btn)
            themeButtons_layout.addWidget(darkColor_Btn)
            themeButtons_layout.addWidget(systemColor_Btn)



            #Enable JavaScript Menu
            javaScript_layout = QHBoxLayout()
            javaScriptTextLabel = QLabel("JavaScript")
            javaScriptToggle = QRadioButton("Enable")

            javaScript_layout.addWidget(javaScriptTextLabel)
            javaScript_layout.addWidget(javaScriptToggle)

            #





            #Layouts Define The Rows In Which The Buttons Will Be Placed

            tab_layout.addLayout(themeButtons_layout)  # Add the button layout to the top of the tab layout
            tab_layout.addLayout(javaScript_layout)    # Add The JavaScript Layout
            tab_layout.addWidget(web_view) # Add the web view to the layout below the buttons
            new_tab.setLayout(tab_layout)  # Set the tab's layout






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

    def update_url_bar(self, index):
        current_tab = self.tabs.widget(index)
        if current_tab:
            web_view = current_tab.findChild(QWebEngineView)
            if web_view:
                self.url_bar.setText(web_view.url().toString())



    #Constructor
    def __init__(self):

        #Setting Up The App Window
        super(MainWindow, self).__init__()

        if pref.shouldLoadSplashScreen:
            self.show_splash_screen()

        '''
        if SystemTheme.dark_mode_enabled:
            self.setStyleSheet("background-color: #1E1E1E; color: #FFFFFF;")
        else:
            self.setStyleSheet("background-color: #FFFFFF; color: #000000;")
        '''

        #EXTRA

        #/EXTRA

        #self.setStyleSheet("background-color: " + themes.theme_color_orange_background[0] + ";") #+  "; color: " + themes.theme_color_orange[0] +  ";")

        #Enabling The Web Engine View Eg The Search Engine
        self.browser = QWebEngineView()

        #self.browser.page().runJavaScript(r"D:\PyCharm Projects\Vision Browser\JavaScript\ForceDarkMode.js")    TODO

        self.setGeometry(100, 100, screen.width, screen.height)

        #Checks Whether App Should Be Opened In Full Screen Or Not
        if pref.fullScreen == True:
            self.showMaximized()

        else:
            self.show()  #ERR CHK

        #Setting Up the Default URL that the browser will load On Start
        #self.browser.setUrl(QUrl(pref.app_defaultURL))

        self.tabs = CustomTabWidget()
        self.setCentralWidget(self.tabs)

        #Add Tab Button
        self.addTab_btn = QAction("Add Tab", self)
        self.addTab_btn.setIcon(QIcon(img.AddTab_Btn_Icon_Path))
        self.addTab_btn.triggered.connect(self.tabs.add_new_tab)

        #Close Tab Button
        self.closeTab_btn = QAction("Close Tab", self)
        self.closeTab_btn.setIcon(QIcon(img.CloseTab_Btn_Icon_Path))
        self.closeTab_btn.triggered.connect(self.close_tab)

        self.menuBar().addAction(self.addTab_btn)
        self.menuBar().addAction(self.closeTab_btn)

        #This Will Allow Us To See The Google WebEngine
        #self.setCentralWidget(self.browser)



        #This the the navigation bar located at the top of browser, it contains reload, forward and back btns
        navbar = QToolBar()
        navbar.setStyleSheet("background-color: " + themes.navBar_color)

        #Adding The Toolbar To The Browser
        self.addToolBar(navbar)


        #Back Button
        back_btn = QAction("Back", self) #Creating A Button
        back_btn.setIcon(QIcon(img.Back_Btn_Icon_Path)) #Setting Icon For Button
        back_btn.triggered.connect(self.back_button_logic) #Logic To Be Performed Upon Clicking the Button
        navbar.addAction(back_btn)  #Add The Button To The Toolbar

        #Forward Button
        forward_btn = QAction("Forward", self) #Creating A Button
        forward_btn.setIcon(QIcon(img.Forward_Btn_Icon_Path)) #Setting Icon For Button
        forward_btn.triggered.connect(self.forward_button_logic) #Logic To Be Performed Upon Clicking the Button
        navbar.addAction(forward_btn)  #Add The Button To The Toolbar

        #Reload Button
        reload_btn = QAction("Reload", self) #Creating A Button
        reload_btn.setIcon(QIcon(img.Reload_Btn_Icon_Path)) #Setting Icon For Button
        reload_btn.triggered.connect(self.reload_button_logic) #Logic To Be Performed Upon Clicking the Button
        navbar.addAction(reload_btn)  #Add The Button To The Toolbar

        #Home Button
        home_btn = QAction("Home", self) #Creating A Button
        home_btn.setIcon(QIcon(img.Home_Btn_Icon_Path)) #Setting Icon For Button
        home_btn.triggered.connect(self.Goto_Home) #Logic To Be Performed Upon Clicking the Button
        navbar.addAction(home_btn)  #Add The Button To The Toolbar


        # URL Bar
        self.url_bar = QLineEdit()
        self.url_bar.setText("Enter A URL")
        self.url_bar.returnPressed.connect(self.Nav_To_Url)
        navbar.addWidget(self.url_bar)

        # Connect the currentChanged signal of the tabs to update the URL bar for the current tab
        self.tabs.currentChanged.connect(self.update_url_bar)

        #*********************************** UI BUTTONS **********************************************************

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
        settings_btn.triggered.connect(self.add_settings_tab) #Logic To Be Performed Upon Clicking the Button
        navbar.addAction(settings_btn)  #Add The Button To The Toolbar


        #About Button
        about_btn = QAction("About", self) #Creating A Button
        #about_btn.setIcon(QIcon(img.About_Btn_Icon_Path)) #Setting Icon For Button TODO
        about_btn.triggered.connect(self.add_about_tab) #Logic To Be Performed Upon Clicking the Button
        navbar.addAction(about_btn)  #Add The Button To The Toolbar


        #ChatGPT Button
        chatGPT_btn = QAction("ChatGPT", self) #Creating A Button
        #chatGPT_btn.setIcon(QIcon(img.About_Btn_Icon_Path)) #Setting Icon For Button TODO
        chatGPT_btn.triggered.connect(self.show_chat_dialog) #Logic To Be Performed Upon Clicking the Button
        navbar.addAction(chatGPT_btn)  #Add The Button To The Toolbar




        #On Url Change
        self.browser.urlChanged.connect(self.UpdateURL)

        if pref.shouldLoadSplashScreen:
            self.browser.page().loadFinished.connect(self.hide_splash_screen)



    def show_splash_screen(self):
        pixmap = QPixmap(pref.splashScreenLogoPath)  # Replace with your actual logo image path
        splash = QSplashScreen(pixmap, Qt.WindowStaysOnTopHint)
        splash.setMask(pixmap.mask())
        splash.show()
        self.splash = splash  # Store a reference to the splash screen

        # Create a QTimer to close the splash screen after a certain duration (e.g., 2 seconds)
        self.splash_timer = QTimer()
        self.splash_timer.timeout.connect(self.hide_splash_screen)
        self.splash_timer.start(2000)  # 2000 milliseconds (2 seconds)

    def hide_splash_screen(self):
        if hasattr(self, 'splash'):
            self.splash.finish(self)  # Close the splash screen
            self.splash_timer.stop()  # Stop the timer
