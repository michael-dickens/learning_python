from tkinter import *

class GUICompIntCalc:
    def __init__(self, master):
        self.master = master
        master.title("Compound Interest Calculator")

        self.balance = 0
        self.entered_number = 0
        self.principal = 0
        self.rate = 0
        self.time = 0
        self.addition = 0

        self.balance_label_text = DoubleVar()
        self.balance_label_text.set(self.balance)
        self.balance_label = Label(master, textvariable=self.balance_label_text)

        self.label = Label(master, text="Balance:")

        #Text Entry
        vcmd = master.register(self.validate)
        self.p = Entry(master, validate="key", validatecommand=(vcmd, '%P'))

        #Buttons
        self.principal_button = Button(master, text="Principal", command=lambda: self.update('principal'))
        self.rate_button = Button(master, text="Rate", command=lambda: self.update('rate'))
        self.time_button = Button(master, text="Time", command=lambda: self.update('time'))
        self.addition_button = Button(master, text="Contribution", command=lambda: self.update('contributions'))
        self.calc_button = Button(master, text="Calculate", command=lambda: self.compIntForm(self.principal, self.rate, self.time, self.addition))

        # Calculator Layout

        self.label.grid(row=0, column=0, sticky=W)
        self.balance_label.grid(row=0, column=1, columnspan=2, sticky=E)

        self.p.grid(row=1, column=0, columnspan=3, sticky=W+E)

        self.principal_button.grid(row=1, column=1, columnspan=3, sticky=W+E)
        self.rate_button.grid(row=2, column=1, columnspan=3, sticky=W+E)
        self.time_button.grid(row=3, column=1, columnspan=3, sticky=W+E)
        self.addition_button.grid(row=4, column=1, columnspan=3, sticky=W+E)
        self.calc_button.grid(row=5, column=0, columnspan=3, sticky=W+E)

    def validate(self, new_text):
        if not new_text: # the field is being cleared
            self.entered_number = 0
            return True

        try:
            self.entered_number = float(new_text)
            return True
        except ValueError:
            return False

    def compIntForm(self, principal, rate, time, contribution):
        rate = rate/100
        balance = principal*((1+rate)**time) + contribution*(((1+rate) ** (time+1) - (1+rate))/rate)
        balance = round(balance,2)
        self.balance = balance
        self.balance_label_text.set(self.balance)

    def update(self, attribute):
        if attribute == 'principal':
            self.principal = self.entered_number
        elif attribute == 'time':
            self.time = self.entered_number
        elif attribute == 'rate':
            self.rate = self.entered_number
        else: # Contributions
            self.addition = self.entered_number

root = Tk()
root.geometry('200x150')
my_gui = GUICompIntCalc(root)
root.mainloop()