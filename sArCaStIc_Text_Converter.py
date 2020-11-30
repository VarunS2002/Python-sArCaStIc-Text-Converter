"""
This program can be run directly to get a GUI for converting the desired text or
it can be used as a module for getting the converted text in a different python program.
Simply add

from sArCaStIc_Text_Converter import SarcasticText

to the import statements and use

SarcasticText.convert_text("<text-to-be-converted>")

to retrieve the converted text in a variable.
"""


class SarcasticText:
    """
    This class is used to convert normal strings to alternatively capitalized strings.
    Initialise this class with a tkinter.Tk() instance as a parameter to get a GUI to
    convert the desired text or
    use the static method convert_text() with the desired text to be converted as a parameter.
    """
    def __init__(self, root) -> None:
        """
        Creates a GUI for converting the desired text

        :param root: tkinter.Tk() instance
        """
        self.root: tkinter.Tk = root
        root.title("sArCaStIc Text Converter")
        root.resizable(False, False)
        frame: tkinter.Frame = tkinter.Frame(root)
        self.text_input: tkinter.Entry = tkinter.Entry(frame, width=50)
        self.text_input.grid(row=0, column=0, sticky=tkinter.N + tkinter.S + tkinter.E + tkinter.W)
        convert: tkinter.Button = tkinter.Button(frame, text="Convert", command=self.__convert_text_gui, width=10)
        convert.grid(row=0, column=1, sticky=tkinter.N + tkinter.S + tkinter.E + tkinter.W)
        self.text_output: tkinter.Entry = tkinter.Entry(frame)
        self.text_output.grid(row=1, column=0, columnspan=2, sticky=tkinter.N + tkinter.S + tkinter.E + tkinter.W)
        frame.pack(fill="both", expand=True)
        self.text_input.focus()
        self.text_input.bind('<Return>', self.__convert_text_gui)

    # noinspection PyUnusedLocal
    def __convert_text_gui(self, click_event=None) -> None:
        converted_text: str = ''
        text: str = (self.text_input.get()).upper()
        if len(text) < 2:
            return
        for i in range(len(text)):
            converted_text += (i % 2 == 0) and text[i].lower() or text[i]
        self.text_output.delete(0, tkinter.END)
        self.text_output.insert(0, converted_text)
        print(converted_text)

    @staticmethod
    def convert_text(input_text: str) -> str:
        """
        Takes a string as a parameter and returns the string by alternatively capitalizing characters
        
        :param input_text: desired text to be converted
        
        :return: converted text
        """
        converted_text: str = ''
        text: str = input_text.upper()
        if len(text) < 2:
            return text
        for i in range(len(text)):
            converted_text += (i % 2 == 0) and text[i].lower() or text[i]
        return converted_text


if __name__ == "__main__":
    import tkinter

    window: tkinter.Tk = tkinter.Tk()
    app: SarcasticText = SarcasticText(window)
    window.mainloop()
