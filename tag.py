from nltk.tokenize import sent_tokenize
from nltk import*
from mini_lexicon import common_keys



common_dict = dict.fromkeys(common_keys, 0)

print(common_dict)
print(len(common_dict))