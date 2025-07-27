# Sistema de Estoque para a Sede

## Descrição

O **Sistema de Estoque para a Sede** foi desenvolvido para gerenciar e monitorar o estoque de diferentes categorias de produtos. O sistema permite acompanhar a quantidade de itens, especificações e garantir a reposição automática de produtos essenciais ao atingir a quantidade mínima definida.

### Funcionalidades:

- **Controle de Estoque por Categorias**: O sistema é dividido em três abas principais:
  - **Estoque de Endomarketing**
  - **Estoque de Produtos de Limpeza**
  - **Estoque de Ações**

Cada aba apresenta as seguintes colunas para controle:

| Coluna                | Descrição                                                        |
| --------------------- | ---------------------------------------------------------------- |
| **Nome do Produto**   | Nome específico do item no estoque.                              |
| **Quantidade Atual**  | Número de unidades em estoque.                                   |
| **Especificação**     | Detalhes sobre o produto (tamanho, cor, embalagem, marca, etc.)  |
| **Quantidade Mínima** | Quantidade mínima do produto no estoque que ativa a notificação. |

### Funcionalidade de Notificação

O sistema envia notificações automáticas sempre que a quantidade de um item atinge ou fica abaixo da quantidade mínima estabelecida.

#### Exemplo de Notificação:

- Se a quantidade mínima de "cards de boas-vindas" for 10 unidades, o sistema enviará uma notificação assim que a quantidade atingir ou ficar abaixo desse valor.

**Notificações incluem:**

- **Alerta no sistema interno**: O sistema gerará um alerta visual dentro do painel para indicar que o produto precisa ser reposto.
- **E-mail de Aviso**: Um e-mail será enviado automaticamente para o responsável pela reposição do item, contendo as seguintes informações:
  - Nome do produto
  - Especificações do produto
  - Quantidade atual no estoque

#### Destinatário do E-mail:

- **albuquerque@teclat.com.br**

### Objetivo do Sistema

O objetivo deste sistema é otimizar o gerenciamento de estoque, evitando a falta de itens essenciais. Ele fornece uma maneira eficiente de monitorar a quantidade de produtos em estoque, emitindo alertas para garantir que os responsáveis possam realizar a reposição de forma ágil e eficaz. O sistema melhora a comunicação entre os setores e contribui para uma gestão mais precisa e eficiente dos recursos.

## Como Rodar o Projeto

### Pré-requisitos

- Python 3.x
- Django
- Biblioteca de envio de e-mail (ex: smtplib)
- Banco de dados configurado (ex: PostgreSQL, MySQL, SQLite, etc.)

### Instalação

1. Clone o repositório para sua máquina local:

   ```bash
   git clone https://github.com/usuario/projeto.git
   cd projeto
   ```

2. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

3. Configure o banco de dados e as variáveis de ambiente (`.env`):

   - Ajuste as configurações do SMTP no arquivo `.env` para que o envio de e-mails funcione corretamente.

4. Execute as migrações do banco de dados:

   ```bash
   python manage.py migrate
   ```

5. Inicie o servidor de desenvolvimento:
   ```bash
   python manage.py runserver
   ```
