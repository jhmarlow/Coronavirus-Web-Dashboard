""" Wrangle Data

Use this file to read in your data and prepare the plotly visualizations. The path to the data files are in
`data/file_name.csv`
"""
from .data_retrievers import *


class CaseTotals:
    """Latest total values for each type"""
    def __init__(self):
        pass

    @staticmethod
    def total_confirmed():
        """Get sum of latest total confirmed

        Returns:
            [type]: [description]
        """
        return JHCovid19TimeseriesData().get_timeseries('Confirmed').iloc[:, [-1]].sum()

    @staticmethod
    def total_recovered():
        """Get sum of latest total recovered

        Returns:
            [type]: [description]
        """
        return JHCovid19TimeseriesData().get_timeseries('Recovered').iloc[:, [-1]].sum()

    @staticmethod
    def total_deaths():
        """Get sum of latest total deaths

        Returns:
            [type]: [description]
        """
        return JHCovid19TimeseriesData().get_timeseries('Deaths').iloc[:, [-1]].sum()

    def totals_values(self):
        """Format results in to list to be plotted

        Returns:
            [type]: [description]
        """
        return [self.total_confirmed().values[0], self.total_recovered().values[0], self.total_deaths().values[0]]

    @staticmethod
    def totals_names():
        """Format results in to list to be plotted.

        Returns:
            [type]: [description]
        """
        return ['Confirmed', 'Recovered', 'Deaths']


# Second chart data wrangling
class CasesByCountry:
    """Latest total count of each type by country"""

    def __init__(self):
        pass

    @staticmethod
    def countries_confirmed():
        """
        Latest confirmed cases by country
        """
        df = JHCovid19TimeseriesData().get_timeseries('Confirmed')
        df = df.groupby('Country/Region').sum()
        return df.iloc[:, [-1]].sort_values(by=df.columns[-1], ascending=False)

    @staticmethod
    def countries_recovered():
        """
        Latest recovered cases by country
        """
        df = JHCovid19TimeseriesData().get_timeseries('Recovered')
        df = df.groupby('Country/Region').sum()
        return df.iloc[:, [-1]].sort_values(by=df.columns[-1], ascending=False)

    @staticmethod
    def countries_deaths():
        """
        Latest deaths cases by country
        """
        df = JHCovid19TimeseriesData().get_timeseries('Deaths')
        df = df.groupby('Country/Region').sum()
        return df.iloc[:, [-1]].sort_values(by=df.columns[-1], ascending=False)


# Third chart data wrangling
class TimeSeriesByType:
    """
    Time series of case types
    """
    def __init__(self):
        pass

    @staticmethod
    def total_time_series_cases():
        return JHCovid19TimeseriesData().get_timeseries('Confirmed').sum(axis=0)[3:]

    @staticmethod
    def total_time_series_recovered():
        return JHCovid19TimeseriesData().get_timeseries('Recovered').sum(axis=0)[3:]

    @staticmethod
    def total_time_series_deaths():
        return JHCovid19TimeseriesData().get_timeseries('Deaths').sum(axis=0)[3:]


# Fourth chart data wrangling
def countries_confirmed_time_series():
    df = JHCovid19TimeseriesData().get_timeseries('Confirmed')
    df = df.groupby('Country/Region').sum()
    return df.iloc[:, 3:].sort_values(by=df.columns[-1], ascending=False)


# Fifth chart data wrangling
class GeoPlotData:
    """
    Class to get data for map bubble plot
    """
    def __init__(self):
        pass

    @staticmethod
    def geo_plot_confirmed():
        df = JHCovid19TimeseriesData().get_timeseries('Confirmed')
        df['Province/State'] = df['Province/State'].fillna("")
        df['Country/Region'] = df['Province/State'] + " " + df['Country/Region']
        return df.iloc[:, [1, 2, 3, -1]]

    @staticmethod
    def geo_plot_recovered():
        df = JHCovid19TimeseriesData().get_timeseries('Recovered')
        df['Province/State'] = df['Province/State'].fillna("")
        df['Country/Region'] = df['Province/State'] + " " + df['Country/Region']
        return df.iloc[:, [1, 2, 3, -1]]

    @staticmethod
    def geo_plot_deaths():
        df = JHCovid19TimeseriesData().get_timeseries('Deaths')
        df['Province/State'] = df['Province/State'].fillna("")
        df['Country/Region'] = df['Province/State'] + " " + df['Country/Region']
        return df.iloc[:, [1, 2, 3, -1]]


def return_latest_dataset_date():
    """Get the latest date in the .csv file, time-series left to right."""
    return JHCovid19TimeseriesData().get_timeseries('Confirmed').columns[-1]
