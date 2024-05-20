from customtkinter import *
from .funcionalidad.funciClass import *
import modules.router.routers as rutas
import modules.funcionalidadBasica.funcionalidad as FunciB 

marco_WidgetsClase = list()


def WidgetsClases(self):

    # Frame Principal

    self.Marco_Class = CTkFrame(
                        self,
                        width=500,
                        height=550,
                        fg_color=self.color_fondo,
                        corner_radius=0
                    )

    self.Marco_Class.grid(row=0, column=0)
    marco_WidgetsClase.append(self.Marco_Class)
    
    # Paneles Principales
        
    self.panelLogo = CTkFrame(
                                self.Marco_Class,
                                width=500,
                                height=90,
                                fg_color=self.color_fondo,
                                corner_radius=0
                            )
    
    self.panelInfo = CTkFrame(
                                self.Marco_Class,
                                width=500,
                                height=386,
                                fg_color=self.color_fondo,
                                corner_radius=0
                            )
    
    self.panelButtons = CTkFrame(
                                self.Marco_Class,
                                width=500,
                                height=75,
                                fg_color=self.color_fondo,
                                corner_radius=0
                            )

    self.panelLogo.grid(row=0, column=0)
    self.panelInfo.grid(row=1, column=0)
    self.panelButtons.grid(row=2, column=0)
    
    # Widgets 35px = 1cm
    
    # Logo
    self.LogoSecundario = CTkLabel(
                                    self.panelLogo,
                                    text='',
                                    image=CTkImage(rutas.imagenes['imagenLogo2'], size=(281.75, 68.25)) # 1127x273
                                )
    
    self.flechaVolver = CTkButton(
                                        self.panelLogo,
                                        text='<',
                                        font=self.fuenteHelveticaBlack_Volver,
                                        width=0,
                                        fg_color='transparent',
                                        hover=False,
                                        text_color=self.color_primario,
                                        cursor="hand2",
                                        command= lambda: FunciB.mostrar_frame(self.panelInicio)
                                    )
    
    #info
    self.nameClase = CTkLabel(
                                self.panelInfo,
                                text='Clase A',
                                font=self.fuenteClarendon_Clases,
                                text_color=self.color_blanco,
                                width=112
                            )
    
    
    
    self.tipoClase = CTkLabel(
                                self.panelInfo,
                                text='Deluxe',
                                font=self.fuenteHelveticaItalic_tipoClase,
                                text_color=self.color_blanco,
                                width=112
                            )
    
    self.iconHouse = CTkLabel(
                                self.panelInfo,
                                text='',
                                image=CTkImage(rutas.imagenes['imagenIconHouse'], size=(85, 80.25))
                            )
    
    mostrarDetallesHabitacion(self, posi_class)
    
    self.iconFurniture = CTkLabel(
                                self.panelInfo,
                                text='',
                                image=CTkImage(rutas.imagenes['imagenIconFurniture'], size=(85, 80.25))
                            )
    
    mostrarFurnitureHabitacion(self, posi_class)
    
    self.textServicios = CTkLabel(
                                self.panelInfo,
                                text='Servicios e Instalaciones',
                                font=self.fuenteClarendon_Clases,
                                text_color=self.color_primario,
                                width=370
                            )
    
    mostrarServiciosHabitacion(self, posi_class)

    
    # Botones
    
    self.flechaIzquierda = CTkButton(
                                        self.panelButtons,
                                        text='<',
                                        font=self.fuenteHelveticaBlack_Flechas,
                                        width=0,
                                        fg_color='transparent',
                                        hover=False,
                                        text_color=self.color_primario,
                                        cursor="hand2",
                                        command= lambda: flechaFunci(self, 'restar')
                                    )
    
    self.flechaDerecha = CTkButton(
                                        self.panelButtons,
                                        text='>',
                                        font=self.fuenteHelveticaBlack_Flechas,
                                        width=0,
                                        fg_color='transparent',
                                        hover=False,
                                        text_color=self.color_primario,
                                        cursor="hand2",
                                        command= lambda: flechaFunci(self, 'sumar')
                                    )
    
    self.botonRentar = CTkButton(
                                    self.panelButtons,
                                    text = 'Rentar',
                                    height=50,
                                    width=240,
                                    fg_color=self.color_secundario,
                                    hover_color=self.color_primario,
                                    corner_radius=20,
                                    text_color=self.color_fondo,
                                    font=self.fuenteHelvetica_Botones,
                                    cursor="hand2"
                                )
    
    
    self.LogoSecundario.place(x=109.125, y=18)
    self.flechaVolver.place(x=10, y=0)
    
    self.nameClase.place(x=194, y=1)
    self.tipoClase.place(x=194, y=28)
    
    self.iconHouse.place(x=45, y=75)
    
    self.iconFurniture.place(x=270, y=75)
    
    self.textServicios.place(x=65.5, y=190)
    
    self.flechaIzquierda.place(x=50, y=-20)
    self.flechaDerecha.place(x=150, y=-20)
    self.botonRentar.place(x=240, y=10)