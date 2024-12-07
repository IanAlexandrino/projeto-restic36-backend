# projeto-restic36-backend

Este é um sistema de gerenciamento médico desenvolvido em Django. Ele foi projetado para gerenciar informações sobre consultas, profissionais de saúde, pacientes, instituições, históricos médicos e prescrições, entre outros.

## 📑 Funcionalidades

- **Gestão de Pacientes**: Cadastro de pacientes com informações detalhadas como CPF, endereço, data de nascimento, entre outros.
- **Gerenciamento de Profissionais de Saúde**: Registro de profissionais, incluindo tipo de profissional e instituição associada.
- **Controle de Instituições**: Cadastro e classificação de instituições com base em tipos definidos.
- **Gestão de Consultas**: Registro de consultas associadas a pacientes, profissionais e instituições.
- **Prescrições Médicas**: Controle de medicamentos prescritos, incluindo dosagem, frequência e responsável pela prescrição.
- **Histórico Médico**: Registro de doenças, diagnósticos e observações relacionadas a pacientes.
- **Histórico de Acesso**: Monitoramento de acessos ao sistema.
- **Gestão de Exames**: Armazenamento de informações sobre exames realizados.

## 🗂️ Estrutura do Banco de Dados

### Principais Entidades

1. **Paciente**
   - Contém informações pessoais como nome, CPF, data de nascimento e contato.
2. **Profissional de Saúde**
   - Relacionado ao tipo de profissional e à instituição onde trabalha.
3. **Instituição**
   - Armazena informações da instituição e é categorizada por tipo.
4. **Consulta**
   - Registra as consultas realizadas, conectando pacientes, profissionais e instituições.
5. **Prescrição Médica**
   - Armazena informações de medicamentos prescritos a pacientes.
6. **Histórico de Doenças**
   - Registra doenças diagnosticadas e suas respectivas datas.
7. **Histórico de Acesso**
   - Gerencia registros de acesso ao sistema por profissionais e pacientes.
8. **Exame**
   - Registra exames realizados, seus resultados e a instituição responsável.

### Relacionamentos

- **Consulta**:
  - Relacionada com **Paciente**, **Profissional de Saúde**, **Instituição** e **Tipo de Consulta**.
- **Profissional de Saúde**:
  - Associado a um **Tipo de Profissional** e a uma **Instituição**.
- **Instituição**:
  - Categorizada por um **Tipo de Instituição**.
- **Prescrição Médica**:
  - Associada a um **Paciente**, **Profissional de Saúde** e **Instituição**.
- **Histórico de Doenças**:
  - Associado a um **Paciente** e a um **Profissional de Saúde**.
- **Exame**:
  - Associado a um **Paciente**, **Profissional de Saúde** e **Instituição**.

## 🚀 Tecnologias Utilizadas

- **Backend**: Django Framework
- **Banco de Dados**: SQLite (com possibilidade de migração para PostgreSQL)
- **Bibliotecas Django**:
  - Django REST Framework (para API, se aplicável)
  - Django Admin (para gerenciamento de dados)

## 🛠️ Configuração do Projeto

### Pré-requisitos

- Python 3.8 ou superior

### Passos para Instalação

1. Clone o repositório:

   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd nome_do_projeto
   ```

2. Crie e ative um ambiente virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Realize as migrações do banco de dados:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Inicie o servidor:

   ```bash
   python manage.py runserver
   ```

6. Acesse o sistema em http://localhost:8000.

## 🧪 Testes

Para executar os testes automatizados:

```bash
python manage.py test
```