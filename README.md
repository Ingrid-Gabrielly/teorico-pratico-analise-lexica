# Validador de Índices

Este trabalho teórico prático consiste em uma função de validação de índices que verifica se uma expressão de índice está no formato esperado para uma variável `x`, usando diferentes padrões (inteiros, intervalos numéricos, nomes entre aspas e intervalos de nomes entre aspas).

## 🐍 Pré-requisitos

Para executar este código, você precisará de:
- Python 3.x

## Clonando o Repositório

Para clonar o repositório e executar o projeto localmente, siga estas etapas:

1. **Abra o terminal** e navegue até o diretório onde deseja clonar o repositório.
2. Execute o comando abaixo para clonar o repositório:

    ```bash
    git clone https://github.com/Ingrid-Gabrielly/teorico-pratico-analise-lexica.git
    ```

3. Navegue até o diretório do projeto clonado:

    ```bash
    cd teorico-pratico-analise-lexica
    ```

## 📁 Estrutura do Código

O projeto contém as seguintes partes principais:

- **Função `is_valid_index(input_string)`**: Recebe uma string e verifica se ela é um índice válido no formato `x[indices]`, usando expressões regulares para identificar os padrões permitidos.
- **Função `main()`**: Contém uma lista de exemplos de índices para testar a função `is_valid_index`. Ela executa a verificação em cada exemplo e exibe se cada um é "Válido" ou "Inválido" de acordo com os padrões definidos.

## ⌨️ Instruções de Execução

1. **Abra o VS Code** e certifique-se de que você está no diretório do projeto onde o arquivo está salvo.
2. No terminal do VS Code, execute o script usando o comando:

    ```bash
    python verificar_indice.py
    ```

## 🔎 Exemplo de Saída

Ao executar o código, você verá a seguinte saída (a depender da lista de exemplos definida):

```plaintext
x[0]: Válido
x[-0]: Inválido
x[10]: Válido
x[-5]: Válido
x[1:5]: Válido
x[-10:-1]: Válido
x[-0:-0]: Inválido
x[-10:1]: Inválido
x["Date"]: Válido
x['New Column']: Válido
x["Data":"State"]: Válido
x['Tested':'Data']: Válido
x[Tested':'Data']: Inválido
x[1:]: Inválido
x[:5]: Inválido
x[1:5:2]: Válido
x[nome]: Inválido
x['nome: Inválido
x["nome']: Inválido
y[1]: Inválido
x[1,2]: Inválido
x[]: Inválido
