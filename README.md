# Python-sArCaStIc-Text-Converter

## [Downloads](https://github.com/VarunS2002/Python-sArCaStIc-Text-Converter/releases)
>[![.exe: v1.0.0](https://img.shields.io/badge/.exe-v1.0.0-brightgreen)](https://github.com/VarunS2002/Python-sArCaStIc-Text-Converter/releases/download/1.0.0/.exe)
[![.py: v1.0.0](https://img.shields.io/badge/.py-v1.0.0-brightgreen)](https://github.com/VarunS2002/Python-sArCaStIc-Text-Converter/releases/download/1.0.0/.py)
>[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

This program is used to convert normal text to sarcastic or mocking text by alternatively capitalizing characters.

For example, 'how are you doing bro?' becomes 'hOw aRe yOu dOiNg bRo?'.

This is particularly used for mocking someone in text messages and used for memes.

This program can be run directly to get a GUI for converting the desired text or
it can be used as a module for getting the converted text in a different python program.

## Installation:

-Types of variants available:
 
 1. `.py` (Python Source Code)
 
 2. `.exe` (Windows Executable)
 
-Requirements for 1:
 
 - Latest version of Python 
 
 - For Windows https://www.python.org/downloads/ is recommended

 - Add Python to PATH/Environment Variables during installation in Windows (recommended)

-Requirements for 2:
 
 - Windows OS  
 
## Usage:

1. Run the program directly to get a GUI for converting the desired text

2. Can be used as a python module to get the converted text in a different python program. Example:
    ```
    from sArCaStIc_Text_Converter import SarcasticText
    converted_text = SarcasticText.convert_text(input("Enter a string: "))
    print(converted_text)
    ```

## Note:

- Use case 1 is available with both the .py and .exe files

- Use case 2 is available only with the .py file

## Screenshots:

- GUI

    ![GUI](https://i.imgur.com/tFHe8me.png)
