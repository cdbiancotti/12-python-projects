import nltk

text = 'This is a table. We should table this offer. The table is in the center.'
text = nltk.word_tokenize(text)
result = nltk.pos_tag(text)
list_index = [i if t[1].startswith(
    'VB') else None for i, t in enumerate(result)]
list_index = list(filter(lambda x: x != None, list_index))

for i, pos in enumerate(list_index):
    new_vb = ''
    while not new_vb:
        new_vb = input(
            'Insert new verb for position {}: '.format(i+1)).strip()
    text.pop(pos)
    text.insert(pos, new_vb)

print(' '.join(text).replace(' .', '.'))
