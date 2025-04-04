import cv2
import face_recognition as fr
from PIL import Image

foto_control = fr.load_image_file("dia14/FotoA.jpg")
foto_prueba = fr.load_image_file("dia14/FotoC.jpg")

foto_control = cv2.cvtColor(foto_control, cv2.COLOR_BGR2RGB)
foto_prueba = cv2.cvtColor(foto_prueba, cv2.COLOR_BGR2RGB)


cara_control = fr.face_locations(foto_control)[0]
cara_control_encoded = fr.face_encodings(foto_control)[0]

cara_prueba = fr.face_locations(foto_prueba)[0]
cara_prueba_encoded = fr.face_encodings(foto_prueba)[0]

cv2.rectangle(foto_control, (cara_control[3], cara_control[0]), (cara_control[1], cara_control[2]), (0, 255, 0), 2)
cv2.rectangle(foto_prueba, (cara_prueba[3], cara_prueba[0]), (cara_prueba[1], cara_prueba[2]), (0, 255, 0), 2)

resultado = fr.compare_faces([cara_control_encoded], cara_prueba_encoded)
print(f"Misma persona? {resultado[0]}")

dis = fr.face_distance([cara_control_encoded], cara_prueba_encoded)[0]
cv2.putText(foto_prueba, f"{resultado} {dis.round(2)}", (10, 30), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 0), 2)

cv2.imshow("Foto Control", foto_control)
cv2.imshow("Foto Prueba", foto_prueba)
cv2.waitKey(0)
cv2.destroyAllWindows()