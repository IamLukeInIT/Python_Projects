from PySide6.QtWidgets import QApplication, QWidget, QPushButton
from subprocess import Popen

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setup()

    def setup(self):
        pass

        #location 1
        sw0_core_btn = QPushButton("SW0_CORE", self)
        sw0_core_btn.move(15, 70)
        sw0_core_btn.clicked.connect(self.sw0_core)

        sw0_4_btn = QPushButton("SW0_4", self)
        sw0_4_btn.move(15, 92)
        sw0_4_btn.clicked.connect(self.sw0_4)

        sw0_5_btn = QPushButton("SW0_5", self)
        sw0_5_btn.move(15, 114)
        sw0_5_btn.clicked.connect(self.sw0_5)

        sw0_8_btn = QPushButton("SW0_8", self)
        sw0_8_btn.move(15, 136)
        sw0_8_btn.clicked.connect(self.sw0_8)

        ##location 2
        sw1_core_btn = QPushButton("SW1_CORE", self)
        sw1_core_btn.move(15, 158)

        sw1_1_btn = QPushButton("SW1_1", self)
        sw1_1_btn.move(15, 180)

        sw1_2_btn = QPushButton("SW1_2", self)
        sw1_2_btn.move(15, 202)

        sw1_3_btn = QPushButton("SW1_3", self)
        sw1_3_btn.move(15, 224)

        sw1_4_btn = QPushButton("SW1_4", self)
        sw1_4_btn.move(15, 246)

        ##location 3
        sw2_core_btn = QPushButton("SW2_CORE", self)
        sw2_core_btn.move(15, 268)

        sw2_1_btn = QPushButton("SW2_1", self)
        sw2_1_btn.move(15, 290)

        sw2_2_btn = QPushButton("SW2_2", self)
        sw2_2_btn.move(15, 312)

        sw2_3_btn = QPushButton("SW2_3", self)
        sw2_3_btn.move(15, 334)

        sw2_4_btn = QPushButton("SW2_4", self)
        sw2_4_btn.move(15, 356)

        sw2_5_btn = QPushButton("SW2_5", self)
        sw2_5_btn.move(15, 378)

        ##location 4
        sw4_core_btn = QPushButton("SW4_CORE", self)
        sw4_core_btn.move(15, 400)

        sw4_1_btn = QPushButton("SW4_1", self)
        sw4_1_btn.move(15, 422)

        sw4_2_btn = QPushButton("SW4_2", self)
        sw4_2_btn.move(15, 444)

        sw4_3_btn = QPushButton("SW4_3", self)
        sw4_3_btn.move(15, 466)

        sw4_4_btn = QPushButton("SW4_4", self)
        sw4_4_btn.move(15, 488)

        ##location 5
        sw9_core_btn = QPushButton("SW9_CORE", self)
        sw9_core_btn.move(15, 510)

        sw9_1_btn = QPushButton("SW9_1", self)
        sw9_1_btn.move(15, 532)

        sw9_2_btn = QPushButton("SW9_2", self)
        sw9_2_btn.move(15, 554)

        sw9_3_btn = QPushButton("SW9_3", self)
        sw9_3_btn.move(15, 576)

        sw9_4_btn = QPushButton("SW9_4", self)
        sw9_4_btn.move(15, 598)

        sw9_5_btn = QPushButton("SW4_5", self)
        sw9_5_btn.move(15, 620)

        sw9_6_btn = QPushButton("SW9_6", self)
        sw9_6_btn.move(15, 642)

        sw9_7_btn = QPushButton("SW9_7", self)
        sw9_7_btn.move(15, 664)

        sw9_8_btn = QPushButton("SW9_8", self)
        sw9_8_btn.move(15, 686)

        sw9_9_btn = QPushButton("SW9_9", self)
        sw9_9_btn.move(15, 708)

        ##location 6
        sw16_1_btn = QPushButton("SW16_1", self)
        sw16_1_btn.move(15, 730)

        #WLC
        wlc_btn = QPushButton("WLC0_1", self)
        wlc_btn.move(15, 752)

        #PRIME
        prime_btn = QPushButton("PRIME", self)
        prime_btn.move(15, 774)

        #ISE
        ise_btn = QPushButton("ISE", self)
        ise_btn.move(15, 796)

        #FMC
        fmc_btn = QPushButton("FMC", self)
        fmc_btn.move(15, 818)


        self.setFixedSize(100, 850)
        self.setWindowTitle("SSH Dashboard")

        self.show()    

    #button actions
    def sw0_core(self):
        Popen("powershell putty.exe user@address_ip")

    def sw0_4(self):
        Popen("powershell putty.exe user@address_ip")

    def sw0_5(self):
        Popen("powershell putty.exe user@address_ip")

    def sw0_8(self):
        Popen("powershell putty.exe user@address_ip") 

if __name__ == "__main__":
    app = QApplication([]) 

    login_window = LoginWindow()

    app.exec()    
