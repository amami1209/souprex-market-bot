from __future__ import annotations
from dataclasses import dataclass
from typing import List
import random
import time


@dataclass
class YahooItem:
    title: str
    price: int
    url: str


def fetch_yahoo_items(keyword: str, limit: int = 30) -> List[YahooItem]:
    """
    TODO: ここをSouprexのヤフオク取得ロジックに置き換える。
    今はデモ用ダミーデータを返す。
    """
    time.sleep(1)  # それっぽい待ち
    items: List[YahooItem] = []
    base = random.randint(12000, 42000)
    for i in range(limit):
        price = max(1000, int(random.gauss(base, base * 0.08)))
        items.append(
            YahooItem(
                title=f"{keyword} サンプル商品 {i+1}",
                price=price,
                url="https://auctions.yahoo.co.jp/"
            )
        )
    return items
