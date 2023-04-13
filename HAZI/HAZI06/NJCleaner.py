import pandas as pd
from datetime import datetime


class NJCleaner:

    def __init__(self, path: str):

        self.data = pd.read_csv(path)

    def order_by_scheduled_time(self) -> pd.DataFrame:
        '''df = self.data

        df['scheduled_time'] = pd.to_datetime(
            df['scheduled_time'], format='%Y-%m-%d %H:%M:%S')

        df.sort_values(by='scheduled_time', inplace=True, ascending=True)
        return df'''
        df = self.data.sort_values(by='scheduled_time')
        return df

    def drop_columns_and_nan(self) -> pd.DataFrame:

        df = self.order_by_scheduled_time()

        df = df.dropna(how='any')

        df = df.drop(columns=['from', 'to'])

        return df

    def convert_date_to_day(self) -> pd.DataFrame:
        df = self.drop_columns_and_nan()

        df['day'] = pd.to_datetime(df['date']).dt.day_name()

        df = df.drop(columns=['date'])
        return df

    def convert_scheduled_time_to_part_of_the_day(self) -> pd.DataFrame:

        df = self.convert_date_to_day()

        # bins_list = [datetime.strptime(date, "%H:%M:%S").time() for date in ['00:00:00', '04:00:00', '08:00:00',  '12:00:00',  '16:00:00',  '20:00:00',  '23:59:59']]

        bins_list = [0, 4-1, 8-1, 12-1, 16-1, 20-1, 24-1]

        df['part_of_the_day'] = pd.cut(pd.to_datetime(df['scheduled_time']).dt.hour, bins=bins_list, labels=[


                                       'late_night', 'early_morning', 'morning', 'afternoon', 'evening', 'night',])

        return df

    '''4:00-7:59 -- early_morning


   8:00-11:59 -- morning  


   12:00-15:59 -- afternoon  


   16:00-19:59 -- evening  


   20:00-23:59 -- night  


   0:00-3:59 -- late_night '''

    def convert_delay(self) -> pd.DataFrame:

        df = self.convert_scheduled_time_to_part_of_the_day()

        df['delay'] = pd.cut(df['delay_minutes'],


                             bins=[-1, 4.99999, float('inf')], labels=[0, 1])

        return df


# - Dobd el a felesleges oszlopokat 'train_id' 'scheduled_time' 'actual_time' 'delay_minutes'. A függvény neve legyen 'drop_unnecessary_columns' és térjen vissza a df-el

    def drop_unnecessary_columns(self) -> pd.DataFrame:

        df = self.convert_delay()

        df = df.drop(columns=['train_id', 'scheduled_time',


                              'actual_time', 'delay_minutes'])
        return df

    def save_first_60k(self, path):

        df = self.drop_unnecessary_columns()

        df.head(60000).to_csv(path, index=False)

    def prep_df(self, path='data/NJ.csv'):

        self.data = self.order_by_scheduled_time()
        self.data = self.drop_columns_and_nan()

        self.data = self.convert_date_to_day()

        self.data = self.convert_scheduled_time_to_part_of_the_day()

        self.data = self.convert_delay()

        self.data = self.drop_unnecessary_columns()

        self.save_first_60k(path)
