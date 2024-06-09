from pathlib import Path
from typing import ClassVar

import pyarrow as pa
import pyarrow.parquet as pq
from pyarrow import orc, csv


class PyArrowParquet:
    extension: ClassVar[str] = "pyarrow.parquet"

    @staticmethod
    def save(data: pa.Table, filepath: Path) -> None:
        pq.write_table(data, filepath)

    @staticmethod
    def load(filepath: Path) -> pa.Table:
        return pq.read_table(filepath)


class PyArrowORC:
    extension: ClassVar[str] = "pyarrow.orc"

    @staticmethod
    def save(data: pa.Table, filepath: Path) -> None:
        orc.write_table(data, filepath)

    @staticmethod
    def load(filepath: Path) -> pa.Table:
        return orc.read_table(filepath)


class PyArrowCSV:
    extension: ClassVar[str] = "pyarrow.csv"

    @staticmethod
    def save(data: pa.Table, filepath: Path) -> None:
        csv.write_csv(data, filepath)

    @staticmethod
    def load(filepath: Path) -> pa.Table:
        return csv.read_csv(filepath)

