import asyncio
import os
import time

from helpers import get_valid_cookies, get_users_data

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
    }


def load_data(from_id: int = 1, to_id: int = 1_000_000) -> None:

    # Get valid cookies (10 by default)
    cookies_list: list[str] = get_valid_cookies()

    array_of_arrays: list[list[int]] = []

    # Generate a list of 1000 lists of 100 integers
    for i in range(from_id, to_id, 100):
        sub_array: list[int] = list(range(i, i + 101))
        array_of_arrays.append(sub_array)
        del sub_array

    # Initialize variables
    rot = users_saved = co = 0
    folder_name: str = 'data'
    os.makedirs(folder_name, exist_ok=True)

    # Start the timer
    start_time: float = time.time()

    # Loop through the list of lists
    for ids in array_of_arrays:
        print('Current Header', co + 1, '/', len(cookies_list))
        headers['Cookie'] = cookies_list[co]

        data = asyncio.run(get_users_data(headers, ids))
        del ids

        for item in data:
            if item:
                text: str = item[0]
                user_id: str = item[1]
                del item

                file_name: str = f'{user_id}.html'
                with open(f'{folder_name}/{file_name}', 'w', encoding='utf-8') as file:
                    file.write(text)
                    del text

                    users_saved += 1
                print(f" -> '{file_name}'")
        del data

        if co == len(cookies_list) - 1:
            co = 0
            sec = 30
            rot += 1

        else:
            co += 1
            sec = 10

        # Sleep for 10 | 30 seconds
        print(f'Sleeping for {sec} seconds...')
        time.sleep(sec)

        if rot == 2:
            rot = 0
            end_time: float = time.time()
            print('Time:', f'{(end_time - start_time):.2f}')
            del end_time, start_time

            print('Saved Persons:', users_saved)
            print('Getting Fresh Cookies ..')

            cookies_start: float = time.time()
            cookies_list = get_valid_cookies()
            cookies_end = time.time()
            print('Cookies Time:', f'{(cookies_end - cookies_start):.2f}')
            del cookies_start, cookies_end

            start_time: float = time.time()





