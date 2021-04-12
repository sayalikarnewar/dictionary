import aiohttp_jinja2
import requests

@aiohttp_jinja2.template('main.html')
async def get_word(request):
    return {}

@aiohttp_jinja2.template('main.html')
async def search(request):
    form = await request.post()
    word = str(form['word'])

    try:
        response_API = requests.get('https://api.dictionaryapi.dev/api/v2/entries/en_US/'+word)
    except Exception:
        return {'response': 'Can not call dictionaryapi'}
    
    try:
        #get partOfSpeech from json file
        partOfSpeech = response_API.json()[0]['meanings'][1]['partOfSpeech']
            
        #get definition from json file
        definition = response_API.json()[0]['meanings'][1]['definitions'][0]['definition']
            
        #print the output
        return {'result' : [{'word': word, 'partOfSpeech':partOfSpeech,'definition':definition}]}
            
    except Exception as e:
        return {'response' : str(e)}
