from customtkinter import *
import modules.router.routers as rutas
import modules.funcionalidadBasica.funcionalidad as FunciB 

def Inicio(self):
        
        self.panelInicio = CTkFrame(
                                     self,
                                     width=500,
                                     height=550,
                                     fg_color=self.color_fondo
                                )
        
        self.panelInicio.grid(row=0, column=0)
        
        self.logoPrincipal = CTkLabel(
                                self.panelInicio,
                                text='',
                                image=CTkImage(rutas.imagenes['imagenLogo1'], size=(350, 144.25)) # 1444x657
                            )
        
        self.botonRentar = CTkButton(
                                        self.panelInicio,
                                        text = 'Rentar Habitacion',
                                        height=50,
                                        width=240,
                                        fg_color=self.color_secundario,
                                        hover_color=self.color_primario,
                                        corner_radius=20,
                                        text_color='#000',
                                        font=self.fuenteHelvetica_Botones,
                                        cursor="hand2",
                                        command= lambda: FunciB.mostrar_frame(self.Marco_Class)
                                    )
        
        self.botonMostrar = CTkButton(
                                        self.panelInicio,
                                        text = 'Mostrar Habitaciones',
                                        height=50,
                                        width=240,
                                        fg_color=self.color_secundario,
                                        hover_color=self.color_primario,
                                        corner_radius=20,
                                        text_color='#000',
                                        font=self.fuenteHelvetica_Botones,
                                        cursor="hand2"
                                    )
        
        self.botonModificar = CTkButton(
                                        self.panelInicio,
                                        text = 'Modificar/Eliminar',
                                        height=50,
                                        width=240,
                                        fg_color=self.color_secundario,
                                        hover_color=self.color_primario,
                                        corner_radius=20,
                                        text_color='#000',
                                        font=self.fuenteHelvetica_Botones,
                                        cursor="hand2"
                                    )
        
        self.decoracionInferior = CTkLabel(
                                self.panelInicio,
                                text='',
                                image=CTkImage(rutas.imagenes['imagenDecoracion'], size=(306, 48)) # 1224x192
                            )
        
        self.logoPrincipal.place(x=75, y=20)
        self.botonRentar.place(x=130, y=220)
        self.botonMostrar.place(x=130, y=300)
        self.botonModificar.place(x=130, y=380)
        self.decoracionInferior.place(x=97, y=470)