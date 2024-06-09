from dataclasses import dataclass

import pytest


# TODO: implement marks dataclass with pytest.MarkDecorator attributes.
#  Example implementation below. The `marks` function is used as an
#  entry point for the plugin in the pyproject.toml.

# @dataclass(frozen=True)
# class PandasMarks:
#     parquet: pytest.MarkDecorator
#     json: pytest.MarkDecorator
#     csv: pytest.MarkDecorator
#
#
# def marks() -> PandasMarks:
#     return PandasMarks(
#         parquet=pytest.mark.record("pandas_parquet"),
#         json=pytest.mark.record("pandas_json"),
#         csv=pytest.mark.record("pandas_csv"),
#     )
