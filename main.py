

from tkinter import *
from tkinter import ttk
from tkinter import font as tkfont
import customtkinter
from PIL import Image, ImageTk
from BMI import BMI
from kcal import kcal
from PageOne import PageOne
from pageTwo import pageTwo
from MoreInfo import moreInfo


class SampleApp(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        customtkinter.CTk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(
            family="Helvetica", size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = customtkinter.CTkFrame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, pageTwo, BMI, kcal, moreInfo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame


            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        """Show a frame for the given page name"""
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)
        self.controller = controller
        GEOMETRY = "1000x600"
        ico = Image.open("photos\ThePerfectDiet (1).ico")
        photo = ImageTk.PhotoImage(ico)
        self.controller.wm_iconphoto(False, photo)
        self.controller.geometry(GEOMETRY)
        self.controller.resizable(0, 0)
        self.controller.title("The Perfect Diet")
        customtkinter.CTkFrame.configure(self,fg_color="#1B262C")


        image2 = Image.open("photos\BGDiet1.png")
        resize_image2 = image2.resize((400, 130))
        img2 = ImageTk.PhotoImage(resize_image2)
        label2 = customtkinter.CTkLabel(self,image=img2)
        label2.image2 = img2
        label2.place(x=300,y=25)
        


        welcome = customtkinter.CTkLabel(
            self,
            text='''Welcome to The Perfect Diet''',
            corner_radius=10,
            text_font=("Arial", 24)
            ,text_color="#BBE1FA"
        )
        welcome.place(x=250, y=175, width=500, height=75)
        # sub = customtkinter.CTkLabel(
        #     self, text="",text_color="#BBE1FA"
        # )
        # sub.place(x=250, y=150, width=500, height=66)

        stary_button = customtkinter.CTkButton(
            self,
            text="Find The Perfect Diet",
            command=lambda: controller.show_frame("PageOne"),
            corner_radius=10,
            text_font=("Arial", 15),
            fg_color="#5F9DF7"
        )
        stary_button.place(x=350, y=250, width=300, height=50)
        BMI_button = customtkinter.CTkButton(
            self,
            text="BMI Calculator",
            command=lambda: controller.show_frame("BMI"),
            corner_radius=10,
            text_font=("Arial", 15),
            fg_color="#5F9DF7"
        )
        BMI_button.place(x=350, y=325, width=300, height=50)

        kcal_button = customtkinter.CTkButton(
            self,
            text="Daily Calorie Intake Calculator",
            command=lambda: controller.show_frame("kcal"),
            corner_radius=10,
            text_font=("Arial", 15),
            fg_color="#5F9DF7"
        )
        kcal_button.place(x=350, y=400, width=300, height=50)

        moreInfo_button = customtkinter.CTkButton(
            self,
            text="More Info",
            command=lambda: controller.show_frame("moreInfo"),
            corner_radius=10,
            text_font=("Arial", 15),
            fg_color="#5F9DF7"
        )
        moreInfo_button.place(x=350, y=475, width=300, height=50)


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
