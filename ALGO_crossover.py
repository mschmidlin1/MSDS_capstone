import pandas as pd


def bars_df_filter_dates(df, monitor):
    "Filters a bars dataframe based on which days the market was actually open."

    return df[df['timestamp'].apply(lambda x: monitor.trading_date(x.date()))].copy()


def add_sma_columns(df: pd.DataFrame, fsma_period: int, ssma_period: int, agg_col='close'):
    """Adds simple moving average (sma) columns to a bars dataframe. 
    
    `fsma_period` - The fast sma period. This will be in count of rows.
    `ssma_period` - The slow sma period. This will be in count of rows. 
    `agg_col` - The df column to perform the sma on. Default is to use the close price from the bars dataframe.

    Since the periods are passed in terms of number of rows the denomination will be in terms of `time_resolution` which is passed to `.get_bars()` when acquiring the bars dataframe.

    Returns DataFrame with the two added columns. The names of the two added columns are `slow_sma` and `fast_sma`.
    """
    df['slow_sma'] = df[agg_col].rolling(ssma_period).mean()
    df['fast_sma'] = df[agg_col].rolling(fsma_period).mean()

    return df

def add_sma_crossovers(df: pd.DataFrame, fsma_col: str, ssma_col: str):
    """Adds 3 columns to a bars dataframe:
    `prev_fsma` - This column is mostly for internal calculations of the bullish and bearish crossovers.
    `bullish_crossover` - This column is true wherever there is a bullish crossover. This is a buying opportunity.
    `bearish_crossover` - This columnd is true wherever there is a bearish crossover. This is a selling opportunity.

    Returns the dataframe with the 3 columns added.
    """

    df['prev_fsma'] = df[fsma_col].shift(1)
    df['bullish_crossover'] = (df[fsma_col] > df[ssma_col]) & (df['prev_fsma'] < df[ssma_col])
    df['bearish_crossover'] = (df[fsma_col] < df[ssma_col]) & (df['prev_fsma'] > df[ssma_col])
    return df