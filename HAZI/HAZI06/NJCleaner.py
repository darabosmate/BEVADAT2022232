import pandas as pd
import datetime

class NJCleaner:

    def __init__(self, path: str):
        self.data = pd.read_csv(path)

    def order_by_scheduled_time(self) -> pd.DataFrame():
        df = self.data.copy()
        df.sort_values(by=['scheduled_time'])
        return df

    def drop_columns_and_nan(self) -> pd.DataFrame():
        df = self.order_by_scheduled_time()
        df = df.dropna(how='any')
        df = df.drop(columns=['from', 'to'])

        return df

    def convert_date_to_day(self) -> pd.DataFrame():
        df = self.drop_columns_and_nan()
        df['day'] = df['date'].datetime.weekday()
        return df


