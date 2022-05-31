from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QListWidgetItem, QInputDialog, QMessageBox
import sys
import Ui_Window


class MainUiClass (QtWidgets.QMainWindow, Ui_Window.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainUiClass, self).__init__(parent)
        self.setupUi(self)

class App (object):
    def __init__(self, ui):
        self.ui = ui

    def btn_Generate_click(self):
        x=''
        y=''
        self.ui.txt_Code.clear()
        self.ui.txt_FEO.clear()
        txt_variable = self.ui.txt_Variable.text()
        TOF = self.ui.cb_TOF.currentIndex()
        TODD = self.ui.cb_TODD.currentIndex()

        
        if txt_variable == '':
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle('Error')
            msg.setText('Error: you must place a varable name.')
            msg.setStandardButtons(QMessageBox.Ok)
            retVal = msg.exec()
            return


        if TOF == 0 and TODD == 0:
            x+="1|Yes;2|No"
            y+="case when [" + txt_variable + "] = ''1'' then ''XX'' else '''' end as [" + txt_variable + "Yes],\n"
            y+="case when [" + txt_variable + "] = ''2'' then ''XX'' else '''' end as [" + txt_variable + "No],"


        if self.ui.lst_Elements.count() != 0 and (TODD == 1 or TODD == 2):
            y+='case '

            for i in range(self.ui.lst_Elements.count()):

                txt_item = self.ui.lst_Elements.item(i).text()

                x+=str(i+1)+'|'+txt_item+';'
                if TOF == 0 and TODD == 1:
                    y+="when [" + txt_variable + "] = ''"+str(i+1)+ "'' then ''XX'' else '''' end as [cb_" + txt_item.replace(" ", '') + "],\n"
                elif TOF == 0 and TODD == 2:
                    y+="when [" + txt_variable + "] = ''" + str(i+1) + "'' then ''" + txt_item + "''\n"
                
            x = x[:-1]

            if TOF == 0 and TODD == 2:
                y+= "else ''''\nend as [txt_" + txt_variable + "],"

        if TOF == 1:
            y+="case when [" + txt_variable + "] = ''True'' then ''XX'' else '''' end as [cb_" + txt_variable + "],\n"

        if TOF == 2:
            y+="CONVERT(varchar(10), cast([" + txt_variable + "] as date), 101) as [" + txt_variable + "],"
        
        self.ui.txt_Code.insertPlainText(y)
        self.ui.txt_FEO.insertPlainText(x)


    def onPressed(self):
        if self.ui.txt_Element.text() != '':
            self.ui.lst_Elements.addItem(self.ui.txt_Element.text())
            self.ui.txt_Element.setText("")

    def btn_Edit_clicked(self):
        item_selected = self.ui.lst_Elements.currentRow()
        text, result = QInputDialog.getText(self.ui, "New element", "Insert new element")
        if result and len(text) != 0:
            self.ui.lst_Elements.takeItem(self.ui.lst_Elements.currentRow())
            self.ui.lst_Elements.insertItem(item_selected, QListWidgetItem(text))

    def btn_Eliminate_clicked(self):
        self.ui.lst_Elements.takeItem(self.ui.lst_Elements.currentRow())

    def btn_Empty_clicked(self):
        self.ui.lst_Elements.clear()

    def TOF_changed(self):
        if self.ui.cb_TOF.currentIndex() != 0:
            flag = False
        else:
            flag = True

        self.ui.cb_TODD.setEnabled(flag)
        self.ui.lst_Elements.setEnabled(flag)
        self.ui.lst_Elements.clear()
        self.ui.txt_Element.setEnabled(flag)
        self.ui.txt_Element.setText('')
        self.ui.btn_Edit.setEnabled(flag)
        self.ui.btn_Eliminate.setEnabled(flag)
        self.ui.btn_Empty.setEnabled(flag)


def main():
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
        ui = MainUiClass()
        apli = App(ui)
        ui.show()

        ui.btn_Generate.clicked.connect(apli.btn_Generate_click)
        ui.lst_Elements.itemDoubleClicked.connect(apli.btn_Edit_clicked)
        ui.txt_Element.returnPressed.connect(apli.onPressed)
        ui.btn_Edit.clicked.connect(apli.btn_Edit_clicked)
        ui.btn_Eliminate.clicked.connect(apli.btn_Eliminate_clicked)
        ui.btn_Empty.clicked.connect(apli.btn_Empty_clicked)
        
        ui.cb_TOF.currentIndexChanged.connect(apli.TOF_changed)
    
        app.exec_()


if __name__ == "__main__":
    main()