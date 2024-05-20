from customtkinter import *

posi_class = 1
widgets_detalles = list()
widgets_furniture = list()
widgets_servicios = list()

def flechaFunci(self, Sumar_o_Restar):
    
    global posi_class
    
    if Sumar_o_Restar == 'sumar':
        posi_class += 1
    elif Sumar_o_Restar == 'restar':
        posi_class -= 1
    
    if posi_class < 1:
        posi_class = 3
    elif posi_class > 3:
        posi_class = 1
    
    LimpiarWidgets(self)
    
    nombreClase(self, posi_class)
    mostrarDetallesHabitacion(self, posi_class)
    mostrarFurnitureHabitacion(self, posi_class)
    mostrarServiciosHabitacion(self, posi_class)
    
    
    
def LimpiarWidgets(self):
    
    for i in range(len(widgets_detalles)):
        widgets_detalles[i].place_forget()
    
    for i in range(len(widgets_furniture)):
        widgets_furniture[i].place_forget()
    
    for i in range(len(widgets_servicios)):
        widgets_servicios[i].place_forget()
    

def nombreClase(self, idClase):
    
    sqlNameClass = f"""
        SELECT clase, tipo FROM Clases
        WHERE id_clase = {idClase};
    """
    
    datosClass = self.bd.consulta(sqlNameClass).fetchone()
    
    self.nameClase.configure(text=f'{datosClass[0]}')
    self.tipoClase.configure(text=f'{datosClass[1]}')


# |~~~| Mostrar detalles Habitacion |~~~|

def mostrarDetallesHabitacion(self, idClase):
    
    sqlDetalles = f"""
        SELECT tamaño_habitacion, ocupacion_maxima FROM Habitaciones
        WHERE id_clase = {idClase}
        LIMIT 1;
    """
    
    detalles = self.bd.consulta(sqlDetalles).fetchone()
    info_detalle = ['m²', 'Personas']
    y_detalle = 95
    
    for i in range(len(detalles)):
        self.infoRoom = CTkLabel(
                                self.panelInfo,
                                text='',
                                font=self.fuenteHelvetica_Texto,
                                text_color=self.color_blanco,
                                width=90,
                                height=0
                            )
        
        widgets_detalles.append(self.infoRoom)
        
        widgets_detalles[i].configure(text=f'{detalles[i]} {info_detalle[i]}')
        widgets_detalles[i].place(x=150, y=y_detalle)
        y_detalle += 20
    
    
    
def mostrarFurnitureHabitacion(self, idClase):
    
    sqlInfo = f"""
        SELECT cuartos, baños,
        CASE
            WHEN terraza = 1 THEN 'Terraza'
        END,
        CASE
            WHEN cocina = 1 THEN 'Cocina'
        END
        FROM Clase_Distribucion
        WHERE id_clase = {idClase};
    """
    
    informacion = self.bd.consulta(sqlInfo).fetchone()
    
    # Modificar los textos según el valor obtenido
    habitaciones_texto = 'Habitación' if informacion[0] == 1 else 'Habitaciones'
    baños_texto = 'Baño' if informacion[1] == 1 else 'Baños'
    
    info_forniture = [f'{informacion[0]} {habitaciones_texto}', f'{informacion[1]} {baños_texto}', informacion[2], informacion[3]]
    y_info = 75
    
    for i in range(len(info_forniture)):
        self.infoFurniture = CTkLabel(
                                self.panelInfo,
                                text='',
                                font=self.fuenteHelvetica_Texto,
                                text_color=self.color_blanco,
                                width=120,
                                height=0
                            )
        

        if info_forniture[i] != None:
            widgets_furniture.append(self.infoFurniture)
            
            widgets_furniture[i].configure(text=f'{info_forniture[i]}')
            widgets_furniture[i].place(x=360, y=y_info)
            y_info += 20
            
            
            
            
def mostrarServiciosHabitacion(self, idClase):
    
    sqlAmenidad = f"""
        SELECT amenidad FROM Clase_Amenidades AS CA
        INNER JOIN Amenidades AS Am
        ON CA.id_amenidad = Am.id_amenidad
        WHERE id_clase = {idClase};
    """
    
    amenidades = self.bd.consulta(sqlAmenidad).fetchall()
    y_amenidad = 230
    temp = True
    
    for index, amenidad in enumerate(amenidades):
        self.infoAmenidades = CTkLabel( 
                                    self.panelInfo,
                                    text='',
                                    font=self.fuenteHelvetica_Texto,
                                    text_color=self.color_blanco,
                                    width=220,
                                    height=0,
                                )

        widgets_servicios.append(self.infoAmenidades)
        
        if temp:
            widgets_servicios[index].configure(text=f'{amenidad[0]}')
            widgets_servicios[index].place(x=20, y=y_amenidad)
            temp = False
        else:
            widgets_servicios[index].configure(text=f'{amenidad[0]}')
            widgets_servicios[index].place(x=260, y=y_amenidad)
            temp = True
        
            y_amenidad += 25