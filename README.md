# Extrator de Dados de Repositórios GitHub

Esta ferramenta em Python permite extrair dados de repositórios, como nomes e linguagens de programação, de um usuário especificado do GitHub. Os dados extraídos são apresentados em um DataFrame do Pandas para fácil análise e manipulação.

## Pré-requisitos

- Python 3.x
- Pacote `requests`
- Pacote `pandas`

Você pode instalar os pacotes necessários usando o pip:

```bash
pip install requests pandas
```

## Configuração

1. Clone este repositório:

```bash
git clone [URL_DO_REPOSITÓRIO]
```

2. Navegue até o diretório do repositório:

```bash
cd nome_do_diretório
```

3. Armazene seu token de acesso ao GitHub:

Salve seu token de acesso ao GitHub em um arquivo chamado `token.txt`. Este será usado para autenticar as requisições à API do GitHub.

**Nota:** Por razões de segurança, nunca compartilhe seu token de acesso ou o envie para repositórios públicos.

## Uso

1. Importe as funções e classes necessárias:

```python
from nome_do_seu_script import read_token_from_file, GitHubRepos
```

2. Leia o token do arquivo e inicialize a ferramenta:

```python
TOKEN = read_token_from_file('token.txt')
github = GitHubRepos('seu_nome_de_usuario_github', TOKEN)
```

3. Extraia os dados e visualize:

```python
df = github.create_dataframe()
print(df)
```

Substitua `seu_nome_de_usuario_github` pelo nome de usuário do GitHub de quem você deseja extrair os repositórios.
