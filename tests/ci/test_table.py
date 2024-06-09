import pyarrow as pa
import ditto
import pytest


def make_table() -> pa.Table:
    return pa.table(
        [
            [1, 2, 3],
            [4.0, 5.0, 6.0],
            [7, 8.0, None],
            [True, False, True],
            ["a", "b", "c"],
        ],
        names=[
            "ints",
            "floats",
            "floats_with_none",
            "bools",
            "strings",
        ]
    )


@ditto.pyarrow.parquet
def test_table_parquet(snapshot) -> None:
    table = make_table()
    result = snapshot(table, "table")
    assert table.equals(result)


@ditto.pyarrow.orc
def test_table_orc(snapshot) -> None:
    table = make_table()
    result = snapshot(table, "table")
    assert table.equals(result)


@ditto.pyarrow.csv
def test_table_csv(snapshot) -> None:
    table = make_table()
    result = snapshot(table, "table")
    assert table.equals(result)

