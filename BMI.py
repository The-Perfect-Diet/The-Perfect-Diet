import tkinter as tk
from tkinter import *
import customtkinter
from PIL import Image, ImageTk



class BMI(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)
        customtkinter.CTkFrame.configure(self,fg_color="#1B262C")
        self.controller = controller
        GEOMETRY = "1000x600"
        self.controller.geometry(GEOMETRY)
        self.controller.resizable(0,0)
        self.controller.title('The Perfect Diet')
        ico = Image.open('photos\ThePerfectDiet (1).ico')
        photo = ImageTk.PhotoImage(ico)
        self.controller.wm_iconphoto(False, photo)
        
        button = customtkinter.CTkButton(self, text="🠔", text_font=("Times",25),
                            command=lambda: controller.show_frame("StartPage"),fg_color="#5F9DF7")
        button.place(x=25, y=25, width=50, height=50)


        def getBMI():
            height = float(heightLabel.get())
            weight = float(weightLabel.get())
            bmi_long = weight/(height**2)*10000
            bmi_short = round(bmi_long,2)
            textarea = customtkinter.CTkTextbox(master = self, text_font=("Arial", 13), corner_radius=10,fg_color="#BBE1FA")
            textarea.place(x=300, y=450, width=400, height=85)
            ANSWER = "Your Body Mass Index value is {bmi}".format(bmi=bmi_short)
            textarea.insert(tk.END, ANSWER)

        title = customtkinter.CTkLabel(self, text_font=("Arial", 24), text="BMI Calculator",text_color="#BBE1FA")
        title.place(x=350, y=70, width=300, height=30)

        category = customtkinter.CTkLabel(self, text_font=("Arial", 14),text = '''  
BMI Categories:
Underweight = < 18.5
Normal weight = 18.5-24.9
Overweight = 25-29.9
Obesity greater than 30 
         ''',text_color="#BBE1FA")
        category.place(x=325, y=100, width=350, height=150)

        height = customtkinter.CTkLabel(self, text_font=("Arial", 13),text = "Enter Your Height",text_color="#BBE1FA")
        height.place(x=300, y=280, width=200, height=30)

        weight = customtkinter.CTkLabel(self, text_font=("Arial", 13), text = "Enter Your Weight",text_color="#BBE1FA")
        weight.place(x=300, y=320, width=200, height=30)

        heightLabel = customtkinter.CTkEntry(self, text="heightLabel", text_font=("Arial", 13),fg_color="#BBE1FA" )
        heightLabel.place(x=500, y=280, width=200, height=30)

        weightLabel = customtkinter.CTkEntry(self, text="weightLabel", text_font=("Arial", 13), fg_color="#BBE1FA" )
        weightLabel.place(x=500, y=320, width=200, height=30)


        button = customtkinter.CTkButton(self, text="Calculate BMI", command = getBMI, text_font=("Arial", 16),fg_color="#5F9DF7").place(x=350, y=370, width=300, height=50)