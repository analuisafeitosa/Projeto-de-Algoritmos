import sqlite3

# Nome do arquivo .edges e do banco de dados
edges_file = 'aves-barn-swallow-contact-network.edges'
sqlite_db = './db/graph.db'

# Conectar ao banco de dados (ele será criado se não existir)
conn = sqlite3.connect(sqlite_db)
cursor = conn.cursor()

# Criar a tabela para armazenar as arestas com peso
cursor.execute('''
    CREATE TABLE IF NOT EXISTS edges (
        origin INTEGER,
        destination INTEGER,
        weight REAL
    )
''')

# Ler o arquivo .edges e inserir os dados no banco de dados
with open(edges_file, 'r') as file:
    for line in file:
        origin, destination, weight = line.strip().split()
        cursor.execute('INSERT INTO edges (origin, destination, weight) VALUES (?, ?, ?)', (int(origin), int(destination), float(weight)))

# Salvar as mudanças e fechar a conexão
conn.commit()
conn.close()

