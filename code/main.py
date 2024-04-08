from funciones import leer_datos, filtrar_calcular_media

def main():
    data = leer_datos('/Users/mariajosecontrerasreal/examen_evaluacionn/examen_mj/data/datos_examen.csv', 'TS')
    media = filtrar_calcular_media(data, 'Tag', 'MariaJose')
    print (media)

if __name__ == "__main__":
    main()