import csv

# 'with' se usa para crear un contexto de manejo del archivo.
# Sin usarlo, tendriamos que administrar el abrir y cerrar de el archivo nosotros mismos

# Aqui estamos abriendo el archivo, y pasando la 'r' para 'read' y asignandolo a la variable 'csv_file'
with open('spreadsheet-01.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # si quieres brincarte la primera fila, Por ejemplo para no capturar los titulos
    next(csv_reader)

    # En este loop, cada linea del archivo csv es accessible como un List de strings.
    for line in csv_reader:
        print(
            line)  # si solamente quieres cierta columna, puedes acceder pasando el indice como line[2] te daria los valores de la tercera columna

# ejemplo de como tomar los valores de un archivo y escribirlos a un archivo nuevo usando un '-' como separador(delimiter) en lugar de comma
# cuando ejecutes esto, un nuevo archivo sera creado. Cuando esto suceda en cualquier ejemplo, borra ese archivo
with open('spreadsheet-01.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('new_names.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file,
                                delimiter='-')  # podrias usar \t para crear un espacio de tabs o cualquier otra cosa

        for line in csv_reader:
            csv_writer.writerow(line)

# ejemplo de como leer un csv file que usa algo mas que un comma
with open('spreadsheet-01.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
