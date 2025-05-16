hvs = {}

def add_hv():
    
    cont = True
#    while cont:
        
    print("\nDatos personales\n")
    id = input("ID del usuario: ")
    name = input("Nombre del ususario: ")
    contact = input("Contacto del usuario: ")
    address = input("Dirección del usuario: ")
    email = input("Correo del usuario: ")
    birthday = input("Fecha de nacimiento del usuario: ")
    
    print("\nFormacion académica\n")
    academic_training = []
    
    cont = True
    while cont:
        institution = input("Nombre de la institución: ")
        title = input("Título conseguido: ")
        title_year = input("Año en el que consiguió el título: ")
        academic_training.append({"institution": institution, "title": title, "title_year": title_year})   
        while True:
            add_more = input("¿Tiene más títulos por agregar? (S/N)\n").lower().strip()
            if add_more == "s":
                break
            elif add_more == "n":
                cont = False
                break
            else:
                print("Opción no válida")
        
    print("\nExperiencia profesional\n")
    
    professional_experience = []
    
    cont = True
    while cont:
        company = input("Nombre de la empresa: ")
        job_title = input("Puesto de trabajo: ")
        functions = input("Funciones en el trabajo: ")
        time_worked = input("Duración en el cargo: ")
        professional_experience.append({"company": company, "job_title": job_title, "functions": functions, "time_worked": time_worked})   
        while True:
            add_more = input("¿Tiene otra experiencia laboral por agregar? (S/N)\n").lower().strip()
            if add_more == "s":
                break
            elif add_more == "n":
                cont = False
                break
            else:
                print("Opción no válida")
                
    print("\nReferencias laborales\n")
    job_references = []
    
    cont = True
    while cont:
        jr_name = input("Nombre : ")
        jr_relationship = input("Relación: ")
        jr_contact = input("Contacto: ")
        job_references.append({"jr_name": jr_name, "jr_relationship": jr_relationship, "jr_contact": jr_contact})   
        while True:
            add_more = input("¿Desea agregar otra referencia laboral? (S/N)\n").lower().strip()
            if add_more == "s":
                break
            elif add_more == "n":
                cont = False
                break
            else:
                print("Opción no válida")
                
    print("\nReferencias familiares\n")
    family_references = []
    
    cont = True
    while cont:
        fr_name = input("Nombre : ")
        fr_relationship = input("Relación: ")
        fr_contact = input("Contacto: ")
        family_references.append({"fr_name": fr_name, "fr_relationship": fr_relationship, "fr_contact": fr_contact})   
        while True:
            add_more = input("¿Desea agregar otra referencia laboral? (S/N)\n").lower().strip()
            if add_more == "s":
                break
            elif add_more == "n":
                cont = False
                break
            else:
                print("Opción no válida")


        
    hvs[id] = {"name": name, "contact": contact, "address": address, "email": email, "birthday": birthday, "academic_training": academic_training, \
               "professional_experience": professional_experience, "job_references": job_references, "family_references": family_references}       


add_hv()
print(hvs)                 

#---------------------------Consultar hojas de vida--------------------------------------------------------------###


def share_():
    search_id = input ("Ingrese un número de documento para buscar: ")
    if search_id in hvs:
        print("\nInformación de la Hoja de Vida\n")
        print(f"Número de documento: {search_id}")
        print(f" Nombre: {hvs[search_id]['name']}")
        print(f" Contacto: {hvs[search_id]['contact']}")
        print(f" Dirección: {hvs[search_id]['address']}")
        print(f" Correo: {hvs[search_id]['email']}")
        print(f" Fecha de nacimiento: {hvs[search_id]['birthday']}")
        
        print("\nFormación Académica:\n")
        for estudio in hvs[search_id]['academic_training']:
            print(f"  Institución: {estudio['institution']}")
            print(f"  Título: {estudio['title']}")
            print(f"  Año: {estudio['title_year']}")
            print("-" * 20)  
            
        
        print("\nExperiencia Profesional:\n")
        for trabajo in hvs[search_id]['professional_experience']:
            print(f"  Empresa: {trabajo['company']}")
            print(f"  Puesto: {trabajo['job_title']}")
            print(f"  Funciones: {trabajo['functions']}")
            print(f"  Duración: {trabajo['time_worked']}")
            print("-" * 20)
    else:
        print("No existe este numero de Documento")
            
        
        

        
share_()







