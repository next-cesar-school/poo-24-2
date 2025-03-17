# NExT 2024.2

![CESAR School](/cesar_school.png)

## Aula de Revisão

### Na aula de hoje

- Manipulação de Arquivos
- Orientação a Objetos

------------------

## Objetivo

Nesta aula, nosso objetivo será revisar os principais conceitos de Programação Orientada a Objetos (POO) e, ao mesmo tempo, relembrar como manipular arquivos em Python. Faremos isso de maneira prática, desenvolvendo juntos um programa que:

1. **Lê dados** de um arquivo de entrada.
2. **Processa** esses dados utilizando classes e métodos.
3. **Gera** um arquivo de saída, aplicando transformações sobre os dados originais.

## 1. Conceitos Principais de POO (Revisão Rápida)

1. **Classe**

    > **Modelo** ou “molde” que descreve um conjunto de objetos com características e comportamentos semelhantes.

2. **Objeto**

    > É uma **instância** concreta de uma classe.

3. **Atributos**

    São as **variáveis** que armazenam o estado de um objeto.

4. **Métodos**

    São as **funções** que descrevem o comportamento do objeto.

5. **Encapsulamento**

    Ideia de **proteger** (ou controlar) o acesso a determinados atributos ou métodos.

6. **Herança**

    Permite uma classe (filha) **herdar** atributos e métodos de outra classe (pai).

7. **Polimorfismo**

    A capacidade de métodos se comportarem de formas diferentes em classes diferentes, mas compartilhando uma mesma **interface**.

## 2. Manipulação de Arquivos em Python

### Leitura

```python
with open('entrada.txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        # Processa cada linha
```

### Escrita

```python
with open('saida.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write("Seu texto aqui\n")
```

### Uso do `with open(...) as ...:`

- Garante que o arquivo seja fechado automaticamente ao sair do bloco;
- Evita problemas de vazamento de recursos.

## 3. Exemplos Práticos

Vamos desenvolver vários programas para colocar em prática os conceitos mais importantes de **manipulação de arquivos** e **programação orientada a objetos**.

### 3.1 Processador de Texto

Uma empresa precisa padronizar como os textos salvos em determinados arquivos são escritos. Você deve criar um programa que peça ao usuário que informe o modo de processamento de arquivo (todo em maiúsculo ou todo em minúsculo) e, em seguida, o nome do arquivo de entrada e o nome do arquivo de saída.

#### 3.1.1 Diagrama Simplificado

```txt
┌────────────────────┐
│ + ProcessadorTexto │
│--------------------│
│ - modo_processo    │
│--------------------│
│ + __init__(...)    │
│ + processar(linha) │
└────────────────────┘

┌───────────────────────────┐
│ Programa Principal (main) │
│---------------------------│
│ 1) Ler arquivo            │
│ 2) Processar linha        │
│ 3) Escrever saída         │
└───────────────────────────┘
```

#### 3.1.2 Requisitos

- O **Processador de Texto** deve ser capaz de converter todas as linhas do arquivo para um desses modos:
  - Modo `upper`, converte a linha para maiúsculas;
  - Modo `lower`, converte a linha para minúsculas;
  - Modo `strip`, remove espaços excedentes;
  - Modo `list`, numerar as linhas.
- O **Processador de Texto** deve ser responsável apenas pela manipulação do texto, mas não dos arquivos;
- O processamento de dados deve ocorrer linha a linha;
- Os arquivos devem ser lidos e escritos em 'utf-8';
- O usuário deve ser notificado quando o programa terminar de executar;
- Arquivos de entrada disponíveis [aqui](/aula_revisao/processador/).

### 3.2 Email Institucional

A Instituição Zesar School precisa automatizar parte do processamento de dados sobre os estudantes. Os dados de entrada são provenientes de um formulário. A partir deles, você deve criar um arquivo `.csv` de saída onde:

- Tenha o **nome** separado do **segundo nome/sobrenome**;
  - Os nomes devem ser escritos em capitular (quando apenas a primeira letra fica maiúscula);
  - As preposições dos nomes devem ser ignoradas;
  - Se o nome do estudante é `ROSA DE AGUIAR MENDONÇA ALVES`, o registro deve ser `Rosa Aguiar`;
- Deve ser criado um email institucional com as iniciais do nome do estudante
  - As preposições dos nomes devem ser ignoradas;
  - O email institucional é sempre `@zesar.school`;
  - Se o nome do estudante é `ROSA DE AGUIAR MENDONÇA ALVES`, o seu email institucional registro deve ser `rama@zesar.school`;
  - Caso outro estudante possua as mesmas iniciais, deve ser incrementado no email um número como `rama2@zesar.school`. Isso deve garantir que os emails sejam únicos;
- O programa deve gerar como saída um arquivo `.csv` com o seguinte cabeçalho:
  - `nome,sobrenome,email_institucional,codigo`
  - Apenas os estudantes matriculados ou com pendências devem ter seus registros no arquivo.
- Arquivo de entrada disponível [aqui](/aula_revisao/email/dados_entrada.csv).
