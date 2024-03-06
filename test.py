from request.request import GSuggest
import pandas as pd
import os

def basic_test(query):
    gsuggest = GSuggest()
    gsuggest_results = gsuggest.get_query_suggestions(query)
    gsuggest_enhanced = gsuggest.get_enhanced_query_suggestions(query)

    basic_gsuggest_results = 'basic_gsuggest_output.csv'
    enhanced_gsuggest_results = 'enhanced_gsuggest_output.csv'

    if os.path.exists(basic_gsuggest_results) or os.path.exists(enhanced_gsuggest_results):
        os.remove(basic_gsuggest_results)
        os.remove(enhanced_gsuggest_results)

    gsuggest_results.to_csv(basic_gsuggest_results)
    gsuggest_enhanced.to_csv(enhanced_gsuggest_results)


if __name__ == '__main__':
    query = 'INSERT YOUR QUERY HERE'
    basic_test(query)
