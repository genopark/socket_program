import os, sys
import logging
import threading
import time
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
import socket
from source import socketcontrol, threadcontrol

class Ui(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(Ui, self).__init__()
        uic.loadUi('main.ui', self)
        self.setWindowTitle('Socket program')
        self.show()

        # setup server and client
        self.server = socketcontrol.SockControl()
        self.serverThread = threadcontrol.ThreadCtrl('Thread_Server')
        self.client = socketcontrol.SockControl()

        # file menu
        self.btnExit = self.findChild(QtWidgets.QAction, 'btnExit')

        # file transfer tab
        self.btnServerEcho = self.findChild(QtWidgets.QPushButton, 'btnServerEcho')
        self.tbServerHostName = self.findChild(QtWidgets.QLineEdit, 'tbServerHostName')
        self.tbServerIP = self.findChild(QtWidgets.QLineEdit, 'tbServerIP')
        self.btnConnectClient = self.findChild(QtWidgets.QPushButton, 'btnConnectClient')
        self.tbConnectClient = self.findChild(QtWidgets.QLineEdit, 'tbConnectClient')
        self.tbClientFileDir = self.findChild(QtWidgets.QLineEdit, 'tbClientFileDir')
        self.btnSelectSendFile = self.findChild(QtWidgets.QPushButton, 'btnSelectSendFile')
        self.btnSetRecvFileDir = self.findChild(QtWidgets.QPushButton, 'btnSetRecvFileDir')

        # qt gui signals
        self.setupSignals()

    def __del__(self):
        x = threadcontrol.ThreadCtrl('Thread_1')
        x.printActiveThreads()
        print('Destructor Executed...')

    def btnServerEchoPressed(self):
        # populate host names
        self.tbServerIP.setText(socket.gethostbyname(socket.gethostname()))
        self.tbServerHostName.setText(socket.gethostname())
        self.server.echoServer()
        self.statusBar().showMessage('File sent successfully!')

    def btnConnectClientPressed(self):
        self.client.setIP(str(self.tbConnectClient.text()), 8080)
        m_recv_dir = 'D:\\python_projects\\socket_program\\downloads\\sample.txt'
        self.client.connectClient(m_recv_dir)

    def btnSelectSendFilePressed(self):
        f = QFileDialog.getOpenFileName(self, "Select File")
        file_dir = str(f[0])
        path, filename = os.path.split(file_dir)
        self.server.setFile(path, filename)

    def btnSetRecvFileDirPressed(self):
        f = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.client.setFileDir(str(f))
        self.tbClientFileDir.setText(str(f))

    def closeApp(self):
        app.quit()

    def setupSignals(self):
        # file menu
        self.btnExit.triggered.connect(self.closeApp)
        self.btnExit.setShortcut("Ctrl+Q")
        self.btnExit.setStatusTip('Leave The App')

        # file transfer tab
        self.btnServerEcho.clicked.connect(self.btnServerEchoPressed)
        self.btnConnectClient.clicked.connect(self.btnConnectClientPressed)
        self.btnSelectSendFile.clicked.connect(self.btnSelectSendFilePressed)
        self.btnSetRecvFileDir.clicked.connect(self.btnSetRecvFileDirPressed)

# execute qt gui
app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()