import themes


#Name Of The Browser
app_name = "Vision Browser"

#This Url Will be Opened By The Browser When It Loads
app_defaultURL = "https://www.google.com"

#This Is The Default Webpage That The Browser Will Load Upon Startup
app_defaultHTMLWebpage = r"D:\PyCharm Projects\Vision Browser\HTML\Entry.html"

#This Checks Whether Browser Should Load A Search Engine Or A HTML Webpage
shouldLoadSearchEngine = True

#Whether the app should be opened full screen or not
fullScreen = True

#Default Theme Of The Browser
defaultTheme = themes.browser_Themes["Orange"]

#Checks Whether Debugging Is Enabled Or Not
debug = True

#Checks Whether Settings Tab Should Be Implemented From Browser Side Or By A HTML Webpage
settingsTabFromHTML = False

#This Specifies Whether The Splash Screen Should Be Shown Upon Browser Start
shouldLoadSplashScreen = True

#This Is The Image That The Browser Will Show Upon Start
splashScreenLogoPath = r"D:\PyCharm Projects\Vision Browser\Icons\Vision_Browser_Logo.png"

#This Is The HTML File That The Browser Will Render For The Settings Tab If <settingsTabFromHTML> Enabled
settingsTabHTMLFile_Path = ""

#If Enabled, Then The Theme Will Apply To All The UI ELements TODO
strongTheme = False
