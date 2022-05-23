from __future__ import print_function
# importamos las librerias que necesitaremos para llevar a  cabo el desarrollo del codigo
import cv2


def main():
    # invocamos la imagen

    image = cv2.imread('pokemon.jpg')
    # mostraremos la imagen
    cv2.imshow("pokemon", image)
    # punto 1 y 2 del problema

    # obtener el recorte del ojo derecho
    ojo_derecho = image[110:150, 120:160]
    imageregion(ojo_derecho, "ojo derecho")
    imagedisplay(ojo_derecho)

    # obtener el recorte del ojo izquierdo
    ojo_izquierdo = image[90:130, 60:100]
    imageregion(ojo_izquierdo, "ojo izquierdo")
    imagedisplay(ojo_izquierdo)

    # obtener el recorte de la sonrisa
    smile = image[130:170, 40:160]
    imageregion(smile, "sonrisa")
    imagedisplay(smile)

    cv2.destroyAllWindows()

    # punto 3 del problema
    image[:, :, :] = (255, 255, 255)  # blanco
    imagebackground(image)
    image[:, :, :] = (0, 0, 255)  # rojo
    imagebackground(image)
    image[:, :, :] = (255, 0, 0)  # azul
    imagebackground(image)
    image[:, :, :] = (0, 255, 0)  # verde
    imagebackground(image)
    image[:, :, :] = (0, 0, 0)  # negro
    imagebackground(image)

    cv2.destroyAllWindows()


# estas 2 funciones nos serviran para recortar el ojo derecho, el ojo izquierdo y la sonrisa y mostrarlas en ventana, ademas nos mostrara informacion en la terminal
def imageregion(image, section):
    print(f"region de interes ({section}): {image.shape}")


def imagedisplay(image):
    cv2.imshow("imagen", image)
    cv2.waitKey(0)


# esta funcion es para agregarle color a la imagen
def imagebackground(image):
    cv2.imshow("imagen", image)
    cv2.waitKey(0)


# inicializamos el codigo invocando la funcion principal llamada main

if __name__ == "__main__":
    main()

