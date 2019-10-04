# Testing approach
For this document to be complete, please gather better (if any) requirements from business unit.

## Functionalities to test:
1. Search by providing text by physical keyboard
2. Search by providing text via site keyboard
3. Search by voice
4. (only for logged in user) check latest searches
5. Check search button (for functionality 2)
6. Check "I'm feeling lucky" button (for functionality 1)
![Testing approach for google.com search engine](https://github.com/misiekofski/selenpy/blob/master/approach/test-approach.png)


## User / anonymous user notes:
1. There might be different results for logged in user and for anonymous user)
2. Some functionalities are only available for logged in users


## Test data
1. Combine functionalities with different test data:
   * empty string
   * some popular string (which shows lot of results)
   * some unpopular string (which shows only few results)
   * some examples you can find in [google_search.feature](https://github.com/misiekofski/selenpy/blob/master/features/google_search.feature)
2. Use different charsets (specific to different languages)
3. Try to overflow query (find maximum text length that is working with search field)

## Security and privacy
1. As input search text is provided by user check:
   * SQL Injections
   * XSS
   * Try to modify HTTP requests (via Burp Suite for example) to check if validation is also implemented on the backend
   * Check if https is in use
2. Check if latest searches disappear when user deletes private data (search history)
3. Check if anonymous user is not tracked by cookies (after some anonymous search session check if google suggest "latest searches")