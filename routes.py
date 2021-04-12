from script import get_word, search

def routes(app):
    app.router.add_get('/', get_word)
    app.router.add_post('/', search, name='search')
