<h1>gsuggest: Simple API Calls to Google Suggestions API</h1>
<p>The point of this library is to assist users in initial keyword research using Google's free Suggestions API. The library returns a Pandas DataFrame that can be exported to any number of formats by the user.</p>
<h2>Install</h2>
<h3>Install the gsuggest library or pull from the Github repo</h3>
<p>To install using pip package manager from PyPI (Recommended, but not working yet, will fix soon):</p>
<pre><code>pip install gsuggest</pre></code>
<p>To install package via Git:</p>
<pre><code>pip install git+https://github.com/thomashopkins96/gsuggest.git</pre></code>
<h2>Basic Usage</h2>
<pre><code>import gsuggest
gsuggest = GSuggest()
suggestions_df = gsuggest.get_query_suggestions("YOUR QUERY")
</pre></code>
<p>The output of the function returns as a Pandas dataframe and can be exported using that Pandas library</p>
<pre><code>suggestions_df.to_csv("suggestions_data_pull.csv")</pre></code>

<strong><p>Documentation still in progress...</strong></p>
