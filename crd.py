import socket
import os

HOST = "192.168.1.13"
PORT = 6666


def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

def menu():
    clear_console()

    print("\n1. Abrir chat")
    print("2. Screenshot")
    print("3. Desconectarse")
    choice = input("Elije una opción: ")
    return choice

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))

    print("Conexión establecida.")

    while True:
        choice = menu()
        sock.sendall(choice.encode("utf-8"))

        if choice.lower() == "1":
            clear_console()
            
            print("\n\nEstás ubicado en el chat.")
            print("Para salir del chat, escribe 'esc'.")
            print("Para hacer un capture de la pantalla principal, escribe 'esc'.")
            while True:
                message = input("Escribe tu mensaje: ")
                sock.sendall(message.encode("utf-8"))
                if message.lower() == "esc":
                    break
        elif choice == "2":
                message = "2"
                sock.sendall(message.encode("utf-8"))
        elif choice == "3":
            sock.sendall("3".encode("utf-8"))
            print("Desconectándose del servidor.")
            break    
        elif choice == "4":
                sock.sendall("4".encode("utf-8"))
        else:
            print("Opción no válida. Inténtalo de nuevo.")

except KeyboardInterrupt:
    print("\nCliente detenido por el usuario.")
finally:
    sock.close()