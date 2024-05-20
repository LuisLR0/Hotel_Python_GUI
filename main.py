from customtkinter import *
import modules.VistaInicio.widgets as inicio
import modules.SeccionRentar.clases as clases
from bd.baseDatos import BaseDatos


class VentanaPrincipal(CTk):
    
    bd = BaseDatos()

    def __init__(self):
        super().__init__()
        
        self.geometry("500x550")
        self.resizable(0, 0)
        
        # |~~| Fuentes |~~|
        self.fuenteHelvetica_Botones = CTkFont(family="HelveticaNowText Bold", size=18)
        self.fuenteHelvetica_Texto = CTkFont(family="HelveticaNowText Bold", size=16)
        self.fuenteClarendon_Clases = CTkFont(family="Clarendon-Bold", size=22)
        self.fuenteHelveticaItalic_tipoClase = CTkFont(family="HelveticaNowText Bold", size=18, slant='italic')
        self.fuenteHelveticaBlack_Flechas = CTkFont(family="HelveticaNowText Bold", size=64)
        self.fuenteHelveticaBlack_Volver = CTkFont(family="HelveticaNowText Bold", size=40)
        
        # |~~| Paleta de Colores |~~|
        self.color_fondo = '#16223d'
        self.color_blanco = '#fcfbfc'
        self.color_primario = '#27a8ca'
        self.color_secundario = '#7ac2dc'
    
        # |~~~| Vista Principal |~~~|
        self.crear_widgets_inicio()
        
        # |~~~| Vista Rentar |~~~|
        self.SeccionRentar()
        
        self.panelInicio.tkraise()
        
    
    def crear_widgets_inicio(self):
        inicio.Inicio(self)
    
    def SeccionRentar(self):
        clases.WidgetsClases(self)
    
    def SeccionMostrar(self):
        pass
    
    def SecccionModificar(self):
        pass
        
ventana = VentanaPrincipal()

ventana.mainloop()