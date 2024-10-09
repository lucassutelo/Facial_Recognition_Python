
# Sistema de Reconhecimento Facial 👤📸

Este projeto implementa um sistema de reconhecimento facial em tempo real utilizando a webcam e imagens armazenadas para identificar pessoas. Ele utiliza as bibliotecas OpenCV para captura de vídeo e a Face Recognition para identificar e verificar as faces.

## 🚀 Funcionalidades

- **Detecção e reconhecimento facial em tempo real**: Captura frames de vídeo via webcam, detecta rostos e tenta reconhecer pessoas previamente armazenadas no sistema.
- **Codificação de rostos**: O sistema utiliza imagens pré-carregadas para gerar codificações faciais, que são comparadas com as faces detectadas.
- **Interface interativa**: Desenha retângulos e rótulos ao redor das faces no vídeo em tempo real, exibindo o nome da pessoa identificada.

## 🛠️ Tecnologias Utilizadas

- **Linguagem**: Python 🐍
- **Bibliotecas**:
  - `face_recognition` para codificação e comparação facial
  - `OpenCV (cv2)` para captura e processamento de vídeo
  - `NumPy` para manipulação de arrays

## 🏗️ Estrutura do Projeto
 - ┣ 📜 facial_recognition.py   # Código principal para reconhecimento facial
 - ┣ 📜 facial_detection.py     # Código auxiliar para deteção facial
 - ┗ 📂 images/                 # Pasta com imagens de referência

## 📸 Como Funciona

1. O sistema carrega todas as imagens da pasta `images/`, gera codificações faciais e associa cada codificação ao nome da pessoa (baseado no nome do arquivo).
2. Utiliza a webcam para capturar frames de vídeo em tempo real.
3. Compara os rostos detectados no vídeo com as codificações previamente carregadas.
4. Se um rosto for reconhecido, desenha um retângulo ao redor dele e exibe o nome. Caso contrário, exibe a mensagem "Desconhecido".

## 🖥️ Como Executar o Projeto

1. Clone este repositório:
   ```bash
   git clone https://github.com/lucassutelo/reconhecimento-facial.git
   ```

2. Instale as dependências:
   ```bash
   sudo apt install cmake #para linux
   pip install -r requirements.txt
   ```

4. Coloque imagens de rostos na pasta `images/` com o nome da pessoa (ex: `joao1.jpg`, `maria1.png`).

5. Execute o script principal:
   ```bash
   python facial_recognition.py
   ```

6. Pressione 'q' para encerrar o programa.

## 📝 Requisitos

- Python 3.x
- Instalar as bibliotecas necessárias:
  ```bash
  sudo apt install cmake #para linux
  pip install face_recognition opencv-python numpy
  ```

## 📄 Licença

Este projeto está sob a licença MIT.
