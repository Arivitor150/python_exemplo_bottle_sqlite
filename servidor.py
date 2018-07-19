from bottle import route, run, template, request
import recomendador

@route('/recomenda')
def recomenda():
    livro = recomendador.recomenda_livro(request.query) 
    return template('views/recomenda.html', livro=livro)
    

@route('/')
def index():
    return template('views/index.html')

run(host='localhost', port=80)