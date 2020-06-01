# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(702, 421)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("monkey-face-cartoon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.cbProjectName = QtWidgets.QComboBox(self.groupBox)
        self.cbProjectName.setToolTip("")
        self.cbProjectName.setEditable(True)
        self.cbProjectName.setObjectName("cbProjectName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cbProjectName)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.deProjectBeginDate = QtWidgets.QDateEdit(self.groupBox)
        self.deProjectBeginDate.setCalendarPopup(True)
        self.deProjectBeginDate.setObjectName("deProjectBeginDate")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.deProjectBeginDate)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.deProjectEndDate = QtWidgets.QDateEdit(self.groupBox)
        self.deProjectEndDate.setCalendarPopup(True)
        self.deProjectEndDate.setObjectName("deProjectEndDate")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.deProjectEndDate)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnCreateProject = QtWidgets.QPushButton(self.groupBox)
        self.btnCreateProject.setObjectName("btnCreateProject")
        self.horizontalLayout.addWidget(self.btnCreateProject)
        self.btnSaveProject = QtWidgets.QPushButton(self.groupBox)
        self.btnSaveProject.setEnabled(False)
        self.btnSaveProject.setObjectName("btnSaveProject")
        self.horizontalLayout.addWidget(self.btnSaveProject)
        self.btnDeleteProject = QtWidgets.QPushButton(self.groupBox)
        self.btnDeleteProject.setStyleSheet("")
        self.btnDeleteProject.setObjectName("btnDeleteProject")
        self.horizontalLayout.addWidget(self.btnDeleteProject)
        self.btnUpdateProject = QtWidgets.QPushButton(self.groupBox)
        self.btnUpdateProject.setObjectName("btnUpdateProject")
        self.horizontalLayout.addWidget(self.btnUpdateProject)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 2)
        self.lstTasks = QtWidgets.QListWidget(self.centralwidget)
        self.lstTasks.setObjectName("lstTasks")
        self.gridLayout.addWidget(self.lstTasks, 1, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.leTaskName = QtWidgets.QLineEdit(self.groupBox_2)
        self.leTaskName.setObjectName("leTaskName")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.leTaskName)
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.deTaskBeginDate = QtWidgets.QDateEdit(self.groupBox_2)
        self.deTaskBeginDate.setCalendarPopup(True)
        self.deTaskBeginDate.setObjectName("deTaskBeginDate")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.deTaskBeginDate)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.deTaskEndDate = QtWidgets.QDateEdit(self.groupBox_2)
        self.deTaskEndDate.setCalendarPopup(True)
        self.deTaskEndDate.setObjectName("deTaskEndDate")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.deTaskEndDate)
        self.verticalLayout_2.addLayout(self.formLayout_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnCreateTask = QtWidgets.QPushButton(self.groupBox_2)
        self.btnCreateTask.setObjectName("btnCreateTask")
        self.horizontalLayout_2.addWidget(self.btnCreateTask)
        self.btnSaveTask = QtWidgets.QPushButton(self.groupBox_2)
        self.btnSaveTask.setEnabled(False)
        self.btnSaveTask.setObjectName("btnSaveTask")
        self.horizontalLayout_2.addWidget(self.btnSaveTask)
        self.btnDeleteTask = QtWidgets.QPushButton(self.groupBox_2)
        self.btnDeleteTask.setObjectName("btnDeleteTask")
        self.horizontalLayout_2.addWidget(self.btnDeleteTask)
        self.btnUpdateTask = QtWidgets.QPushButton(self.groupBox_2)
        self.btnUpdateTask.setObjectName("btnUpdateTask")
        self.horizontalLayout_2.addWidget(self.btnUpdateTask)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.gridLayout.addWidget(self.groupBox_2, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 702, 21))
        self.menubar.setObjectName("menubar")
        self.menu_Fichier = QtWidgets.QMenu(self.menubar)
        self.menu_Fichier.setObjectName("menu_Fichier")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpenDB = QtWidgets.QAction(MainWindow)
        self.actionOpenDB.setObjectName("actionOpenDB")
        self.actionNewDB = QtWidgets.QAction(MainWindow)
        self.actionNewDB.setObjectName("actionNewDB")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menu_Fichier.addAction(self.actionOpenDB)
        self.menu_Fichier.addAction(self.actionNewDB)
        self.menu_Fichier.addSeparator()
        self.menu_Fichier.addAction(self.actionQuit)
        self.menubar.addAction(self.menu_Fichier.menuAction())
        self.label.setBuddy(self.cbProjectName)
        self.label_2.setBuddy(self.deProjectBeginDate)
        self.label_3.setBuddy(self.deProjectEndDate)
        self.label_4.setBuddy(self.leTaskName)
        self.label_5.setBuddy(self.deTaskBeginDate)
        self.label_6.setBuddy(self.deTaskEndDate)

        self.retranslateUi(MainWindow)
        self.btnCreateTask.clicked.connect(MainWindow.createTask)
        self.btnCreateProject.clicked.connect(MainWindow.createProject)
        self.btnSaveProject.clicked.connect(MainWindow.saveProject)
        self.btnDeleteProject.clicked.connect(MainWindow.deleteProject)
        self.btnUpdateProject.clicked.connect(MainWindow.updateProject)
        self.btnSaveTask.clicked.connect(MainWindow.saveTask)
        self.btnDeleteTask.clicked.connect(MainWindow.deleteTask)
        self.btnUpdateTask.clicked.connect(MainWindow.updateTask)
        self.actionNewDB.triggered.connect(MainWindow.newDB)
        self.actionOpenDB.triggered.connect(MainWindow.openDB)
        self.actionQuit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gestionnaire de projets"))
        self.groupBox.setTitle(_translate("MainWindow", "Projets"))
        self.label.setText(_translate("MainWindow", "Nom du projet"))
        self.cbProjectName.setStatusTip(_translate("MainWindow", "Entrez ou selectionnez un projet"))
        self.label_2.setText(_translate("MainWindow", "Date de debut"))
        self.label_3.setText(_translate("MainWindow", "Date de fin"))
        self.btnCreateProject.setText(_translate("MainWindow", "Creer"))
        self.btnSaveProject.setText(_translate("MainWindow", "Sauver"))
        self.btnDeleteProject.setText(_translate("MainWindow", "Supprimer"))
        self.btnUpdateProject.setText(_translate("MainWindow", "Modifier"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Taches"))
        self.label_4.setText(_translate("MainWindow", "Nom de la tache"))
        self.leTaskName.setPlaceholderText(_translate("MainWindow", "Entrez le nom de la tache"))
        self.label_5.setText(_translate("MainWindow", "Date de debut"))
        self.label_6.setText(_translate("MainWindow", "Date de fin"))
        self.btnCreateTask.setText(_translate("MainWindow", "Creer"))
        self.btnSaveTask.setText(_translate("MainWindow", "Sauver"))
        self.btnDeleteTask.setText(_translate("MainWindow", "Supprimer"))
        self.btnUpdateTask.setText(_translate("MainWindow", "Modifier"))
        self.menu_Fichier.setTitle(_translate("MainWindow", "&Fichier"))
        self.actionOpenDB.setText(_translate("MainWindow", "&Ouvrir une db"))
        self.actionOpenDB.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionNewDB.setText(_translate("MainWindow", "&Nouvelle db"))
        self.actionNewDB.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionQuit.setText(_translate("MainWindow", "&Quitter"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))