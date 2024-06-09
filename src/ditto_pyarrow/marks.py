from dataclasses import dataclass

import pytest


@dataclass(frozen=True)
class PyArrowMarks:
    parquet: pytest.MarkDecorator


def marks() -> PyArrowMarks:
    return PandasMarks(
        parquet=pytest.mark.record("pyarrow_parquet"),
    )

