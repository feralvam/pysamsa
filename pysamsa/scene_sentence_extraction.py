import nltk


def get_scenes(ucca_passage):
    ''' Return all the scenes in the given ucca_passage
    '''
    ucca_scenes = [x for x in ucca_passage.layer('1').all if x.tag == "FN" and x.is_scene()]
    text_scenes = []
    for scene in ucca_scenes:
        words = []
        previous_word = ''
        for terminal in scene.get_terminals(False, True):
            word = terminal.text
            if word == previous_word:
                # TODO: Iterating this way on the scene sometimes yields duplicates.
                continue
            words.append(word)
            previous_word = word
        text_scenes.append(words)
    return text_scenes


def get_sentences(text):
    '''Splits the input text into its sentences and each output sentence to words.'''
    word_tokenizer = nltk.tokenize.WordPunctTokenizer()
    sentence_tokenizer = nltk.data.load(f'tokenizers/punkt/english.pickle')
    return [word_tokenizer.tokenize(sentence)
            for sentence in sentence_tokenizer.tokenize(text)]
