import aiohttp
from typing import Sequence
from dataclasses import dataclass


@dataclass
class data:
    chat_id: int
    text: str


async def sendMessage(token:str, data: Sequence[data]):
    async with aiohttp.ClientSession() as session:
        async with session.post(f"https://api.telegram.org/bot{token}/sendMessage", data=data) as response:
            print(response.status)