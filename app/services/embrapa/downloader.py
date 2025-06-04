import requests
import polars as pl

from app.services.embrapa.site import data_sources
from app.db.model import vitivinicultura


def download_all() -> list[str]:
    """Download all data from the Embrapa Wine site and store it in the database."""

    vitivinicultura.create_tables()

    statuses: list[dict] = []

    for source in data_sources:
        print(f"Getting data from {source['source']}")
        payload = requests.get(source["url"])
        q = pl.scan_csv(
            payload.content,
            separator=source["delimiter"],
            ignore_errors=True,
            null_values=["nd", "*"],
            has_header=source["has_header"],
            schema=source["schema"],
        )
        df = q.collect()
        df = df.with_columns(pl.lit(source["tag"]).alias("tag")).drop("id")

        table: str = f"vitivinicultura.{source["target"]}"
        df.write_database(
            table_name=table,
            engine="adbc",
            if_table_exists="append",
            connection="postgresql://dba:F3rr4r1!2025@fiap-pb-db.postgres.database.azure.com:5432/embrapa_wine",
        )
        status = {
            "source": source["source"],
            "target": source["target"],
            "tag": source["tag"],
            "table": table,
            "rows": len(df),
        }

        statuses.append(status)
    return statuses

