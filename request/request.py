import urllib
import requests
import json
import pandas as pd
import logging

from utils.utils import *

class GSuggest:
    def __init__(self):
        self.base_url = "https://google.com/complete/search?client=chrome&q="

    def get_query_suggestions(self, query):
        utf_query = urllib.parse.quote(query, safe = '')

        r = requests.get("{}{}".format(self.base_url, utf_query))
        google_suggestions = json.loads(r.content)

        if google_suggestions[1]:
            df_dict = {}
            df_dict['seed_keyword'] = query
            df_dict['suggested_queries'] = google_suggestions[1]
            df_dict['suggestion_relevance'] = google_suggestions[4]['google:suggestrelevance']
            df_dict['suggestion_subtypes'] = google_suggestions[4]['google:suggestsubtypes']
            df_dict['suggestion_type'] = google_suggestions[4]['google:suggesttype']
            df = pd.DataFrame(df_dict)

            return df

        else:
            print('Did not return any suggestions for "{}"'.format(query))
            return None

    def get_enhanced_query_suggestions(self, query, filter_out_non_query_kws = True, n_combos = 2, remove_stopwords = False):
        if self.get_query_suggestions(query) is not None:
            seed_kws = self.get_query_suggestions(query)['suggested_queries'].tolist()
            individual_terms = set()
            if remove_stopwords == True:
                for x in seed_kws:
                    split_term_list = stopwords_removal(tokenize(x))
            else:
                for x in seed_kws:
                    split_term_list = tokenize(x)

                    for term in split_term_list:
                        individual_terms.add(term)
            
            additional_suggested_queries = []

            for x in individual_terms:
                request_suggestions = self.get_query_suggestions('{} {}'.format(query, x))
            if request_suggestions is not None:
                additional_suggested_queries.append(request_suggestions)

            if n_combos > 1:
                combos = make_combinations(individual_terms, n_combos)
            for c in combos:
                additional_suggested_queries.append(self.get_query_suggestions('{} {}'.format(query, c)))

            raw_res = pd.concat(additional_suggested_queries).reset_index(drop=True)
            if filter_out_non_query_kws == True:
                return raw_res[raw_res['suggested_queries'].str.contains(query)].reset_index(drop=True)
            else:
                return raw_res