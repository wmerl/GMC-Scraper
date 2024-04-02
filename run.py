from loader import load_data

if __name__ == '__main__':
    from_id: int = 1
    to_id: int = 1_000_000

    load_data(from_id, to_id)

    print('Done!')
#
# The code above is the entry point of the program. It imports the load_data function from loader.py and runs it with the specified range of IDs. The function will save the HTML files in the data folder.
#
# The load_data function generates a list of lists of IDs, fetches the data for each ID, and saves the HTML files. It uses asyncio to make multiple requests concurrently and aiohttp to make HTTP requests. The function also handles rate limiting by rotating through a list of cookies and sleeping for 10 or 30 seconds between requests.
#
# The get_valid_cookies function generates a list of valid cookies by opening a headless browser, visiting a URL, and extracting the cookies. It uses undetected_chromedriver to prevent detection by websites.
#
# The fetch function makes an HTTP request to a URL with the specified headers and returns the response text and user ID. It handles different HTTP status codes and rate limiting.
#
# The program uses asyncio.run to run the get_users_data function asynchronously and fetch data for multiple IDs concurrently. It saves the HTML files in the data folder and prints the file names as they are saved.
#
# The program sleeps for 10 or 30 seconds between requests to avoid rate limiting and rotates through a list of cookies to prevent getting blocked.
#
# The program is designed to be efficient and handle rate limiting while fetching data for a large number of IDs. It uses asyncio and aiohttp to make asynchronous requests and save the data concurrently.
#
# The program can be run from the command line with python run.py to start fetching data for the specified range of IDs. It will save the HTML files in the data folder and print Done! when it finishes.
#
# The program can be modified to handle different ranges of IDs, increase the number of cookies, or change the sleep times between requests. It can also be extended to handle other types of data or processing tasks.
#
# Overall, the program is a robust and efficient solution for fetching data for a large number of IDs while handling rate limiting and other challenges. It demonstrates the use of asyncio, aiohttp, and undetected_chromedriver to build a scalable and reliable web scraping solution.
#
#
#
# Happy Extraction!