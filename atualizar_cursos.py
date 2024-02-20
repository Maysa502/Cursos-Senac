import sys
from PyQt5.QtWidgets import QApplication, QWidget,QTableWidget, QTableWidgetItem,QLabel,QLineEdit, QVBoxLayout, QPushButton
import mysql.connector as mycon

cx = mycon.connect(
    host="127.0.0.1",
    port="6556",
    user="root",
    password="senac@123",
    database="Senac"
)
cursor = cx.cursor()

class AtualizarCursos(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout()
        self.setGeometry(100,100,350,400)
        self.setWindowTitle("Cursos Cadastrados")

        labelID = QLabel("Id Curso:")
        self.editId = QLineEdit()

        labelNomeCurso = QLabel("Nome do Curso:")
        self.editNomeCurso = QLineEdit()

        labelCargaHoraria = QLabel("Carga Horaria:")
        self.editCargaHoria = QLineEdit()

       
        psbCadastro = QPushButton("Cadastrar")

        layout.addWidget(labelID)
        layout.addWidget(self.editId)

        layout.addWidget(labelNomeCurso)
        layout.addWidget(self.editNomeCurso)


        layout.addWidget(labelCargaHoraria)
        layout.addWidget(self.editCargaHoria)


        layout.addWidget(psbCadastro)
        psbCadastro.clicked.connect(self.upCli)

        tbcursos = QTableWidget(self)
        tbcursos.setColumnCount(4)
        tbcursos.setRowCount(10)

        headerLine=["Id","Nome do Curso","Carga Horaria"]

        tbcursos.setHorizontalHeaderLabels(headerLine)
        cursor.execute("select * from cursos")
        lintb = 0
        for linha in cursor:
            tbcursos.setItem(lintb,0,QTableWidgetItem(str(linha[0])))
            tbcursos.setItem(lintb,1,QTableWidgetItem(linha[1]))
            tbcursos.setItem(lintb,2,QTableWidgetItem(linha[2]))
            lintb+=1

       
        layout.addWidget(tbcursos)
        self.setLayout(layout)

        # obrigatório colocar .text() em todos edit
    
    def upCli(self):
        if (self.editId.text() == ""):
            print("Não é possivel atualizar sem o id do curso")



        elif(self.editNomeCurso.text()=="" and self.editCargaHoria.text()==""):
            print("Não é possivel atualizar se não houver dados")




        elif(self.editNomeCurso.text()!="" and self.editCargaHoria.text()==""):
            cursor.execute("update cursos set nome_cursos=%s where cursos_id=%s", 
                           (self.editNomeCurso.text(), self.editId.text()))
            
        


        elif(self.editNomeCurso.text()=="" and self.editCargaHoria.text()!=""):
            cursor.execute("update cursos set carga_horaria=%s where cursos_id=%s", 
                           (self.editCargaHoria.text(), self.editId.text()))
            
        
        else:
            cursor.execute("update cursos set nome_cursos=%s, carga_horaria=%s where cursos_id=%s", 
                           (self.editNomeCurso.text(),self.editCargaHoria.text(), self.editId.text()))

        cx.commit()
        print("Todas as modificaçõe foram realizadas!")     

if __name__=="__main__":
    app = QApplication(sys.argv)
    tela = AtualizarCursos()
    tela.show()
    sys.exit(app.exec_())