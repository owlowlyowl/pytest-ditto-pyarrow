from pathlib import Path
from typing import ClassVar


# TODO: rename class.
class _NEW_IO_CLASS:
    # Extension should have plugin suffix as prefix, e.g, `pytest-ditto-pandas`
    # has the extenstion "pandas.{io_type}" where `io_type` is something like
    # pickle, csv, parquet, json, etc. So, for json it would be 'pandas.json'.
    # TODO: assign extension type
    extension: ClassVar[str] = ""

    @staticmethod
    def save(data: pd.DataFrame, filepath: Path) -> None:
        # TODO: implement save
        raise NotImplementedError()

    @staticmethod
    def load(filepath: Path) -> pd.DataFrame:
        # TODO: implement load
        raise NotImplementedError()
