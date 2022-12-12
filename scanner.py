import socket


TARGET_IP = "127.0.0.1"
STARTED_PORT = 1
FINISHED_PORT = 1024


for port in range(STARTED_PORT, FINISHED_PORT+1):
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  result = sock.connect_ex((TARGET_IP, port))
  if result == 0:
    print("Port {}: OPEN".format(port))
  sock.close()
