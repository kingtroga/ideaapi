import threading
import websocket
import json


def receive_messages(ws):
    while True:
        try:
            message = ws.recv()
        except websocket._exceptions.WebSocketConnectionClosedException:
            break
        try:
            data = json.loads(message)
        except json.decoder.JSONDecodeError:
            try:
                ws.close()
            except websocket._exceptions.WebSocketConnectionClosedException:
                break
            print("Bye...")
            break
        if ('user' in data) and ('message' in data):
            if data['user'] != 'Damisi Babalola':
                print(f"\n{data['user']}: {data['message']}\n")

def send_messages(message):
    global message_to_send
    message_to_send = message
    data = json.dumps({'message': message_to_send})
    ws.send(data)


if __name__ == "__main__":
    ws = websocket.WebSocket()
    ws.connect("ws://127.0.0.1:8000/ws/chat/lobby/c310020b3769b40be179be8b60396b161b5c7512/")

    data = json.loads(ws.recv())
    print(data)

    # Start two threads for receiving and sending messages
    receive_thread = threading.Thread(target=receive_messages, args=(ws,))

    receive_thread.start()

    try:
        while True:
            message = input("Enter your message: ")
            if message.lower() == 'exit':
                break
            send_messages(message)
    except KeyboardInterrupt:
        pass
    finally:
        ws.close()


  

