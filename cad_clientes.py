import sys
import mysql.connector as mc
from PyQt5.QtWidgets import QApplication, QWidget,QLabel,QLineEdit, QVBoxLayout, QPushButton

con = mc.connect(
    host="127.0.0.1",
    port="6556",
    user="root",
    password="senac@123",
    database="Senac"
)

cursor = con.cursor()

class CadCursos(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(30,40,600,250)
        self.setWindowTitle("Cadastro de Cursos")

        labelNomeCurso = QLabel("Nome do Curso")
        self.editNomeCurso = QLineEdit()

        labelCargaHoraria = QLabel("Carga Horaria")
        self.editCargaHoraria = QLineEdit()

        psbCadastro = QPushButton("Cadastrar")

        self.labelMsg = QLabel("Rua Coronel Luís Americano, 130 Tatuapé, São Paulo - SP, 03308-020")
        
        layout = QVBoxLayout()
        layout.addWidget(labelNomeCurso)
        layout.addWidget(self.editNomeCurso)

        layout.addWidget(labelCargaHoraria)
        layout.addWidget(self.editCargaHoraria)


        layout.addWidget(psbCadastro)
        psbCadastro.clicked.connect(self.CadCur)

        layout.addWidget(self.labelMsg)

        self.setLayout(layout)
    
    def CadCur(self):
        cursor.execute("insert into cursos (nome_cursos,carga_horaria)values(%s,%s)",
                       (self.editNomeCurso.text(),self.editCargaHoraria.text()))
        con.commit()
        self.labelMsg.setText("Cursos Cadastrado")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tela = CadCursos()
    tela.show()
    sys.exit(app.exec_())