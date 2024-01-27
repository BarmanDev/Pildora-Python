import psutil

def obtener_informacion_cpu():
    cpu_info = psutil.cpu_percent(interval=1, percpu=True)
    print(f"\nInformación de CPU: {cpu_info}%")

def obtener_informacion_memoria():
    memoria_info = psutil.virtual_memory()
    print(f"\nInformación de memoria:")
    print(f"  Total: {memoria_info.total} bytes")
    print(f"  Disponible: {memoria_info.available} bytes")
    print(f"  Porcentaje de uso: {memoria_info.percent}%")

def obtener_informacion_discos():
    discos_info = psutil.disk_usage('/')
    print(f"\nInformación de disco:")
    print(f"  Total: {discos_info.total} bytes")
    print(f"  Usado: {discos_info.used} bytes")
    print(f"  Disponible: {discos_info.free} bytes")
    print(f"  Porcentaje de uso: {discos_info.percent}%")

def obtener_informacion_red():
    red_info = psutil.net_io_counters()
    print(f"\nInformación de red:")
    print(f"  Bytes recibidos: {red_info.bytes_recv}")
    print(f"  Bytes enviados: {red_info.bytes_sent}")

def menu():
    while True:
        print("\nSeleccione una opción:")
        print("1. Información de CPU")
        print("2. Información de memoria ram")
        print("3. Información de discos")
        print("4. Información de red")
        print("5. Salir")

        opcion = input("Pulsa el número de la opción: ")

        if opcion == '1':
            obtener_informacion_cpu()
        elif opcion == '2':
            obtener_informacion_memoria()
        elif opcion == '3':
            obtener_informacion_discos()
        elif opcion == '4':
            obtener_informacion_red()
        elif opcion == '5':
            print("\nChao pescao!")
            break
        else:
            print("Es del 1 al 5 dedos gordos :)")

if __name__ == "__main__":
    menu()