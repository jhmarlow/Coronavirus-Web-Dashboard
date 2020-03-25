import pandas as pd
from datetime import date

# A small API to retrieve JohnHopkins (JH) data on Covid-19
# DataSource: https://github.com/CSSEGISandData/COVID-19
# Written by Jacob Marlow


class JHCovid19TimeseriesData:
    """
    A class to retrieve time-series .csv files from John Hopkins Gitlab project
    """""

    def __init__(self):
        self.url = None

    @staticmethod
    def get_description():
        """
        Provide link to data description
        :param self:
        :return:
        """
        print('For a data description please look at:\n'
              ' https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/README.md')

    def get_timeseries(self, type):
        """
        Confirmed, Deaths, Recovered
        """

        self.url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/' \
                   'csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-{}.csv'.format(type)
        return pd.read_csv(self.url)


class JHCovid19DailyReports:
    """
    A class to retrieve daily reports
    """

    def __init__(self):
        self.url = None
        self.date = None

    @staticmethod
    def get_description():
        """
        Provide link to data description
        :param self:
        :return:
        """
        print('For a data description please look at:\n'
              'https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data')

    def get_dated_report(self, date):
        """
        Get daily report of specified date
        MM-DD-YYYY
        :return:
        """
        self.url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/' \
                   'csse_covid_19_data/csse_covid_19_daily_reports/{}.csv'.format(date)
        return pd.read_csv(self.url)

    def get_todays_report(self):
        self.url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/' \
                   'csse_covid_19_data/csse_covid_19_daily_reports/{}.csv'\
            .format(date.today().strftime("%m-%d-%Y"))

        # if no data available
        try:
            return pd.read_csv(self.url)
        except:
            print('No file currently available for today')


class WHOSituationReports:
    """
    A class to get the twice weekly reports from the World Health Organisation (WHO)
    """

    def __init__(self):
        self.url = None

    @staticmethod
    def get_description():
        """
        Provide link to data description
        :param self:
        :return:
        """
        print('For a data description please look at:\n'
              'https://github.com/CSSEGISandData/COVID-19/tree/master/who_covid_19_situation_reports')

    def get_report(self):
        self.url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/' \
                   'who_covid_19_situation_reports/who_covid_19_sit_rep_time_series/' \
                   'who_covid_19_sit_rep_time_series.csv'
        return pd.read_csv(self.url)

