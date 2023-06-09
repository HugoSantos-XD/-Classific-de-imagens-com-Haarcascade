import cv2 #importando a biblioteca do OpenCv 

camera = cv2.VideoCapture(0)
classificador = cv2.CascadeClassifier(r'cascades/haarcascade_eye.xml') #procurando o arquivo xml 

while True:
    check,img = camera.read() #abrindo a camera

    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #converter imagem colorida para cinza
    objetos = classificador.detectMultiScale(imgGray,minSize=(50,50),scaleFactor = 1.5) #detectar olhos na imagem cinza

    # print(objetos) #detectando as coordenadas de onde os olhos estão 
    for x,y,l,a in objetos:
        cv2.rectangle(img,(x,y),(x+l,y+a),(255,0,0),2) #retangulo irá mapear os olhos
    cv2.imshow('IMAGEM',img) #exibir imagem original
    if cv2.waitKey(1) & 0xFF == ord('q'):
                break


