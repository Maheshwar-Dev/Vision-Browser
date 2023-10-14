import ImageColorConverter as ImgConverter
import images as img
import preferences as pref
import themes
import windowClass as winclass
import SystemTheme as systheme

userPrefs_File_Path = r"D:\PyCharm Projects\Vision Browser\userPrefs.txt"

def Init():
    try:
        prefFile = open(userPrefs_File_Path, 'r')

        if pref.debug:
            if prefFile:
                print("File <userPrefs> opened successfully")
            else:
                print("Error! Cant Find <userPrefs.txt>")

        fileLine = str(prefFile.readline())

        prevTheme = ""

        if fileLine.__contains__("THEME:ORANGE"):
            prevTheme = themes.theme_color_orange
            prefFile.close()
        elif fileLine.__contains__("THEME:CYAN"):
            prevTheme = themes.theme_color_cyan
            prefFile.close()
        elif fileLine.__contains__("THEME:LIME"):
            prevTheme = themes.theme_color_lime
            prefFile.close()
        elif fileLine.__contains__("THEME:PINK"):
            prevTheme = themes.theme_color_pink
            prefFile.close()
        elif fileLine.__contains__("THEME:VOILET"):
            prevTheme = themes.theme_color_voilet
            prefFile.close()
        elif fileLine.__contains__("THEME:LIGHT"):
            prevTheme = themes.theme_color_light
            prefFile.close()
        elif fileLine.__contains__("THEME:DARK"):
            prevTheme = themes.theme_color_dark
            prefFile.close()
        else:
            print("<File Error>! The File <userPrefs.txt> Doesn't Contain A Theme Variable\n")
            prefFile.close()
            exit(1)

    except Exception as e:
        print("Error! The File <userPrefs.txt> Couldn't Be Found")
        prefFile.close()


    if pref.defaultTheme == "Orange":
        #Update The File
        try:
            prefFile = open(userPrefs_File_Path, 'w')
            prefFile.write("THEME:ORANGE")
            prefFile.close()
        except Exception as e:
            #Error Occured Then Close The File And Exit The Program
            print("<Error>! ", e)
            prefFile.close()
            exit(0)

        #Change Icon Background
        ImgConverter.replace_color(img.Forward_Btn_Icon_Path, prevTheme[1], themes.theme_color_orange[1])
        ImgConverter.replace_color(img.Back_Btn_Icon_Path, prevTheme[1], themes.theme_color_orange[1])
        ImgConverter.replace_color(img.Reload_Btn_Icon_Path, prevTheme[1], themes.theme_color_orange[1])
        ImgConverter.replace_color(img.Home_Btn_Icon_Path, prevTheme[1], themes.theme_color_orange[1])
        ImgConverter.replace_color(img.Voice_Btn_Icon_Path, prevTheme[1], themes.theme_color_orange[1])
        ImgConverter.replace_color(img.Search_Btn_Icon_Path, prevTheme[1], themes.theme_color_orange[1])
        ImgConverter.replace_color(img.Settings_Btn_Icon_Path, prevTheme[1], themes.theme_color_orange[1])
        ImgConverter.replace_color(img.AddTab_Btn_Icon_Path, prevTheme[1], themes.theme_color_orange[1])
        ImgConverter.replace_color(img.CloseTab_Btn_Icon_Path, prevTheme[1], themes.theme_color_orange[1])

        #winclass.setSty
        if pref.debug == True:
            print("Converted To Orange")

        #Change Other UI Background
        themes.navBar_color = themes.theme_color_orange_background[0]

    elif pref.defaultTheme == "Pink":
        #Update The File
        try:
            prefFile = open(userPrefs_File_Path, 'w')
            prefFile.write("THEME:PINK")
            prefFile.close()
        except Exception as e:
            #Error Occured Then Close The File And Exit The Program
            print("<Error>! ", e)
            prefFile.close()
            exit(0)
        #Change Icon Background
        ImgConverter.replace_color(img.Forward_Btn_Icon_Path, prevTheme[1], themes.theme_color_pink[1])
        ImgConverter.replace_color(img.Back_Btn_Icon_Path, prevTheme[1], themes.theme_color_pink[1])
        ImgConverter.replace_color(img.Reload_Btn_Icon_Path, prevTheme[1], themes.theme_color_pink[1])
        ImgConverter.replace_color(img.Home_Btn_Icon_Path, prevTheme[1], themes.theme_color_pink[1])
        ImgConverter.replace_color(img.Voice_Btn_Icon_Path, prevTheme[1], themes.theme_color_pink[1])
        ImgConverter.replace_color(img.Search_Btn_Icon_Path, prevTheme[1], themes.theme_color_pink[1])
        ImgConverter.replace_color(img.Settings_Btn_Icon_Path, prevTheme[1], themes.theme_color_pink[1])
        ImgConverter.replace_color(img.AddTab_Btn_Icon_Path, prevTheme[1], themes.theme_color_pink[1])
        ImgConverter.replace_color(img.CloseTab_Btn_Icon_Path, prevTheme[1], themes.theme_color_pink[1])

        if pref.debug == True:
            print("Converted To Pink")

        #Change Other UI Background
        themes.navBar_color = themes.theme_color_pink_background[0]

    elif pref.defaultTheme == "Cyan":
        #Update The File
        try:
            prefFile = open(userPrefs_File_Path, 'w')
            prefFile.write("THEME:CYAN")
            prefFile.close()
        except Exception as e:
            #Error Occured Then Close The File And Exit The Program
            print("<Error>! ", e)
            prefFile.close()
            exit(0)
        #Change Icon Background
        ImgConverter.replace_color(img.Forward_Btn_Icon_Path, prevTheme[1], themes.theme_color_cyan[1])
        ImgConverter.replace_color(img.Back_Btn_Icon_Path, prevTheme[1], themes.theme_color_cyan[1])
        ImgConverter.replace_color(img.Reload_Btn_Icon_Path, prevTheme[1], themes.theme_color_cyan[1])
        ImgConverter.replace_color(img.Home_Btn_Icon_Path, prevTheme[1], themes.theme_color_cyan[1])
        ImgConverter.replace_color(img.Voice_Btn_Icon_Path, prevTheme[1], themes.theme_color_cyan[1])
        ImgConverter.replace_color(img.Search_Btn_Icon_Path, prevTheme[1], themes.theme_color_cyan[1])
        ImgConverter.replace_color(img.Settings_Btn_Icon_Path, prevTheme[1], themes.theme_color_cyan[1])
        ImgConverter.replace_color(img.AddTab_Btn_Icon_Path, prevTheme[1], themes.theme_color_cyan[1])
        ImgConverter.replace_color(img.CloseTab_Btn_Icon_Path, prevTheme[1], themes.theme_color_cyan[1])

        if pref.debug == True:
            print("Converted To Cyan")

        #Change Other UI Background
        themes.navBar_color = themes.theme_color_cyan_background[0]

    elif pref.defaultTheme == "Voilet":
        #Update The File
        try:
            prefFile = open(userPrefs_File_Path, 'w')
            prefFile.write("THEME:VOILET")
            prefFile.close()
        except Exception as e:
            #Error Occured Then Close The File And Exit The Program
            print("<Error>! ", e)
            prefFile.close()
            exit(0)
        #Change Icon Background
        ImgConverter.replace_color(img.Forward_Btn_Icon_Path, prevTheme[1], themes.theme_color_voilet[1])
        ImgConverter.replace_color(img.Back_Btn_Icon_Path, prevTheme[1], themes.theme_color_voilet[1])
        ImgConverter.replace_color(img.Reload_Btn_Icon_Path, prevTheme[1], themes.theme_color_voilet[1])
        ImgConverter.replace_color(img.Home_Btn_Icon_Path, prevTheme[1], themes.theme_color_voilet[1])
        ImgConverter.replace_color(img.Voice_Btn_Icon_Path, prevTheme[1], themes.theme_color_voilet[1])
        ImgConverter.replace_color(img.Search_Btn_Icon_Path, prevTheme[1], themes.theme_color_voilet[1])
        ImgConverter.replace_color(img.Settings_Btn_Icon_Path, prevTheme[1], themes.theme_color_voilet[1])
        ImgConverter.replace_color(img.AddTab_Btn_Icon_Path, prevTheme[1], themes.theme_color_voilet[1])
        ImgConverter.replace_color(img.CloseTab_Btn_Icon_Path, prevTheme[1], themes.theme_color_voilet[1])

        if pref.debug == True:
            print("Converted To Voilet")

        #Change Other UI Background
        themes.navBar_color = themes.theme_color_voilet_background[0]

    elif pref.defaultTheme == "Lime":
        #Update The File
        try:
            prefFile = open(userPrefs_File_Path, 'w')
            prefFile.write("THEME:LIME")
            prefFile.close()
        except Exception as e:
            #Error Occured Then Close The File And Exit The Program
            print("<Error>! ", e)
            prefFile.close()
            exit(0)
        #Change Icon Background
        ImgConverter.replace_color(img.Forward_Btn_Icon_Path, prevTheme[1], themes.theme_color_lime[1])
        ImgConverter.replace_color(img.Back_Btn_Icon_Path, prevTheme[1], themes.theme_color_lime[1])
        ImgConverter.replace_color(img.Reload_Btn_Icon_Path, prevTheme[1], themes.theme_color_lime[1])
        ImgConverter.replace_color(img.Home_Btn_Icon_Path, prevTheme[1], themes.theme_color_lime[1])
        ImgConverter.replace_color(img.Voice_Btn_Icon_Path, prevTheme[1], themes.theme_color_lime[1])
        ImgConverter.replace_color(img.Search_Btn_Icon_Path, prevTheme[1], themes.theme_color_lime[1])
        ImgConverter.replace_color(img.Settings_Btn_Icon_Path, prevTheme[1], themes.theme_color_lime[1])
        ImgConverter.replace_color(img.AddTab_Btn_Icon_Path, prevTheme[1], themes.theme_color_lime[1])
        ImgConverter.replace_color(img.CloseTab_Btn_Icon_Path, prevTheme[1], themes.theme_color_lime[1])

        if pref.debug == True:
            print("Converted To Lime")

        #Change Other UI Background
        themes.navBar_color = themes.theme_color_lime_background[0]

    elif pref.defaultTheme == "Light":
        #Update The File
        try:
            prefFile = open(userPrefs_File_Path, 'w')
            prefFile.write("THEME:LIGHT")
            prefFile.close()
        except Exception as e:
            #Error Occured Then Close The File And Exit The Program
            print("<Error>! ", e)
            prefFile.close()
            exit(0)
        #Change Icon Background
        ImgConverter.replace_color(img.Forward_Btn_Icon_Path, prevTheme[1], themes.theme_color_light[1])
        ImgConverter.replace_color(img.Back_Btn_Icon_Path, prevTheme[1], themes.theme_color_light[1])
        ImgConverter.replace_color(img.Reload_Btn_Icon_Path, prevTheme[1], themes.theme_color_light[1])
        ImgConverter.replace_color(img.Home_Btn_Icon_Path, prevTheme[1], themes.theme_color_light[1])
        ImgConverter.replace_color(img.Voice_Btn_Icon_Path, prevTheme[1], themes.theme_color_light[1])
        ImgConverter.replace_color(img.Search_Btn_Icon_Path, prevTheme[1], themes.theme_color_light[1])
        ImgConverter.replace_color(img.Settings_Btn_Icon_Path, prevTheme[1], themes.theme_color_light[1])
        ImgConverter.replace_color(img.AddTab_Btn_Icon_Path, prevTheme[1], themes.theme_color_light[1])
        ImgConverter.replace_color(img.CloseTab_Btn_Icon_Path, prevTheme[1], themes.theme_color_light[1])

        if pref.debug == True:
            print("Converted To Light")

        #Change Other UI Background
        themes.navBar_color = themes.theme_color_light_background[0]

    elif pref.defaultTheme == "Dark":
        #Update The File
        try:
            prefFile = open(userPrefs_File_Path, 'w')
            prefFile.write("THEME:DARK")
            prefFile.close()
        except Exception as e:
            #Error Occured Then Close The File And Exit The Program
            print("<Error>! ", e)
            prefFile.close()
            exit(0)
        #Change Icon Background
        ImgConverter.replace_color(img.Forward_Btn_Icon_Path, prevTheme[1], themes.theme_color_dark[1])
        ImgConverter.replace_color(img.Back_Btn_Icon_Path, prevTheme[1], themes.theme_color_dark[1])
        ImgConverter.replace_color(img.Reload_Btn_Icon_Path, prevTheme[1], themes.theme_color_dark[1])
        ImgConverter.replace_color(img.Home_Btn_Icon_Path, prevTheme[1], themes.theme_color_dark[1])
        ImgConverter.replace_color(img.Voice_Btn_Icon_Path, prevTheme[1], themes.theme_color_dark[1])
        ImgConverter.replace_color(img.Search_Btn_Icon_Path, prevTheme[1], themes.theme_color_dark[1])
        ImgConverter.replace_color(img.Settings_Btn_Icon_Path, prevTheme[1], themes.theme_color_dark[1])
        ImgConverter.replace_color(img.AddTab_Btn_Icon_Path, prevTheme[1], themes.theme_color_dark[1])
        ImgConverter.replace_color(img.CloseTab_Btn_Icon_Path, prevTheme[1], themes.theme_color_dark[1])

        if pref.debug == True:
            print("Converted To Dark")

        #Change Other UI Background
        themes.navBar_color = themes.theme_color_dark_background[0]

    elif pref.defaultTheme == "System":
        #Update The File for Dark Theme
        if systheme.dark_mode_enabled:
            try:
                prefFile = open(userPrefs_File_Path, 'w')
                prefFile.write("THEME:DARK")
                prefFile.close()
            except Exception as e:
                #Error Occured Then Close The File And Exit The Program
                print("<Error>! ", e)
                prefFile.close()
                exit(0)
            #Change Icon Background
            ImgConverter.replace_color(img.Forward_Btn_Icon_Path, prevTheme[1], themes.theme_color_dark[1])
            ImgConverter.replace_color(img.Back_Btn_Icon_Path, prevTheme[1], themes.theme_color_dark[1])
            ImgConverter.replace_color(img.Reload_Btn_Icon_Path, prevTheme[1], themes.theme_color_dark[1])
            ImgConverter.replace_color(img.Home_Btn_Icon_Path, prevTheme[1], themes.theme_color_dark[1])
            ImgConverter.replace_color(img.Voice_Btn_Icon_Path, prevTheme[1], themes.theme_color_dark[1])
            ImgConverter.replace_color(img.Search_Btn_Icon_Path, prevTheme[1], themes.theme_color_dark[1])
            ImgConverter.replace_color(img.Settings_Btn_Icon_Path, prevTheme[1], themes.theme_color_dark[1])
            ImgConverter.replace_color(img.AddTab_Btn_Icon_Path, prevTheme[1], themes.theme_color_dark[1])
            ImgConverter.replace_color(img.CloseTab_Btn_Icon_Path, prevTheme[1], themes.theme_color_dark[1])

            if pref.debug == True:
                print("Converted To System_Dark")

            #Change Other UI Background
            themes.navBar_color = themes.theme_color_dark_background[0]


        #Update The File For Light Theme
        else:
            try:
                prefFile = open(userPrefs_File_Path, 'w')
                prefFile.write("THEME:LIGHT")
                prefFile.close()
            except Exception as e:
                #Error Occured Then Close The File And Exit The Program
                print("<Error>! ", e)
                prefFile.close()
                exit(0)
            #Change Icon Background
            ImgConverter.replace_color(img.Forward_Btn_Icon_Path, prevTheme[1], themes.theme_color_light[1])
            ImgConverter.replace_color(img.Back_Btn_Icon_Path, prevTheme[1], themes.theme_color_light[1])
            ImgConverter.replace_color(img.Reload_Btn_Icon_Path, prevTheme[1], themes.theme_color_light[1])
            ImgConverter.replace_color(img.Home_Btn_Icon_Path, prevTheme[1], themes.theme_color_light[1])
            ImgConverter.replace_color(img.Voice_Btn_Icon_Path, prevTheme[1], themes.theme_color_light[1])
            ImgConverter.replace_color(img.Search_Btn_Icon_Path, prevTheme[1], themes.theme_color_light[1])
            ImgConverter.replace_color(img.Settings_Btn_Icon_Path, prevTheme[1], themes.theme_color_light[1])
            ImgConverter.replace_color(img.AddTab_Btn_Icon_Path, prevTheme[1], themes.theme_color_light[1])
            ImgConverter.replace_color(img.CloseTab_Btn_Icon_Path, prevTheme[1], themes.theme_color_light[1])

            if pref.debug == True:
                print("Converted To System_Light")

            #Change Other UI Background
            themes.navBar_color = themes.theme_color_light_background[0]

    else:
        print("Undefined Theme")

