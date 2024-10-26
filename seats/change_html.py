import os

def convertir_txt_a_html(carpeta_base):
    # Recorre todas las carpetas y subcarpetas en el directorio base
    for root, dirs, files in os.walk(carpeta_base):
        for file in files:
            if file.endswith(".txt"):
                ruta_txt = os.path.join(root, file)
                
                # Lee el contenido del archivo txt
                with open(ruta_txt, 'r', encoding='utf-8') as archivo_txt:
                    contenido_txt = archivo_txt.read()
                
                # Define la ruta del archivo HTML
                nombre_html = file.replace('.txt', '.html')
                ruta_html = os.path.join(root, nombre_html)
                
                # Escribe el contenido directamente en el archivo HTML
                with open(ruta_html, 'w', encoding='utf-8') as archivo_html:
                    archivo_html.write(contenido_txt)
                
                print(f"Archivo HTML creado: {ruta_html}")

# Especifica la carpeta base como el mismo nivel donde está el script
carpeta_base = os.path.dirname(__file__)
convertir_txt_a_html(carpeta_base)
