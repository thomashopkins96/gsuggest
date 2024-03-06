import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from itertools import combinations

def make_combinations(term_list, combo_length):
  unique_combinations = list(combinations(term_list, combo_length))
  unique_string_suffixes = []
  for tup in unique_combinations:
    unique_string_suffixes.append(' '.join(map(str, tup)))

  return unique_string_suffixes

def remove_stopwords(query, stopwords = stopwords.words('english')):
  word_tokens = word_tokenize(query)
  filtered_word = [w for w in word_tokens if not w.lower() in stopwords]

  return filtered_word