def main():
    try:
        open('config.txt')
    except OSError as err:
        if err.errno == 2:
            print("No se pudo encontrar el archivo config.txt")
        elif err.errno == 13:
            print("Encontré config.txt pero es un directorio, no pude leerlo")


if __name__ == '__main__':
    main()