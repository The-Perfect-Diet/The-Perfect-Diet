import tkinter as tk  # python 3
from tkinter import font as tkfont  # python 3
from tkinter import *
from PIL import ImageTk, Image
from io import BytesIO

from tkinter import messagebox as msg
import pandastable as pt
import pandas as pd
import requests
from pandastable import Table, TableModel
import customtkinter
from PIL import Image, ImageTk





class pageTwo(customtkinter.CTkFrame):

    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)
        self.controller = controller
        ico = Image.open('photos\ThePerfectDiet (1).ico')
        photo = ImageTk.PhotoImage(ico)
        self.controller.wm_iconphoto(False, photo)
        customtkinter.CTkFrame.configure(self,fg_color="#1B262C")
        
        
        
        # Set the geometry of Tkinter frame
        #win.geometry("1000x600")

        # Define Function to print the input value
        button = customtkinter.CTkButton(self, text="🠔", text_font=("Times",25),
                            command=lambda: controller.show_frame("PageOne"),fg_color="#5F9DF7")
        button.place(x=25,y=25,width=50,height=50)

        


        def display_min_sugar():
            x = isugar.get()
            minsugar1 = minsug.get()
            query = ""
            if x == 1:
                if minsugar1 == "":
                    minsug.insert(0, 0)

                query += "minSugar=" + minsugar1 + "&"

                return query
            else:
                minsug.delete(0, END)

                return ""


        def display_max_sugar():
            x = xsugar.get()
            maxsugar1 = maxsug.get()
            query = ""
            if x == 1:
                if maxsugar1 == "":
                    maxsug.insert(0, 36)
                query += "maxSugar=" + maxsugar1 + "&"

                return query
            else:
                maxsug.delete(0, END)
                return ""


        def display_min_iron():
            x = iiron.get()
            miniron1 = miniron.get()
            query = ""
            if x == 1:
                if miniron1 == "":
                    miniron.insert(0, 8)
                query += "minIron=" + miniron1 + "&"
                return query
            else:
                miniron.delete(0, END)
                return ""


        def display_max_iron():
            x = xiron.get()
            maxiron1 = maxiron.get()
            query = ""
            if x == 1:
                if maxiron1 == "":
                    maxiron.insert(0, 15)
                query += "maxIron=" + maxiron1 + "&"
                return query
            else:
                maxiron.delete(0, END)
                return ""


        def display_min_protein():
            x = iprotein.get()
            minprotein1 = minprotein.get()
            query = ""
            if x == 1:
                if minprotein1 == "":
                    minprotein.insert(0, 15)
                query += "minProtein=" + minprotein1 + "&"
                return query
            else:
                minprotein.delete(0, END)
                return ""


        def display_max_protein():
            x = xprotein.get()
            maxprotein1 = maxprotein.get()
            query = ""
            if x == 1:
                if maxprotein1 == "":
                    maxprotein.insert(0, 40)
                query += "maxProtein=" + maxprotein1 + "&"
                return query
            else:
                maxprotein.delete(0, END)
                return ""


        def display_min_calories():
            x = icalories.get()
            mincalories1 = mincalories.get()
            query = ""
            if x == 1:
                if mincalories1 == "":
                    mincalories.insert(0, 200)
                query += "minCalories=" + mincalories1 + "&"
                return query
            else:
                mincalories.delete(0, END)
                return ""


        def display_max_calories():
            x = xcalories.get()
            maxcalories1 = maxcalories.get()
            query = ""
            if x == 1:
                if maxcalories1 == "":
                    maxcalories.insert(0, 600)
                query += "maxCalories=" + maxcalories1 + "&"
                return query
            else:
                maxcalories.delete(0, END)
                return ""


        def display_min_potassium():
            x = ipotassium.get()
            minpotassium1 = minpotassium.get()
            query = ""
            if x == 1:
                if minpotassium1 == "":
                    minpotassium.insert(0, 200)
                query += "minPotassium=" + minpotassium1 + "&"
                return query
            else:
                minpotassium.delete(0, END)
                return ""


        def display_max_potassium():
            x = xpotassium.get()
            maxpotassium1 = maxpotassium.get()
            query = ""
            if x == 1:
                if maxpotassium1 == "":
                    maxpotassium.insert(0, 900)
                query += "maxPotassium=" + maxpotassium1 + "&"
                return query
            else:
                maxpotassium.delete(0, END)
                return ""


        def display_min_sodium():
            x = isodium.get()
            minsodium1 = minsodium.get()
            query = ""
            if x == 1:
                if minsodium1 == "":
                    minsodium.insert(0, 200)
                query += "minSodium=" + minsodium1 + "&"
                return query
            else:
                minsodium.delete(0, END)
                return ""


        def display_max_sodium():
            x = xsodium.get()
            maxsodium1 = maxsodium.get()
            query = ""
            if x == 1:
                if maxsodium1 == "":
                    maxsodium.insert(0, 700)
                query += "maxSodium=" + maxsodium1 + "&"
                return query
            else:
                maxsodium.delete(0, END)
                return ""


        def display_min_fat():
            x = ifat.get()
            minfat1 = minfat.get()
            query = ""
            if x == 1:
                if minfat1 == "":
                    minfat.insert(0, 2)
                query += "minFat=" + minfat1 + "&"
                return query
            else:
                minfat.delete(0, END)
                return ""


        def display_max_fat():
            x = xfat.get()
            maxfat1 = maxfat.get()
            query = ""
            if x == 1:
                if maxfat1 == "":
                    maxfat.insert(0, 10)
                query += "maxFat=" + maxfat1 + "&"
                return query
            else:
                maxfat.delete(0, END)
                return ""


        def display_min_carbs():
            x = icarbs.get()
            mincarbs1 = mincarbs.get()
            query = ""
            if x == 1:
                if mincarbs1 == "":
                    mincarbs.insert(0, 10)
                query += "minCarbs=" + mincarbs1 + "&"
                return query
            else:
                mincarbs.delete(0, END)
                return ""


        def display_max_carbs():
            x = xcarbs.get()
            maxcarbs1 = maxcarbs.get()
            query = ""
            if x == 1:
                if maxcarbs1 == "":
                    maxcarbs.insert(0, 50)
                query += "maxCarbs=" + maxcarbs1 + "&"
                return query
            else:
                maxcarbs.delete(0, END)
                return ""


        def x():
            query = display_max_calories() + display_min_calories() + display_max_carbs() + display_min_carbs() + display_max_fat() + display_min_fat() + display_max_sodium() + display_min_sodium() + display_max_potassium() + display_min_potassium() + display_max_protein() + display_min_protein() + display_max_iron() + display_min_iron() + display_max_sugar() + display_min_sugar()

            apiKey = "9174a00b9ebd462286df99af41177363"
            urlAPi = f"https://api.spoonacular.com/recipes/findByNutrients?apiKey={apiKey}&" + query
            r = requests.get(urlAPi)
            data = r.json()
            win2 = customtkinter.CTkToplevel()
            win2.configure(fg_color="#1B262C")
            win2.title("Recipes")
            

            for i in range(len(data)):
                image = data[i]["image"]
                u = requests.get(image)
                img = Image.open(BytesIO(u.content))
                img = ImageTk.PhotoImage(img)
                panel = customtkinter.CTkLabel(win2, image=img)
                panel.image = img
                if i < 5:
                    panel.grid(row=0, column=i)
                elif i < 10:
                    panel.grid(row=6, column=i - 5)
                title = data[i]["title"]
                titlelabel = customtkinter.CTkLabel(win2, text=title,text_font=("Helvetica", 12),width=100,wraplength=200,justify="center",text_color="#BBE1FA")
                if i < 5:
                    titlelabel.grid(row=1, column=i)
                elif i < 10:
                    titlelabel.grid(row=7, column=i - 5)
                calories = data[i]["calories"]
                calorielabel = customtkinter.CTkLabel(win2, text=f"Calories: {calories}",text_font=("Helvetica", 12),text_color="#BBE1FA")
                if i < 5:
                    calorielabel.grid(row=2, column=i)
                elif i < 10:
                    calorielabel.grid(row=8, column=i - 5)
                carbs = data[i]["carbs"]
                carbslabel = customtkinter.CTkLabel(win2, text=f"Carbs: {carbs}",text_font=("Helvetica", 12),text_color="#BBE1FA")
                if i < 5:
                    carbslabel.grid(row=3, column=i)
                elif i < 10:
                    carbslabel.grid(row=9, column=i - 5)
                fat = data[i]["fat"]
                fatlabel = customtkinter.CTkLabel(win2, text=f"Fat: {fat}",text_font=("Helvetica", 12),text_color="#BBE1FA")
                if i < 5:
                    fatlabel.grid(row=4, column=i)
                elif i < 10:
                    fatlabel.grid(row=10, column=i - 5)
                protein = data[i]["protein"]
                proteinlabel = customtkinter.CTkLabel(win2, text=f"Protein: {protein}",text_font=("Helvetica", 12),text_color="#BBE1FA")
                if i < 5:
                    proteinlabel.grid(row=5, column=i)
                elif i < 10:
                    proteinlabel.grid(row=11, column=i - 5)


            





        welcome = customtkinter.CTkLabel(self, text="Recipes", text_font=("Arial", 26),text_color="#BBE1FA")
        welcome.place(x=285, y=0, width=500, height=125)
        msg = customtkinter.CTkLabel(self, text="Please Choose your Dietary Needs", text_font=("Arial", 22),text_color="#BBE1FA")
        msg.place(x=250, y=85, width=600, height=50)

        isugar = IntVar()
        min_sugar = customtkinter.CTkCheckBox(self, text="Min Sugar:", variable=isugar, onvalue=1, offvalue=0, command=display_min_sugar,text_color="#BBE1FA")
        min_sugar.place(x=125, y=150, width=150, height=30)

        xsugar = IntVar()
        max_sugar = customtkinter.CTkCheckBox(self, text="Max Sugar:", variable=xsugar, onvalue=1, offvalue=0, command=display_max_sugar,text_color="#BBE1FA")
        max_sugar.place(x=125, y=200, width=150, height=30)

        minsug = customtkinter.CTkEntry(self, text="minsugar", text_font=("Arial", 13),fg_color="#BBE1FA" )
        minsug.place(x=225, y=150, width=40, height=30)

        maxsug = customtkinter.CTkEntry(self, text="maxsugar", text_font=("Arial", 13),fg_color="#BBE1FA" )
        maxsug.place(x=225, y=200, width=40, height=30)

        icarbs = IntVar()
        min_carbs = customtkinter.CTkCheckBox(self, text="Min Carbs:", variable=icarbs, onvalue=1, offvalue=0, command=display_min_carbs,text_color="#BBE1FA")
        min_carbs.place(x=325, y=150, width=150, height=30)

        xcarbs = IntVar()
        max_carbs = customtkinter.CTkCheckBox(self, text="Max Carbs:", variable=xcarbs, onvalue=1, offvalue=0, command=display_max_carbs,text_color="#BBE1FA")
        max_carbs.place(x=325, y=200, width=150, height=30)

        mincarbs = customtkinter.CTkEntry(self, text="mincarbs", text_font=("Arial", 13),fg_color="#BBE1FA" )
        mincarbs.place(x=425, y=150, width=40, height=30)

        maxcarbs = customtkinter.CTkEntry(self, text="maxcarbs", text_font=("Arial", 13),fg_color="#BBE1FA" )
        maxcarbs.place(x=425, y=200, width=40, height=30)

        ifat = IntVar()
        min_fat = customtkinter.CTkCheckBox(self, text="Min Fat:", variable=ifat, onvalue=1, offvalue=0, command=display_min_fat,text_color="#BBE1FA")
        min_fat.place(x=515, y=150, width=150, height=30)

        xfat = IntVar()
        max_fat = customtkinter.CTkCheckBox(self, text="Max Fat:", variable=xfat, onvalue=1, offvalue=0, command=display_max_fat,text_color="#BBE1FA")
        max_fat.place(x=515, y=200, width=150, height=30)

        minfat = customtkinter.CTkEntry(self, text="minfat", text_font=("Arial", 13),fg_color="#BBE1FA" )
        minfat.place(x=600, y=150, width=40, height=30)

        maxfat = customtkinter.CTkEntry(self, text="maxfat", text_font=("Arial", 13),fg_color="#BBE1FA" )
        maxfat.place(x=600, y=200, width=40, height=30)

        isodium = IntVar()
        min_sodium = customtkinter.CTkCheckBox(self, text="Min Sodium:", variable=isodium, onvalue=1, offvalue=0, command=display_min_sodium,text_color="#BBE1FA")
        min_sodium.place(x=695, y=150, width=150, height=30)

        xsodium = IntVar()
        max_sodium = customtkinter.CTkCheckBox(self, text="Max Sodium:", variable=xsodium, onvalue=1, offvalue=0, command=display_max_sodium,text_color="#BBE1FA")
        max_sodium.place(x=695, y=200, width=150, height=30)

        minsodium = customtkinter.CTkEntry(self, text="minsodium", text_font=("Arial", 13),fg_color="#BBE1FA" )
        minsodium.place(x=805, y=150, width=40, height=30)

        maxsodium = customtkinter.CTkEntry(self, text="maxsodium", text_font=("Arial", 13),fg_color="#BBE1FA" )
        maxsodium.place(x=805, y=200, width=40, height=30)

        ipotassium = IntVar()
        min_potassium = customtkinter.CTkCheckBox(self, text="Min Potassium:", variable=ipotassium, onvalue=1, offvalue=0,
                                    command=display_min_potassium,text_color="#BBE1FA")
        min_potassium.place(x=125, y=270, width=150, height=30)

        xpotassium = IntVar()
        max_potassium = customtkinter.CTkCheckBox(self, text="Max Potassium:", variable=xpotassium, onvalue=1, offvalue=0,
                                    command=display_max_potassium,text_color="#BBE1FA")
        max_potassium.place(x=125, y=320, width=150, height=30)

        minpotassium = customtkinter.CTkEntry(self, text="minpotassium", text_font=("Arial", 13),fg_color="#BBE1FA" )
        minpotassium.place(x=250, y=270, width=40, height=30)

        maxpotassium = customtkinter.CTkEntry(self, text="maxpotassium", text_font=("Arial", 13),fg_color="#BBE1FA" )
        maxpotassium.place(x=250, y=320, width=40, height=30)

        iiron = IntVar()
        min_iron = customtkinter.CTkCheckBox(self, text="Min Iron:", variable=iiron, onvalue=1, offvalue=0, command=display_min_iron,text_color="#BBE1FA")
        min_iron.place(x=325, y=270, width=150, height=30)

        xiron = IntVar()
        max_iron = customtkinter.CTkCheckBox(self, text="Max Iron:", variable=xiron, onvalue=1, offvalue=0, command=display_max_iron,text_color="#BBE1FA")
        max_iron.place(x=325, y=320, width=150, height=30)

        miniron = customtkinter.CTkEntry(self, text="miniron", text_font=("Arial", 13), fg_color="#BBE1FA")
        miniron.place(x=415, y=270, width=40, height=30)

        maxiron = customtkinter.CTkEntry(self, text="maxiron", text_font=("Arial", 13),fg_color="#BBE1FA" )
        maxiron.place(x=415, y=320, width=40, height=30)

        iprotein = IntVar()
        min_protein = customtkinter.CTkCheckBox(self, text="Min Protein:", variable=iprotein, onvalue=1, offvalue=0,
                                command=display_min_protein,text_color="#BBE1FA")
        min_protein.place(x=515, y=270, width=150, height=30)

        xprotein = IntVar()
        max_protein = customtkinter.CTkCheckBox(self, text="Max Protein:", variable=xprotein, onvalue=1, offvalue=0,
                                command=display_max_protein,text_color="#BBE1FA")
        max_protein.place(x=515, y=320, width=150, height=30)

        minprotein = customtkinter.CTkEntry(self, text="minprotein", text_font=("Arial", 13), fg_color="#BBE1FA")
        minprotein.place(x=620, y=270, width=40, height=30)

        maxprotein = customtkinter.CTkEntry(self, text="maxprotein", text_font=("Arial", 13),fg_color="#BBE1FA" )
        maxprotein.place(x=620, y=320, width=40, height=30)

        icalories = IntVar()
        min_calories = customtkinter.CTkCheckBox(self, text="Min Calories:", variable=icalories, onvalue=1, offvalue=0,
                                command=display_min_calories,text_color="#BBE1FA")
        min_calories.place(x=695, y=270, width=150, height=30)

        xcalories = IntVar()
        max_calories = customtkinter.CTkCheckBox(self, text="Max Calories:", variable=xcalories, onvalue=1, offvalue=0,
                                command=display_max_calories,text_color="#BBE1FA")
        max_calories.place(x=695, y=320, width=150, height=30)

        mincalories = customtkinter.CTkEntry(self, text="mincalories", text_font=("Arial", 13),fg_color="#BBE1FA" )
        mincalories.place(x=810, y=270, width=40, height=30)

        maxcalories = customtkinter.CTkEntry(self, text="maxcalories", text_font=("Arial", 13),fg_color="#BBE1FA" )
        maxcalories.place(x=810, y=320, width=40, height=30)

        find_recipe_button = customtkinter.CTkButton(self, text="Find Recipe", command=x, text_font=("Arial", 20),fg_color="#5F9DF7")
        find_recipe_button.place(x=375, y=430, width=300, height=50)