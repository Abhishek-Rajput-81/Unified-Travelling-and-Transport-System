import tkinter
import tkinter.messagebox
import customtkinter
from PIL import Image, ImageTk
import os
from tkinter import PhotoImage
import random
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter import simpledialog
import mysql.connector
import PIL
from PIL import ImageTk,Image





window8 = customtkinter.CTk()
customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("blue") 

class Route(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Route Information Page")
        self.geometry(f"{1100}x{700}")


      
        travel_vehicle = os.environ['TRAVEL_VEHICLE']


        self.sidebar_frame0 = customtkinter.CTkFrame(self, width=100,height=30, corner_radius=0) 
        self.sidebar_frame0.grid(row=0, column=10, rowspan=10)
        self.sidebar_frame0.grid_rowconfigure(8, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame0, text="Available "+travel_vehicle, font=customtkinter.CTkFont(size=30, weight="bold"))
        self.logo_label.grid(row=0, column=15, padx=150, pady=20)
        
        Number_of_train = os.environ['NUMBER_OF_TRAIN']
        global f1
        global f2
        global rawa1
        global rawc1
        global new_Train1_fare
        global new_Train2_fare
        f1 = os.environ['F1']
        f2 = os.environ['F2']
        rawa = os.environ['RAWA']
        rawc = os.environ['RAWC']

        rawa1 = int(rawa)
        rawc1 = int(rawc)
          
        if int(Number_of_train) == 2:
          Train1_PNR = os.environ['TRAIN1_PNR'] 
          Train1_Name = os.environ['TRAIN1_NAME'] 
          Train1_dur = os.environ['TRAIN1_DUR'] 
          Train1_type = os.environ['TRAIN1_TYPE'] 
          Train1_cap = os.environ['TRAIN1_CAP'] 
          # global Train1_fare
          Train1_fare = os.environ['TRAIN1_FARE'] 
          new_Train1_fare = Train1_fare
  
          Train2_PNR = os.environ['TRAIN2_PNR'] 
          Train2_Name = os.environ['TRAIN2_NAME'] 
          Train2_dur = os.environ['TRAIN2_DUR'] 
          Train2_type = os.environ['TRAIN2_TYPE'] 
          Train2_cap = os.environ['TRAIN2_CAP'] 
          # global Train2_fare
          Train2_fare = os.environ['TRAIN2_FARE'] 
          new_Trai2_fare = Train2_fare
  
  
          self.sidebar_frame1=customtkinter.CTkFrame(self,width=200,height=100)
          self.sidebar_frame1.grid(row=15,column=10,rowspan=25, padx=20, pady=10)
  
          self.vehicle_id_1 = customtkinter.CTkLabel(self.sidebar_frame1, text="Train ID = "+Train1_PNR,font=customtkinter.CTkFont(size=20),anchor="w")
          self.vehicle_id_1.grid(row=15, column=15, padx=100, pady=10)
          self.vehicle_name_1 = customtkinter.CTkLabel(self.sidebar_frame1, text="Train Name = "+Train1_Name,font=customtkinter.CTkFont(size=20),anchor="w")
          self.vehicle_name_1.grid(row=16, column=15, padx=100, pady=10)
  
          self.source_1 = customtkinter.CTkLabel(self.sidebar_frame1, text="From = "+f1,font=customtkinter.CTkFont(size=20),anchor="w")
          self.source_1.grid(row=15, column=16, padx=100, pady=10)
          self.destination_1 = customtkinter.CTkLabel(self.sidebar_frame1, text="To = "+f2,font=customtkinter.CTkFont(size=20),anchor="w")
          self.destination_1.grid(row=16, column=16, padx=100, pady=10)
  
          self.duration_1 = customtkinter.CTkLabel(self.sidebar_frame1, text="Duration = "+Train1_dur,font=customtkinter.CTkFont(size=20),anchor="w")
          self.duration_1.grid(row=17, column=16, padx=100, pady=10)
          self.vehicle_type_1 = customtkinter.CTkLabel(self.sidebar_frame1, text="Type = "+Train1_type,font=customtkinter.CTkFont(size=20),anchor="w")
          self.vehicle_type_1.grid(row=18, column=16, padx=100, pady=10)
          self.fare_1 = customtkinter.CTkLabel(self.sidebar_frame1, text="Fare = "+Train1_fare,font=customtkinter.CTkFont(size=20),anchor="w")
          self.fare_1.grid(row=19, column=16, padx=100, pady=10)
  
          self.continue_button = customtkinter.CTkButton(self.sidebar_frame1,text="Book",command=self.Book1)
          self.continue_button.grid(row=16, column=17,rowspan=100, padx=20, pady=(10,10))
  
  
  
  
           
          self.sidebar_frame2=customtkinter.CTkFrame(self,width=200,height=100)
          self.sidebar_frame2.grid(row=40,column=10,rowspan=20, padx=20, pady=10)
  
          self.vehicle_id_2 = customtkinter.CTkLabel(self.sidebar_frame2, text="Train ID = "+Train2_PNR,font=customtkinter.CTkFont(size=20),anchor="w")
          self.vehicle_id_2.grid(row=41, column=15, padx=100, pady=10)
          self.vehicle_name_2 = customtkinter.CTkLabel(self.sidebar_frame2, text="Train Name = "+Train2_Name,font=customtkinter.CTkFont(size=20),anchor="w")
          self.vehicle_name_2.grid(row=42, column=15, padx=100, pady=10)
  
          self.source_2 = customtkinter.CTkLabel(self.sidebar_frame2, text="From = "+f1,font=customtkinter.CTkFont(size=20),anchor="w")
          self.source_2.grid(row=41, column=16, padx=100, pady=10)
          self.destination_2 = customtkinter.CTkLabel(self.sidebar_frame2, text="To = "+f2,font=customtkinter.CTkFont(size=20),anchor="w")
          self.destination_2.grid(row=42, column=16, padx=100, pady=10)
  
          self.duration_2 = customtkinter.CTkLabel(self.sidebar_frame2, text="Duration = "+Train2_dur,font=customtkinter.CTkFont(size=20),anchor="w")
          self.duration_2.grid(row=43, column=16, padx=100, pady=10)
          self.vehicle_type_2 = customtkinter.CTkLabel(self.sidebar_frame2, text="Type = "+Train2_type,font=customtkinter.CTkFont(size=20),anchor="w")
          self.vehicle_type_2.grid(row=44, column=16, padx=100, pady=10)
          self.fare_2 = customtkinter.CTkLabel(self.sidebar_frame2, text="Fare = "+Train2_fare,font=customtkinter.CTkFont(size=20),anchor="w")
          self.fare_2.grid(row=45, column=16, padx=100, pady=10)
  
          self.continue_button = customtkinter.CTkButton(self.sidebar_frame2,text="Book",command = self.Book2)
          self.continue_button.grid(row=42, column=17,rowspan=100, padx=20, pady=(10,10))
        else:
          Train1_PNR = os.environ['TRAIN1_PNR'] 
          Train1_Name = os.environ['TRAIN1_NAME'] 
          Train1_dur = os.environ['TRAIN1_DUR'] 
          Train1_type = os.environ['TRAIN1_TYPE'] 
          Train1_cap = os.environ['TRAIN1_CAP'] 
          # global Train1_fare
          Train1_fare = os.environ['TRAIN1_FARE'] 
          new_Train1_fare = Train1_fare

          self.sidebar_frame1=customtkinter.CTkFrame(self,width=200,height=100)
          self.sidebar_frame1.grid(row=15,column=10,rowspan=25, padx=20, pady=10)
  
          self.vehicle_id_1 = customtkinter.CTkLabel(self.sidebar_frame1, text="Train ID = "+Train1_PNR,font=customtkinter.CTkFont(size=20),anchor="w")
          self.vehicle_id_1.grid(row=15, column=15, padx=100, pady=10)
          self.vehicle_name_1 = customtkinter.CTkLabel(self.sidebar_frame1, text="Train Name = "+Train1_Name,font=customtkinter.CTkFont(size=20),anchor="w")
          self.vehicle_name_1.grid(row=16, column=15, padx=100, pady=10)
  
          self.source_1 = customtkinter.CTkLabel(self.sidebar_frame1, text="From = "+f1,font=customtkinter.CTkFont(size=20),anchor="w")
          self.source_1.grid(row=15, column=16, padx=100, pady=10)
          self.destination_1 = customtkinter.CTkLabel(self.sidebar_frame1, text="To = "+f2,font=customtkinter.CTkFont(size=20),anchor="w")
          self.destination_1.grid(row=16, column=16, padx=100, pady=10)
  
          self.duration_1 = customtkinter.CTkLabel(self.sidebar_frame1, text="Duration = "+Train1_dur,font=customtkinter.CTkFont(size=20),anchor="w")
          self.duration_1.grid(row=17, column=16, padx=100, pady=10)
          self.vehicle_type_1 = customtkinter.CTkLabel(self.sidebar_frame1, text="Type = "+Train1_type,font=customtkinter.CTkFont(size=20),anchor="w")
          self.vehicle_type_1.grid(row=18, column=16, padx=100, pady=10)
          self.fare_1 = customtkinter.CTkLabel(self.sidebar_frame1, text="Fare = "+Train1_fare,font=customtkinter.CTkFont(size=20),anchor="w")
          self.fare_1.grid(row=19, column=16, padx=100, pady=10)
  
          self.continue_button = customtkinter.CTkButton(self.sidebar_frame1,text="Book")
          self.continue_button.grid(row=16, column=17,rowspan=100, padx=20, pady=(10,10))
  
    def Book1(self):
      self.destroy()
      total_fare = int(new_Train1_fare*rawa1 + (new_Train1_fare/2)*rawc1)
      result = f"Your ticket has been booked\nFrom : {f1}\nTo : {f2}\nNumber of Adults : {rawa1}\nNumber of Adults : {rawc1}\nAmount : {total_fare}"

      conformation = customtkinter.CTkToplevel(self)
      conformation.title("Ticket Conformation Window")
      conformation.geometry("600*400")

      self.sidebar_frame0 = customtkinter.CTkFrame(conformation, width=30,height=5, corner_radius=0) 
      self.sidebar_frame0.grid(row=0, column=10, rowspan=10)
      self.sidebar_frame0.grid_rowconfigure(8, weight=1)
      self.logo_label = customtkinter.CTkLabel(self.sidebar_frame0, text=result, font=customtkinter.CTkFont(size=20))
      self.logo_label.grid(row=0, column=0, padx=30, pady=15)

       
    def Book2(self):
      self.destroy()
      total_fare = int(new_Train2_fare*rawa1 + (new_Train2_fare/2)*rawc1)
      result = f"Your ticket has been booked\nFrom : {f1}\nTo : {f2}\nNumber of Adults : {rawa1}\nNumber of Adults : {rawc1}\nAmount : {total_fare}"
      

      conformation = customtkinter.CTkToplevel(self)
      conformation.title("Ticket Conformation Window")
      conformation.geometry("600*800")

      self.sidebar_frame0 = customtkinter.CTkFrame(conformation, width=30,height=5, corner_radius=0) 
      self.sidebar_frame0.grid(row=0, column=10, rowspan=10)
      self.sidebar_frame0.grid_rowconfigure(8, weight=1)
      self.logo_label = customtkinter.CTkLabel(self.sidebar_frame0, text=result, font=customtkinter.CTkFont(size=20))
      self.logo_label.grid(row=0, column=0, padx=30, pady=15)  



   


if __name__ == "__main__":
    app7 = Route()
    app7.mainloop()
