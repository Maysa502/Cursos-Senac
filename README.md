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





Criação do Contêiner
Execute os seguintes comandos para criar o contêiner:

bash
Copy code
docker run --name srv-mysql -v ~/dadosclientes:/var/lib/mysql -p 3784:3306 -e MYSQL_ROOT_PASSWORD=senac@123 -d mysql
Isso criará um contêiner MySQL chamado srv-mysql com o diretório dadosclientes como volume persistente e a porta 3784 mapeada para a porta padrão do MySQL (3306).

Lembre-se de substituir senac@123 pela senha desejada para o usuário root do MySQL.

Exemplo de Uso
Consulte o arquivo exemplo.py neste repositório para um exemplo simples de como estabelecer uma conexão entre o Python e o MySQL utilizando o driver instalado.

python
Copy code
import mysql.connector

# Configurações de conexão
config = {
    'user': 'root',
    'password': 'senac@123',
    'host': 'localhost',
    'port': 3784,
    'database': 'seu_banco_de_dados',
}

# Conecta ao banco de dados
conexao = mysql.connector.connect(**config)

# Executa operações no banco de dados...

# Fecha a conexão
conexao.close()
Lembre-se de substituir seu_banco_de_dados pelo nome do seu banco de dados.

Contribuições
Se desejar contribuir para a melhoria deste exemplo, siga o fluxo padrão do GitHub:

Faça um fork do repositório.
Crie um novo branch para sua funcionalidade ou correção de bug.
Faça suas alterações e envie um pull request.
Licença
Este exemplo está licenciado sob a Licença MIT.
