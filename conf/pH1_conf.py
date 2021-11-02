import PySide6
import serial
from PySide6 import QtGui
from modbus_tk import modbus_rtu
import modbus_tk.defines as cst
from ui import pH1_ui as pH1
from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QWidget
from threading import Thread
from utils.modbus_util import *
import time


class MySignal(QObject):
    aSignal = Signal(str)
    writeLog=Signal(str)

class ph_1(QWidget):
    def closeEvent(self, event: PySide6.QtGui.QCloseEvent) -> None:
        if self.port!=None:
            self.port.close()
        self.read_status = False

    def __init__(self):
        super(ph_1, self).__init__()
        # 引入子窗口类
        self.ui = pH1.Ui_Form()
        self.ui.setupUi(self)
        #控制参数
        self.read_status = True
        self.port= None
        self.adress=None
        #按钮连接
        # self.ui.con.clicked.connect(self.thread_connect)
        self.ui.con.clicked.connect(self.showDiglog)
        self.ui.uncon.clicked.connect(self.unConnect)
        self.ui.diglog.button.clicked.connect(self.closeDiglog)
        self.ui.pushButton.clicked.connect(self.change_adress)
        # 增加信息_
        self.ms = MySignal()
        self.ms.aSignal.connect(self.change_read)
        # add msg to UI
        self.ms.writeLog.connect(self.change_wirtelog)

    def showDiglog(self):
        if self.adress==None:
            self.ui.diglog.show()
        if self.port != None and self.port.is_open:
            self.thread_writeLog("当前设备已连接" + "\n" + "---------------------------------------------")
    def closeDiglog(self):
        self.adress=self.ui.diglog.edit.text()
        self.ui.diglog.accept()
        # Connect the Serial
        self.thread_connect()

    # -----------------------------------------------------
    # Function  读取通讯参数
    def thread_read(self):
        th = Thread(target=self.send_read)
        th.setDaemon(True)
        th.start()

    def send_read(self):
        # Judge the adress is rightful
        self.adress = self.ui.diglog.edit.text()
        try:
            res=self.master.execute(int(self.adress),cst.READ_HOLDING_REGISTERS,0,4)
        except:
            self.thread_writeLog("数据读取异常，请检查地址位"+"\n"+"---------------------------------------------")
            self.adress=None
            self.port.close()
            return  None

        self.read_status=True
        while (self.read_status):
            try:
                res=self.master.execute(int(self.adress),cst.READ_HOLDING_REGISTERS,0,4)
                self.ui.LineEdit.setText(str(res[0]))
                self.ui.LineEdit_2.setText(str(res[1]))
                self.ui.LineEdit_3.setText(str(res[2]))
                self.ui.LineEdit_4.setText(str(res[3]))
                time.sleep(0.8)
            except:
                print("错误，但是不会结束的")
    def change_read(self, edit):
        self.ui.LineEdit_2.setText(edit)

# -----------------------------------------------------
    # Function 连接modbus
    def thread_connect(self):
        th = Thread(target=self.send_connect)
        th.setDaemon(True)
        th.start()

    def send_connect(self):
        #串口处理
        # function->
        try:
            if self.port!=None and self.port.is_open:
                    self.thread_writeLog("当前设备已连接" + "\n" + "---------------------------------------------")
                    return None
            self.port = serial.Serial(port=getUSB(), baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=1)
            self.master = modbus_rtu.RtuMaster(self.port)
            self.master.set_timeout(5.0)
            self.master.set_verbose(True)
            self.thread_writeLog("连接成功" + "\n" + str(self.port) + "\n" + "---------------------------------------------")
            # Read Serial Data
            self.read_status=True
            self.thread_read()
        except :
            self.adress=None
            self.thread_writeLog("连接失败，请正确选择设备，并仔细检查接线"+"\n"+"---------------------------------------------")

    def change_connect(self, edit):
        self.ui.LineEdit_2.setText(edit)
#  -----------------------------------------------------
    # Write the Log of User

    def thread_writeLog(self,msg):
        th=Thread(target=self.send_writeLog,args=(msg,))
        th.start()
    def send_writeLog(self,msg):
        self.ms.writeLog.emit(str(msg))
    def change_wirtelog(self,msg):
        self.ui.textBrowser.append(msg)
#  -----------------------------------------------------
    #关闭当前连接

    def unConnect(self):
        self.read_status=False
        if self.port!=None:
            self.port.close()
            self.adress=None
            self.thread_writeLog("连接已断开"+"\n"+"---------------------------------------------")
            return None
        self.thread_writeLog("未建立连接" + "\n" + "---------------------------------------------")

#  -----------------------------------------------------
    # 改变设备地址位
    def change_adress(self):
        self.read_status=False
        if eval(self.adress)<10:
            adress="0"+self.adress
        if eval(self.ui.lineEdit.text())<10:
            changeAdress="0"+self.ui.lineEdit.text()
        send_data = bytes.fromhex(crc16Add(adress+" 10 00 02 00 01 02 00 "+changeAdress))
        resp = self.port.write(send_data)
        self.close()
#  -----------------------------------------------------









