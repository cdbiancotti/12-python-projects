import nltk
import requests
import json
import string

try:
    response = requests.get('https://shortstories-api.herokuapp.com/')
    response.raise_for_status()
    data_dict = json.loads(response.text)
    text = data_dict.get('story', '')
    text = nltk.word_tokenize(text)
    result = nltk.pos_tag(text)
    list_index = [i if t[1] == 'VB' else None for i, t in enumerate(result)]
    list_index = list(filter(lambda x: x != None, list_index))

    for i, pos in enumerate(list_index):
        new_vb = ''
        while not new_vb:
            new_vb = input(
                'Insert new verb for position {}: '.format(i+1)).strip()
        text.pop(pos)
        text.insert(pos, new_vb)
    print('\n\n')
    print(data_dict.get('title'), end='\n\n')
    print(' '.join(text).replace(' .', '.').replace(
        ' ,', ',').replace(' !', '!').replace(' ?', '?'), end='\n\n')
    print(f"A story created by {data_dict.get('author')} and edited for YOU!!")
except Exception as e:
    print('Sorry Bro...')
