hvs = {}

def add_hv():
    """
    Función para agregar una hoja de vida al diccionario hvs.
    """
    print("\nDatos personales\n")
    id_usuario = input("ID del usuario: ")  # Usar nombres de variables descriptivos
    nombre = input("Nombre del usuario: ")
    contacto = input("Contacto del usuario: ")
    direccion = input("Dirección del usuario: ")
    correo = input("Correo del usuario: ")
    fecha_nacimiento = input("Fecha de nacimiento del usuario: ")

    print("\nFormacion académica\n")
    formacion_academica = []  # Usar nombres en minúsculas y descriptivos

    continuar_formacion = True
    while continuar_formacion:
        institucion = input("Nombre de la institución: ")
        titulo = input("Título conseguido: ")
        titulo_anio = input("Año en el que consiguió el título: ")
        formacion_academica.append({
            "institucion": institucion,
            "titulo": titulo,
            "titulo_anio": titulo_anio,
        })
        while True:
            agregar_mas = input("¿Tiene más títulos por agregar? (S/N)\n").lower().strip()
            if agregar_mas == "s":
                break
            elif agregar_mas == "n":
                continuar_formacion = False
                break
            else:
                print("Opción no válida")

    print("\nExperiencia profesional\n")
    experiencia_profesional = []  # Usar nombres en minúsculas y descriptivos

    continuar_experiencia = True
    while continuar_experiencia:
        empresa = input("Nombre de la empresa: ")
        puesto_trabajo = input("Puesto de trabajo: ")
        funciones = input("Funciones en el trabajo: ")
        tiempo_trabajado = input("Duración en el cargo: ")
        experiencia_profesional.append({
            "empresa": empresa,
            "puesto_trabajo": puesto_trabajo,
            "funciones": funciones,
            "tiempo_trabajado": tiempo_trabajado,
        })
        while True:
            agregar_mas_experiencia = input("¿Tiene otra experiencia laboral por agregar? (S/N)\n").lower().strip()
            if agregar_mas_experiencia == "s":
                break
            elif agregar_mas_experiencia == "n":
                continuar_experiencia = False
                break
            else:
                print("Opción no válida")

    hvs[id_usuario] = {  # Usar el id_usuario como clave
        "nombre": nombre,  # Corregir las claves para que coincidan
        "contacto": contacto,
        "direccion": direccion,
        "correo": correo,
        "fecha_nacimiento": fecha_nacimiento,
        "formacion_academica": formacion_academica,
        "experiencia_profesional": experiencia_profesional,
    }
    print("Hoja de vida agregada exitosamente") #Indicar que se agregó la hoja de vida



def share_():
    """
    Función para buscar y mostrar una hoja de vida por ID.
    """
    search_id = input("Ingrese un número de documento para buscar: ")

    if search_id in hvs:
        print("\nInformación de la Hoja de Vida\n")
        print(f"Número de documento: {search_id}")
        print(f"Nombre: {hvs[search_id]['nombre']}")
        print(f"Contacto: {hvs[search_id]['contacto']}")
        print(f"Dirección: {hvs[search_id]['direccion']}")
        print(f"Correo: {hvs[search_id]['correo']}")
        print(f"Fecha de nacimiento: {hvs[search_id]['fecha_nacimiento']}")

        print("\nFormación Académica:\n")
        for estudio in hvs[search_id]['formacion_academica']:
            print(f"  Institución: {estudio['institucion']}")
            print(f"  Título: {estudio['titulo']}")
            print(f"  Año: {estudio['titulo_anio']}")
            print("-" * 20)  # Separador visual

        print("\nExperiencia Profesional:\n")
        for trabajo in hvs[search_id]['experiencia_profesional']:
            print(f"  Empresa: {trabajo['empresa']}")
            print(f"  Puesto: {trabajo['puesto_trabajo']}")
            print(f"  Funciones: {trabajo['funciones']}")
            print(f"  Duración: {trabajo['tiempo_trabajado']}")
            print("-" * 20)  # Separador visual
    else:
        print(f"No se encontró ninguna hoja de vida con el ID: {search_id}")



add_hv()
share_()
