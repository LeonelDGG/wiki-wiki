import wikipedia

language = 'en'

def setLanguage():
    print('Languages availables: ')
    languages = wikipedia.languages()
    for lang in languages:
        print(f'{lang} : {languages[lang]}')

    selected_lang = input('(*) Option (default = en): ')
    if(selected_lang):
        global language
        language = selected_lang


def search(query):
    wikipedia.set_lang(language)
    ans = wikipedia.summary('software').split('.')
    for line in ans:
        print(line)



if __name__ == "__main__":
    
    q = input('(*) Search: ')
    
    setLanguage()
    
    search(q)