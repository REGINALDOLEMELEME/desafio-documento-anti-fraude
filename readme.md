# Desafio Documento Anti-Fraude

Este é um projeto desenvolvido para realizar verificações de cartões a fim de prevenir fraudes. A aplicação utiliza integração com serviços externos e armazenamento na nuvem para processar e armazenar os dados.

## Estrutura do Projeto

- **app.py**: Arquivo principal que inicia a aplicação.
- **services/**: Contém a lógica de integração com serviços externos.
- **utils/**: Inclui funções auxiliares reutilizáveis no projeto.
- **requirments.txt**: Lista de dependências Python necessárias para executar a aplicação.
- **.env**: Arquivo de configuração para variáveis de ambiente.

## Configuração e Uso

### Pré-requisitos

- Python 3.8+
- Pip (Gerenciador de pacotes do Python)
- Conta e configurações de serviços necessários (por exemplo, Azure).

### Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/REGINALDOLEMELEME/desafio-documento-anti-fraude.git
    cd desafio-documento-anti-fraude
    ```

2. Instale as dependências:

    ```bash
    pip install -r src/requirments.txt
    ```

3. Configure as variáveis de ambiente criando um arquivo `.env` na pasta `src` com o seguinte conteúdo:

    ```env
    ENDPOINT={BASE_ENDPOINT}
    SUBSCRIPTION_KEY={BASE_SUBSCRIPTION_KEY}
    AZURE_STORAGE_CONNECTION_STRING={BASE_AZURE_STORAGE_CONNECTION_STRING}
    CONTAINER_NAME={BASE_CONTAINER_NAME}
    ```

    Substitua os valores com suas credenciais e configurações.

4. Execute a aplicação:

    ```bash
    python src/app.py
    ```

## Funcionalidades

- Verificação de documentos utilizando APIs externas.
- Armazenamento seguro de informações na nuvem.

## Contribuições

Contribuições são bem-vindas! Siga os passos para criar um pull request com suas melhorias.

---

Feito com :heart: por REGINALDOLEMELEME.
