import livros_dao as dao
#opcoes_pergunta1 = ["opcao 1", "opcao 2", "opcao 3"]

def recomenda_livro(perguntas):
    pergunta_1 = int(perguntas["perg1"])-1
    return dao.livro_com_caracteristicas(500,"Romance","Dificil")
    