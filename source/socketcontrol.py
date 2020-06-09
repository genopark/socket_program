import os, socket
from source import threadcontrol

class SockControl(socket.socket):
    def __init__(self, type=socket.AF_INET, stream=socket.SOCK_STREAM):
        #socket.socket.__init__(self, type, stream)
        socket.socket.__init__(self)
        self.host = ''
        self.port = 54321
        self.file_dir = "//downloads"
        self.file_name = "sample"

    def connectClient(self, recv_dir):
        # connect to server
        self.connect((self.host, self.port))
        print("Connected to: " + str(self.host))

        # save file in directory
        file = open(recv_dir, 'wb')
        file_data = self.recv(1024)
        file.write(file_data)
        file.close()
        self.reset()
        print("File downloaded, socket reset.")

    def echoServer(self):
        # wait for connection
        m_hostname = socket.gethostname()
        host = socket.gethostbyname(m_hostname)
        port = 8080
        self.bind((host, port))
        self.listen(1)
        print("Computer Name is:" + m_hostname)
        print("Computer IP Address is:" + host)
        print("Waiting for any incoming conections ...")

        # connection made by client
        conn, addr = self.accept()
        print(addr, " has connected to the server")
        filename = self.file_dir + "\\" + self.file_name
        #filename = 'D:\\python_projects\\serverclient\\server\\sample.txt'
        file = open(filename, 'rb')
        file_data = file.read(1024)
        conn.send(file_data)
        print("Data has been transmitted successfully")
        self.reset()

    def echoThreadedServer(self):
        d = threadcontrol.ThreadCtrl('ServerThread')
        d.startThread(self.echoServer)

    def getHostIP(self):
        return self.host

    def reset(self):
        self.close()
        self.__init__()

    def setFile(self, dir, name):
        self.setfiledir(dir)
        self.setFileName(name)

    def setFileDir(self, dir):
        self.file_dir = dir

    def setFileName(self, name):
        self.file_name = name

    def setIP(self, host, port):
        self.host = host
        self.port = port

class QSockControl():
    def __init__(self):
        self.s = 2