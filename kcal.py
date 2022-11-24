import tkinter as tk
from tkinter import *
import customtkinter
from PIL import Image, ImageTk


class kcal(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)
        customtkinter.CTkFrame.configure(self,fg_color="#1B262C")
        self.controller = controller
        var0 = IntVar()
        var00 = IntVar()
        button = customtkinter.CTkButton(self, text="🠔", text_font=("Times",25),
                            command=lambda: controller.show_frame("StartPage"))
        button.place(x=25,y=25,width=50,height=50)
        ico = Image.open('photos\ThePerfectDiet (1).ico')
        photo = ImageTk.PhotoImage(ico)
        self.controller.wm_iconphoto(False, photo)
        def getCaloricNeeds():
            height = float(height_Label.get())
            weight = float(weight_Label.get())
            age = float(age_Label.get())
            male = var0.get()
            female =var00.get()
            if male == 1:
                caloric_men = 66.47 + (13.75 * weight) + (5.003 * height) - (6.755 * age)
                caloric_men2 = round(caloric_men,2)
                textarea = customtkinter.CTkTextbox(master = self,text_font=("Arial", 13),corner_radius=10,fg_color="#BBE1FA")
                textarea.place(x=300,y=450,width=400,height=85)
                ANSWER = "Your Daily Calorie Intake should be {calc} KCAL".format(calc=caloric_men2)
                textarea.insert(tk.END, ANSWER)
            if female == 1:
                caloric_women = 655.1 + (9.563 * weight) + (1.850 * height) - (4.676 * age)
                caloric_women2 = round(caloric_women,2)
                textarea = customtkinter.CTkTextbox(master = self,text_font=("Arial", 13),corner_radius=10,fg_color="#BBE1FA")
                textarea.place(x=300,y=450,width=400,height=85)
                ANSWER = "Your Daily Calorie Intake should be {calc} KCAL".format(calc=caloric_women2)
                textarea.insert(tk.END, ANSWER)
        def malefunc():
            if var0.get() == 1:
                female1.configure(state=DISABLED)
            else:
                female1.configure(state=NORMAL)
        def femalefunc():
            if var00.get() == 1:
                male1.configure(state=DISABLED)
            else:
                male1.configure(state=NORMAL)
        calorie_title = customtkinter.CTkLabel(self, text_font=("Arial", 24),text = "Daily Calorie Intake",text_color="#BBE1FA")
        calorie_title.place(x=350,y=70,width=300,height=30)

        male1 = customtkinter.CTkCheckBox(self, text_font=("Arial", 13),text="Male",variable=var0, onvalue=1, offvalue=0, command=malefunc,text_color="#BBE1FA")
        male1.place(x=400,y=150,width=200,height=30)

        female1 = customtkinter.CTkCheckBox(self, text_font=("Arial", 13),text="Female",variable=var00, onvalue=1, offvalue=0, command=femalefunc,text_color="#BBE1FA")
        female1.place(x=500,y=150,width=200,height=30)

        height = customtkinter.CTkLabel(self, text_font=("Arial", 13),text = "Enter Your Height",text_color="#BBE1FA")
        height.place(x=300,y=200,width=200,height=30)

        weight = customtkinter.CTkLabel(self, text_font=("Arial", 13),text = "Enter Your Weight",text_color="#BBE1FA")
        weight.place(x=300,y=250,width=200,height=30)

        age = customtkinter.CTkLabel(self, text_font=("Arial", 13),text="What is your age?",text_color="#BBE1FA")
        age.place(x=300,y=300,width=200,height=30)


        height_Label = customtkinter.CTkEntry(self, text_font=("Arial", 13),fg_color="#BBE1FA")
        height_Label.place(x=500,y=200,width=200,height=30)

        weight_Label = customtkinter.CTkEntry(self, text_font=("Arial", 13),fg_color="#BBE1FA")
        weight_Label.place(x=500,y=250,width=200,height=30)

        age_Label = customtkinter.CTkEntry(self, text_font=("Arial", 13),fg_color="#BBE1FA")
        age_Label.place(x=500,y=300,width=200,height=30)


        button = customtkinter.CTkButton(self, text="Calculate Daily Calorie Intake", command = getCaloricNeeds,text_font=("Arial",16))
        button.place(x=350,y=375,width=300,height=50)


        