import re
import os
import string
import webbrowser
from PyQt5 import QtCore, QtGui, QtWidgets

from gui.ray_fusion import *
from core.variables import *
from core.toolbox.bruteforce_core import *


tutorial_link = "http://www.youtube.com/watch?v=_ztQQWMoVX4"    # Video Tutorial link


class Ray_Fusion(QtWidgets.QDialog,Ui_ray_fusion):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        self.retranslateUi(self)

        self.custom_user_wordlist = str()          # Path to the custom user wordlist
        self.custom_password_wordlist = str()      # Path to the custom password wordlist

        self.start_flag = True                      # If False then Stop

        self.table_index = 0
        self.bruteforce_core = Bruteforce_Attack()      # Bruteforce Attack Class

        self.http_https_pixmap = QtGui.QPixmap("%s/resources/Page-World.ico" % (os.getcwd()))
        self.telnet_pixmap = QtGui.QPixmap("%s/resources/Application-Osx-Terminal.ico" % (os.getcwd()))
        self.ftp_pixmap = QtGui.QPixmap("%s/resources/Ftp.ico" % (os.getcwd()))
        self.red_led = QtGui.QPixmap("%s/resources/red_led.png" % (os.getcwd()))
        self.green_led = QtGui.QPixmap("%s/resources/green_led.png" % (os.getcwd()))

        self.http_https_radio.clicked.connect(self.HTTP_HTTPS_Mode)
        self.telnet_radio.clicked.connect(self.TELNET_Mode)
        self.ftp_radio.clicked.connect(self.FTP_Mode)
        self.default_wordlist_radio.clicked.connect(self.select_Wordlist_type)
        self.custom_wordlist_radio.clicked.connect(self.select_Wordlist_type)
        self.settings_button.clicked.connect(self.show_hide_settings)
        self.help_button.clicked.connect(self.show_help)
        self.launch_bruteforce.clicked.connect(self.Start_Attack)

        self.save_credentials.clicked.connect(self.save_bruteforced_credentials)
        self.clear_credentials.clicked.connect(self.clear_bruteforced_credentials)

        self.userlist_button.clicked.connect(self.select_custom_user_wordlist)
        self.passwordlist_button.clicked.connect(self.select_custom_password_wordlist)

        self.bruteforce_core.Next_Try_signal.connect(self.display_progress)
        self.bruteforce_core.We_Got_Error_signal.connect(self.display_error_message)
        self.bruteforce_core.successful_login_signal['QString', 'QString'].connect(self.show_credentials)

        self.bruteforce_core.Finished_bruteforce_signal.connect(self.Stop_Notification)

        self.reset_objects()
        self.set_Window_Max()

        self.HTTP_HTTPS_Mode()
        self.custom_wordlist_groupbox.setVisible(False)




    def reset_objects(self):
        self.credential_table.clear()
        self.save_credentials.setEnabled(False)
        self.clear_credentials.setEnabled(False)
        self.statistics_username.setText("Username: ")
        self.statistics_password.setText("Password: ")
        self.statistics_percentage.setText("0% Complete")


    def set_Window_Max(self):
        try:
            self.setWindowFlags(
            QtCore.Qt.WindowMinMaxButtonsHint |
            QtCore.Qt.WindowCloseButtonHint |
            QtCore.Qt.Dialog)
        except:pass


    def show_help(self):
        QtWidgets.QMessageBox.about(self,"About Fern - Ray Fusion","Fern - Ray Fusion is a bruteforce attack tool used to audit the list of supported network services and returns login credentials of the target service when successful.")
        answer = QtWidgets.QMessageBox.question(self,"Tutorial","Would you like to view a video tutorial on how to use the tool?",QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if(answer == QtWidgets.QMessageBox.Yes):
            webbrowser.open_new_tab(tutorial_link)


    def HTTP_HTTPS_Mode(self):
        self.port_edit.setVisible(False)
        self.label.setPixmap(self.http_https_pixmap)
        self.target_edit.clear()
        self.target_edit.setFocus()

    def TELNET_Mode(self):
        self.port_edit.setVisible(True)
        self.port_edit.setText("23")
        self.label.setPixmap(self.telnet_pixmap)
        self.target_edit.clear()
        self.target_edit.setFocus()

    def FTP_Mode(self):
        self.port_edit.setVisible(True)
        self.port_edit.setText("21")
        self.label.setPixmap(self.ftp_pixmap)
        self.target_edit.clear()
        self.target_edit.setFocus()


    def select_Wordlist_type(self):
        if(self.default_wordlist_radio.isChecked()):
            self.custom_wordlist_groupbox.setVisible(False)
            return
        self.custom_wordlist_groupbox.setVisible(True)


    def show_hide_settings(self):
        if(self.settings_groupbox.isVisible()):
            self.settings_button.setText("Show Settings")
            self.settings_groupbox.setVisible(False)
            self.custom_wordlist_groupbox.setVisible(False)
            return
        self.settings_button.setText("Hide Settings")
        self.settings_groupbox.setVisible(True)
        self.select_Wordlist_type()


    def select_custom_user_wordlist(self):
        self.custom_user_wordlist = str()
        path = QtWidgets.QFileDialog.getOpenFileName(self,"Select User Wordlist",str())[0]
        if(path):
            self.custom_user_wordlist = path
            self.user_wordlist_led.setPixmap(self.green_led)
            return
        self.custom_user_wordlist = str()
        self.user_wordlist_led.setPixmap(self.red_led)


    def select_custom_password_wordlist(self):
        self.custom_password_wordlist = str()
        path = QtWidgets.QFileDialog.getOpenFileName(self,"Select Password Wordlist",str())[0]
        if(path):
            self.custom_password_wordlist = path
            self.password_wordlist_led.setPixmap(self.green_led)
            return
        self.custom_password_wordlist= str()
        self.password_wordlist_led.setPixmap(self.red_led)


    def display_progress(self):
        statistics = self.bruteforce_core.next_try_details                      # [23%,"username","password"]
        self.statistics_percentage.setText("<font color=green><b>" + statistics[0] + " Complete</b></font>")
        if(len(statistics[1]) > 7):
            self.statistics_username.setText("Username: <font color=green>" + statistics[1][0:7] + "...</font>")
        else:
            self.statistics_username.setText("Username: <font color=green>" + statistics[1] + "</font>")
        if(len(statistics[2]) > 7):
            self.statistics_password.setText("Password: <font color=green>" + statistics[2][0:7] + "...</font>")
        else:
            self.statistics_password.setText("Password: <font color=green>" + statistics[2] + "</font>")



    def clear_table(self):
        self.table_index = 0
        row_number = self.credential_table.rowCount()
        column_number = self.credential_table.columnCount()

        for row in range(row_number):
            self.credential_table.removeRow(0)

        for column in range(column_number):
            self.credential_table.removeColumn(0)

        self.save_credentials.setEnabled(False)
        self.clear_credentials.setEnabled(False)


    def display_table_header(self):
        self.clear_table()
        column_headers = ("Username","Password")
        for column,header in enumerate(column_headers):
            self.credential_table.insertColumn(column)
            column_header = QtWidgets.QTableWidgetItem()
            self.credential_table.setHorizontalHeaderItem(column,column_header)
            self.credential_table.horizontalHeaderItem(column).setText(header + ' '* 5)
            self.credential_table.resizeColumnsToContents()


    def show_credentials(self,username,password):
        if(not self.credential_table.columnCount()):
            self.display_table_header()

        self.credential_table.insertRow(self.table_index)


        item = QtWidgets.QTableWidgetItem()
        self.credential_table.setItem(self.table_index,0,item)
        item.setText(str(username) + ' ' * 5)

        item = QtWidgets.QTableWidgetItem()
        self.credential_table.setItem(self.table_index,1,item)
        item.setText(str(password) + ' ' * 5)

        self.save_credentials.setEnabled(True)
        self.clear_credentials.setEnabled(True)



        self.credential_table.resizeColumnsToContents()
        self.table_index += 1


    def display_error_message(self):
        QtWidgets.QMessageBox.warning(self,"Message",self.bruteforce_core.get_exception())
        self.bruteforce_core.stop_Attack()
        self.launch_bruteforce.setText("Start")
        self.bruteforce_core.terminate()
        self.bruteforce_core.control = False
        self.start_flag = True
        self.enable_controls(True)


    def enable_controls(self,status):
        self.groupBox.setEnabled(status)
        self.settings_groupbox.setEnabled(status)
        self.custom_wordlist_groupbox.setEnabled(status)

    def save_bruteforced_credentials(self):
        target_address = str(self.target_edit.text())
        target_port = str(self.port_edit.text())
        target_service = str()

        if(self.http_https_radio.isChecked()):
            target_service = "HTTP/HTTPS (Basic Authentication)"
            target_port = str()
        if(self.telnet_radio.isChecked()):
            target_service = "TELNET"
        if(self.ftp_radio.isChecked()):
            target_service = "FTP (File Transfer Protocol)"

        file_path = QtWidgets.QFileDialog.getSaveFileName(self,"Save Credentials","report.html")[0]
        if(file_path):

            rows = self.credential_table.rowCount()
            columns = self.credential_table.columnCount()

            file_object = open(file_path,"w")
            html_header = ray_fusion_reports_html % (target_address,target_port,target_service)
            file_object.write(html_header)

            for row in range(rows):
                file_object.write("<tr>")
                for column in range(columns):
                    item = self.credential_table.item(row,column)
                    file_object.write('<td>' + str(item.text()) + '</td>')
                file_object.write("</tr>")

            file_object.write('</table></body></html>')

            file_object.flush()
            file_object.close()

            QtWidgets.QMessageBox.information(self,"Reports","Successfully saved reports to " + file_path)



    def clear_bruteforced_credentials(self):
        choice = QtWidgets.QMessageBox.question(self,"Clear Credentials","Are you sure you want to clear all bruteforced results?",QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if(choice == QtWidgets.QMessageBox.Yes):
            self.clear_table()
            self.save_credentials.setEnabled(False)
            self.clear_credentials.setEnabled(False)


    def Stop_Notification(self):
        self.enable_controls(True)
        self.launch_bruteforce.setText("Start")
        self.bruteforce_core.stop_Attack()
        self.start_flag = True


    def Start_Attack(self):
        self.target_address = str(self.target_edit.text())
        self.target_port = str(self.port_edit.text())
        self.time_interval = int(self.time_interval_spinbox.value())

        if(not bool(self.target_address)):
            QtWidgets.QMessageBox.warning(self,"Target Address","Please input a valid target adddress")
            self.target_edit.setFocus()
            return

        if(self.http_https_radio.isChecked()):
            self.bruteforce_core.set_attack_type("HTTP")
            valid_http = re.compile(r"^(https|http)://\S*",re.IGNORECASE)            # HTTP/HTTPS url regular expression
            if not valid_http.match(self.target_address):
                QtWidgets.QMessageBox.warning(self,"Invalid HTTP Address","The HTTP(HyperText Transfer Protocol) address should be fully qualified:\n\nExample:\nhttp://10.18.122.15\nhttps://www.foobar.com\nhttp://www.foobar.com/sports/index.html")
                return

        if(self.telnet_radio.isChecked()):
            self.bruteforce_core.set_attack_type("TELNET")
            if not self.target_port.isdigit():                                      # Check if use inputed a valid TCP port number
                QtWidgets.QMessageBox.warning(self,"Invalid Port Number","Remote Telnet Server port must be digits")
                return
            if(self.start_flag == True):
                QtWidgets.QMessageBox.warning(self,"Telnet Protocol","Please note that the Telnet protocol is very unreliable with its connection status responces, therefore the bruteforce attack on telnet might return false results as positive")

        if(self.ftp_radio.isChecked()):
            self.bruteforce_core.set_attack_type("FTP")
            if not self.target_port.isdigit():
                QtWidgets.QMessageBox.warning(self,"Invalid Port Number","Remote FTP Server port must be digits")
                return

        if(self.default_wordlist_radio.isChecked()):
            self.default_wordlist = "%s/extras/wordlists/common.txt"%(os.getcwd())       # Default Wordlist Path
            self.bruteforce_core.user_wordlist = self.default_wordlist
            self.bruteforce_core.password_wordlist = self.default_wordlist

        if(self.custom_wordlist_radio.isChecked()):
            if(not bool(self.custom_user_wordlist)):                                # Check if custom user list has been set
                QtWidgets.QMessageBox.warning(self,"Wordlist","Custom user wordlist has not been set, Please browse and select a user wordlist file of your choice")
                return
            if(not bool(self.custom_password_wordlist)):                            # Check if custom password list has been set
                QtWidgets.QMessageBox.warning(self,"Wordlist","Custom password wordlist has not been set, Please browse and select a password wordlist file of your choice")
                return

            self.bruteforce_core.user_wordlist = self.custom_user_wordlist
            self.bruteforce_core.password_wordlist = self.custom_password_wordlist

        self.bruteforce_core.empty_username = bool(self.blank_username_checkbox.isChecked())
        self.bruteforce_core.empty_password = bool(self.blank_password_checkbox.isChecked())

        self.bruteforce_core.setTimer(self.time_interval)                               # Set time in seconds
        self.bruteforce_core.set_target_address(self.target_address,self.target_port)   #

        if(self.start_flag == True):
            self.reset_objects()
            self.clear_table()
            self.enable_controls(False)
            self.launch_bruteforce.setText("Stop")
            self.start_flag = False
            self.bruteforce_core.start()
        else:
            self.enable_controls(True)
            self.launch_bruteforce.setText("Start")
            self.bruteforce_core.stop_Attack()
            self.start_flag = True







