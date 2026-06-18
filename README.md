## Startar Projeto

### 1. Clonar o repositório

```bash
git clone git@github.com:nathanreis-droid/desafio-dogao.git
```

### 2. Criar o ambiente virtual

```bash
python -m venv .venv
```

### 3. Ativar o ambiente virtual

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux/MacOS

```bash
source .venv/bin/activate
```

### 4. Instalar as dependências do projeto

```bash
pip install -r requirements.txt
```

---

## Executando o Projeto

### Iniciar o servidor de desenvolvimento

```bash
python manage.py runserver
```

Após executar o comando, acesse:

```text
http://127.0.0.1:8000/login/
```

---
### Criar usuário administrador

```bash
python manage.py createsuperuser
```

### Acessar o painel administrativo

```text
http://127.0.0.1:8000/admin/
```

---

## Estrutura de Dependências

Todas as bibliotecas necessárias para execução do projeto estão listadas no arquivo:

```text
requirements.txt
```

Para instalar ou atualizar as dependências, execute:

```bash
pip install -r requirements.txt
```
