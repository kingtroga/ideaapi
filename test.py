import threading
import websocket
import json

def receive_messages(ws):
    while True:
        message = ws.recv()
        data = json.loads(message)
        print(f"{data['user']}: {data['message']}")

def send_messages(ws):
    while True:
        message = input("Enter your message (type 'exit' to close the connection): ")
        if message == 'exit':
            break
        data = {'message': message}
        ws.send(json.dumps(data))

if __name__ == "__main__":
    ws = websocket.WebSocket()
    ws.connect("ws://127.0.0.1:8000/ws/chat/lobby/c310020b3769b40be179be8b60396b161b5c7512/")

    # Start two threads for receiving and sending messages
    receive_thread = threading.Thread(target=receive_messages, args=(ws,))
    send_thread = threading.Thread(target=send_messages, args=(ws,))

    receive_thread.start()
    send_thread.start()

    # Wait for both threads to finish
    receive_thread.join()
    send_thread.join()

    ws.close()
