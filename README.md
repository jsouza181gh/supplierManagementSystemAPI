Olá, seja bem vindo(a) à API da Supplier Managemente System da Geeco!

## Porque o usar essa stack?
- **Python**: Foi escolhido por a linguagem com que tenho a maior experiência prática, além de ser uma linguagem de alto nível que aumenta a produtividade na criação e manutenção do código;

- **Flask**: Foi escolhido por ser um framework moderno em que podemos determinar facilmente a arquitera ideal para cada tipo de projeto e por ter ferramentas ideais para uma API ;

- **SQLAlchemy**: Foi escolhido por ser um ORM que facilita a conexão e operações com banco de dados sem perder a possibilidade de um controle fino;

- **PostegreSQL** (Supabase): Foi escolhido por unir a robustes do PostgreSQL com a facilidade de hospedagem do Supabase;

- **Supabase** Storage: Foi escolhido por fornecer uma API que traz muita facilidade para armazenamento e operações com arquivos;

- **Pydantic**: Foi escolhido por facilar a validação de formato e tipo dos dados que chegam à API, criando classes schemas;

- **Pandas**: Foi escolhido por facilitar o processo de tratamento, modelagem de dados e conexão direta com o engine do SQLAlchemy para mapear os dados para o banco. 

## Dependências do Projeto

- **Python** (Recomendado vesões posteriores a 3.10, o projeto está usando 3.13.9)

---

## Inicialização do Projeto

1. Clonar o repositório:
    Abra o teminal na pasta dejesada e execute "git clone https://github.com/jsouza181gh/supplierManagementSystemAPI.git"

2. Acesse a pasta do projeto:
    Execute "cd supplierManagementSystemAPI", para entrar na pasta do projeto.

3. Crie o ambiente virtual:
    Execute "python -m venv venv", para criar o ambiente virtual do projeto.

4. Ativar o ambiente virtual:
    Execute "venv\Scripts\activate" (cmd) ou .\venv\Scripts\Activate.ps1 (powershell), para ativar o ambiente virtual.

5. Instalar dependências:
    Execute "pip install -r requirements.txt", para instalar as dependências no ambiente virtual.

6. Configurar o ".env":
    Crie o arquivo ".env" e preencha as variáveis de ambiente referente ao projeto, conforme o exemplo abaixo:

    ![Configuração do .env](readmeImages/Configuracao%20do%20.env.png)

7. Rodar a aplicação:
    Execute "flask run", para inicializar a aplicação ela estará em "http://localhost:5000/".

## Organização do Projeto:

1. Pasta "controllers":
    Nela temos os "controllers" responsáveis por receber as requisições http enviar para o processamento noservices e retornar a resposta ao cliente, definir os endpoints e proteção JWT.

        documentController: Responsável por receber as requisições para as operações dos documentos anexados em cada fornecedor. Informações que serão salvas no banco de dados e storage;

        itemController: Responsável por receber as requisições referentes as operações com produtos e serviços. Informações que serão salvas no banco de dados;

        supplierController: Responsável por receber as requisições referentes as operações com fornecedores. Informações que serão salvas no banco de dados;
    
        userController: Responsável por receber as requisições referentes as operações do usuário, como validaçãoe cadastro. Informações que serão salvas no banco de dados;

        __init__: Responsável por inicializar as blueprints dos controllers.

2. Pasta "entities":
    Nela temos as entidades que são mapeadas para o banco de dados, definindo sua estrutura e relacionamentos.

        document: Define os campos da tabela documents do banco de dadose relacionamento Many to One com suppliers;

        item_supplier: Define os campos das chaves estrangeiras da tabela associativa item_supplier, para relacionamento Many to Many entre items e suppliers;

        item: Define os campos da tabela items e relacionamento com suppliers através da tabela item_supplier;

        supplier: Define os campos da tabela suppliers e relacionamento com items através da tabela item_supplier;

        user: Define os campos da tabela users, que será utilizada para sessões dos usuários.

3. Pasta "Excel":
    Nela temos o arquivo em excel com os dados dos fornecedore e itens mapeados para o banco de dados,

4. Pasta "repositories":
    Nela temos as operações solicitadas pelos services feitas diretamente no banco de dados utilizando o SQLAlchemy.

        documentRopository: Faz as operações relacionadas a documentos anexados à fornecedores no banco de dados;

        itemRepository: Faz as operações relacionadas aos produtos e serviços no banco de dados;

        supplierRepository: Faz as operações relacionadas aos fornecedores no banco de dados;

        userRepository: Faz as operações relacionadas aos usuários no banco de dados;

5. Pasta "schemas":
    Nela temos os "schemas" do pydantic, utilizados para validação de tipo e formato dos dados a serem recebidos nos controllers.

6. Pasta "services":
    Nela temos as regras de negócio, validações e processamento dos dados vindos do controller.

    documentService: Faz o processamentos dos dados de documentos anexados no documentController, cria o DTO para response e trata as exceções vindas do documentRepository;

    itemService: Faz o processamentos dos dados recebidos no itemController, cria o DTO para response e trata as exceções vindas do itemRepository;

    supplierService: Faz o processamentos dos dados recebidos no supplierController, cria o DTO para response e trata as exceções vindas do supplierRepository;

    userService: Faz o processamentos dos dados recebidos no userController, cria o DTO para response, trata as exceções vindas do userRepository, faz a criptografia de senhas a serem salvas e valida credenciais;

7. Pasta "venv":
    Pasta responsável pelo ambiente virtual da aplicação, facilitando o isolamento e instalação de dependências.

8. Arquivo ".gitignore":
    Determina qual arquivos ou pastas não devem ser versionados pelo git.

9. Arquivo "app.py":
    Arquivo principal do projeto, ele que define as configurações e gerencia o fluxo da aplicação.

10. Arquivo "database.py":
    Arquivo responsável por realizar a conexão com o banco de dados e criar a engine para suas operações.

11. Arquivo "exceptions.py":
    Arquivo que contem as classes de exceções que serão lançadas pelo durante o tratamento no services.

12. Arquivo "exportExcelData.py:"
    Arquivo que contém a pipeline pra tratamento, modelagem e mapeamento dos dados da planilha em excel para o banco de dados.

13. Arquivo "requirements.txt":
    Arquivo que contém todas as dependências do projeto e pode ser usado para instalar as exatas versões evitando bugs.

14. Arquivo "supabaseClient.py":
    Arquivo que faz a conexão como o Supabase Storage em fornece o client para operações com os arquivos de fornecedores.

