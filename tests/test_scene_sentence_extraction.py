from pysamsa.scene_sentence_extraction import get_sentences


def test_get_sentences():
    text = 'You are waiting for a train . A train that will take you far away .'
    expected_sentences = [
        ['You', 'are', 'waiting', 'for', 'a', 'train', '.'],
        ['A', 'train', 'that', 'will', 'take', 'you', 'far', 'away', '.'],
    ]
    sentences = get_sentences(text)
    assert sentences == expected_sentences
