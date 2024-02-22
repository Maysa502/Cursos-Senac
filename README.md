# Criação e catalogação dos cursos da instituição Serviço Nacional de Aprendizagem Comercial 
#### *A comunicação na criação e atualização do Banco de dados será feita via conexão do Python com o Mysql*
!["Imagem Python com MySQL"](https://miro.medium.com/v2/resize:fit:756/1*h7LcQWcRstxl5TdwBu7s5A.png)


A comunicação entre Python e MySQL é significativa em diversos contextos, proporcionando uma série de benefícios e possibilidades.
Sua integração  é uma escolha comum e eficaz para desenvolvedores que buscam uma solução abrangente para o gerenciamento e manipulação de dados em suas aplicações. A combinação dessas tecnologias oferece flexibilidade, desempenho e uma variedade de recursos para atender a uma ampla gama de necessidades de desenvolvimento de software.
A comunicação entre o Python e o banco MySQL será estabelecida por meio do driver mysql-connector-python.

### Configuração da Comunicação
#### Instalação do Driver
Para instalar o driver necessário, utilize o seguinte comando:
``` python
  python -m pip install mysql-connector-python
```
---
### Configuração do Banco de Dados MySQL
O banco de dados está em um contêiner Docker. Siga os passos abaixo para criar o contêiner em um servidor Fedora com o Docker instalado:
#### Criação do volume 
``` shell
mkdir cursossenac 
```

## Criação do Contêiner
<center>
<img src="https://cdn.iconscout.com/icon/free/png-256/free-docker-226091.png" height="100" width="100">
</center>

#### Execute os seguintes comandos para criar o contêiner:


``` linux
docker run --name srv-mysql -v ~/dadosclientes:/var/lib/mysql -p 3784:3306 -e MYSQL_ROOT_PASSWORD=senac@123 -d mysql
```
**Isso criará um contêiner MySQL chamado srv-mysql com o diretório dadosclientes como volume persistente e a porta 3784 mapeada para a porta padrão do MySQL (3306).**

* Lembre-se: substitua senac@123 pela senha desejada para o usuário root do MySQL.
  
---

## Criação banco de dados da tabela Cursos

``` sql
create database Senac;

use Senac;

create table cursos(
cursos_id int auto_increment primary key,
nome_curso varchar(50) not null,
carga_horaria varchar(30) not null,
);
```
---

#### Arquivo cad_cursos.py
*Este arquivo tem o proposito inicial de cadastrar os cursos e coloca-lo no DataBase Senac na tabela Cursos*
``` sql
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
```
---

#### Arquivo listar_cursos.py
*Em seguida, criaremos um arquivo pra ajudar na consulta de dados da tabela Cursos do banco Senac*
``` sql
import sys
from PyQt5.QtWidgets import QApplication, QWidget,QTableWidget, QTableWidgetItem, QVBoxLayout
import mysql.connector as mycon

cx = mycon.connect(
    host="127.0.0.1",
    port="6556",
    user="root",
    password="senac@123",
    database="Senac"
)
cursor = cx.cursor()

class ExibirCursos(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100,100,350,300)
        self.setWindowTitle("Cursos cadastrados")

        tbcursos = QTableWidget(self)
        tbcursos.setColumnCount(3)
        tbcursos.setRowCount(10)

        headerLine=["Id","Nome do Curso", "Carga Horaria"]

        tbcursos.setHorizontalHeaderLabels(headerLine)
        cursor.execute("select * from cursos")
        lintb = 0
        for linha in cursor:
            tbcursos.setItem(lintb,0,QTableWidgetItem(str(linha[0])))
            tbcursos.setItem(lintb,1,QTableWidgetItem(linha[1]))
            tbcursos.setItem(lintb,2,QTableWidgetItem(linha[2]))
            lintb+=1

        layout = QVBoxLayout()
        layout.addWidget(tbcursos)
        self.setLayout(layout)

if __name__=="__main__":
    app = QApplication(sys.argv)
    tela = ExibirCursos()
    tela.show()
    sys.exit(app.exec_())
```
---

#### Arquivo atualizar_cursos.py
*Por fim, este ultimo arquivo que tem a função de atualizar os dados da tabela Cursos do Database Senac. A atualização de bancos de dados é crucial para garantir a precisão, segurança e eficiência das informações armazenadas. Isso permite adaptar-se a mudanças nos requisitos, corrigir falhas de segurança, melhorar o desempenho e oferecer suporte a novas funcionalidades, contribuindo para a integridade e relevância dos dados ao longo do tempo*

```sql
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
```

---
---
#### Agradecemos por utilizar este repositório! A integração entre Python e MySQL para criar e manter o banco de dados da rede Senac oferece uma solução robusta e flexível. Lembre-se de manter o banco de dados atualizado para garantir a confiabilidade e a eficiência das informações. Em caso de dúvidas ou sugestões, sinta-se à vontade para contribuir ou entrar em contato. Feliz codificação!



