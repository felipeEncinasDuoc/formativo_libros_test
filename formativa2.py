#formativa2
inventario=[
    {"id":1,
     "titulo":"titulo_test",
     "precio":0,
     "disponible":False
     }
]

def print_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar libro")
    print("2. Buscar libro")
    print("3. Eliminar libro")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar libros")
    print("6. Salir")
    print("=====================================")
    
def validar_menu(min,max):
    try:
        menu_input_local=int(input("Ingrese una opcion: "))
    except:
        print("Debe ingresar un numero")
        return -1
    if min<=menu_input_local<=max:
        return menu_input_local
    else:
        print(f"Ingrese una opcion entre {min} y {max}")
        return None
    
def validar_id(id):
    try:
        id=int(id)
    except:
        return False
    else:
        if id>0:
            return True
        else: 
            return False

def validar_nombre(nombre):
    if nombre and not nombre.isspace():
        return True
    else:
        return False
    
def validar_precio(precio):
    try:
        precio=float(precio)
    except:
        return False
    else:
        if precio>0:
          return True
        else: 
            return False
        
def agregar(inventario):
    id=input("Ingrese ID del libro: ")
    titulo=input("Ingrese titulo del libro: ")
    precio=input("Ingrese precio del libro: ")
    if validar_id(id) and validar_nombre(titulo) and validar_precio(precio):
        inventario.append(
            {
                "id":int(id),
                "titulo":titulo,
                "precio":float(precio),
                "disponible":False
                }
        )
        print(f"Libro '{titulo}' agregado")
    else:
        print("Error")
        print("Libro no agregado")
    
def buscar(inventario):
    try:
        target=input("Ingrese ID del libro: ")
    except:
        return None, -1
    if validar_id(target):
        for index,libro in enumerate(inventario):
            if libro["id"]==int(target):
                return index,1
        return None, -1
            

def eliminar(inventario):
    index,existe=buscar(inventario)
    if existe==1:
        inventario.pop(index)
        print("Libro eliminado")
    else: print("Libro no encontrado")
        
        
def actualizar(inventario):
    count=0
    for libro in inventario:
        if libro["precio"]<=15000:
            libro["disponible"]=True
            count+=1
    if count>0:
        print(f"Se actualizaron {count} de {len(inventario)} libros")

def mostrar_todo(inventario):
    actualizar(inventario)
    if inventario:
        print("=== LISTA DE LIBROS ===")
        print("")
        for libro in inventario:
            print(f"ID: {libro["id"]}")
            print(f"Título: {libro["titulo"]}")
            print(f"Precio: {libro["precio"]}")
            if libro["disponible"]:
                print("Estado: DISPONIBLE")
            else: print("Estado: NO DISPONIBLE")
            print("********************************************")
            print("")
    else: print("No hay libros en inventario")

while True:
    print_menu()
    user_input=validar_menu(1,6)
    if user_input != -1:
        match user_input:
            case 1:
                agregar(inventario)
            case 2:
                index,existe=buscar(inventario)
                if existe==1:
                    actualizar(inventario)
                    print("")
                    print("******Resultado de busqueda******")
                    print(f"ID: {inventario[index]["id"]}")
                    print(f"Título: {inventario[index]["titulo"]}")
                    print(f"Precio: {inventario[index]["precio"]}")
                    if inventario[index]["disponible"]:
                        print("Estado: DISPONIBLE")
                    else: print("Estado: NO DISPONIBLE")
                else: print("Libro no encontrado")
            case 3:
                eliminar(inventario)
            case 4:
                actualizar(inventario)
            case 5:
                mostrar_todo(inventario)
            case 6:
                print("Gracias por usar el sistema. Vuelva Pronto")
                break
        print("")
        print("")
