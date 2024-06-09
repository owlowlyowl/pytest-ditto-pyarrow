import pandas as pd
import pyarrow as pa



def test_table_parquet() -> None:
    df = pd.DataFrame(
        {
            'one': [-1, np.nan, 2.5],
            'two': ['foo', 'bar', 'baz'],
            'three': [True, False, True],
        },
        index=list('abc'),
    )

    table = pa.Table.from_pandas(df)
