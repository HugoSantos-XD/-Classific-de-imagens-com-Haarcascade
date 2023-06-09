import cv2 #importando a biblioteca do OpenCv 

video = cv2.VideoCapture(0)

amostra = 1

while True:
    check,img = video.read() #abrindo a camera
    imgCinza = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #converter imagem colorida para cinza

    if cv2.waitKey(1) & 0xFF == ord('q'):
                imgR = cv2.resize(imgCinza,(220,220))
                cv2.imwrite(f'fotos/p/im{amostra}.jpg',imgR)
                amostra += 1
    cv2.imshow('imagem',img)
    cv2.waitKey(1)

