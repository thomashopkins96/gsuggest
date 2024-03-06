import nltk
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from itertools import combinations

def make_combinations(term_list, combo_length):
  unique_combinations = list(combinations(term_list, combo_length))
  unique_string_suffixes = []
  for tup in unique_combinations:
    unique_string_suffixes.append(' '.join(map(str, tup)))

  return unique_string_suffixes

def tokenize(word):
  word_tokens = word_tokenize(word)

  return word_tokens

def stopwords_removal(word_tokens, stopwords = stopwords.words('english')):
  filtered_word = [w for w in word_tokens if not w.lower() in stopwords]

  return filtered_word