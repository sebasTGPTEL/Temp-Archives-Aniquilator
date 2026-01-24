import os 
import shutil
import time
from datetime import datetime

paths = [
    r'C:\Users\gamer\AppData\Local\Temp',
    r'C:\Windows\Temp',
    r'C:\Windows\SoftwareDistribution\Download',
    r'C:\Users\gamer\AppData\Local\Microsoft\Windows\INetCache'
]

    
log_dir = r"C:\Users\gamer\OneDrive\Escritorio\pyhton\TempAniquilator\Logs"
os.makedirs(log_dir, exist_ok=True)

log_file = os.path.join(
    log_dir,
    f"Limpieza_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
)

def escribir_log(mensaje):
    with open (log_file, "a", encoding="utf-8") as log:
        log.write(f"[{datetime.now()}] {mensaje}\n")
        
escribir_log("=== INICIO DEL PROGRAMA ===")

def limpieza_general():
    global eliminados_arch, eliminados_carp, omitidos_arch, omitidos_carp
    eliminados_arch = 0
    eliminados_carp = 0
    omitidos_arch = 0
    omitidos_carp = 0
    for base_path in paths:
        if not os.path.exists(base_path):
            print(f"El directorio {base_path} no se encuentra")
            continue
        print(f"\nRecorriendo {base_path}")
        
        print(f"Eliminando archivos temporales de {base_path}")
        for root, dirs, files in os.walk(base_path, topdown=False):
            
            for file in files:
                try:
                    os.remove(os.path.join(root, file))
                    eliminados_arch += 1
                except FileNotFoundError:
                    omitidos_arch += 1
                    print(f"El archivo {file} se ha omitido")
                except PermissionError:
                    omitidos_arch += 1
                    print(f"El archivo {file} se ha omitido")
                    pass
                except Exception as e:
                    escribir_log(f"ERROR {e}")
                      
                
            for dir in dirs:
                dir_path = os.path.join(root, dir)
                try:
                    if os.path.islink(dir_path):
                        os.unlink(dir_path)
                    else:
                        shutil.rmtree(dir_path)
                    eliminados_carp += 1
                except FileNotFoundError:
                    omitidos_carp += 1
                    print(f"El archivo {file} se ha omitido")
                except PermissionError:
                    omitidos_carp += 1
                    print(f"La carpeta {dir} se ha omitido")   
                except Exception as e:
                    escribir_log(f"ERROR {e}")
                
                    
            print(f"La eliminacion de archivos temporales de {base_path} ha terminado.")
    print("\nRESUMEN")
    print("-----------")
    print(f"Se han eliminado {eliminados_arch} archivos.")
    print(f"Se han omitido {omitidos_arch} archivos.")
    print(f"Se han eliminado {eliminados_carp} carpetas.")
    print(f"Se han omitido {omitidos_carp} carpetas")
    escribir_log("RESUMEN")
    escribir_log(f"Se han eliminado {eliminados_arch} archivos.")
    escribir_log(f"Se han omitido {omitidos_arch} archivos.")
    escribir_log(f"Se han eliminado {eliminados_carp} carpetas.")
    escribir_log(f"Se han omitido {omitidos_carp} carpetas")
    input("\nPresiona ENTER para salir.")
    
def dry_run():
    global carpetas, archivos
    archivos = 0
    carpetas = 0
    print("\nModo Dry Run (simulacion)")
    print("-------------------------")
    
    for base_path in paths:
        if not os.path.exists(base_path):
            print(f"Directorio {base_path} no encontrado")
            continue
        
        print(f"Analizando {base_path}")
        
        for root, dirs, files in os.walk(base_path):
            for file in files:
                archivos += 1
                ruta = os.path.join(root, file)
                print(f"[DRY] Archivo → {ruta}")
                escribir_log(f"DRY-RUN ARCHIVO: {ruta}")
            
            for dir in dirs:
                carpetas += 1
                ruta = os.path.join(root, dir)
                print(f"[DRY] Carpeta → {ruta}")
                escribir_log(f"DRY-RUN CARPETA: {ruta}")
    print("\nRESUMEN")
    print("-----------")
    print(f"Se han encontrado {archivos} archivos.")
    print(f"Se han encontrado {carpetas} carpetas.")
    input("\nPresiona ENTER para salir.")
                
            
    
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

