import sqlite3

def abre_bd():
    conn = sqlite3.connect("livros.db")
    return conn.cursor()

def livro_com_caracteristicas(paginas,genero,tipo_leitura):
    query_string = " SELECT * FROM livros WHERE generos LIKE '%{}%' AND paginas <= {} AND tipo_leitura LIKE '{}';".format(genero, paginas,tipo_leitura)
    cursor = abre_bd()
    resultado = cursor.execute(query_string)
    livro = convert_db_para_dict(resultado.fetchone())
    return livro
    

def convert_db_para_dict(linha):
    return {'id':linha[0],'nome':linha[1], 'sinopse': linha[2]}    