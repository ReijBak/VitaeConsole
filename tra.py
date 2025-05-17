def buscar_por_nombre():
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
    else:
        print(f"No se encontraron hojas de vida con el nombre '{nombre_busqueda}'.")

# Asumiendo que 'hvs' es tu diccionario de hojas de vida
hvs = {
    "12345": {
        "name": "Juan Perez",
        "contact": "310...",
        "address": "Calle...",
        "email": "juan@...",
        "birthday": "01/01/1990",
        "academic_training": [
            {"institution": "Universidad A", "title": "Ingeniero", "title_year": "2015"}
        ],
        "professional_experience": [
            {"company": "Empresa X", "job_title": "Desarrollador", "functions": "...", "time_worked": "2 años"}
        ],
        "job_references": [
            {"jr_name": "Maria Lopez", "jr_relationship": "Jefe", "jr_contact": "311..."}
        ],
        "family_references": [
            {"fr_name": "Pedro Perez", "fr_relationship": "Hermano", "fr_contact": "312..."}
        ]
    },
    "67890": {
        "name": "Ana Gómez",
        "contact": "315...",
        "address": "Avenida...",
        "email": "ana@...",
        "birthday": "15/05/1992",
        "academic_training": [
            {"institution": "Universidad B", "title": "Abogada", "title_year": "2018"}
        ],
        "professional_experience": [
            {"company": "Bufete Y", "job_title": "Abogada Junior", "functions": "...", "time_worked": "3 años"}
        ],
        "job_references": [
            {"jr_name": "Carlos Ruiz", "jr_relationship": "Colega", "jr_contact": "313..."}
        ],
        "family_references": [
            {"fr_name": "Sofia Gómez", "fr_relationship": "Madre", "fr_contact": "314..."}
        ]
    },
    "13579": {
        "name": "Juan Carlos Perez",
        "contact": "320...",
        "address": "Carrera...",
        "email": "juancarlos@...",
        "birthday": "20/11/1988",
        "academic_training": [
            {"institution": "Politécnico Z", "title": "Técnico en...", "title_year": "2010"}
        ],
        "professional_experience": [
            {"company": "Industrias W", "job_title": "Operario", "functions": "...", "time_worked": "5 años"}
        ],
        "job_references": [
            {"jr_name": "Laura Vargas", "jr_relationship": "Supervisor", "jr_contact": "316..."}
        ],
        "family_references": [
            {"fr_name": "Elena Pérez", "fr_relationship": "Tía", "fr_contact": "317..."}
        ]
    }
}

buscar_por_nombre()