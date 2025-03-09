import os
import platform
import socket

# System Information
print(f"Machine Type: {platform.machine()}")
print(f"Processor: {platform.processor()}")

# Set and Get
socket.setdefaulttimeout(50)
print(f"Default Socket Timeout: {socket.getdefaulttimeout()} seconds")

print(f"Operating System: {platform.system()}")
print(f"Current Process ID: {os.getpid()}")

# Fork a new process
if hasattr(os, 'fork'):
    pid = os.fork()
    if pid == 0:
        print(f"Child Process ID: {os.getpid()}")
        os._exit(0)
    else:
        os.wait()

# File Handling with os Module
file_name = "fdpractice.txt"
fd = os.open(file_name, os.O_RDWR | os.O_CREAT)

print(f"Current Process ID: {os.getpid()}")
os.write(fd, b"Some string to write to the file")
os.lseek(fd, 0, 0)

if hasattr(os, 'fork'):
    pid = os.fork()
    if pid == 0:
        print(f"Child Process ID: {os.getpid()}")
        data = os.read(fd, 100)
        print(f"File Content: {data.decode()}")
        os.close(fd)
        os._exit(0)
    else:
        os.wait()
        os.close(fd)
