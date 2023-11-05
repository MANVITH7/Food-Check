

from PyQt5 import QtCore, QtGui, QtWidgets

import mysql.connector
con =mysql.connector.connect(host='localhost', user='root', password = 'mysql')
cur = con.cursor()
cur.execute("use products")

def check(fooditem, item):
    query = "select * from "  + fooditem + " where ingredients like '%"+item+"%'"
    cur.execute(query)
    result = cur.fetchall()
    if len(result) == 0:
        return True
    else:
        return False
    

def isVegan(fooditem):
    vegan = ["egg", "milk", "cheese", "butter", "chocolate", "pork", "gelatin"]
    b = 0
    for i in vegan:
        a = check(fooditem, i)
        if a == False:
            b = 1
            break
    if b == 0:
        return True
    else:
        return False
        
def isVeg(fooditem):
    veg = ["egg", "pork", "gelatin"]
    b = 0
    for i in veg:
        a = check(fooditem, i)
        if a == False:
            b = 1
            break
    if b == 0:
        return True
    else:
        return False
        
def hasGluten(fooditem):
    a = check(fooditem, "Wheat")
    if a == False:
        return True
    else:
        return False
        
def hasSoy(fooditem):
    a = check(fooditem, "Soy")
    if a == False:
        return True
    else:
        return False

def hasPeanuts(fooditem):
    a = check(fooditem, "Peanut")
    if a == False:
        return True
    else:
        return False

def hasPalmOil(fooditem):
    a = check(fooditem, "Palm Oil")
    if a == False:
        return True
    else:
        return False

def hasNFlavors(fooditem):
    a = check(fooditem, "Natural Flavor")
    if a == False:
        return True
    else:
        return False
        
def hasHFCS(fooditem):
    a = check(fooditem, "High Fructose Corn Syrup")
    if a == False:
        return True
    else:
        return False

def hasAFlavors(fooditem):
    a = check(fooditem, "Artificial Flavor")
    if a == False:
        return True
    else:
        return False
        
def hasAFD(fooditem):
    a = check(fooditem, "Artificial Food Dye")
    if a == False:
        return True
    else:
        return False
        
def isDb(fooditem):
    db = ["Sugar", "High Fructose Corn Syrup", "Honey"]
    b = 0
    for i in db:
        a = check(fooditem, i)
        if a == False:
            b = 1
            break
    if b == 1:
        return True
    else:
        return False
    
def isLIF(fooditem):
    a = check(fooditem, "Milk")
    if a == False:
        return False
    else:
        return True
class Ui_App(object):
    def setupUi(self, App):
        App.setObjectName("App")
        App.resize(501, 606)
        App.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(App)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(220, 30, 181, 20))
        self.comboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet("border-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 236, 98);\n""color: black;")
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 30, 151, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: black;")
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 160, 121, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("color: black;")
        self.groupBox.setObjectName("groupBox")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setGeometry(QtCore.QRect(0, 20, 121, 20))
        self.checkBox.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_2.setGeometry(QtCore.QRect(0, 40, 121, 20))
        self.checkBox_2.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_7 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_7.setGeometry(QtCore.QRect(0, 60, 121, 20))
        self.checkBox_7.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.checkBox_7.setObjectName("checkBox_7")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(160, 160, 151, 101))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("color: black;")
        self.groupBox_2.setObjectName("groupBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_3.setGeometry(QtCore.QRect(0, 20, 151, 20))
        self.checkBox_3.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_4.setGeometry(QtCore.QRect(0, 40, 151, 20))
        self.checkBox_4.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_10 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_10.setGeometry(QtCore.QRect(0, 60, 151, 20))
        self.checkBox_10.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.checkBox_10.setObjectName("checkBox_10")
        self.checkBox_11 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_11.setGeometry(QtCore.QRect(0, 80, 151, 20))
        self.checkBox_11.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.checkBox_11.setObjectName("checkBox_11")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(330, 160, 151, 101))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setStyleSheet("color: black;")
        self.groupBox_3.setObjectName("groupBox_3")
        self.checkBox_5 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_5.setGeometry(QtCore.QRect(0, 20, 151, 20))
        self.checkBox_5.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_6.setGeometry(QtCore.QRect(0, 40, 151, 20))
        self.checkBox_6.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_13 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_13.setGeometry(QtCore.QRect(0, 60, 151, 20))
        self.checkBox_13.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.checkBox_13.setObjectName("checkBox_13")
        self.checkBox_14 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_14.setGeometry(QtCore.QRect(0, 80, 151, 20))
        self.checkBox_14.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.checkBox_14.setObjectName("checkBox_14")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(180, 340, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setMouseTracking(False)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("background-color: rgb(255, 165, 0);""color: black;")
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 110, 211, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: black;")
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(55, 390, 391, 111))
        self.textBrowser.setObjectName("textBrowser")
        App.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(App)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 501, 22))
        self.menubar.setObjectName("menubar")
        App.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(App)
        self.statusbar.setObjectName("statusbar")
        App.setStatusBar(self.statusbar)

        self.retranslateUi(App)
        QtCore.QMetaObject.connectSlotsByName(App)

    def retranslateUi(self, App):
        _translate = QtCore.QCoreApplication.translate
        App.setWindowTitle(_translate("App", "MainWindow"))
        self.comboBox.setCurrentText(_translate("App", "SELECT FOOD"))
        self.comboBox.setItemText(0, _translate("App", "Ice Cream"))
        self.comboBox.setItemText(1, _translate("App", "Bread"))
        self.comboBox.setItemText(2, _translate("App", "Egg Bites"))
        self.comboBox.setItemText(3, _translate("App", "Jif"))
        self.comboBox.setItemText(4, _translate("App", "Corn Flakes"))
        self.comboBox.setItemText(5, _translate("App", "Lays"))
        self.comboBox.setItemText(6, _translate("App", "Mac and Cheese"))
        self.comboBox.setItemText(7, _translate("App", "Oreo"))
        self.comboBox.setItemText(8, _translate("App", "Rice Krispies Treats"))
        self.comboBox.setItemText(9, _translate("App", "Silk Soy Milk"))
        self.comboBox.setItemText(10, _translate("App", "Popcorn"))
        self.label.setText(_translate("App", "Select Food Item:"))
        self.groupBox.setTitle(_translate("App", "Allergens:"))
        self.checkBox.setText(_translate("App", "peanuts"))
        self.checkBox_2.setText(_translate("App", "gluten-free"))
        self.checkBox_7.setText(_translate("App", "soy"))
        self.groupBox_2.setTitle(_translate("App", "Harmful Products:"))
        self.checkBox_3.setText(_translate("App", "palm oil"))
        self.checkBox_4.setText(_translate("App", "artificial flavoring"))
        self.checkBox_10.setText(_translate("App", "artificial food dye"))
        self.checkBox_11.setText(_translate("App", "natural flavors"))
        self.groupBox_3.setTitle(_translate("App", "Dietary Restrictions:"))
        self.checkBox_5.setText(_translate("App", "vegetarian"))
        self.checkBox_6.setText(_translate("App", "vegan"))
        self.checkBox_13.setText(_translate("App", "lactose intolerant"))
        self.checkBox_14.setText(_translate("App", "diabetic"))
        self.pushButton.setText(_translate("App", "Get Result"))
        self.pushButton.clicked.connect(self.get_result)
        self.label_2.setText(_translate("App", "Select Filters to Apply:"))
        self.textBrowser.setHtml(_translate("App", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))

       
        
    def get_result(self):
        
        self.textBrowser.clear()
        selected_item = self.comboBox.currentText()

        
        checked_items = []
        peanuts = False
        gluten_free = False
        soy = False
        palm_oil = False
        artificial_flavors = False
        artificial_food_dye = False
        Natural_flavors = False
        vegetarian = False
        vegan = False
        lactose_intolerant = False
        diabetic = False
        

        
        if self.checkBox.isChecked():
            peanuts = True
            checked_items.append(peanuts)
        if self.checkBox_2.isChecked():
            gluten_free = True
            checked_items.append(gluten_free)
        if self.checkBox_7.isChecked():
            soy = True
            checked_items.append(soy)
        if self.checkBox_3.isChecked():
            palm_oil = True
            checked_items.append(palm_oil)
        if self.checkBox_4.isChecked():
            artificial_flavors = True
            checked_items.append(artificial_flavors)
        if self.checkBox_10.isChecked():
            artificial_food_dye = True
            checked_items.append(artificial_food_dye)
        if self.checkBox_11.isChecked():
            Natural_flavors = True
            checked_items.append(Natural_flavors)
        if self.checkBox_5.isChecked():
            vegetarian = True
            checked_items.append(vegetarian)
        if self.checkBox_6.isChecked():
            vegan = True
            checked_items.append(vegan)
        if self.checkBox_13.isChecked():
            lactose_intolerant = True
            checked_items.append(lactose_intolerant)
        if self.checkBox_14.isChecked():
            diabetic = True
            checked_items.append(diabetic)
            
        
        if (selected_item == "Ice Cream"):
            sItem = "blue_bell_brown_rim_buttered_pecan_ice_cream"
        
        elif (selected_item == "Egg Bites"):
            sItem = "egg_bites"
        
        elif (selected_item == "Corn Flakes"):
            sItem = "kelloggs_corn_flakes"
        
        elif (selected_item == "Mac and Cheese"):
            sItem = "mac_and_cheese"
            
        elif (selected_item == "Rice Krispies Treats"):
            sItem = "rice_krispies_treats"
            
        elif (selected_item == "Silk Soy Milk"):
            sItem = "silk_soy_milk"
            
        elif (selected_item == "Popcorn"):
            sItem = "amc_popcorn"
        else:
            sItem = selected_item
        
        
        issues = []
        
        if (peanuts):
            check = hasPeanuts(sItem)
            if check == True:
                issues.append("It contains Peanuts")
                print("ok")
        
        if (gluten_free):
            check = hasGluten(sItem)
            if check == True:
                issues.append("It contains Gluten")
        
        if (soy):
            check = hasSoy(sItem)
            if check == True:
                issues.append("It contains Soy")
        
        if (palm_oil):
            check = hasPalmOil(sItem)
            if check == True:
                issues.append("It contains Palm Oil")
                
        if (artificial_flavors):
            check = hasAFlavors(sItem)
            if check == True:
                issues.append("It contains Artifical Flavors")
       
        if (artificial_food_dye):
            check = hasAFD(sItem)
            if check == True:
                issues.append("It contains Artifical Food Dyes")    
                
        if (Natural_flavors):
            check = hasNFlavors(sItem)
            if check == True:
                issues.append("It contains Natural Flavors") 
                
        
        if (vegetarian):
            check = isVeg(sItem)
            if check == False:
                issues.append("It is not Vegetarian")
                
        if (vegan):
            check = isVegan(sItem)
            if check == False:
                issues.append("It is not Vegan")
        
        if (lactose_intolerant):
            check = isLIF(sItem)
            if check == False:
                issues.append("It is not Lactose Intolerant Friendly")
        
        if (diabetic):
            check = isDb(sItem)
            if check == True:
                issues.append("It contains Sugar")

        
        self.process_selection(selected_item, issues)

    def process_selection(self, sItem, issues):
        if (len(issues) == 0):
            Output = sItem + " meets all your requirements and is safe for consumption!"
            self.textBrowser.append(Output)
            self.textBrowser.setStyleSheet("color: green")
        else:
            Output = sItem + " does not meet your requirements and has the following issues: "
            for i in issues:
                Output = Output + "\n" + i
            self.textBrowser.append(Output)
            self.textBrowser.setStyleSheet("color: red")
            

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    App = QtWidgets.QMainWindow()
    ui = Ui_App()
    ui.setupUi(App)
    App.show()
    sys.exit(app.exec_())
