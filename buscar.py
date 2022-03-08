def buscar_ASerrano():
        búsqueda = input("Nombre del contacto a buscar:")
        for nombre, num in agenda.items():
            if nombre.startswith(búsqueda):
                print("El número de teléfono de %s es el %s" % (nombre,agenda[nombre]))   


if opción == 2:    
        buscar_ASerrano()


