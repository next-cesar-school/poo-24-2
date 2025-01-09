# NExT 2024.2 | POO

![CESAR School](/cesar_school.png)

## Aula 12 - Projeto

### Na aula de hoje

- Vamos criar uma aplicação que utilize:
  - Classes, objetos e atributos;
  - Encapsulamento e abstração;
  - Herança e polimorfismo;
  - Validação de dados (CPF, endereço);
  - Manipulação de arquivos JSON.

------------------

## Objetivo

Esta aula tem como foco consolidar todos os conceitos aprendidos ao longo do curso por meio do desenvolvimento de um projeto prático: o **FORJA Contatos**. Este projeto será uma aplicação de console que gerencia contatos de pessoas e jogos relacionados a estúdios de desenvolvimento.

O objetivo é criar uma aplicação que utilize uma combinação de conceitos fundamentais de **Programação Orientada a Objetos (POO)**. Essa seleção de funcionalidades foi planejada para refletir os pilares do curso, permitindo que os alunos consolidem o conhecimento em herança, encapsulamento, polimorfismo e manipulação de dados. A aplicação serve como um exemplo prático e funcional que simula um cenário real de gestão de contatos, reforçando a importância de cada conceito abordado.

Vamos realizar a integração dos projetos CEP e CPF com o FORJA Contatos.

## Diagrama UML das Classes

A aplicação será estruturada com base em cinco classes principais, que apresentam relações de herança e composição entre si.

Estrutura de Classes

```text
Entidade (abs)
|
|-- Pessoa
|   |-- CPF
|   |-- Endereco
|       |-- CEP
|
|-- Jogo

GameStudio
|
|-- Lista de Pessoas
|-- Lista de Jogos
```

### Descrição das Classes

- **`Entidade`**: Classe base **abstrata** com atributos comuns a `Pessoa` e `Jogo`, com `nome` e `ativo`.
- **`Pessoa`**: Representa uma pessoa do estúdio, contendo `CPF`, `Endereço`.
- **`Jogo`**: Representa um jogo do estúdio, com `status` de projeto (em pre-produção, em desenvolvimento, lançado...) e se está ativo ou não.
- **`GameStudio`**: Classe central que armazena listas de `Pessoas` e `Jogos`.
- **`Endereco/CEP`**: Classe para representar endereços com número e complemento.

## Funcionalidades

A aplicação **FORJA Contatos** oferecerá as seguintes funcionalidades, cada uma contribuindo com controle e organização eficiente dos dados de estúdios e seus membros.

A manipulação de arquivos **JSON** permite a persistência de dados, sendo essencial para manter o progresso salvo. O **menu interativo** simplifica o uso, tornando a aplicação acessível a todos os usuários.

- Adicionar novo **GameStudio**;
- Adicionar nova **Pessoa** (com validação de CPF e preenchimento automático de endereço via CEP);
- Adicionar novo **Jogo** (associado ao GameStudio);
- Listar Pessoas cadastradas;
- Listar Jogos cadastrados;
- Salvar dados em arquivo JSON;
- Carregar dados de arquivo JSON;
- Menu interativo em console para selecionar operações.

## Implementação do Código

Para facilitar o desenvolvimento e garantir a correção das dependências, recomenda-se seguir a seguinte ordem de implementação:

1. Implementar a classe base `CPF` (se ainda não estiver implementada);
2. Implementar a classe base `CEP` (se ainda não estiver implementada);
3. Criar a classe `Endereco`, que herda de CEP e adiciona os atributos `número` e `complemento`; Lembre-se de usar `super()` para acessar o contrutor, os atributos e os métodos da classe base;
4. Desenvolver a **classe abstrata** `Entidade`, que servirá como base para `Pessoa` e `Jogo`; Esta classe deve possuir os atributos nome (`str`) e ativo (`bool = True`) e os métodos `exibir_info()` (abstrato) e `atualizar_ativo(bool)`.
5. Implementar a classe `Pessoa`, utilizando `Endereco` e `CPF` como composições;
6. Criar a classe `Jogo`, herdando de `Entidade`;
7. Construir a classe `GameStudio`, que gerenciará listas de `Pessoa` e `Jogo`;
8. Desenvolver o menu interativo em um arquivo principal (por exemplo, `main.py`).

## Como deixar seu código mais supimpa para seu portfólio

Pensando em usar este projeto como portfólio, o segredo é impressionar pela excelência! Depois que tudo estiver funcionando:

1. **Versionamento**: Versione o código com cuidado, usando mensagens de commit claras e bem estruturadas;
2. **Design de Código**: Revise seu código buscando eventuais melhorias em como você realizou as relações entre as classes, nomes de variáveis, nomes de métodos, estruturas de repetição...
3. **Exceções**: Implemente Exceções personalizadas, trazendo mais robustez para seu código;
4. **Documentação**: Documente os módulos, classes e os métodos públicos de forma adequada;
5. **README**: Explique do que se trata o projeto e pontue que você está iniciando seus estudos em programação;
6. **Testes Unitários**: Procure alcançar 100% de cobertura nos testes unitários (geralmente, quem está começando ainda não sabe o que são testes unitários);
7. **LinkedIn**: Registre esta sua conquista no LinkedIn fazendo uma postagem com texto breve, explicando o que você aprendeu com o projeto, e adicionando um link para o repositório.
