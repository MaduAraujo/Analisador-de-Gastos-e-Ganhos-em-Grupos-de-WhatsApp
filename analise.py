import pandas as pd
import matplotlib.pyplot as plt
import re

# Etapa 1: Carrega e processa o arquivo do WhatsApp
def processar_arquivo_whatsapp(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
        linhas = f.readlines()

    # Etapa 2: Expressão regular para pegar data, nome, categoria e valor
    # Foi adicionado um grupo para capturar a categoria antes do valor
    pattern = re.compile(r'(\d{2}/\d{2}/\d{4} \d{2}:\d{2}) - ([^:]+): (.+?) ([+-]?\d+)\b')
    dados = []

    # Etapa 3: Aplica o padrão para cada linha
    for linha in linhas:
        match = pattern.search(linha)
        if match:
            data, remetente, categoria, valor = match.groups()
            dados.append([data, remetente, categoria.strip(), int(valor)])

    # Etapa 4: Cria o DataFrame com pandas
    df = pd.DataFrame(dados, columns=['Data', 'Remetente', 'Categoria', 'Valor'])

    # Converte a coluna 'Data' para o formato datetime
    df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y %H:%M')
    return df

# Etapa 5: Analisa os dados e gera tabelas e gráfico
def analisar_transacoes(df):
    gastos = df[df['Valor'] < 0].copy()
    ganhos = df[df['Valor'] > 0].copy()

    print("\n--- 📊 Tabela de Gastos ---")
    if not gastos.empty:
        print(gastos[['Data', 'Categoria', 'Valor']].to_string(index=False))
    else:
        print("Nenhum gasto registrado.")

    print("\n--- 📈 Tabela de Ganhos ---")
    if not ganhos.empty:
        print(ganhos[['Data', 'Categoria', 'Valor']].to_string(index=False))
    else:
        print("Nenhum ganho registrado.")

    # Etapa 6: Mostra maior gasto
    if not gastos.empty:
        maior_gasto = gastos.loc[gastos['Valor'].idxmin()]
        print(f"\n--- 💸 Maior Gasto ---")
        print(f"Categoria: {maior_gasto['Categoria']} | Valor: R$ {abs(maior_gasto['Valor'])} | Data: {maior_gasto['Data'].strftime('%d/%m/%Y %H:%M')}")
    else:
        print("\n💸 Nenhum gasto identificado.")

    # Etapa 7: Gráfico de pizza simplificado
    total_gastos = -gastos['Valor'].sum() if not gastos.empty else 0
    total_ganhos = ganhos['Valor'].sum() if not ganhos.empty else 0
    labels = ['Gastos', 'Ganhos']
    valores = [total_gastos, total_ganhos]
    cores = ['red', 'blue']

    if total_gastos + total_ganhos > 0:
        plt.figure(figsize=(7, 7))
        plt.pie(valores, labels=labels, colors=cores, autopct='%1.1f%%', startangle=90, explode=(0.05, 0))
        plt.title('Resumo Financeiro Total', fontsize=16)
        plt.axis('equal')
        plt.tight_layout()
        plt.show()
    else:
        print("\nNão há dados suficientes para gerar o gráfico de resumo financeiro.")

    # Nova Etapa: Gráficos mensais
    gerar_graficos_mensais(df)

    # Nova Etapa: Gráficos por categoria e por pessoa
    gerar_graficos_por_agrupamento(gastos)

# Nova Função: Gerar gráficos mensais de gastos e ganhos
def gerar_graficos_mensais(df):
    if df.empty:
        print("\nNão há dados para gerar gráficos mensais.")
        return

    df['AnoMes'] = df['Data'].dt.to_period('M')

    # Agrupa por AnoMes para gastos
    gastos_mensais = df[df['Valor'] < 0].groupby('AnoMes')['Valor'].sum().abs()
    # Agrupa por AnoMes para ganhos
    ganhos_mensais = df[df['Valor'] > 0].groupby('AnoMes')['Valor'].sum()

    # Gráfico de Gastos Mensais
    if not gastos_mensais.empty:
        plt.figure(figsize=(12, 6))
        gastos_mensais.plot(kind='bar', color='#ff6666')
        plt.title('Gastos Mensais', fontsize=16)
        plt.xlabel('Mês/Ano', fontsize=12)
        plt.ylabel('Valor (R$)', fontsize=12)
        plt.xticks(rotation=45, ha='right')
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()
    else:
        print("\nNão há dados de gastos para gerar o gráfico mensal.")

    # Gráfico de Ganhos Mensais
    if not ganhos_mensais.empty:
        plt.figure(figsize=(12, 6))
        ganhos_mensais.plot(kind='bar', color='#66b3ff')
        plt.title('Ganhos Mensais', fontsize=16)
        plt.xlabel('Mês/Ano', fontsize=12)
        plt.ylabel('Valor (R$)', fontsize=12)
        plt.xticks(rotation=45, ha='right')
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()
    else:
        print("\nNão há dados de ganhos para gerar o gráfico mensal.")

# Nova Função: Gerar gráficos por agrupamento (categoria ou remetente)
def gerar_graficos_por_agrupamento(df_gastos):
    if df_gastos.empty:
        print("\nNão há gastos para agrupar por categoria ou pessoa.")
        return

    print("\n--- 📊 Análise por Agrupamento ---")

    # Agrupar gastos por Categoria
    gastos_por_categoria = df_gastos.groupby('Categoria')['Valor'].sum().abs().sort_values(ascending=False)

    if not gastos_por_categoria.empty:
        plt.figure(figsize=(12, 7))
        gastos_por_categoria.head(10).plot(kind='bar', color='salmon')
        plt.title('Top 10 Gastos por Categoria', fontsize=16)
        plt.xlabel('Categoria', fontsize=12)
        plt.ylabel('Valor Total Gasto (R$)', fontsize=12)
        plt.xticks(rotation=45, ha='right')
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()
    else:
        print("Não há gastos suficientes para agrupar por categoria.")

    # Agrupar gastos por Remetente (Pessoa)
    gastos_por_remetente = df_gastos.groupby('Remetente')['Valor'].sum().abs().sort_values(ascending=False)

    if not gastos_por_remetente.empty:
        plt.figure(figsize=(12, 7))
        gastos_por_remetente.head(10).plot(kind='bar', color='lightcoral')
        plt.title('Top 10 Gastos por Pessoa (Remetente)', fontsize=16)
        plt.xlabel('Pessoa (Remetente)', fontsize=12)
        plt.ylabel('Valor Total Gasto (R$)', fontsize=12)
        plt.xticks(rotation=45, ha='right')
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()
    else:
        print("Não há gastos suficientes para agrupar por pessoa.")


### 9. Exportar os Dados para .csv
# Esta função irá salvar o DataFrame completo em um arquivo CSV, facilitando a visualização e o uso em outras ferramentas.
def exportar_para_csv(df, nome_arquivo='transacoes_whatsapp.csv'):
    df.to_csv(nome_arquivo, index=False)
    print(f"\n✅ Dados exportados com sucesso para '{nome_arquivo}'")

# Etapa 8: Executa o script
if __name__ == "__main__":
    caminho = 'conversas_whatsapp.txt'
    try:
        df = processar_arquivo_whatsapp(caminho)
        analisar_transacoes(df)
        exportar_para_csv(df)
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho}' não foi encontrado. Por favor, verifique o caminho.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")