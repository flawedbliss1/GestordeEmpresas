# Gestor de Empresas

Sistema simples em Python para cadastrar empresas, gerenciar seus pesos, calcular totais com base em quantidades informadas e executar tarefas auxiliares (soma de dias e leitura de informações de NFe). Os dados são persistidos localmente em um arquivo JSON.

> Para uso pessoal, distribuído publicamente por fins de adição ao portfólio pessoal.

---

## Funcionalidades

- **Multiplicar peso** — seleciona uma empresa e calcula `quantidade × peso`.
- **Adicionar empresa** — cadastra uma nova empresa com seu respectivo peso.
- **Remover empresa** — remove uma empresa cadastrada.
- **Listar empresas** — exibe todas as empresas e seus pesos.
- **Mudar peso** — atualiza o peso de uma empresa já cadastrada.
- **Somar dias** — calculadora de datas: o usuário informa um número de dias e o programa soma à data de hoje.
- **Listar informações de NFe** — lê um arquivo `.json` de nota fiscal e exibe suas informações.

Os dados das empresas são salvos automaticamente no arquivo `empresas.json`, garantindo persistência entre execuções.

---

## Requisitos

- **Python 3.6+**

---

## 🚀 Como executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/flawedbliss1/GestordeEmpresas.git
