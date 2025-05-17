cvs = {}

import re

def validate_phone(prompt):
    while True:
        phone = input(prompt).strip()
        if phone.isdigit() and 7 <= len(phone) <= 15:
            return phone
        else:
            print("Número telefónico inválido. Ingrese solo dígitos (7 a 15 dígitos).")

def validate_min_length(prompt, min_length=3):
    while True:
        value = input(prompt).strip()
        if len(value) >= min_length:
            return value
        else:
            print(f"El valor debe tener al menos {min_length} caracteres.")

def validate_year(prompt):
    while True:
        year = input(prompt).strip()
        if year.isdigit() and 1900 <= int(year) <= 2025:
            return year
        else:
            print("Año inválido. Ingrese un número entre 1900 y 2025.")



def validate_phone(prompt):
    while True:
        phone = input(prompt).strip()
        if phone.isdigit() and 7 <= len(phone) <= 15:
            return phone
        else:
            print("Número telefónico inválido. Ingrese solo dígitos (7 a 15 dígitos).")

def validate_min_length(prompt, min_length=3):
    while True:
        value = input(prompt).strip()
        if len(value) >= min_length:
            return value
        else:
            print(f"El valor debe tener al menos {min_length} caracteres.")

def validate_year(prompt):
    while True:
        year = input(prompt).strip()
        if year.isdigit() and 1900 <= int(year) <= 2025:
            return year
        else:
            print("Año inválido. Ingrese un número entre 1900 y 2025.")

def validate_email(prompt):
    pattern = r'^\S+@\S+\.\S+$'
    while True:
        email = input(prompt).strip()
        if re.match(pattern, email):
            return email
        else:
            print("Correo inválido. Ingrese un correo válido (ej. ejemplo@dominio.com).")

def validate_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        else:
            print("Este campo no puede estar vacío.")

def validate_numeric_id(prompt):
    while True:
        value = input(prompt).strip()
        if value.isdigit():
            return value
        else:
            print("ID inválido. Ingrese solo números.")

def add_cv():
    

    print("\nDatos personales\n")
    id = validate_numeric_id("ID del usuario: ")
    name = validate_min_length("Nombre del usuario: ", 3)
    contact = validate_phone("Contacto del usuario: ")
    address = validate_non_empty("Dirección del usuario: ")
    email = validate_email("Correo del usuario: ")
    birthday = validate_non_empty("Fecha de nacimiento del usuario: ")

    print("\nFormacion académica\n")
    academic_training = []

    cont = True
    while cont:
        institution = validate_non_empty("Nombre de la institución: ")
        title = validate_non_empty("Título conseguido: ")
        title_year = validate_year("Año en el que consiguió el título: ")
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
        company = validate_non_empty("Nombre de la empresa: ")
        job_title = validate_non_empty("Puesto de trabajo: ")
        functions = validate_non_empty("Funciones en el trabajo: ")
        time_worked = validate_non_empty("Duración en el cargo: ")
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
        jr_name = validate_non_empty("Nombre : ")
        jr_relationship = validate_non_empty("Relación: ")
        jr_contact = validate_phone("Contacto: ")
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
        fr_name = validate_non_empty("Nombre : ")
        fr_relationship = validate_non_empty("Relación: ")
        fr_contact = validate_phone("Contacto: ")
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
        ec_institution = validate_non_empty("Nombre de la institución: ")
        ec_title = validate_non_empty("Certificación conseguida: ")
        ec_title_year = validate_year("Año en el que consiguió la certificación: ")
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



    cvs[id] = {"name": name, "contact": contact, "address": address, "email": email, "birthday": birthday, "academic_training": academic_training, \
               "professional_experience": professional_experience, "job_references": job_references, "family_references": family_references, \
               "skills": skills, "extra_certifications": extra_certifications}       
            
                 

#---------------------------Consultar hojas de vida--------------------------------------------------------------###


def search_id():
    search_id = input ("Ingrese un número de documento para buscar: ")
    if search_id in cvs:
        print("\nInformación de la Hoja de Vida\n")
        print(f"Número de documento: {search_id}")
        print(f" Nombre: {cvs[search_id]['name']}")
        print(f" Contacto: {cvs[search_id]['contact']}")
        print(f" Dirección: {cvs[search_id]['address']}")
        print(f" Correo: {cvs[search_id]['email']}")
        print(f" Fecha de nacimiento: {cvs[search_id]['birthday']}")
        
        print("\nFormación Académica:\n")
        for estudio in cvs[search_id]['academic_training']:
            print(f"  Institución: {estudio['institution']}")
            print(f"  Título: {estudio['title']}")
            print(f"  Año: {estudio['title_year']}")
            print("-" * 20)  
            
        
        print("\nExperiencia Profesional:\n")
        for trabajo in cvs[search_id]['professional_experience']:
            print(f"  Empresa: {trabajo['company']}")
            print(f"  Puesto: {trabajo['job_title']}")
            print(f"  Funciones: {trabajo['functions']}")
            print(f"  Duración: {trabajo['time_worked']}")
            print("-" * 20)
        
        print ("\nReferencias laborales")
        for referencia_j in cvs[search_id]['job_references']:
            print(f"  Nombre: {referencia_j['jr_name']}")
            print(f"  Relación: {referencia_j['jr_relationship']}")
            print(f"  Contacto: {referencia_j['jr_contact']}")
            print("-" * 20)
            
        print ("\nReferencias Familiares")
        for referencia_f in cvs[search_id]['family_references']:
            print(f"  Nombre: {referencia_f['fr_name']}")
            print(f"  Relación: {referencia_f['fr_relationship']}")
            print(f"  Contacto: {referencia_f['fr_contact']}")
            print("-" * 20)
        
        print ("\nHabilidades de vida")
        for skill in cvs[search_id]['skills']:
            print(skill)
            
            
        print("\nCertificados adicionales:\n")
        for estudio in cvs[search_id]['extra_certifications']:
            print(f"  Institución: {estudio['ec_institution']}")
            print(f"  Título: {estudio['ec_title']}")
            print(f"  Año: {estudio['ec_title_year']}")
            print("-" * 20)
    else:
        print("No existe este numero de Documento")
        
def search_name():
    nombre_busqueda = input("Ingrese el nombre a buscar: ").strip().lower()
    resultados = []
    for documento, datos in cvs.items():
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
    for documento1, datos in cvs.items():
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

def filter_cvs():
    if not cvs:
        print("No hay hojas de vida registradas.")
        return

    print("--- Filtrar hojas de vida ---")
    print("1. Mostrar todas")
    print("2. Filtrar por años de experiencia")
    print("3. Filtrar por título académico")
    print("4. Filtrar por habilidad")

    option = input("Seleccione una opción (1-4): ").strip()

    results = []

    if option == '1':
        results = list(cvs.items())

    elif option == '2':
        try:
            min_years = int(input("Ingrese el número mínimo de años de experiencia: "))
            for doc_id, data in cvs.items():
                total_years = 0
                for job in data.get("professional_experience", []):
                    try:
                        duration = int(job["time_worked"].split()[0])  # se asume formato como "2 años"
                        total_years += duration
                    except:
                        continue
                if total_years >= min_years:
                    results.append((doc_id, data))
        except ValueError:
            print("Entrada no válida. Debe ingresar un número.")
            return

    elif option == '3':
        keyword = input("Ingrese una palabra clave del título académico: ").lower()
        for doc_id, data in cvs.items():
            for edu in data.get("academic_training", []):
                if keyword in edu["title"].lower():
                    results.append((doc_id, data))
                    break

    elif option == '4':
        skill_input = input("Ingrese la habilidad que desea buscar: ").strip().lower()
        for doc_id, data in cvs.items():
            if skill_input in [s.lower() for s in data.get("skills", [])]:
                results.append((doc_id, data))
    else:
        print("Opción no válida.")
        return

    if results:
        print(f"--- Se encontraron {len(results)} hoja(s) de vida ---")
        for doc_id, data in results:
            print(f"ID: {doc_id}")
            print(f" Nombre: {data['name']}")
            print(f" Correo electrónico: {data['email']}")
            print(f" Habilidades: {', '.join(data.get('skills', []))}")
            print(f" Formación académica:")
            for edu in data.get("academic_training", []):
                print(f"   - {edu['title']} en {edu['institution']} ({edu['title_year']})")
            print(f" Experiencia profesional:")
            for job in data.get("professional_experience", []):
                print(f"   - {job['job_title']} en {job['company']} ({job['time_worked']})")
    else:
        print("No se encontraron hojas de vida con ese criterio.")


def search_cv():
    options = {
        "1": search_id,
        "2": search_name,
        "3": search_email
    }
    print("\nSeleccione como quiere buscar la hoja de vida\n")
    print("1. Buscar por ID.")
    print("2. Buscar por nombre.")
    print("3. Buscar por e-mail.")

    choice = input("\nSeleccione una opción (1-3): ").strip()
    action = options.get(choice)
    if action:
        action()
    else:
        print("Opción no válida.")


        

###--------------------actualizar-----------------###

def update():
    id = input("Ingrese el ID del usuario que desea actualizar: ")
    
    if id not in cvs:
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
            cvs[id]["name"] = input("Nuevo nombre: ")
            cvs[id]["contact"] = input("Nuevo contacto: ")
            cvs[id]["address"] = input("Nueva dirección: ")
            cvs[id]["email"] = input("Nuevo correo electrónico: ")
            cvs[id]["birthday"] = input("Nueva fecha de nacimiento: ")

        elif option == "2":
            print("\nAñadir nueva formación académica:")
            institution = validate_non_empty("Nombre de la institución: ")
            title = validate_non_empty("Título conseguido: ")
            title_year = input("Año del título: ")
            new_academic = {"institution": institution, "title": title, "title_year": title_year}
            cvs[id].setdefault("academic_training", []).append(new_academic)

        elif option == "3":
            print("\nAñadir nueva experiencia profesional:")
            company = validate_non_empty("Nombre de la empresa: ")
            job_title = input("Puesto: ")
            functions = input("Funciones: ")
            time_worked = input("Duración: ")
            new_exp = {"company": company, "job_title": job_title, "functions": functions, "time_worked": time_worked}
            cvs[id].setdefault("professional_experience", []).append(new_exp)

        elif option == "4":
            print("\nAgregar habilidades:")
            new_skill = input("Escriba una habilidad: ")
            cvs[id].setdefault("skills", set()).add(new_skill)

        elif option == "5":
            print("\nAgregar referencia:")
            name = input("Nombre de la referencia: ")
            relation = input("Relación: ")
            phone = input("Teléfono: ")
            new_ref = {"name": name, "relation": relation, "phone": phone}
            cvs[id].setdefault("references", []).append(new_ref)

        elif option == "6":
            print("Saliendo del menú de actualización.")
            break

        else:
            print("Opción inválida. Intente de nuevo.")

####------------------------ Generar reportes -------------------------####


import json
import csv

def generate_reports():
    if not cvs:
        print("No hay hojas de vida registradas.")
        return

    print("\n--- Generar Reportes ---")
    print("1. Listado de hojas de vida con experiencia superior a N años")
    print("2. Candidatos con cierta certificación o formación específica")
    print("3. Exportar hojas de vida (JSON, CSV o TXT)")

    option = input("Seleccione una opción (1-3): ").strip()

    if option == "1":
        try:
            min_years = int(input("Ingrese el número mínimo de años de experiencia: "))
            print(f"\nCandidatos con más de {min_years} años de experiencia:")
            for doc_id, data in cvs.items():
                total_years = 0
                for job in data.get("professional_experience", []):
                    try:
                        duration = int(job["time_worked"].split()[0])
                        total_years += duration
                    except:
                        continue
                if total_years > min_years:
                    print(f"- {data['name']} ({total_years} años)")
        except ValueError:
            print("Entrada inválida. Debe ingresar un número.")

    elif option == "2":
        keyword = input("Ingrese una palabra clave de la formación o certificación: ").lower()
        print(f"\nCandidatos con formación o certificación que incluye '{keyword}':")
        for doc_id, data in cvs.items():
            found = False
            for edu in data.get("academic_training", []):
                if keyword in edu["title"].lower():
                    found = True
            for cert in data.get("extra_certifications", []):
                if keyword in cert["ec_title"].lower():
                    found = True
            if found:
                print(f"- {data['name']} ({data['email']})")

    elif option == "3":
        print("\nSeleccione el formato de exportación:")
        print("1. JSON")
        print("2. CSV")
        print("3. TXT")
        format_opt = input("Opción (1-3): ").strip()
        file_name = input("Ingrese el nombre del archivo (sin extensión): ").strip()

        if format_opt == "1":
            with open(f"{file_name}.json", "w", encoding="utf-8") as f:
                json.dump(cvs, f, ensure_ascii=False, indent=4)
            print(f"Exportación completa: {file_name}.json")

        elif format_opt == "2":
            with open(f"{file_name}.csv", "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["ID", "Nombre", "Correo", "Formación", "Experiencia", "Habilidades"])
                for doc_id, data in cvs.items():
                    edu_titles = "; ".join([e["title"] for e in data.get("academic_training", [])])
                    job_titles = "; ".join([j["job_title"] for j in data.get("professional_experience", [])])
                    skills = ", ".join(data.get("skills", []))
                    writer.writerow([doc_id, data["name"], data["email"], edu_titles, job_titles, skills])
            print(f"Exportación completa: {file_name}.csv")

        elif format_opt == "3":
            with open(f"{file_name}.txt", "w", encoding="utf-8") as f:
                for doc_id, data in cvs.items():
                    f.write(f"ID: {doc_id}\nNombre: {data['name']}\nCorreo: {data['email']}\n")
                    f.write("Formación académica:\n")
                    for edu in data.get("academic_training", []):
                        f.write(f"  - {edu['title']} en {edu['institution']} ({edu['title_year']})\n")
                    f.write("Experiencia profesional:\n")
                    for job in data.get("professional_experience", []):
                        f.write(f"  - {job['job_title']} en {job['company']} ({job['time_worked']})\n")
                    f.write(f"Habilidades: {', '.join(data.get('skills', []))}\n")
                    f.write("-" * 40 + "\n")
            print(f"Exportación completa: {file_name}.txt")

        else:
            print("Opción no válida.")

    else:
        print("Opción no válida.")


####------------------------ menu principal -------------------------####

def menu():
    while True:
        print("\n---- MENÚ PRINCIPAL ---\n")
        print("1. Registrar hoja de vida")
        print("2. Consultar hoja de vida")
        print("3. Actualizar hoja de vida")
        print("4. Generar reportes")
        print("5. Salir")
        

        option = input("\nSeleccione una opción (1-5): ").strip()

        match option:
            case "1":
                add_cv()
            case "2":
                print("1. Buscar por ID")
                print("2. Buscar por nombre")
                print("3. Buscar por email")
                print("4. Filtrar hojas de vida")
                sub_option = input("Elige un tipo de busqueda (1-4): ").strip()

                if sub_option == "1":
                    search_id()
                elif sub_option == "2":
                    search_name()
                elif sub_option == "3":
                    search_email()
                elif sub_option == "4":
                    filter_cvs()
                else:
                    print("Opción inválida, Intente de nuevo.")

            case "3":
                update()
            case "4":
                generate_reports()
            case "5":
                print("¡Hasta pronto!")
                break
            case _:
                print("Opción inválida, Intente de nuevo.")


if __name__ == "__main__":
    menu()


