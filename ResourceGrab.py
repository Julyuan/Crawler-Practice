#import requests
#from bs4 import BeautifulSoup
#import pyqt4
#def crawler(url, form = None):
#    try:
#        r = requests.post(url, timeout = 30, data = form)
#        r.encoding = r.apparent_encoding
#        return r.text
#    except:
#        print("爬虫发生异常")

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLineEdit
from PyQt5.QtGui import QIcon

class Example(QWidget):

    def __init__(self, parent = None):

        super(Example, self).__init__(parent)
        self.initUI()

    def initUI(self):

        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle('icourse资料下载')
        self.setWindowIcon(QIcon('xdbcb8.ico'))

        self.bt1 = QPushButton('下载', self)
        self.bt1.setGeometry(215, 350, 70 ,30)
        self.bt1.setToolTip('<b>点击这里</b>')
        self.bt1.clicked.connect(self.showMessage)  

        self.text1 = QLineEdit('在这里输入网址', self)
        self.text1.selectAll()
        self.text1.setFocus()
        self.text1.setGeometry(125, 200, 250 ,30)
        
        self.text2 = QLineEdit('在这里输入资料的名字',self)
        self.text2.selectAll()
        self.text2.setFocus()
        self.text2.setGeometry(125,100,250,30)

        self.show()    

    def showMessage(self):
        input_url = str(self.text1.text())
        input_name = str(self.text2.text())
        out_str = '你输入的url地址是' + input_url + ',你输入的资料名是' + input_name
        QMessageBox.about(self, "123", out_str)    
            
    def closeEvent(self, event):

        reply = QMessageBox.question(self, '确认', '确认退出吗', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()        
        else:
            event.ignore()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())