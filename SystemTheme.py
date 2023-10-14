import winreg

import preferences as pref

dark_mode_enabled = False

def is_dark_mode_enabled():
    try:
        # Open the Windows Registry to check the dark mode setting
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize')

        # Query the AppsUseLightTheme value (0 for dark mode, 1 for light mode)
        apps_use_light_theme, _ = winreg.QueryValueEx(key, 'AppsUseLightTheme')

        # Close the registry key
        winreg.CloseKey(key)

        # Return True if dark mode is enabled (AppsUseLightTheme is 0)
        return apps_use_light_theme == 0

    except Exception as e:
        print("<Error!> Exception Caught, ", e)
        return False


dark_mode_enabled = is_dark_mode_enabled()

if pref.debug:
    if dark_mode_enabled:
        print("Dark mode is enabled in Windows.")
    else:
        print("Dark mode is not enabled in Windows.")



