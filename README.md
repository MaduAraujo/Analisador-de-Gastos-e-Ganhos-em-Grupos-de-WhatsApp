# 💬 Analisador de Gastos e Ganhos em Grupos de WhatsApp

Este projeto em Python lê um arquivo ```.txt``` exportado de um grupo do WhatsApp e analisa mensagens que envolvem valores financeiros. 

## ✨ Funcionalidades

* **Processamento Inteligente:** Lê e interpreta mensagens de texto do WhatsApp para identificar transações financeiras (gastos e ganhos).
* **Tabelas Detalhadas:** Apresenta tabelas claras de todas as transações de gastos e ganhos.
* **Identificação do Maior Gasto:** Destaca automaticamente a maior despesa registrada.
* **Resumo Financeiro Total:** Gera um gráfico de pizza que mostra a proporção total entre gastos e ganhos.
* **Análise de Fluxo Mensal:** Cria gráficos de barras para visualizar a evolução mensal de gastos e ganhos.
* **Agrupamento por Categoria:** Apresenta um gráfico dos 10 maiores gastos por categoria, ajudando a identificar onde seu dinheiro está sendo mais investido.
* **Agrupamento por Pessoa/Remetente:** Gera um gráfico dos 10 maiores gastos por remetente (pessoa), útil para rastrear quem está registrando as despesas.
* **Exportação para CSV:** Salva todos os dados processados em um arquivo CSV para análises posteriores em outras ferramentas (Excel, Google Sheets, etc.).

## 🚀 Como Usar

Siga estes passos simples para configurar e rodar o analisador financeiro:

### Pré-requisitos

Certifique-se de ter Python instalado em seu sistema. Você também precisará das seguintes bibliotecas Python:

* `pandas`
* `matplotlib`
* `re` (geralmente já incluído no Python)

Você pode instalar as bibliotecas necessárias usando `pip`:

```bash
pip install pandas matplotlib
```

### Preparação do Arquivo de Conversa

1.  **Exporte sua conversa do WhatsApp:**

      * No WhatsApp, abra a conversa que contém os registros financeiros.
      * Toque no nome do grupo/contato na parte superior para ver as informações.
      * Role para baixo e selecione "Exportar conversa".
      * Escolha "Sem mídia" para exportar apenas o texto.
      * Salve este arquivo de texto com o nome **`conversas_whatsapp.txt`** no **mesmo diretório** onde você salvou o script Python (`analisador_financeiro.py`).

     **Formato da Mensagem:** Para que o script funcione corretamente, suas mensagens de transação devem seguir um padrão específico:

    > `[Data e Hora] - [Nome do Remetente]: [Categoria da Transação] [+/-Valor]`

     **Exemplos Válidos:**

    >   * `21/06/2025 17:00 - Maria Eduarda: Padaria -20`
    >   * `21/06/2025 17:00 - Maria Eduarda: Cartão +100`
    >   * `20/06/2025 10:30 - Carlos: Salário +2500`
    >   * `22/06/2025 09:00 - Bruno: Academia -80`

### Executando o Script

1.  **Salve o Código:** Salve o código Python fornecido em um arquivo, por exemplo, `analisador_financeiro.py`.

2.  **Execute via Terminal:** Abra um terminal ou prompt de comando, navegue até o diretório onde você salvou os arquivos e execute o script:

    ```bash
    python analisador_financeiro.py
    ```

### Saída

O script irá imprimir no console as tabelas de gastos e ganhos, o maior gasto, e então exibirá uma série de gráficos interativos (um por um) em janelas separadas:

  * Gráfico de Pizza: Resumo Financeiro Total
  * Gráfico de Barras: Gastos Mensais
  * Gráfico de Barras: Ganhos Mensais
  * Gráfico de Barras: Top 10 Gastos por Categoria
  * Gráfico de Barras: Top 10 Gastos por Pessoa (Remetente)
