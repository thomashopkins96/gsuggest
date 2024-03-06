import urllib
import requests
import json
import pandas as pd

from utils.utils import *

class GSuggest:
    def __init__(self, query):
        self.base_url = "https://google.com/complete/search?client=chrome&q="
        self.query = query

    def get_query_suggestions(self):
        utf_query = urllib.parse.quote(self.query, safe = '')

        r = requests.get("{}{}".format(self.base_url, utf_query))
        google_suggestions = json.loads(r.content)

        if google_suggestions[1]:
            df_dict = {}
            df_dict['seed_keyword'] = self.query
            df_dict['suggested_queries'] = google_suggestions[1]
            df_dict['suggestion_relevance'] = google_suggestions[4]['google:suggestrelevance']
            df_dict['suggestion_subtypes'] = google_suggestions[4]['google:suggestsubtypes']
            df_dict['suggestion_type'] = google_suggestions[4]['google:suggesttype']
            df = pd.DataFrame(df_dict)

            return df

        else:
            print('Did not return any suggestions for "{}"'.format(self.query))

    def enhanced_query_suggestions(self, filter_out_non_query_kws = True, n_word_combinations = 2):
        if GSuggest.get_query_suggestions(self.query) is not None:
            seed_kws = GSuggest.get_query_suggestions(self.query)['suggested_queries'].tolist()

            individual_terms = set()

            for x in seed_kws:
                split_term_list = remove_stopwords(x)
            for term in split_term_list:
                if term not in self.query:
                    individual_terms.add(term)

            additional_suggested_queries = []

            for x in individual_terms:
                request_suggestions = GSuggest.get_query_suggestions('{} {}'.format(self.query, x))
            if request_suggestions is not None:
                additional_suggested_queries.append(request_suggestions)

            if n_word_combinations > 1:
                combos = make_combinations(individual_terms, n_word_combinations)
            for c in combos:
                additional_suggested_queries.append(GSuggest.get_query_suggestions('{} {}'.format(self.query, c)))

            raw_res = pd.concat(additional_suggested_queries).reset_index(drop=True)
            if filter_out_non_query_kws == True:
                return raw_res[raw_res['suggested_queries'].str.contains(self.query)].reset_index(drop=True)
            else:
                return raw_res