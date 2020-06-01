import sys

from PyQt5.QtCore import QTranslator, QLocale
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog

from ui_main import Ui_MainWindow


class Application(QMainWindow, Ui_MainWindow):  # Recette de cuisine ligne1
    def __init__(self, parent=None):  # ligne2
        super().__init__(parent)  # ligne 3
        self.setupUi(self)  # ligne 4

    # Notre code python
    def createProject(self):
        self.btnSaveProject.setEnabled(True)
        self.btnCreateProject.setEnabled(False)

    def saveProject(self):
        self.btnSaveProject.setEnabled(False)
        self.btnCreateProject.setEnabled(True)

    def updateProject(self):
        pass

    def deleteProject(self):
        pass

    def createTask(self):
        pass

    def saveTask(self):
        pass

    def deleteTask(self):
        pass

    def updateTask(self):
        pass

    def openDB(self):
        filename, filter = QFileDialog().getOpenFileName(
            caption=self.tr("Ouvrir un fichier DB"),
            filter=self.tr("Fichier DB (*.db)"),
        )
        print(filename)

    def newDB(self):
        filename, filter = QFileDialog().getSaveFileName(
            caption=self.tr("Creer un nouveau fichier DB"),
            filter=self.tr("Fichier DB (*.db)")
        )
        print(filename)


# Lancement du programme principal
if __name__ == '__main__':  # Recette de cuisine n°2 ligne 1
    app = QApplication(sys.argv)  # ligne 2
    # Recette de cuisine du traducteur
    translator = QTranslator()
    if len(sys.argv) == 1:  # si pas de langue spécifiée
        locale = QLocale()
        translator.load(locale, "i18n", ".")  # nom du fichier de traduction
    else:
        translator.load("i18n." + sys.argv[1])  # on charge la langue indiquée
    app.installTranslator(translator)  # on installe le traducteur
    # fin de la recette du traducteur
    window = Application()  # ligne 3, on appelle la "class" au-dessus
    window.show()  # ligne 4, on affiche l’écran
    app.exec_()  # ligne 5, on démarre l’application
