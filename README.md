# 🗂️ Sistema RH

Sistema web de administração de funcionários desenvolvido com Django.

---

## 📋 Sobre o projeto

O Sistema RH é uma aplicação web genérica para gerenciamento de funcionários em ambiente empresarial. Permite cadastrar departamentos, funcionários e registrar horas trabalhadas, calculando automaticamente as horas extras de cada colaborador.

O sistema possui dois perfis de acesso:

- **Administrador** — gerencia todos os funcionários, departamentos e registros de horas.
- **Funcionário** — acessa apenas o próprio perfil e os próprios registros.

---

## 🚀 Tecnologias utilizadas

- Python 3
- Django 5
- PostgreSQL
- psycopg2-binary
- python-decouple
- HTML5 / CSS3

---

## ⚙️ Como rodar o projeto localmente

### Pré-requisitos

- Python 3.11+
- PostgreSQL instalado e rodando
- Git

### Passo a passo

**1. Clone o repositório**

```bash
git clone https://github.com/paulo-bento/sistema-rh.git
cd sistema-rh
```

**2. Crie e ative o ambiente virtual**

```bash
python -m venv venv
source venv/bin/activate
```

**3. Instale as dependências**

```bash
pip install -r requirements.txt
```

**4. Configure o banco de dados**

No PostgreSQL, crie o banco e o usuário:

```sql
CREATE DATABASE rh_db;
CREATE USER rh_user WITH PASSWORD 'rh_pass';
GRANT ALL PRIVILEGES ON DATABASE rh_db TO rh_user;
ALTER DATABASE rh_db OWNER TO rh_user;
```

**5. Crie o arquivo `.env` na raiz do projeto**

```env
SECRET_KEY=sua-secret-key-aqui
DEBUG=True
DB_NAME=rh_db
DB_USER=rh_user
DB_PASSWORD=rh_pass
DB_HOST=localhost
DB_PORT=5432
```

**6. Execute as migrations**

```bash
python manage.py migrate
```

**7. Crie o superusuário**

```bash
python manage.py createsuperuser
```

**8. Rode o servidor**

```bash
python manage.py runserver
```

Acesse em: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🗄️ Modelos

| Model | Descrição |
|---|---|
| `Departamento` | Representa um setor da empresa |
| `Funcionario` | Vinculado a um usuário Django via OneToOne |
| `RegistroHoras` | Registro diário de horas trabalhadas por funcionário |

---

## ✅ Funcionalidades

- Login e logout com autenticação Django
- Controle de acesso por perfil (admin / funcionário)
- CRUD completo de funcionários com CBVs
- CRUD completo de registros de horas com CBVs
- Cálculo automático de horas extras via Django Signals
- Feedback de ações com Django Messages
- Formulários com ModelForms
- Paginação e filtro de busca por nome

---

## 👥 Equipe

Felipe Erik, João Paulo e Raul Carvalho

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
