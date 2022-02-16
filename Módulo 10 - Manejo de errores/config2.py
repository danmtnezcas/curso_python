def main():
    try:
        open("/path/to/mars.jpg")
    except FileNotFoundError as err:
        print("No se pudo encontrar el archivo config.txt!", err)
        
        

if __name__ == '__main__':
    main()