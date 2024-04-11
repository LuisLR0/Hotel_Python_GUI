from customtkinter import *
from components.widgets import *


class VentanaPrincipal(CTk):

    def __init__(self):
        super().__init__()
        
        self.geometry("500x550")
        self.resizable(0, 0)
        
        # |~~| Fuentes |~~|
        self.fuenteHelvetica_Botones = CTkFont(family="HelveticaNowText Bold", size=18)
        
        # |~~| Paleta de Colores |~~|
        self.color_fondo = '#16233c'
        self.color_primario = '#27a8ca'
        self.color_secundario = '#7ac2dc'
    
        # |~~~| Vista Principal |~~~|
        self.widgets_inicio = [] # Lista donde se guardan los widgets creados del Inicio FUTURO
        self.v_principal = True # FUTURO
        self.crear_widgets_inicio()
        
    
    def crear_widgets_inicio(self):
        Inicio(self)
    
    def SeccionRentar(self):
        pass
    
    def SeccionMostrar(self):
        pass
    
    def SecccionModificar(self):
        pass
        
        
ventana = VentanaPrincipal()

ventana.mainloop()