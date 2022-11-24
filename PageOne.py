import tkinter as tk
from tkinter import font as tkfont
from tkinter import *

from tkinter import messagebox as msg
import pandastable as pt
import pandas as pd
from pandastable import Table, TableModel
import customtkinter
from PIL import Image, ImageTk


class PageOne(customtkinter.CTkFrame):

    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)
        self.controller = controller
        ico = Image.open('photos\ThePerfectDiet (1).ico')
        photo = ImageTk.PhotoImage(ico)
        self.controller.wm_iconphoto(False, photo)
        customtkinter.CTkFrame.configure(self,fg_color="#1B262C")


        # Set the geometry of Tkinter frame
        # win.geometry("1000x600")

        # Define Function to print the input value
        def display_lowsuagr():
            low_sugar = var1.get()
            if low_sugar == 1:
                t9.configure(state=DISABLED)
                range1.configure(state=DISABLED)
            else:
                range1.configure(state=NORMAL)
                t9.configure(state=NORMAL)

        def display_highsugar():
            high_sugar = var9.get()

            if high_sugar == 1:
                range1.configure(state=DISABLED)
                t1.configure(state=DISABLED)
            else:
                range1.configure(state=NORMAL)
                t1.configure(state=NORMAL)

        def display_lowiron():
            low_iron = var2.get()
            if low_iron == 1:
                t10.configure(state=DISABLED)
                range4.configure(state=DISABLED)
            else:
                range4.configure(state=NORMAL)
                t10.configure(state=NORMAL)

        def display_highiron():
            high_iron = var10.get()

            if high_iron == 1:
                range4.configure(state=DISABLED)
                t2.configure(state=DISABLED)
            else:
                range4.configure(state=NORMAL)
                t2.configure(state=NORMAL)

        def display_lowprotein():
            low_protein = var3.get()
            if low_protein == 1:
                t11.configure(state=DISABLED)
                range7.configure(state=DISABLED)
            else:
                range7.configure(state=NORMAL)
                t11.configure(state=NORMAL)

        def display_highprotein():
            high_protein = var11.get()

            if high_protein == 1:
                range7.configure(state=DISABLED)
                t3.configure(state=DISABLED)
            else:
                range7.configure(state=NORMAL)
                t3.configure(state=NORMAL)

        def display_lowcalories():
            low_calories = var4.get()
            if low_calories == 1:
                t12.configure(state=DISABLED)
                range10.configure(state=DISABLED)
            else:
                range10.configure(state=NORMAL)
                t12.configure(state=NORMAL)

        def display_highcalories():
            high_calories = var12.get()
            if high_calories == 1:
                range10.configure(state=DISABLED)
                t4.configure(state=DISABLED)
            else:
                range10.configure(state=NORMAL)
                t4.configure(state=NORMAL)

        def display_lowpotass():
            low_potassium = var5.get()
            if low_potassium == 1:
                t13.configure(state=DISABLED)
                range13.configure(state=DISABLED)
            else:
                range13.configure(state=NORMAL)
                t13.configure(state=NORMAL)

        def display_highpotass():
            high_potassium = var13.get()
            if high_potassium == 1:
                range13.configure(state=DISABLED)
                t5.configure(state=DISABLED)
            else:
                range13.configure(state=NORMAL)
                t5.configure(state=NORMAL)

        def display_lowsodium():
            low_sodium = var6.get()
            if low_sodium == 1:
                t14.configure(state=DISABLED)
                range16.configure(state=DISABLED)
            else:
                range16.configure(state=NORMAL)
                t14.configure(state=NORMAL)

        def display_highsodium():
            high_sodiun = var14.get()
            if high_sodiun == 1:
                range16.configure(state=DISABLED)
                t6.configure(state=DISABLED)
            else:
                range16.configure(state=NORMAL)
                t6.configure(state=NORMAL)

        def display_lowfat():
            low_fat = var7.get()
            if low_fat == 1:
                t15.configure(state=DISABLED)
                range19.configure(state=DISABLED)
            else:
                range19.configure(state=NORMAL)
                t15.configure(state=NORMAL)

        def display_highfat():
            high_fat = var15.get()
            if high_fat == 1:
                range19.configure(state=DISABLED)
                t7.configure(state=DISABLED)
            else:
                range19.configure(state=NORMAL)
                t7.configure(state=NORMAL)

        def display_lowcarbs():
            low_carbs = var8.get()
            if low_carbs == 1:
                t16.configure(state=DISABLED)
                range22.configure(state=DISABLED)
            else:
                range22.configure(state=NORMAL)
                t16.configure(state=NORMAL)

        def display_highcarbs():
            high_carbs = var16.get()
            if high_carbs == 1:
                range22.configure(state=DISABLED)
                t8.configure(state=DISABLED)
            else:
                range22.configure(state=NORMAL)
                t8.configure(state=NORMAL)

        def display_rangesugar():
            range_one = var20.get()
            if range_one == 1:
                range2.insert("0", 5)
                range3.insert("0", 25)
                t1.configure(state=DISABLED)
                t9.configure(state=DISABLED)

            else:
                t1.configure(state=NORMAL)
                t9.configure(state=NORMAL)
                range2.delete("0", END)
                range3.delete("0", END)

        def display_rangeiron():
            range212 = var21.get()
            if range212 == 1:
                t2.configure(state=DISABLED)
                t10.configure(state=DISABLED)
                range5.insert("0", 2.1)
                range6.insert("0", 2.5)

            else:
                t2.configure(state=NORMAL)
                t10.configure(state=NORMAL)
                range5.delete("0", END)
                range6.delete("0", END)

        def display_rangeprotein():
            range222 = var22.get()
            if range222 == 1:
                range8.insert("0", 7.5)
                range9.insert("0", 20)
                t3.configure(state=DISABLED)
                t11.configure(state=DISABLED)

            else:
                t3.configure(state=NORMAL)
                t11.configure(state=NORMAL)
                range8.delete("0", END)
                range9.delete("0", END)

        def display_rangecalories():
            range232 = var23.get()
            if range232 == 1:
                range11.insert("0", 150)
                range12.insert("0", 250)
                t4.configure(state=DISABLED)
                t12.configure(state=DISABLED)

            else:
                t4.configure(state=NORMAL)
                t12.configure(state=NORMAL)
                range11.delete("0", END)
                range12.delete("0", END)

        def display_rangepotass():
            range242 = var24.get()
            if range242 == 1:
                range14.insert("0", 200)
                range15.insert("0", 220)
                t5.configure(state=DISABLED)
                t13.configure(state=DISABLED)

            else:
                t5.configure(state=NORMAL)
                t13.configure(state=NORMAL)
                range14.delete("0", END)
                range15.delete("0", END)

        def display_rangesodium():
            range25 = var25.get()
            if range25 == 1:
                range17.insert("0", 120)
                range18.insert("0", 600)
                t6.configure(state=DISABLED)
                t14.configure(state=DISABLED)

            else:
                t6.configure(state=NORMAL)
                t14.configure(state=NORMAL)
                range17.delete("0", END)
                range18.delete("0", END)

        def display_rangefat():
            range26 = var26.get()
            if range26 == 1:
                range20.insert("0", 3)
                range21.insert("0", 17)
                t7.configure(state=DISABLED)
                t15.configure(state=DISABLED)
            else:
                t7.configure(state=NORMAL)
                t15.configure(state=NORMAL)
                range20.delete("0", END)
                range21.delete("0", END)

        def display_rangecarbs():
            range27 = var27.get()
            if range27 == 1:
                range23.insert("0", 15)
                range24.insert("0", 30)
                t8.configure(state=DISABLED)
                t16.configure(state=DISABLED)

            else:
                t8.configure(state=NORMAL)
                t16.configure(state=NORMAL)
                range23.delete("0", END)
                range24.delete("0", END)

        # Define empty variables
        var1 = IntVar()
        var2 = IntVar()
        var3 = IntVar()
        var4 = IntVar()
        var5 = IntVar()
        var6 = IntVar()
        var7 = IntVar()
        var8 = IntVar()
        var9 = IntVar()
        var10 = IntVar()
        var11 = IntVar()
        var12 = IntVar()
        var13 = IntVar()
        var14 = IntVar()
        var15 = IntVar()
        var16 = IntVar()
        var20 = IntVar()
        var21 = IntVar()
        var22 = IntVar()
        var23 = IntVar()
        var24 = IntVar()
        var25 = IntVar()
        var26 = IntVar()
        var27 = IntVar()

        msg = customtkinter.CTkLabel(self, text="Please Choose your Dietary Needs", text_font=("Arial", 22),text_color="#BBE1FA")
        msg.place(x=250, y=50, width=600, height=50)

        def click():
            win = Toplevel()
            win.geometry("1000x600")
            win.title('Table app')
            
            f = Frame(win)
            f.pack(fill=BOTH, expand=1)

            df = pd.read_csv('Updated_csv.csv')
            if var1.get() == 1:
                df = df[df['Sugars, total(g)'] < 5]
            if var2.get() == 1:
                df = df[df['Iron (mg)'] < 2.1]
            if var3.get() == 1:
                df = df[df['Protein (g)'] < 7.5]

            if var4.get() == 1:
                df = df[df['Energy (kcal)'] < 150]
            if var5.get() == 1:
                df = df[df['Potassium (mg)'] < 200]
            if var6.get() == 1:
                df = df[df['Sodium (mg)'] < 120]

            if var7.get() == 1:
                df = df[df['Total Fat (g)'] < 3]
            if var8.get() == 1:
                df = df[df['Carbohydrate (g)'] < 15]
            if var9.get() == 1:
                df = df[df['Sugars, total(g)'] > 25]
            if var10.get() == 1:
                df = df[df['Iron (mg)'] > 2.5]
            if var11.get() == 1:
                df = df[df['Protein (g)'] > 20]
            if var12.get() == 1:
                df = df[df['Energy (kcal)'] > 250]
            if var13.get() == 1:
                df = df[df['Potassium (mg)'] > 220]
            if var14.get() == 1:
                df = df[df['Sodium (mg)'] > 600]
            if var15.get() == 1:
                df = df[df['Total Fat (g)'] > 17.5]
            if var16.get() == 1:
                df = df[df['Carbohydrate (g)'] > 30]
            if var20.get() == 1:
                df = df[(df['Sugars, total(g)'] > float(range2.get())) & (df['Sugars, total(g)'] < float(range3.get()))]

            if var21.get() == 1:
                df = df[(df['Iron (mg)'] > float(range5.get())) & (df['Iron (mg)'] < float(range6.get()))]

            if var22.get() == 1:
                df = df[(df['Protein (g)'] > float(range8.get())) & (df['Protein (g)'] < float(range9.get()))]

            if var23.get() == 1:
                df = df[(df['Energy (kcal)'] > float(range11.get())) & (df['Energy (kcal)'] < float(range12.get()))]

            if var24.get() == 1:
                df = df[(df['Potassium (mg)'] > float(range14.get())) & (df['Potassium (mg)'] < float(range15.get()))]

            if var25.get() == 1:
                df = df[(df['Sodium (mg)'] > float(range17.get())) & (df['Sodium (mg)'] < float(range18.get()))]

            if var26.get() == 1:
                df = df[(df['Total Fat (g)'] > float(range20.get())) & (df['Total Fat (g)'] < float(range21.get()))]

            if var27.get() == 1:
                df = df[(df['Carbohydrate (g)'] > float(range20.get())) & (df['Carbohydrate (g)'] < float(range21.get()))]

            pt = Table(f, dataframe=df, showtoolbar=True, showstatusbar=True)
            pt.show()

            win.mainloop()

        # Define a Checkbox
        t1 = customtkinter.CTkCheckBox(self, text="Low Sugar", variable=var1, onvalue=1, offvalue=0,
                                       command=display_lowsuagr,text_color="#BBE1FA")
        t1.place(x=100, y=150, width=200, height=30)

        t9 = customtkinter.CTkCheckBox(self, text="High Sugar", variable=var9, onvalue=1, offvalue=0,
                                       command=display_highsugar,text_color="#BBE1FA")
        t9.place(x=100, y=180, width=200, height=30)

        range1 = customtkinter.CTkCheckBox(self, text="Range: ", variable=var20, onvalue=1, offvalue=0,
                                           command=display_rangesugar,text_color="#BBE1FA")
        range1.place(x=100, y=210, width=200, height=30)

        range2 = customtkinter.CTkEntry(self, text="Sugar", text_font=("Arial", 13),fg_color="#BBE1FA" )
        range2.place(x=175, y=209, width=45, height=35)

        range3 = customtkinter.CTkEntry(self, text="Sugar2", text_font=("Arial", 13),fg_color="#BBE1FA" )
        range3.place(x=220, y=209, width=45, height=35)

        t2 = customtkinter.CTkCheckBox(self, text="Low Iron", variable=var2, onvalue=1, offvalue=0,
                                       command=display_lowiron,text_color="#BBE1FA")
        t2.place(x=300, y=150, width=200, height=30)

        t10 = customtkinter.CTkCheckBox(self, text="High Iron", variable=var10, onvalue=1, offvalue=0,
                                        command=display_highiron,text_color="#BBE1FA")
        t10.place(x=300, y=180, width=200, height=30)

        range4 = customtkinter.CTkCheckBox(self, text="Range: ", variable=var21, onvalue=1, offvalue=0,
                                           command=display_rangeiron,text_color="#BBE1FA")
        range4.place(x=300, y=210, width=200, height=30)

        range5 = customtkinter.CTkEntry(self, text="Iron", text_font=("Arial", 13),fg_color="#BBE1FA" )
        range5.place(x=375, y=209, width=45, height=35)

        range6 = customtkinter.CTkEntry(self, text="Iron2", text_font=("Arial", 13), fg_color="#BBE1FA")
        range6.place(x=420, y=209, width=45, height=35)

        t3 = customtkinter.CTkCheckBox(self, text="Low Protein", variable=var3, onvalue=1, offvalue=0,
                                       command=display_lowprotein,text_color="#BBE1FA")
        t3.place(x=500, y=150, width=200, height=35)

        t11 = customtkinter.CTkCheckBox(self, text="High Protein", variable=var11, onvalue=1, offvalue=0,
                                        command=display_highprotein,text_color="#BBE1FA")
        t11.place(x=500, y=180, width=200, height=30)

        range7 = customtkinter.CTkCheckBox(self, text="Range: ", variable=var22, onvalue=1, offvalue=0,
                                           command=display_rangeprotein,text_color="#BBE1FA")
        range7.place(x=500, y=210, width=200, height=30)

        range8 = customtkinter.CTkEntry(self, text="Protein", text_font=("Arial", 13), fg_color="#BBE1FA")
        range8.place(x=575, y=209, width=45, height=35)

        range9 = customtkinter.CTkEntry(self, text="Protein2", text_font=("Arial", 13), fg_color="#BBE1FA")
        range9.place(x=620, y=209, width=45, height=35)

        t4 = customtkinter.CTkCheckBox(self, text="Low Calories", variable=var4, onvalue=1, offvalue=0,
                                       command=display_lowcalories,text_color="#BBE1FA")
        t4.place(x=700, y=150, width=200, height=30)

        t12 = customtkinter.CTkCheckBox(self, text="High Calories", variable=var12, onvalue=1, offvalue=0,
                                        command=display_highcalories,text_color="#BBE1FA")
        t12.place(x=700, y=180, width=200, height=30)

        range10 = customtkinter.CTkCheckBox(self, text="Range: ", variable=var23, onvalue=1, offvalue=0,
                                            command=display_rangecalories,text_color="#BBE1FA")
        range10.place(x=700, y=210, width=200, height=30)

        range11 = customtkinter.CTkEntry(self, text="Calories", text_font=("Arial", 13), fg_color="#BBE1FA")
        range11.place(x=775, y=209, width=45, height=35)

        range12 = customtkinter.CTkEntry(self, text="Calories2", text_font=("Arial", 13), fg_color="#BBE1FA")
        range12.place(x=820, y=209, width=45, height=35)

        t5 = customtkinter.CTkCheckBox(self, text="Low Potassium", variable=var5, onvalue=1, offvalue=0,
                                       command=display_lowpotass,text_color="#BBE1FA")
        t5.place(x=100, y=300, width=200, height=30)

        t13 = customtkinter.CTkCheckBox(self, text="High Potassium", variable=var13, onvalue=1, offvalue=0,
                                        command=display_highpotass,text_color="#BBE1FA")
        t13.place(x=100, y=330, width=200, height=30)

        range13 = customtkinter.CTkCheckBox(self, text="Range: ", variable=var24, onvalue=1, offvalue=0,
                                            command=display_rangepotass,text_color="#BBE1FA")
        range13.place(x=100, y=360, width=200, height=30)

        range14 = customtkinter.CTkEntry(self, text="Potassium", text_font=("Arial", 13),fg_color="#BBE1FA" )
        range14.place(x=175, y=359, width=45, height=35)

        range15 = customtkinter.CTkEntry(self, text="Potassium2", text_font=("Arial", 13),fg_color="#BBE1FA" )
        range15.place(x=220, y=359, width=45, height=35)

        t6 = customtkinter.CTkCheckBox(self, text="Low Sodium", variable=var6, onvalue=1, offvalue=0,
                                       command=display_lowsodium,text_color="#BBE1FA")
        t6.place(x=300, y=300, width=200, height=30)

        t14 = customtkinter.CTkCheckBox(self, text="High Sodium", variable=var14, onvalue=1, offvalue=0,
                                        command=display_highsodium,text_color="#BBE1FA")
        t14.place(x=300, y=330, width=200, height=30)

        range16 = customtkinter.CTkCheckBox(self, text="Range: ", variable=var25, onvalue=1, offvalue=0,
                                            command=display_rangesodium,text_color="#BBE1FA")
        range16.place(x=300, y=360, width=200, height=30)

        range17 = customtkinter.CTkEntry(self, text="Sodium", text_font=("Arial", 13),fg_color="#BBE1FA" )
        range17.place(x=375, y=359, width=45, height=35)

        range18 = customtkinter.CTkEntry(self, text="Sodium2", text_font=("Arial", 13),fg_color="#BBE1FA" )
        range18.place(x=420, y=359, width=45, height=35)

        t7 = customtkinter.CTkCheckBox(self, text="Low Fat", variable=var7, onvalue=1, offvalue=0,
                                       command=display_lowfat,text_color="#BBE1FA")
        t7.place(x=500, y=300, width=200, height=30)

        t15 = customtkinter.CTkCheckBox(self, text="High Fat", variable=var15, onvalue=1, offvalue=0,
                                        command=display_highfat,text_color="#BBE1FA")
        t15.place(x=500, y=330, width=200, height=30)

        range19 = customtkinter.CTkCheckBox(self, text="Range: ", variable=var26, onvalue=1, offvalue=0,
                                            command=display_rangefat,text_color="#BBE1FA")
        range19.place(x=500, y=360, width=200, height=30)

        range20 = customtkinter.CTkEntry(self, text="Fat", text_font=("Arial", 13),fg_color="#BBE1FA" )
        range20.place(x=575, y=359, width=45, height=35)

        range21 = customtkinter.CTkEntry(self, text="Fat2", text_font=("Arial", 13),fg_color="#BBE1FA" )
        range21.place(x=620, y=359, width=45, height=35)

        t8 = customtkinter.CTkCheckBox(self, text="Low Carbs", variable=var8, onvalue=1, offvalue=0,
                                       command=display_lowcarbs,text_color="#BBE1FA")
        t8.place(x=700, y=300, width=200, height=30)

        t16 = customtkinter.CTkCheckBox(self, text="High Carbs", variable=var16, onvalue=1, offvalue=0,
                                        command=display_highcarbs,text_color="#BBE1FA")
        t16.place(x=700, y=330, width=200, height=30)

        range22 = customtkinter.CTkCheckBox(self, text="Range: ", variable=var27, onvalue=1, offvalue=0,
                                            command=display_rangecarbs,text_color="#BBE1FA")
        range22.place(x=700, y=360, width=200, height=30)

        range23 = customtkinter.CTkEntry(self, text="Carbs", text_font=("Arial", 13),fg_color="#BBE1FA" )
        range23.place(x=775, y=359, width=45, height=35)

        range24 = customtkinter.CTkEntry(self, text="Carbs2", text_font=("Arial", 13),fg_color="#BBE1FA" )
        range24.place(x=820, y=359, width=45, height=35)

        btn = customtkinter.CTkButton(self, text="Show My Diet", text_font=("Arial", 20), command=click,fg_color="#5F9DF7")
        btn.place(x=375, y=430, width=300, height=50)
        button = customtkinter.CTkButton(self, text="🠔", text_font=("Times", 25),
                                         command=lambda: controller.show_frame("StartPage"),fg_color="#5F9DF7")
        button.place(x=25, y=25, width=50, height=50)
        recipe_button = customtkinter.CTkButton(self, text="Recipes", text_font=("Times", 20),
                                                command=lambda: controller.show_frame("pageTwo"),fg_color="#5F9DF7")
        recipe_button.place(x=850, y=500, width=135, height=75)

    def welcome_msg(self):
        self.welcome = customtkinter.CTkLabel(self, text=f"Welcome {self.controller.user_name}", text_font=("Arial", 26))
        self.welcome.place(x=250, y=0, width=500, height=125)