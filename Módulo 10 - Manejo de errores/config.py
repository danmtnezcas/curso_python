def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("No se pudo encontrar el archivo config.txt!")
    except PermissionError:
        print("Encontré config.txt pero es un directorio, no pude leerlo")


if __name__ == '__main__':
    main()