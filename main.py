#  This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#     Author: Gareis, Leonel

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