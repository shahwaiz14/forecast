import pandas as pd

from shroomdk import ShroomDK


def get_asset_price_data(sdk: ShroomDK, asset: str) -> pd.DataFrame:
    assert asset == "weth" or asset == "matic", "Pick either 'weth' or 'matic'"
    sql = f"""
        SELECT hour AS datetime,
            price
        FROM ethereum.core.fact_hourly_token_prices
        WHERE symbol ILIKE '{asset}'
        ORDER BY hour DESC;
        """

    result_set = sdk.query(sql)
    df = pd.DataFrame(result_set.records)
    df["datetime"] = pd.to_datetime(df["datetime"])
    return df
