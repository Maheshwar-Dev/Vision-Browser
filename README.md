# Vision-Browser
This is a qt based web-browser created using python


**Before Running Program**

Note That Before Running The App You Must Go To The *images.py* Script and Edit The Image File Paths As They Are Different For Each Computer.

The *Icons* Folder Within This Project Contains All The Icons For Your Browser UI.

You Must Correct File Paths For Every Single Icon. 

**How To Know A Icon's File Path??**

Just Find The Icon In Your Pc and Then Right Click. Click On Copy As File Path.

Icon Can Be Of Any Image Format Like *.png* , *.jpg* , *.jpeg* etc.

Paste The File Path In The *image filepath variable* and Add *r* Before It So That It Corrects Windows Path Like 

**Changing UI Icons**

You Can Also Change UI Icons By Adding Your Own Image Path Instead Of The Default Ones In The *images.py* Script


**Forward_Btn_Icon_Path = r"C://Users/Downloads/myImg.png"**



**Colors**
The *themes.py* Contains All The Colors For The UI Elements.

In Order To Change Color Of A UI Element, Just Locate Its Color Variable in *themes.py* And Change Its Color By Adding A Color Code.

Eg- **navBar_Color = "0xFFFF"**

Note: It Is Important For The Color Code To Be Represented In HexaDecimal Format. Writing Direct "Red" or "Blue" Would Generate An Error.

Anything Starting With *0x*  Is A Hexadecimal Number.

Likewise Color Codes Are Also Represented In HexaDecimals.

**How To Know Color Code Of A Color??**

Just Go To Google -> Search *Color Picker* and From There Pick Your Favourite Color And Copy Its Color Code.

Paste That Color Code In The Variable Data And Bingo, The UI Element's Color Will Be Changed.
