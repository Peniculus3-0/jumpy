import customtkinter
import tkinter
import math
import time
from PIL import Image, ImageTk
import os

# La classe animation comprend tout ce qui est relié à l'animation et est appelé dans le code du UI
class Animation(customtkinter.CTkFrame):
   def __init__(self, *args, header_name="Animation",**kwargs):
        super().__init__(*args, **kwargs)

        # Définition du nombre d'images par seconde des animation
        self.fps_idle = 500
        self.fps_jump = 500

        # Définition du booléen pour gérer les fils d'exécution
        self.bool = 0

        # Définition du nombre d'images dans chaque animation
        self.num_frames_jump = 480
        self.num_frames_idle = 1140

        # Dimensions en pixel des images (même pour les deux)
        self.size_x = 550
        self.size_y = 550

        # Paramètres pour trouver le dossier où sont les images
        self.frame_prefix_idle = "idle-"
        self.frame_prefix_jump = "jump-"
        self.folder_name = "C:\\git\\jumpy\\SolidWorksAnimation\\"
        self.frame_type = "000"
        self.header_name = header_name

        # Les deux prochaines boucles collectent et emmagasinent les images dans chacun de leur dictionnaire pour améliorer les performances

        self.frames = {}

        for i in range(1,self.num_frames_jump + 1):

            if i <= 9:
                self.frame_type = "000"
            elif i <= 99 and i >= 10:
                self.frame_type = "00"
            elif i >= 100 and i <= 999:
                self.frame_type = 0
            elif i >= 1000:
                self.frame_type = ''

            filename = os.path.join(f"{self.folder_name}{self.frame_prefix_jump}{self.frame_type}{i}.png")
            image = Image.open(filename).resize((self.size_x, self.size_y), resample=Image.LANCZOS)
            self.frames[i] = ImageTk.PhotoImage(image)

        print("idle images are loaded")

        for i in range(1, self.num_frames_idle + 1):

            if i <= 9:
                self.frame_type = "000"
            elif i <= 99 and i >= 10:
                self.frame_type = "00"
            elif i >= 100 and i <= 999:
                self.frame_type = 0
            elif i >= 1000:
                self.frame_type = ''

            filename = os.path.join(f"{self.folder_name}{self.frame_prefix_idle}{self.frame_type}{i}.png")
            image = Image.open(filename).resize((self.size_x, self.size_y), resample=Image.LANCZOS)
            self.frames[i + self.num_frames_jump] = ImageTk.PhotoImage(image)

        print("jump images are loaded")

        # Initialise la première image de la première animation dans le label customtkinter

        self.frame_type = "000"
        self.frame_num = 1
        self.canvas = customtkinter.CTkLabel(self, image=customtkinter.CTkImage(Image.open(os.path.join(f"{self.folder_name}{self.frame_prefix_idle}{self.frame_type}{self.frame_num}.png")), size=(self.size_x, self.size_y)))
        self.canvas.configure(text="")
        self.canvas.grid(row=0, column=0, padx=10, pady=10)

   # Permet de changer la valeur booléenne dans le code du UI
   def boolean(self):
       self.bool = 1

   # Permet de changer la valeur booléenne dans le code du UI
   def boolean_false(self):
       self.bool = 0

   # S'occupe du traitement de l'animation au repos
   def idle(self):

       fps = self.fps_idle
       num_frames = self.num_frames_idle

       i = 1
       while 1:

           if i > self.num_frames_idle:
               i = 1

           new_tk_image = self.frames[i + self.num_frames_jump]
           self.canvas.configure(image=new_tk_image)
           self.canvas.image = new_tk_image

           # Attend le bon délais entre deux images
           self.canvas.after(int(1000 / fps))
           i += 1

           # Changement d'animation
           if self.bool == 1:
               break

   # S'occupe du traitement de l'animation de saut
   def jump(self):

       fps = self.fps_jump
       num_frames = self.num_frames_jump

       for i in range(1, num_frames):
           new_tk_image = self.frames[i]
           self.canvas.configure(image=new_tk_image)
           self.canvas.image = new_tk_image
           self.canvas.after(int(1000 / fps))

       # Retour à l'animation de repos
       Animation.idle(self)