# === Your task ==============================================================
# Let's have some 'fun'.
# Go to http://en.wikipedia.org/wiki/Garden_path_sentence and have a brief read 
# at what a 'Garden Path sentence' is (at the top) and look at the 'Examples'

# Create the file garden.py for this task.
# 1. Use some Garden Path sentences or think up your own (at least 5).
# 2. Tokenise and perform Entity recognition for each of the sentences 
#    after you have stored them in a list called gardenpathSentences.
# 3. See how spaCy has categorised these sentences and look up the entities you
#    don't understand
# 4. At the bottom of your file, write a comment about two unusual entities 
# you found that spaCy gave one of the words of your sentences - did you expect this?

import spacy #This statement should work if you have spaCy installed 

nlp = spacy.load('en_core_web_sm')

gardenpathSentences = ["The old man the boat.", "The florist sent the flowers was pleased", "The cotton clothing is made of grows in Mississippi", "The girl told the story cried", "Fat people eat accumulates", "That Jill is never here hurts", "Helen is expecting tomorrow to be a bad day"]


for x in gardenpathSentences:
    doc = nlp(x)
    print([token.orth_ for token in doc])

    print([(i, i.label_, i.label) for i in doc.ents])

"""
['Helen', 'is', 'expecting', 'tomorrow', 'to', 'be', 'a', 'bad', 'day']
[(Helen, 'GPE', 384), (tomorrow, 'DATE', 391), (a bad day, 'DATE', 391)]

I expected a person entity for Helen however Helen received a geopolitical entity
I  was amused by the date entity for 'a bad day' as I did not expect it but in hindsight I should have 
"""    