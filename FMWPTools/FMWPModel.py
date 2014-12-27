# -*- coding: utf-8 -*-
__author__ = '奕成'
import sys
import subprocess
import re
import fmwp_mainwindow
from fmwp_mainwindow import Ui_MainWindow
from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import QMessageBox
from PyQt4.QtGui import QStandardItemModel
from PyQt4.QtGui import QStandardItem

def get_specified_wifi_info(wifi_name):
        """
        Get specified wifi detail info
        :param wifi_name: The wifi detail info you want
        :return:The detail info (decoded big5)
        """
        wifi_detail_result = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles', 'name='+wifi_name, 'key=clear'])
        return wifi_detail_result.decode("big5")

def get_wifi_password(specified_wifi_info):
        """
        Get specified wifi detail info
        :param wifi_name: The wifi detail info you want (input para need utf-8 encode)
        :return:The detail info
        """
        # Extract password line by matching 金鑰內容.+\r\n|Key Content.+\r\n
        # Because the python program is utf-8 so need to encode wifi_detail_result to utf8
        password_line_message = re.findall("金鑰內容.+\r\n|Key Content.+\r\n", specified_wifi_info)
        if len(password_line_message) != 0:
            for i in range(0, len(password_line_message)):
                password = password_line_message[i]
                password = password[password.index(':')+2:password.index('\r')]
                return password
        else:
            return None
def get_history_connected_wifi():
    """
    Get the history connected wifi list by operating windows built-in netsh script
    :return:All connected wifi list
    """
    # shell=True means the command is run in the windows cmd COMSPEC / Unix bash /bin/sh
    # netsh is a batch script ,so don't need to type cmd or set shell=True
    wifi_profiles_result = subprocess.check_output(["netsh", "wlan", "show", "profiles"])
    # Windows cmd encoder is big5 ,so decode big5 by using unicode
    history_wifi_list = []
    # find all matched string and put into list
    #: .+\W => The start string is : and end \r\n , .+ means any characters
    temp_list = re.findall(": .+\r\n", unicode(wifi_profiles_result, "big5"))
    # clear : and \r\n by replacing specified string,note: | is or so means if match : or \r\n then replace to ""
    for i in range(0, len(temp_list)):
        # Get clear wifi name (remove : and \r\n)
        # Method 1 : regular expression:
        # history_wifi_list.append(re.sub(": |\r\n","",temp_list[i]))
        # Method 2 : Get the password by slicing
        wifi_name_line = temp_list[i]
        history_wifi_list.append(wifi_name_line[wifi_name_line.index(':')+2:wifi_name_line.index('\r')])
    return history_wifi_list


class MainWindow(QMainWindow, Ui_MainWindow):
    selected_index = -1
    history_wifi_list = []
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.showHistoryWIFIButton.clicked.connect(self.on_show_history_wifi_name)
        self.findMissingPasswordButton.clicked.connect(self.on_show_password)
        self.showWIFIListView.clicked.connect(self.on_wifi_listview_selected)

    @pyqtSlot()
    def on_show_history_wifi_name(self):
        self.history_wifi_list = get_history_connected_wifi()
        model = QStandardItemModel(self.showWIFIListView)
        # Get each history wifi name
        for wifi_name in  self.history_wifi_list:
            item = QStandardItem(wifi_name)
            # Add the item to the model
            model.appendRow(item)
        self.showWIFIListView.setModel(model)
        self.showWIFIListView.show()

    @pyqtSlot("QModelIndex")
    def on_wifi_listview_selected(self, index):
        """
        Get Selected item's index from QListView
        :param index:Selected item's index (QModelIndex Object ) from QListView
        :return:Selected index
        """
        # Get selected index from QListView
        self.selected_index = index.row()

    @pyqtSlot()
    def on_show_password(self):
        _msg_box = QMessageBox()

        if self.selected_index != -1 and len(self.history_wifi_list) > 0:
            wifi_name = self.history_wifi_list[self.selected_index]
            wifi_detail_result = get_specified_wifi_info(wifi_name)
            # Because the python program is utf-8 so need to encode wifi_detail_result to utf8
            password = get_wifi_password(wifi_detail_result.encode("utf-8"))
            if password is not None:
                _msg_box.setWindowTitle("Finding result")

                _msg_box.setText("The password is :" + password)
            else:
                _msg_box.setText("This wifi's password input on webpage,so can't get")
        else:
            _msg_box.setText("not choose yet")

        _msg_box.exec_()


if __name__ == "__main__":
    app = fmwp_mainwindow.QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())