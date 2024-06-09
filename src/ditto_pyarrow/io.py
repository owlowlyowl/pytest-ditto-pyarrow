from pathlib import Path
from typing import ClassVar

import pyarrow as pa
import pyarrow.parquet as pq


class ArrowTableParquet:
    extension: ClassVar[str] = "arrow.table.parquet"

    @staticmethod
    def save(data: pa.Table, filepath: Path) -> None:
        pq.write_table(data, filepath)

    @staticmethod
    def load(filepath: Path) -> pa.Table:
        pq.read_table(filepath)
