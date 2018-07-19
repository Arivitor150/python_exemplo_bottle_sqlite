import sqlite3

conn = sqlite3.connect("livros.db")
cursor = conn.cursor()

resultado = cursor.execute("SELECT * FROM livros WHERE generos LIKE '%{}%'".format("Romance"))

linhas = resultado.fetchall()
for linha in linhas:
    print(linha[1])