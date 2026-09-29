# Sistema de Gestão de Notas

> Script em Python 3 para cadastro de notas de alunos, cálculo de média e
> verificação automática da situação final (Aprovado / Reprovado).

[![Python](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-est%C3%A1vel-brightgreen.svg)](#)

---

## Sobre o projeto

O **Sistema de Gestão de Notas** é um script simples e didático, escrito em
Python 3, que permite a um professor (ou a um aluno) cadastrar as notas de
um aluno, calcular a média aritmética e exibir a situação final.

O projeto foi pensado como exercício de introdução à linguagem Python,
cobrindo conceitos fundamentais como:

- Funções e modularização
- Estruturas de repetição (`while`)
- Tratamento de exceções (`try` / `except`)
- Listas
- Formatação de strings (`f-strings`)

---

## Funcionalidades

- Cadastro interativo de notas via terminal
- Validação de entrada (aceita apenas números entre `0` e `10`)
- Encerramento do cadastro digitando `fim`
- Cálculo automático da média aritmética
- Classificação do aluno:
  - **Aprovado** — média maior ou igual a `7.0`
  - **Reprovado** — média menor que `7.0`
- Exibição de relatório final com todas as notas, média e situação
- Tratamento de erros para entradas inválidas

---

## Requisitos

- **Python 3.6 ou superior** (por causa do uso de `f-strings`)
- Nenhuma dependência externa — apenas biblioteca padrão

---

## Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/sistema-notas.git
cd sistema-notas
```

### 2. Execute o script

```bash
python3 notas.py
```

No Windows, dependendo da instalação:

```bash
python notas.py
```

---

## Exemplo de uso

```text
=== Sistema de Gestão de Notas ===
Digite a nota do aluno (ou 'fim' para encerrar): 8.5
Digite a nota do aluno (ou 'fim' para encerrar): 6.0
Digite a nota do aluno (ou 'fim' para encerrar): 9.0
Digite a nota do aluno (ou 'fim' para encerrar): 11
Por favor, insira uma nota válida entre 0 e 10.
Digite a nota do aluno (ou 'fim' para encerrar): abc
Entrada inválida. Digite um número ou 'fim'.
Digite a nota do aluno (ou 'fim' para encerrar): fim

--- RELATÓRIO FINAL ---
Notas inseridas: [8.5, 6.0, 9.0]
Média do aluno: 7.83
Situação do aluno: Aprovado
------------------------
```

---

## Estrutura do código

O script é organizado em funções pequenas, cada uma com responsabilidade única:

| Função | Descrição |
|---|---|
| `cadastrar_notas()` | Solicita as notas ao usuário e retorna uma lista |
| `calcular_media(notas)` | Calcula a média aritmética da lista |
| `verificar_situacao(media)` | Retorna `"Aprovado"` ou `"Reprovado"` |
| `exibir_relatorio(notas, media, situacao)` | Imprime o relatório final |
| `main()` | Orquestra o fluxo do programa |

### Fluxo de execução

```
main()
  │
  ├── cadastrar_notas()        → lista de notas
  │
  ├── calcular_media(notas)    → média
  │
  ├── verificar_situacao(media) → situação
  │
  └── exibir_relatorio(...)    → imprime na tela
```

---

## Regras de negócio

| Regra | Descrição |
|---|---|
| Faixa válida de notas | Somente valores entre `0` e `10` (inclusive) |
| Comando de encerramento | Digitar `fim` (case-insensitive) |
| Média de aprovação | `>= 7.0` |
| Lista vazia | Se nenhuma nota for informada, o script encerra sem relatório |

---

## Tratamento de erros

| Situação | Comportamento |
|---|---|
| Usuário digita valor fora da faixa | Mensagem de aviso e repete a pergunta |
| Usuário digita texto não numérico | Mensagem de erro e repete a pergunta |
| Usuário não informa nenhuma nota | Mensagem `"Nenhuma nota foi informada."` e encerra |

---

## Possíveis melhorias

Ideias para expandir o projeto:

- [ ] Suporte a **múltiplos alunos** em uma mesma execução
- [ ] Cadastro com **nome do aluno** associado às notas
- [ ] Persistência em **arquivo** (`.txt`, `.csv` ou `.json`)
- [ ] Leitura de notas a partir de um **arquivo externo**
- [ ] Interface em **linha de comando** com `argparse`
- [ ] Testes automatizados com `pytest`
- [ ] Configuração da **média de aprovação** como parâmetro
- [ ] Cálculo de **nota mínima necessária** para aprovação
- [ ] Versão com **interface gráfica** (Tkinter)
- [ ] Versão web com **Flask** ou **FastAPI**

---

## Estrutura de arquivos sugerida

```
sistema-notas/
├── notas.py          # script principal
├── README.md         # este arquivo
├── LICENSE           # licença MIT
└── tests/
    └── test_notas.py # testes (a implementar)
```

---

## Testando manualmente

Casos de teste rápidos para validar o comportamento:

| Cenário | Entrada | Resultado esperado |
|---|---|---|
| Aluno aprovado | `8`, `9`, `7`, `fim` | Média `8.00`, situação `Aprovado` |
| Aluno reprovado | `5`, `4`, `6`, `fim` | Média `5.00`, situação `Reprovado` |
| Nota exatamente na média | `7`, `7`, `7`, `fim` | Média `7.00`, situação `Aprovado` |
| Nota fora da faixa | `11`, `-1`, `5`, `fim` | Apenas `5` é aceita |
| Texto inválido | `abc`, `7`, `fim` | Apenas `7` é aceita |
| Nenhuma nota | `fim` | `"Nenhuma nota foi informada."` |

---

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).

---

## Autoria

**Patricia Gomes Dias** — desenvolvimento inicial

Se você usar este projeto como base para estudos ou melhorias, mantenha os
créditos à autora original.

---

## Contribuindo

Contribuições são bem-vindas. Se quiser propor uma melhoria:

1. Faça um **fork** do repositório
2. Crie uma branch descritiva (`git checkout -b feat/multiplos-alunos`)
3. Commit suas mudanças (`git commit -m "feat: suporte a multiplos alunos"`)
4. Faça o push (`git push origin feat/multiplos-alunos`)
5. Abra um **Pull Request**

---

## Agradecimentos

Projeto desenvolvido como exercício de aprendizado de Python, cobrindo
conceitos básicos de entrada de dados, validação, cálculo e formatação
de saída.
