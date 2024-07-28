import sqlite3
import re

# Caminhos dos arquivos
mysql_file = r'C:\Users\valfr\Downloads\controleoficina.sql'
sqlite_file = r'C:\Repositorios_GitHube\MeusProjetos\TWTODOS\db.sqlite3'

# Função para limpar e adaptar o SQL para o SQLite
def adapt_sql_for_sqlite(sql):
    # Remove crases
    sql = sql.replace('`', '')
    # Remove comandos de engine
    sql = re.sub(r'ENGINE=.*?;', '', sql)
    # Remove comandos de charset
    sql = re.sub(r'CHARSET=.*?;', '', sql)
    # Ajusta tipos de dados
    sql = sql.replace('INT(11)', 'INTEGER')
    # Remove comentários e comandos SET
    sql = re.sub(r'--.*?\n', '', sql)
    sql = re.sub(r'SET.*?;', '', sql)
    # Remove comandos de transação que não são suportados pelo SQLite
    sql = re.sub(r'START TRANSACTION;', '', sql)
    sql = re.sub(r'COMMIT;', '', sql)
    sql = re.sub(r'AUTOCOMMIT=.*?;', '', sql)
    # Remove qualquer comando que comece com "/*" ou "*/"
    sql = re.sub(r'/\*.*?\*/', '', sql)
    # Adicione mais ajustes conforme necessário
    return sql

# Ler o arquivo SQL exportado
with open(mysql_file, 'r', encoding='utf-8') as f:
    sql = f.read()

# Adaptar o SQL para o SQLite
sql = adapt_sql_for_sqlite(sql)

# Conectar ao banco de dados SQLite
conn = sqlite3.connect(sqlite_file)
cursor = conn.cursor()

# Executar os comandos SQL
try:
    cursor.executescript(sql)
    print("Dados importados com sucesso!")
except sqlite3.Error as e:
    print(f"Erro ao importar os dados: {e}")

# Fechar a conexão
conn.close()
