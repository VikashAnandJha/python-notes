from googlesearch import search

query = "goldratetoday.shop"  # Replace with your search query
website = "goldratetoday.shop"
# Perform the search and retrieve the URLs of the search results
# num is the number of results, stop is the total results to retrieve
search_results = search(query, num_results=50, advanced=True)

# Print the URLs of the search results
i = 0
for result in search_results:
    i += 1
    print(i, result.title, result.url)
    if (website in result.url):
        print("====== found =======")
        break
