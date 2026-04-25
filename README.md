# Sistema de Agenda para Clinica de Estetica

## Descricao
Sistema web para clinica de estetica com autenticacao, menu principal, cadastro de procedimentos, cadastro de clientes, ficha de anamnese, agenda de atendimentos e visao de gerenciamento mensal.

O projeto foi estruturado para crescer de forma organizada, com separacao entre rotas, regras de negocio, acesso a dados, templates HTML e arquivos estaticos.

## Tecnologias utilizadas
- Python 3
- Flask
- Flask-Login
- Flask-SQLAlchemy
- SQLite
- HTML
- CSS
- JavaScript
- Git
- GitHub
- VS Code

## Estrutura do projeto

```bash
projeto_clinica/
+-- app/
¦   +-- database/
¦   ¦   +-- db.py
¦   ¦   +-- __init__.py
¦   +-- models/
¦   ¦   +-- anamnesis.py
¦   ¦   +-- appointment.py
¦   ¦   +-- client.py
¦   ¦   +-- procedure.py
¦   ¦   +-- user.py
¦   ¦   +-- __init__.py
¦   +-- repositories/
¦   +-- routes/
¦   +-- services/
¦   +-- static/
¦   ¦   +-- css/
¦   ¦   +-- js/
¦   +-- templates/
¦   ¦   +-- anamnesis/
¦   ¦   +-- appointments/
¦   ¦   +-- auth/
¦   ¦   +-- clients/
¦   ¦   +-- main/
¦   ¦   +-- procedures/
¦   +-- utils/
¦   +-- config.py
¦   +-- __init__.py
+-- instance/
¦   +-- clinica.sqlite3
+-- .env.example
+-- .gitignore
+-- app.py
+-- README.md
+-- requirements.txt
+-- run.py
+-- wsgi.py
```

## Arquitetura

### routes
Recebem as requisicoes HTTP, validam o fluxo web e encaminham a operacao para a camada de servicos.

### services
Concentram as regras de negocio, como:
- autenticacao
- calculo de lucro
- validacao de conflito de horario
- preparacao de lembretes simulados

### repositories
Isolam o acesso ao banco de dados para leitura e escrita das entidades.

### models
Representam as entidades principais do sistema:
- User
- Client
- Procedure
- Appointment
- Anamnesis

### templates
Organizam as telas HTML por funcionalidade.

### static
Mantem CSS e JavaScript separados para preservar legibilidade e facilitar manutencao.

## Como executar o projeto

1. Abra a pasta `C:\Users\Moyses\Desktop\projeto_clinica` no VS Code.
2. Instale as dependencias:

```bash
python -m pip install -r requirements.txt
```

3. Execute a aplicacao:

```bash
python run.py
```

4. Acesse no navegador:

```text
http://127.0.0.1:5000
```

## Credenciais iniciais

```text
Usuario: admin
Senha: admin123
```

## Funcionalidades atuais
- Login e logout
- Menu principal
- Cadastro de procedimentos com calculo automatico de lucro
- Cadastro de clientes com WhatsApp
- Ficha de anamnese vinculada a cliente
- Agenda mensal com horario AM/PM e duracao
- Validacao de conflito de horarios
- Lembretes simulados para futura integracao com WhatsApp
- Gerenciamento mensal com custo, valor e lucro

## Estrategia de branches

### Branches principais
- `main`: branch estavel, recebe apenas codigo revisado
- `develop`: branch de integracao do desenvolvimento

### Branches de funcionalidade
- `feature/auth-login`: login, logout e autenticacao
- `feature/dashboard`: tela inicial, menu principal e navegacao
- `feature/database`: estrutura do banco, modelos e persistencia
- `feature/procedures`: cadastro e listagem de procedimentos
- `feature/clients-anamnesis`: cadastro de clientes e ficha de anamnese
- `feature/appointments`: agenda, conflitos de horario e gerenciamento mensal
- `feature/layout-ui`: organizacao visual, CSS, responsividade e templates
- `docs/readme`: documentacao do projeto

### Observacao importante
Como a primeira versao funcional atual cruza varias areas do sistema ao mesmo tempo, foi criada uma branch de consolidacao:

- `feature/clinic-core`

Ela preserva a base funcional atual sem poluir a `main`, enquanto as proximas evolucoes podem seguir separadas por modulo.

## Commits sugeridos

```text
chore: create develop and feature branch strategy
feat: add clinic core Flask architecture
feat: add authentication flow
feat: add procedures module
feat: add clients and anamnesis module
feat: add appointments and management module
style: refine UI structure and styles
docs: update project README
```
