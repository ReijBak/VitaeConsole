hvs = {}

def add_hv():
    
    cont = True
#    while cont:

    print("\nDatos personales\n")
    id = input("ID del usuario: ")
    name = input("Nombre del usuario: ")
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

    print("\nHabilidades de vida\n")
    skills = []

    cont = True
    while cont:        
        responsibility = input("¿Usted se considera una persona responsable? (S/N): ").lower().strip()
        if responsibility == "n":
            cont = False
        elif responsibility == "s":
            skills.append("Responsabilidad")
            cont = False
    cont = True
    while cont:
        punctuality = input("¿Usted se considera una persona puntual? (S/N): ").lower().strip()
        if punctuality == "n":
            cont = False
        elif punctuality == "s":
            skills.append("Puntualidad")
            cont = False
    cont = True
    while cont:
        honesty = input("¿Usted se considera una persona honesta? (S/N): ").lower().strip()
        if honesty == "n":
            cont = False
        elif honesty == "s":
            skills.append("Honestidad")
            cont = False
    cont = True
    while cont:
        kindness = input("¿Usted se considera una persona amable? (S/N): ").lower().strip()
        if kindness == "n":
            cont = False
        elif kindness == "s":
            skills.append("Amabilidad")
            cont = False
    cont = True
    while cont:
        friendly = input("¿Usted se considera una persona amigable? (S/N): ").lower().strip()
        if friendly == "n":
            cont = False
        elif friendly == "s":
            skills.append("Amigable")
            cont = False
    cont = True
    while cont:
        optimistic = input("¿Usted se considera una persona optimista? (S/N): ").lower().strip()
        if optimistic == "n":
            cont = False

        elif optimistic == "s":
            skills.append("Optimista")
            cont = False
            
    print("\nCertificaciones adicionales\n")
    extra_certifications = []

    cont = True
    while cont:
        ec_institution = input("Nombre de la institución: ")
        ec_title = input("Certificación conseguida: ")
        ec_title_year = input("Año en el que consiguió la certificación: ")
        extra_certifications.append({"ec_institution": ec_institution, "ec_title": ec_title, "ec_title_year": ec_title_year})   
        while True:
            add_more = input("¿Tiene más títulos por agregar? (S/N)\n").lower().strip()
            if add_more == "s":
                break
            elif add_more == "n":
                cont = False
                break
            else:
                print("Opción no válida")



    hvs[id] = {"name": name, "contact": contact, "address": address, "email": email, "birthday": birthday, "academic_training": academic_training, \
               "professional_experience": professional_experience, "job_references": job_references, "family_references": family_references, \
               "skills": skills, "extra_certifications": extra_certifications}       
            


                 

#---------------------------Consultar hojas de vida--------------------------------------------------------------###


def search_id():
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
        
        print ("\nReferencias laborales")
        for referencia_j in hvs[search_id]['job_references']:
            print(f"  Nombre: {referencia_j['jr_name']}")
            print(f"  Relación: {referencia_j['jr_relationship']}")
            print(f"  Contacto: {referencia_j['jr_contact']}")
            print("-" * 20)
            
        print ("\nReferencias Familiares")
        for referencia_f in hvs[search_id]['family_references']:
            print(f"  Nombre: {referencia_f['fr_name']}")
            print(f"  Relación: {referencia_f['fr_relationship']}")
            print(f"  Contacto: {referencia_f['fr_contact']}")
            print("-" * 20)
        
        print ("\nHabilidades de vida")
        for skill in hvs[search_id]['skills']:
            print(skill)
            
            
        print("\nCertificados adicionales:\n")
        for estudio in hvs[search_id]['extra_certifications']:
            print(f"  Institución: {estudio['ec_institution']}")
            print(f"  Título: {estudio['ec_title']}")
            print(f"  Año: {estudio['ec_title_year']}")
            print("-" * 20)
    else:
        print("No existe este numero de Documento")
        
def search_name():
    nombre_busqueda = input("Ingrese el nombre a buscar: ").strip().lower()
    resultados = []
    for documento, datos in hvs.items():
        if datos['name'].lower() == nombre_busqueda:
            resultados.append((documento, datos))

    if resultados:
        print(f"\nSe encontraron {len(resultados)} hojas de vida con el nombre '{nombre_busqueda}':\n")
        for documento, datos in resultados:
            print("\nInformación de la Hoja de Vida\n")
            print(f"Número de documento: {documento}")
            print(f" Nombre: {datos['name']}")
            print(f" Contacto: {datos['contact']}")
            print(f" Dirección: {datos['address']}")
            print(f" Correo: {datos['email']}")
            print(f" Fecha de nacimiento: {datos['birthday']}")

            print("\nFormación Académica:\n")
            for estudio in datos['academic_training']:
                print(f"  Institución: {estudio['institution']}")
                print(f"  Título: {estudio['title']}")
                print(f"  Año: {estudio['title_year']}")
                print("-" * 20)

            print("\nExperiencia Profesional:\n")
            for trabajo in datos['professional_experience']:
                print(f"  Empresa: {trabajo['company']}")
                print(f"  Puesto: {trabajo['job_title']}")
                print(f"  Funciones: {trabajo['functions']}")
                print(f"  Duración: {trabajo['time_worked']}")
                print("-" * 20)

            print("\nReferencias laborales")
            for referencia_j in datos['job_references']:
                print(f"  Nombre: {referencia_j['jr_name']}")
                print(f"  Relación: {referencia_j['jr_relationship']}")
                print(f"  Contacto: {referencia_j['jr_contact']}")
                print("-" * 20)

            print("\nReferencias Familiares")
            for referencia_f in datos['family_references']:
                print(f"  Nombre: {referencia_f['fr_name']}")
                print(f"  Relación: {referencia_f['fr_relationship']}")
                print(f"  Contacto: {referencia_f['fr_contact']}")
                print("-" * 20)
            
            print ("\nHabilidades de vida\n")
            for skill in datos['skills']:
                print(skill)
                
            print("\nCertificados adicionales:\n")
            for estudio in datos['extra_certifications']:
                print(f"  Institución: {estudio['ec_institution']}")
                print(f"  Título: {estudio['ec_title']}")
                print(f"  Año: {estudio['ec_title_year']}")
                print("-" * 20)
    else:
        print(f"No se encontraron hojas de vida con el nombre '{nombre_busqueda}'.")
        
def search_email():
    email_busqueda = input("ingrese el email a buscar: ").strip().lower()
    resultados1 = []
    for documento1, datos in hvs.items():
        if datos['email'].lower() == email_busqueda:
            resultados1.append((documento1, datos))
    
    if resultados1:
        print(f"\nSe encontraron {len(resultados1)} hojas de vida con el email '{email_busqueda}':\n")
        for documento, datos in resultados1:
            print("\nInformación de la Hoja de Vida\n")
            print(f"Número de documento: {documento1}")
            print(f" Nombre: {datos['name']}")
            print(f" Contacto: {datos['contact']}")
            print(f" Dirección: {datos['address']}")
            print(f" Correo: {datos['email']}")
            print(f" Fecha de nacimiento: {datos['birthday']}")

            print("\nFormación Académica:\n")
            for estudio in datos['academic_training']:
                print(f"  Institución: {estudio['institution']}")
                print(f"  Título: {estudio['title']}")
                print(f"  Año: {estudio['title_year']}")
                print("-" * 20)

            print("\nExperiencia Profesional:\n")
            for trabajo in datos['professional_experience']:
                print(f"  Empresa: {trabajo['company']}")
                print(f"  Puesto: {trabajo['job_title']}")
                print(f"  Funciones: {trabajo['functions']}")
                print(f"  Duración: {trabajo['time_worked']}")
                print("-" * 20)

            print("\nReferencias laborales")
            for referencia_j in datos['job_references']:
                print(f"  Nombre: {referencia_j['jr_name']}")
                print(f"  Relación: {referencia_j['jr_relationship']}")
                print(f"  Contacto: {referencia_j['jr_contact']}")
                print("-" * 20)

            print("\nReferencias Familiares")
            for referencia_f in datos['family_references']:
                print(f"  Nombre: {referencia_f['fr_name']}")
                print(f"  Relación: {referencia_f['fr_relationship']}")
                print(f"  Contacto: {referencia_f['fr_contact']}")
                print("-" * 20)
            
            print ("\nHabilidades de vida\n")
            for skill in datos['skills']:
                print(skill)
            
            print("\nCertificados adicionales:\n")
            for estudio in datos['extra_certifications']:
                print(f"  Institución: {estudio['ec_institution']}")
                print(f"  Título: {estudio['ec_title']}")
                print(f"  Año: {estudio['ec_title_year']}")
                print("-" * 20)
    else:
        print(f"No se encontraron hojas de vida con el email '{email_busqueda}'.")
        
        
        

        

###--------------------actualizar-----------------###

def update():
    id = input("Ingrese el ID del usuario que desea actualizar: ")
    
    if id not in hvs:
        print("ID no encontrado.")
        return
    
    while True:
        print("\n¿Qué desea actualizar?")
        print("1. Datos personales")
        print("2. Añadir nueva formación académica")
        print("3. Añadir nueva experiencia profesional")
        print("4. Agregar habilidades")
        print("5. Agregar referencias")
        print("6. Salir del menú de actualización")
        
        option = input("Seleccione una opción (1-6): ").strip()
        
        if option == "1":
            print("\nActualización de datos personales:")
            hvs[id]["name"] = input("Nuevo nombre: ")
            hvs[id]["contact"] = input("Nuevo contacto: ")
            hvs[id]["address"] = input("Nueva dirección: ")
            hvs[id]["email"] = input("Nuevo correo electrónico: ")
            hvs[id]["birthday"] = input("Nueva fecha de nacimiento: ")

        elif option == "2":
            print("\nAñadir nueva formación académica:")
            institution = input("Nombre de la institución: ")
            title = input("Título conseguido: ")
            title_year = input("Año del título: ")
            new_academic = {"institution": institution, "title": title, "title_year": title_year}
            hvs[id].setdefault("academic_training", []).append(new_academic)

        elif option == "3":
            print("\nAñadir nueva experiencia profesional:")
            company = input("Nombre de la empresa: ")
            job_title = input("Puesto: ")
            functions = input("Funciones: ")
            time_worked = input("Duración: ")
            new_exp = {"company": company, "job_title": job_title, "functions": functions, "time_worked": time_worked}
            hvs[id].setdefault("professional_experience", []).append(new_exp)

        elif option == "4":
            print("\nAgregar habilidades:")
            new_skill = input("Escriba una habilidad: ")
            hvs[id].setdefault("skills", set()).add(new_skill)

        elif option == "5":
            print("\nAgregar referencia:")
            name = input("Nombre de la referencia: ")
            relation = input("Relación: ")
            phone = input("Teléfono: ")
            new_ref = {"name": name, "relation": relation, "phone": phone}
            hvs[id].setdefault("references", []).append(new_ref)

        elif option == "6":
            print("Saliendo del menú de actualización.")
            break

        else:
            print("Opción inválida. Intente de nuevo.")

####------------------------ Generar reportes -------------------------####

# def generate_reports():

####------------------------ menu principal -------------------------####

def menu():
    while True:
        print("\n---- MENÚ PRINCIPAL ----")
        print("1. Registrar hoja de vida")
        print("2. Consultar hoja de vida por id")
        print("3. Actualizar hoja de vida")
        print("4. Consultar hoja de vida por nombre")
        print("5. Consultar hoja de vida por email")
        print("6. Generar reportes")
        print("7. Salir")
        

        option = input("Seleccione una opción (1-6): ").strip()

        match option:
            case "1":
                add_hv()
            case "2":
                search_id()
            case "3":
                update()
            case "4":
                search_name()
            case "5":
                search_email()
            case "6":
               search_id()  # generar reporte
            case "7":
                print("¡Hasta pronto!")
                break
            case _:
                print("Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    menu()