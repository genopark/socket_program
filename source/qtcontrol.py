from PyQt5.QtWidgets import QFileDialog, QDialogButtonBox, QVBoxLayout, QDialog, QMessageBox

class QDialogCustom(QDialog):
    def __init__(self, *args, **kwargs):
        super(QDialogCustom, self).__init__(*args, **kwargs)

        self.setWindowTitle()
        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

class QFDCustom(QFileDialog):
    def __init__(self, *args, **kwargs):
        super(QFDCustom, self).__init__(*args, **kwargs)

    def getCsvPath(self):
        qfd = QFileDialog()
        title = "Select CSV File"
        path = "C:\\"
        filter = "csv(*.csv)"
        f = QFileDialog.getOpenFileName(qfd, title, path, filter)
        return f

class QMsgCustom(QMessageBox):
    def __init__(self, *args, **kwargs):
        super(QMsgCustom, self).__init__(*args, **kwargs)

    def showErrorMessage(self, msg="", info_msg = ""):
        self.setIcon(QMessageBox.Critical)
        self.setText(msg)
        self.setInformativeText(info_msg)
        self.setWindowTitle("Error")
        self.exec_()
