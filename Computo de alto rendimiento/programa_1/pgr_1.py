from email.mime import image
from itertools import count
import os
import cv2

input_images_path = "/home/ismael/PycharmProjects/Computo de alto rendimiento/programa_1"
files_names = os.listdir(input_images_path)
#print(files_names)
#print("paso 1")
count=1
for file_name in files_names:
    #print("paso 2 dentro del for")
    if file_name.split(".")[-1] not in ["jpg"]:
        continue
    
    print(file_name)
    #print("Paso 3 saliendo del primer if")
    image_path= input_images_path +"/"+ file_name
    #print(image_path)
    image= cv2.imread(image_path)
    #print("paso 4 despues de leer imagen")
    
    if image is None:
        continue

    cv2.imshow("Image" + str(count), image)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()
    cv2.imwrite("Nueva_imagen"+str(count)+".jpg", image)
    count+=1
    #print("final despues del contador")