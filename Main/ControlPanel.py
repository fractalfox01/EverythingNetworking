try:
    import tkinter as tk
except (ImportError) as e:
    print(e, "\nTrying as Tkinter")
try:
    import Tkinter as tk
except (ImportError) as e:
    print(e, "\nCheck to see if tkinter/Tkinter is imported")
import os
import subprocess
import SubnetCalculation
#import _thread
#import Converter



class myProg(tk.Tk):
    def __init__(self, master):
        tk.Tk.__init__(self, master)
        self.converter_count = 0
        self.master = master
        self.main_window()

    def main_window(self):
        f = tk.Frame(self, bg="black", width=1000, height=1000)
        f.pack()
        #
        headerArea= tk.Frame(f, bg="white")
        headerArea.pack(expand=True, fill=tk.BOTH)

        global textArea
        textArea = tk.Frame(f, bg="lightgreen")
        textArea.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        global convertArea
        convertArea = tk.Frame(f, bg="lightgreen")
        convertArea.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        #convertArea.pack_forget()
        global buttonArea_sub
        buttonArea_sub = tk.Frame(f, bg="lightgreen")
        buttonArea_sub.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)
        global buttonArea_con
        buttonArea_con = tk.Frame(f, bg="lightgreen")
        buttonArea_con.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

        # Grid Details-------------------------------
        #   self.grid()

        #HEADERAREA===================================================
        # Lable Detailed headerArea---------------------------
        self.mainHeader = tk.StringVar()
        head = tk.Label(headerArea, font=("Calibri Bold",20), textvariable=self.mainHeader, bg="turquoise")
        head.grid(column=0, row=0, ipadx=145)
        mainHead = "Networking Control Panel"
        self.mainHeader.set(mainHead)

        #if self.sub_count == False:
        #CONVERTAREA================================================
        # labels Deatiled convertArea-------------------------
        self.entryVariable = tk.StringVar()
        self.entry = tk.Entry(convertArea, font=("Calibri", 15), textvariable=self.entryVariable, width=20)
        self.entry.grid(column=1, row=0, columnspan=2, padx=10)
        self.entry.focus()

        self.entryReturned = tk.StringVar()
        self.entry = tk.Entry(convertArea, font=("Calibri", 15) ,textvariable=self.entryReturned, width=20)
        self.entry.grid(column=1, row=1, columnspan=2, padx=10)

        self.convertLabel = tk.StringVar()
        ConvertLabel = tk.Label(convertArea, font=("Calibri", 15), textvariable=self.convertLabel, bg="lightgrey")
        ConvertLabel.grid(column=0, row=0)
        self.convertLabel.set(u"Enter Value To Convert")
        convertArea.pack_forget()

        #TEXTAREA=====================================================
        #Labels Detailed textArea----------------------------
        self.filler0 = tk.StringVar()
        label1 = tk.Label(textArea, textvariable=self.filler0, bg="lightgreen")
        label1.grid(column=0, row=0, ipadx=55, ipady=5)

        self.filler1 = tk.StringVar()
        label2 = tk.Label(textArea, textvariable=self.filler1, bg="lightgreen")
        label2.grid(column=2, row=0, ipadx=55, ipady=5)

        self.filler2 = tk.StringVar()
        label3 = tk.Label(textArea, textvariable=self.filler2, bg="lightgreen")
        label3.grid(column=0, row=6, columnspan=2)

        self.myLabel = tk.StringVar()
        label = tk.Label(textArea, font=("Calibri",15) ,textvariable=self.myLabel, bg="lightgreen")
        header = "Subnetted Output"
        self.myLabel.set(header)
        label.grid(column=1, row=0)

        self.label_startIP = tk.StringVar()
        lbl_startIP = tk.Label(textArea, font=("Calibri", 14), textvariable=self.label_startIP, bg="lightgrey")
        lbl_startIP.grid(column=0, row=1, ipadx=20, pady=5)
        self.label_startIP.set("Start IP")

        self.label_endIP = tk.StringVar()
        lbl_endIP = tk.Label(textArea, font=("Calibri", 14), textvariable=self.label_endIP, bg="lightgrey")
        lbl_endIP.grid(column=0, row=2, ipadx=25, pady=5)
        self.label_endIP.set("End IP")

        self.label_mask = tk.StringVar()
        lbl_mask = tk.Label(textArea, font=("Calibri", 14), textvariable=self.label_mask, bg="lightgrey")
        lbl_mask.grid(column=0, row=3, ipadx=28, pady=5)
        self.label_mask.set("Mask")

        self.label_numHosts = tk.StringVar()
        lbl_numHosts = tk.Label(textArea, font=("Calibri", 14), textvariable=self.label_numHosts, bg="lightgrey")
        lbl_numHosts.grid(column=0, row=4, ipadx=5, pady=5)
        self.label_numHosts.set("# of Hosts")

        # Entries Deatailed textArea---------------------------
        self.entry_startIP = tk.StringVar()
        self.start_IP = tk.Entry(textArea, font=("Calibri", 14), textvariable=self.entry_startIP, bd=5, relief="ridge")
        self.start_IP.grid(column=1, row=1, columnspan=2)

        self.entry_endIP = tk.StringVar()
        self.end_IP = tk.Entry(textArea, font=("Calibri", 14), textvariable=self.entry_endIP, bd=5, relief="ridge")
        self.end_IP.grid(column=1, row=2, columnspan=2)

        self.entry_mask = tk.StringVar()
        self.ent_mask = tk.Entry(textArea, font=("Calibri", 14), textvariable=self.entry_mask, bd=5, relief="ridge")
        self.ent_mask.grid(column=1, row=3, columnspan=2)

        self.entry_hosts = tk.StringVar()
        self.ent_host = tk.Entry(textArea, font=("calibri", 14), textvariable=self.entry_hosts, width=7, bd=5, relief=("ridge"))
        self.ent_host.grid(column=1, row=4, padx=20)

        #BUTTONAREA SUB===================================================
        # Buttons Detailes buttonArea_sub---------------------------
        converter = tk.Button(buttonArea_sub, text="Converter", command=self.new_converter, bg="red", bd=5, relief="raised")
        converter.grid(column=1, row=2, padx=10)
        subnet = tk.Button(buttonArea_sub, text="Subnets", command=self.new_subnet, bg="red", bd=5, relief="raised")
        subnet.grid(column=2, row=2, padx=5)
        find_Mask = tk.Button(buttonArea_sub, text="Find Mask", command=self.Mask_button_click, bg="turquoise", bd=5, relief="raised")
        find_Mask.grid(column=1, row=3, pady=5, ipadx=2)
        find_Range = tk.Button(buttonArea_sub, text="Find Range", command=self.Calculate_Range, bg="turquoise", bd=5, relief="raised")
        find_Range.grid(column=1, row=4, pady=5)
        find_host = tk.Button(buttonArea_sub, text="Find Hosts", command=self.Calculate_Hosts, bg="turquoise", bd=5, relief="raised")
        find_host.grid(column=1, row=5, pady=5, ipadx=2)

        #BUTTONAREA CON====================================================
        # Buttons Detailed buttonArea_con----------------------------
        converter = tk.Button(buttonArea_con, text="Converter", command=self.new_converter, bg="red", bd=5, relief="raised")
        converter.grid(column=1, row=0, padx=10)
        subnet = tk.Button(buttonArea_con, text="Subnets", command=self.new_subnet, bg="red", bd=5, relief="raised")
        subnet.grid(column=2, row=0, padx=5)
        button_Hex_Bin = tk.Button(buttonArea_con, text=u"Hex 2 Bin", bg="turquoise", bd=5, relief="raised", command=self.hex_bin)
        button_Hex_Bin.grid(column=1, row=1, pady=5)
        button_Hex_Dec = tk.Button(buttonArea_con, text=u"Hex 2 Dec", bg="turquoise", bd=5, relief="raised", command=self.hex_dec)
        button_Hex_Dec.grid(column=2, row=1, pady=5)
        button_Bin_Dec = tk.Button(buttonArea_con, text=u"Bin 2 Dec", bg="turquoise", bd=5, relief="raised", command=self.bin_dec)
        button_Bin_Dec.grid(column=1, row=2, pady=5)
        button_Bin_Hex = tk.Button(buttonArea_con, text=u"Bin 2 Hex", bg="turquoise", bd=5, relief="raised", command=self.bin_hex)
        button_Bin_Hex.grid(column=2, row=2, pady=5, ipadx=2)
        button_Dec_Bin = tk.Button(buttonArea_con, text=u"Dec 2 Bin", bg="turquoise", bd=5, relief="raised", command=self.dec_bin)
        button_Dec_Bin.grid(column=1, row=3, pady=5)
        button_Dec_Hex = tk.Button(buttonArea_con, text=u"Dec 2 Hex", bg="turquoise", bd=5, relief="raised", command=self.dec_hex)
        button_Dec_Hex.grid(column=2, row=3, pady=5)
        buttonArea_con.pack_forget()

    def Mask_button_click(self):
        order = ["start IP", "end IP", "hosts"]
        result = []
        r = SubnetCalculation.subnet_calculation
        result = r.verify_IP(self.entry_startIP.get(), self.entry_endIP.get(), self.entry_hosts.get())
        print(result)
        for indx in range(0, 3):
            try:
                if result[indx] != 'valid' and indx == 0:
                    self.entry_startIP.set(self.entry_startIP.get() +" invalid IP")
                    order[indx] = "1"
                    break
                if result[indx] != 'valid' and indx == 1:
                    self.entry_endIP.set(self.entry_endIP.get() + " invalid ip")
                    order[indx] = "1"
                    break
                if result[indx] != 'valid' and indx == 2:
                    self.entry_hosts.set(self.entry_hosts.get() + " invalid host")
                    order[indx] = "1"
                    break
            except TypeError as e:
                print(e)
        if "1" not in order:
            SubnetCalculation.calculateMask(self.entry_startIP.get(), self.entry_endIP.get(), self.entry_hosts.get())



    def Calculate_Range():
        pass

    def Calculate_Hosts():
        pass

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
                self.entryReturned.set(i[1])
        except ValueError as e:
            self.entryReturned.set(e)
            print(e)

    def new_converter(self):
        try:
            textArea.pack_forget()
            convertArea.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
            buttonArea_sub.pack_forget()
            buttonArea_con.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)
        except:
            pass

    def new_subnet(self):
        try:
            convertArea.pack_forget()
            textArea.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
            buttonArea_con.pack_forget()
            buttonArea_sub.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)
        except (AttributeError, NameError) as e:
            print(e)
def Calculate_Mask(fip, lip, hst):
    countnum = 0
    countdot = 0
    firstip = fip
    fip_total = len(firstip)
    lastip = lip
    lip_total = len(lastip)
    host = hst
    digits = ["1","2","3","4","5","6","7","8","9"]
    for i in firstip: # check that first ip is all numbers - 3 dots
        if i in digits:
            countnum += 1
        if i == ".":
            countdot += 1
    if fip_total != (countnum + countdot) or countdot != 3 or countnum < 4 or countnum > 12: # redo to check if right instead of wrong. (...12345) passes this test
        return "Not A Valid IP Address"
    count = 0
    for i in lastip:
        for j in digits:
            if i == str(j):
                count += 1
    if lip_total != count:
        pass # needs to return error with last ip

if __name__ == "__main__":
    prog = myProg(None)
    prog.title('Networking Control Panel')
    prog.configure(background="black", borderwidth=10)
    prog.mainloop()
