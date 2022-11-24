from tkinter import *
import tkinter as tk                

from PIL import Image, ImageTk
import customtkinter


class moreInfo(customtkinter.CTkFrame):
    

    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)
        self.controller = controller
        ico = Image.open('photos\ThePerfectDiet (1).ico')
        photo = ImageTk.PhotoImage(ico)
        self.controller.wm_iconphoto(False, photo)
        customtkinter.CTkFrame.configure(self,fg_color="#1B262C")

        
        
    
        button = customtkinter.CTkButton(self, text="←",text_font=("Times",25),
                            command=lambda: controller.show_frame("StartPage"))
        button.place(x=25,y=25,width=50,height=50)

        # title = customtkinter.CTkLabel(self,text='''Our Team
        #     Remeber the talened and passionate team I mentioned before ?! 
        #     Let me introduce you to our team who made such an amazing Appl :

        # ''', text_font=("Times", 16),text_color="#BBE1FA")
        # title.grid(column=0, row= 0, columnspan=5)
        welcome = customtkinter.CTkLabel(
            self,
            text='''
    Welcome to The Perfect Diet
                      
            ''',
            corner_radius=10,
            text_font=("Arial", 24)
            ,text_color="#BBE1FA"
        )
        welcome.grid(column=0, row= 0, columnspan=5)

        doc = customtkinter.CTkLabel(self,text='''The Perfect Diet Application  is introduced to make the whole process of dieting and everything
        related to it easier and all in one place so the user can find everything they want such as BMI, Calories intake per day 
        according to your body stats, finding ingredients by nutrients needed! and also finding recipes by nutrients.
        For example you can Enter your Weight, Height and you will get your body mass index so you get an idea about what is 
        your body status right now (Under Weight, Normal Weight, Over Weight Or obese) and also you can check how many calories 
        your body needs depending on your body stats and see how many calories you need to lose/keep your weight.
        Next thing you can choose what type of nutrients you want in your diet (Low/High sugar, Low/High Protein, Low/High carbs, ...etc)
        and find what type of ingredients satisfies your diet needs, on the other hand as a bonus you will be able to search for 
        recipes that include the nutrients you want.
        We want to spread Healthiness, Take care of yourselves out there and stay healthy (Believe me you will need it)!
        ''' 
        , text_font=("Times", 13),text_color="#BBE1FA")
        doc.grid(column=0, row=1, columnspan=5)

        # Read the Image
        image = Image.open("photos/Khader.png")
        # Resize the image using resize() method
        resize_image = image.resize((150, 150))
        img = ImageTk.PhotoImage(resize_image)
        # create label and add resize image
        label1 = customtkinter.CTkLabel(self,image=img)
        label1.image = img
        label1.grid(column=0, row= 2, padx=25)
        label = customtkinter.CTkLabel(self,text='''Mohammad Khader''',text_color="#BBE1FA",text_font=("Times",13))
        label.grid(column=0, row=3, padx=25)

        #---------------------------------------------
        image2 = Image.open("photos/Asad.png")
        resize_image2 = image2.resize((150, 150))
        img2 = ImageTk.PhotoImage(resize_image2)
        label2 = customtkinter.CTkLabel(self,image=img2)
        label2.image2 = img2
        label2.grid(column=1, row= 2, padx=25)
        label = customtkinter.CTkLabel(self,text='''Asad Hijawi''',text_color="#BBE1FA",text_font=("Times",13))
        label.grid(column=1, row=3, padx=25)

        #-------------------------------------------------
        image2 = Image.open("photos/Albeleisi.png")
        resize_image2 = image2.resize((150, 150))
        img2 = ImageTk.PhotoImage(resize_image2)
        label2 = customtkinter.CTkLabel(self,image=img2)
        label2.image2 = img2
        label2.grid(column=2, row= 2, padx=25)
        label = customtkinter.CTkLabel(self,text='''Mostafa Albelbeisi''',text_color="#BBE1FA",text_font=("Times",13))
        label.grid(column=2, row=3, padx=25)

        #------------------------------------
        image2 = Image.open("photos/Tareq.png")
        resize_image2 = image2.resize((150, 150))
        img2 = ImageTk.PhotoImage(resize_image2)
        label2 = customtkinter.CTkLabel(self,image=img2)
        label2.image2 = img2
        label2.grid(column=3, row= 2, padx=25)
        label = customtkinter.CTkLabel(self,text='''Tareq Al-Zoubi''',text_color="#BBE1FA",text_font=("Times",13))
        label.grid(column=3, row=3, padx=25)

        #---------------------------------------
        image2 = Image.open("photos/Hanoti.png")
        resize_image2 = image2.resize((150, 150))
        img2 = ImageTk.PhotoImage(resize_image2)
        label2 = customtkinter.CTkLabel(self,image=img2)
        label2.image2 = img2
        label2.grid(column=4, row= 2, padx=25)
        label = customtkinter.CTkLabel(self,text='''Mohammad Al-Hanoti''',text_color="#BBE1FA",text_font=("Times",13))
        label.grid(column=4, row=3, padx=25)

    


    