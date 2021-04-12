from script import get_word, search

def routes(app):
    app.router.add_get('https://sayalikarnewar.github.io/dictionary/', get_word)
    app.router.add_post('https://sayalikarnewar.github.io/dictionary/', search, name='search')
