import cv2

def capture_video():
    # Inicia a captura de vídeo da webcam
    cap = cv2.VideoCapture(0)

    # Verifica se a captura foi aberta corretamente
    if not cap.isOpened():
        print("Erro ao acessar a webcam.")
        return

    # Carrega o classificador Haar Cascade para detecção de rostos
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    try:
        while True:
            # Captura frame por frame
            ret, frame = cap.read()

            if not ret:
                break

            # Converte o frame para escala de cinza
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detecta rostos no frame
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            # Desenha retângulos ao redor dos rostos detectados
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            # Exibe o frame com detecções
            cv2.imshow('Face Detection', frame)

            # Parar o loop ao pressionar a tecla 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    except KeyboardInterrupt:
        pass

    # Libera a captura de vídeo e fecha todas as janelas
    cap.release()
    cv2.destroyAllWindows()

# Chama a função para capturar e exibir vídeo da webcam
if __name__ == "__main__":
    capture_video()