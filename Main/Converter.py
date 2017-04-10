'''
Program Name:
    Converter.py

Description:
    A program that can perform multiple conversions.
    capability to convert type decimal to binary, binary to decimal,
    binary to hexadecimal, hexadecimal to binary, and hexadecimal to decimal
'''
try:
    import Tkinter as tkinter
except ImportError as e:
    print("Import failed\n", e, "\nTrying again")
try:
    import tkinter
except ImportError as e:
    print("If This Import Failed Look at code\n", e)

class ConverterGUI(tkinter.Tk):
    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initMain()

    def initMain(self):
        self.grid()

        #     Buttons Defined----------------------------
        button_Hex_Bin = tkinter.Button(self, font=("Calibri", 16) ,text=u"Hex 2 Bin", fg="white", bg="blue" ,padx=3, pady=5 ,command=self.hex_bin)
        button_Hex_Bin.grid(column=3, row=1)
        button_Hex_Dec = tkinter.Button(self,  font=("Calibri", 16) ,text=u"Hex 2 Dec", fg="white", bg="blue" ,command=self.hex_dec)
        button_Hex_Dec.grid(column=3, row=2)
        button_Bin_Dec = tkinter.Button(self,  font=("Calibri", 16) ,text=u"Bin 2 Dec", fg="white", bg="blue" ,padx=3, pady=3 ,command=self.bin_dec)
        button_Bin_Dec.grid(column=3, row=3)
        button_Bin_Hex = tkinter.Button(self,  font=("Calibri", 16) ,text=u"Bin 2 Hex", fg="white", bg="blue" ,padx=3, pady=3 ,command=self.bin_hex)
        button_Bin_Hex.grid(column=3, row=4)
        button_Dec_Bin = tkinter.Button(self,  font=("Calibri", 16) ,text=u"Dec 2 Bin", fg="white", bg="blue" ,padx=3, pady=3 ,command=self.dec_bin)
        button_Dec_Bin.grid(column=3, row=5)
        button_Dec_Hex = tkinter.Button(self,  font=("Calibri", 16) ,text=u"Dec 2 Hex", fg="white", bg="blue" ,command=self.dec_hex)
        button_Dec_Hex.grid(column=3, row=6)

        #    Entries Defined----------------------------
        self.entryVariable = tkinter.StringVar()
        self.entry = tkinter.Entry(self, font=("Calibri", 20), textvariable=self.entryVariable)
        self.entry.grid(column=1, row=1, sticky="EW")
        self.entry.focus()

        self.entryReturned = tkinter.StringVar()
        self.entry = tkinter.Entry(self, font=("Calibri", 20) ,textvariable=self.entryReturned)
        self.entry.grid(column=0, row=3, columnspan=3, sticky='EW')

        #    Labels Defined-----------------------------
        self.convertLabel = tkinter.StringVar()
        ConvertLabel = tkinter.Label(self, textvariable=self.convertLabel, anchor="w", fg="white", bg="grey")
        ConvertLabel.grid(column=0, row=1, sticky='EW')
        self.convertLabel.set(u"Enter Value To Convert")

        # image test-------------------------------------
        # myimage = tkinter.Image(name=r"C:\Users\Fractal-LT\Vieste_Night.jpg", imgtype='image')
        # myimage.grid(column=4, row=0, columnspan=3, rowspan=3)

    def convert_to_binary(self, num):
        #for i in range(0,100,2):
        try:
            i = int(num)
            if i == 0:
                pass
            else:
                i = str(bin(i))
                i = i.split('b')
                i = i[:2]
                return i[1]
        except (TypeError, ValueError) as e:
            print()
            print(e)
            return "\nTry Again :("

    def hex_convert(self, x):
        x = x.upper()
        bi_total = ""
        binary = []
        decimal = ""
        count = 0
        try:
            hexaList = [['1', '1'],['2', '2'],['3','3'], ['4', '4'],['5', '5'],['6', '6'],['7', '7'],['8', '8'],['9', '9'],['A', '10'],['B', '11'],['C', '12'],['D', '13'],['E', '14'],['F', '15']]
            for i in hexaList:
                for j in i:

                    if x == j:
                        if count > 0:
                            break
                        else:
                            decimal = int(hexaList[hexaList.index(i)][1])
                            binary.append(self.convert_to_binary(int(decimal)))
                            if count >= 0:
                                for k in binary:
                                    if len(k) < 4:
                                        k = "0"*(4-len(k)) + k
                                bi_total += k
                        count += 1
        except TypeError as e:
            print(e)
        return bi_total

    def hex_bin(self):
        theHex = self.entryVariable.get()
        theHex = str(theHex)
        hList = []
        total = ""
        if len(theHex) > 1:
            for i in range(len(theHex)):
                hList.append(theHex[i])
        else:
            hList.append(theHex)
        for i in hList:
            if i == "0":
                total += "0000"
            else:
                total += self.hex_convert(i)
        self.entryReturned.set(total.rstrip())

    def hex_dec(self):
        theHex = self.entryVariable.get()
        self.entryReturned.set(int(theHex, 16))
    def bin_hex(self):
        decimal = self.entryVariable.get()
        decimal = int(decimal, 2)
        decimal = hex(int(decimal))
        decimal = decimal.split('x')
        hexadecimal = decimal[1]
        self.entryReturned.set(hexadecimal)
    def bin_dec(self):
        decimal = self.entryVariable.get()
        decimal = int(decimal, 2)
        self.entryReturned.set(decimal)
    def dec_hex(self):
        try:
            decimal = self.entryVariable.get()
            decimal = hex(int(decimal))
            decimal = decimal.split('x')
            self.entryReturned.set(decimal[1])
        except ValueError as e:
            self.myText.set(e)
            print(e)
    def dec_bin(self):
        try:
            decimal = self.entryVariable.get()
            i = int(decimal)
            if i == 0:
                self.entryReturned.set("00000000")
            else:
                i = str(bin(i))
                i = i.split('b')
                print(i[:2])
                self.entryReturned.set(i[1])
        except ValueError as e:
            self.entryReturned.set(e)
            print(e)

if __name__ == "__main__":
    prog = ConverterGUI(None)
    prog.title('Converter Gui')
    prog.configure(background="turquoise")
    prog.mainloop()
