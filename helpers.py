import time
import aiohttp
import asyncio
import undetected_chromedriver as uc

from asyncio import Task
from typing import Any
from undetected_chromedriver import ChromeOptions, Chrome


def get_valid_cookies(cookies_number: int = 10) -> list[str]:
    valid_cookies: list[str] = []

    for _ in range(cookies_number):
        chrome_options: ChromeOptions = uc.ChromeOptions()
        chrome_options.add_argument("--no-sandbox")

        driver: Chrome = Chrome(options=chrome_options)
        del chrome_options

        gmc_url: str = 'https://www.gmc-uk.org/doctors/19343'

        driver.get(gmc_url)
        time.sleep(2)
        driver.refresh()
        time.sleep(1)

        cookies: list[dict] = driver.get_cookies()
        cookie_header: str = "; ".join([f"{cookie['name']}={cookie['value']}" for cookie in cookies])
        del cookies

        print(cookie_header)

        valid_cookies.append(cookie_header)
        del cookie_header

        driver.delete_all_cookies()
        driver.close()
        del driver

    return valid_cookies


async def fetch(s: aiohttp.ClientSession, headers: dict[str: str], use_id: str | int) -> tuple[str, str] | None:
    url: str = f'https://www.gmc-uk.org/doctors/{use_id}'

    async with s.get(url, headers=headers) as r:

        if r.status == 429:
            print('Too Many Requests')
            return None

        if r.status == 404:
            return None

        if r.status == 403:
            r.raise_for_status()

        return await r.text(), str(use_id)


async def fetch_all(s: aiohttp.ClientSession, headers: dict[str: str], subarray: list[int]) -> tuple[Any]:
    tasks: list[Task[dict]] = []
    for use_id in subarray:
        task: Task = asyncio.create_task(fetch(s, headers, use_id))
        tasks.append(task)
        del task, use_id

    del subarray
    res: tuple[Any] = await asyncio.gather(*tasks)
    return res


async def get_users_data(headers: dict[str: str], subarray: list[int]) -> tuple[Any]:
    async with aiohttp.ClientSession() as session:
        json_data: tuple[Any] = await fetch_all(session, headers, subarray)
        return json_data
