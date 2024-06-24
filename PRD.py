import socket
import pyautogui
import base64
import os


def capture_screen():
    screenshot = pyautogui.screenshot()
    encoded_image = base64.b64encode(screenshot.tobytes())
    connection.sendall(encoded_image)
    # Guardar la imagen en el escritorio
    desktop_path = os.path.expanduser("~/Desktop")
    screenshot.save(os.path.join(desktop_path, "screenshot.png"))


def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


HOST = "192.168.1.13"
PORT = 6666

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST, PORT))
    sock.listen(1)

    print(f"Servidor escuchando en {HOST}:{PORT}...")

    connection, client_address = sock.accept()
    print(f"Cliente conectado desde {client_address}")

    chat = False

    while True:
        data = connection.recv(1024).decode("utf-8")

        if data.lower() == "exit" or data == "3":
            print("Cliente solicitó cerrar la conexión.")
            break
        elif data.lower() == "esc":
            chat = False
        elif data == "1" or chat:
            if chat == False:
                clear_console()
                print("\n\nEstás ubicado en el chat.")
                print("Para salir del chat, escribe 'esc'.")

            chat = True
            print(data)
        elif data == "2":
            capture_screen()

except KeyboardInterrupt:
    print("\nServidor detenido por el usuario.")
finally:
    sock.close()
    print("Servidor desconectado")
