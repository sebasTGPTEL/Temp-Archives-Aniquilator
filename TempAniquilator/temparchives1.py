import os 
import shutil
import time

paths = [
    r'C:\Users\gamer\AppData\Local\Temp',
    r'C:\Windows\Temp',
    r'C:\Windows\SoftwareDistribution\Download',
    r'C:\Users\gamer\AppData\Local\Microsoft\Windows\INetCache'
]

def limpieza_general():
    for base_path in paths:
        if not os.path.exists(base_path):
            print(f"El directorio {base_path} no se encuentra")
            continue
        print(f"\nRecorriendo {base_path}")

        for root, dirs, files in os.walk(base_path, topdown=False):
            print(f"Eliminando archivos temporales de {base_path}")
            time.sleep(3)
            for file in files:
                try:
                    os.remove(os.path.join(root, file))
                except PermissionError:
                    print(f"El archivo {file} se ha omitido")
                    time.sleep(1)
                    pass
                
            for dir in dirs:
                dir_path = os.path.join(root, dir)
                try:
                    if os.path.islink(dir_path):
                        os.unlink(dir_path)
                    else:
                        shutil.rmtree(dir_path)
                except PermissionError:
                    print(f"La carpeta {dir} se ha omitido")
                    time.sleep(1)
                except Exception:
                    pass
            print(f"La eliminacion de archivos temporales de {base_path} ha terminado.")
   
    input("Presiona Enter para salir...")
    
def dry_run():
    pass

print("\nBienvenido a el limpiador de archivos temporales")
print("------------------------------------------------")
print("1.Iniciar limpieza general")
print("2.Iniciar dry run")
print("3.Salir")
try:
    opcion = int(input("Selecciona tu opcion(1/2/3): "))
except ValueError:
    print("Introduzca una opcion valida(1/2/3)") 

if 1 <= opcion <= 3:
    if opcion == 1:
        limpieza_general()
    elif opcion == 2:
        dry_run()
    elif opcion == 3:
        print("Ha salido del programa con exito.")
    else:
        print("Error.")
        print("Introduzca una opcion valida(1/2/3)")
else:
    print("Introduzca una opcion valida(1/2/3)")