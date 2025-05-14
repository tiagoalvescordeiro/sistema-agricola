import sqlite3
from datetime import datetime

# Caminho do banco SQLite
DB_NAME = 'irrigacao.db'

# Criação da tabela
def criar_tabela():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS leituras (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            umidade REAL,
            fosforo INTEGER,
            potassio INTEGER,
            ph REAL,
            timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Leitura dos dados do arquivo dados.txt
def ler_dados_txt(arquivo='dados.txt'):
    dados = []
    with open(arquivo, 'r') as f:
        for linha in f:
            if linha.strip():
                try:
                    partes = linha.strip().split('|')
                    umidade = float(partes[0].split(':')[1].replace('%', '').strip())
                    fosforo = int(partes[1].split(':')[1].strip())
                    potassio = int(partes[2].split(':')[1].strip())
                    ph = float(partes[3].split(':')[1].strip())
                    dados.append((umidade, fosforo, potassio, ph, datetime.now().isoformat()))
                except Exception as e:
                    print(f"⚠️ Erro ao processar linha: {linha.strip()} -> {e}")
    return dados

# Inserção no banco
def inserir_dados(dados):
    print(f"Inserindo {len(dados)} linhas no banco...")
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.executemany('''
        INSERT INTO leituras (umidade, fosforo, potassio, ph, timestamp)
        VALUES (?, ?, ?, ?, ?)
    ''', dados)
    conn.commit()
    conn.close()

# Leitura (consulta)
def listar_todos():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM leituras')
    for linha in cursor.fetchall():
        print(linha)
    conn.close()

# Atualizar pH de uma leitura
def atualizar_ph(id, novo_ph):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('UPDATE leituras SET ph = ? WHERE id = ?', (novo_ph, id))
    conn.commit()
    conn.close()

# Remover uma linha
def deletar_leitura(id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM leituras WHERE id = ?', (id,))
    conn.commit()
    conn.close()

# Executa o fluxo principal
if __name__ == '__main__':
    criar_tabela()
    dados = ler_dados_txt()
    inserir_dados(dados)
    print("📥 Leituras inseridas com sucesso! Aqui estão os registros:")
    listar_todos()
