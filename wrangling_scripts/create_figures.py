import pandas as pd
import numpy as np
import plotly.graph_objs as go
from wrangling_scripts.wrangle_data import *

# Use this file to read in your data and prepare the plotly visualizations. The path to the data files are in
# `data/file_name.csv`

# Parameters for plot
opacity_val = 0.8
marker_line_color_val = 'rgb(8,48,107)'
marker_line_width_val = 1.2


def return_figures():
    """Creates five plotly visualizations.
    Create go data and layout append them in list and
    then add to figure at bottom of function.

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations

    """

    # First plot of total cases
    graph_one = [go.Bar(
        x=CaseTotals().totals_names(),
        y=CaseTotals().totals_values(),
        marker_color=['orange', 'green', 'crimson'],
        width=0.5,
        opacity=opacity_val,
        marker_line_color=marker_line_color_val,
        marker_line_width=marker_line_width_val)]

    # Set layout
    layout_one = dict(title='Total Cases Count',
                      yaxis=dict(title='Case Count'),
                      font=dict(
                          size=9,
                          color="#7f7f7f"),
                      )

    # Second plot
    # Top 30 countries
    graph_two = []
    range_start = 0
    range_end = 30
    graph_two.append(
        go.Bar(
            x=CasesByCountry().countries_confirmed().index[range_start:range_end],
            y=CasesByCountry().countries_confirmed().values[range_start:range_end, 0],
            marker_color='orange',
            name='Cases',
            opacity=opacity_val,
            marker_line_color=marker_line_color_val,
            marker_line_width=marker_line_width_val))

    countries_to_plot = CasesByCountry().countries_confirmed().index[range_start:range_end]

    graph_two.append(
        go.Bar(
            x=CasesByCountry().countries_recovered().loc[countries_to_plot, :].index,
            y=CasesByCountry().countries_recovered().loc[countries_to_plot].values[:, 0],
            marker_color='green',
            name='Recoveries',
            opacity=opacity_val,
            marker_line_color=marker_line_color_val,
            marker_line_width=marker_line_width_val))

    graph_two.append(
        go.Bar(
            x=CasesByCountry().countries_deaths().loc[countries_to_plot, :].index,
            y=CasesByCountry().countries_deaths().loc[countries_to_plot].values[:, 0],
            marker_color='crimson',
            name='Deaths',
            opacity=opacity_val,
            marker_line_color=marker_line_color_val,
            marker_line_width=marker_line_width_val))

    layout_two = dict(title='Top 30 Countries by Confirmed Cases',
                      yaxis=dict(title='Case Count'),
                      font=dict(
                          size=9,
                          color="#7f7f7f"))

    # Third chart
    # Plots cases by type
    graph_three = [go.Scatter(
        x=TimeSeriesByType().total_time_series_cases().index,
        y=TimeSeriesByType().total_time_series_cases().values,
        mode='lines+markers',
        name='Confirmed'),

        go.Scatter(
            x=TimeSeriesByType().total_time_series_recovered().index,
            y=TimeSeriesByType().total_time_series_recovered().values,
            mode='lines+markers',
            name='Recovered'),

        go.Scatter(
            x=TimeSeriesByType().total_time_series_deaths().index,
            y=TimeSeriesByType().total_time_series_deaths().values,
            mode='lines+markers',
            name='Deaths')]

    layout_three = dict(title='Total Cases History',
                        xaxis=dict(title='Date (MM-DD-YY)'),
                        yaxis=dict(title='Case Count'),
                        font=dict(
                            size=9,
                            color="#7f7f7f"))

    fig3 = go.Figure(data=graph_three, layout=go.Layout(layout_three))

    # Graph four
    # Time series of confirmed cases by country
    df = countries_confirmed_time_series()
    graph_four = []
    for i in range(df.shape[0]):
        graph_four.append(
            go.Scatter(
                x=df.columns,
                y=df.iloc[i, :],
                mode='lines+markers',
                name=df.index[i]))

    layout_four = dict(title='Confirmed Cases History by Country',
                       xaxis=dict(title='Date (MM-DD-YY)'),
                       yaxis=dict(title='Case Count'),
                       showlegend=True,
                       font=dict(
                           size=9,
                           color="#7f7f7f"))

    fig4 = go.Figure(data=graph_four, layout=go.Layout(layout_four))

    # Graph five
    # Bubble map of case type
    geoplot = []
    df = GeoPlotData().geo_plot_confirmed()
    geoplot.append(go.Scattergeo(
        lon=df['Long'],
        lat=df['Lat'],
        text=df[['Country/Region', str(df.columns[-1])]],
        name='Confirmed',
        marker=dict(
            size=abs(df[df.columns[-1]].replace(np.nan, 0) / 1000),
            line_color='rgb(40,40,40)',
            line_width=0.5,
            color='orange')))

    df = GeoPlotData().geo_plot_recovered()
    geoplot.append(go.Scattergeo(
        lon=df['Long'],
        lat=df['Lat'],
        text=df[['Country/Region', str(df.columns[-1])]],
        name='Recovered',
        marker=dict(
            size=abs(df[df.columns[-1]].replace(np.nan, 0) / 1000),
            line_color='rgb(40,40,40)',
            line_width=0.5,
            color='green')))

    df = GeoPlotData().geo_plot_deaths()
    geoplot.append(go.Scattergeo(
        lon=df['Long'],
        lat=df['Lat'],
        text=df[['Country/Region', str(df.columns[-1])]],
        name='Deaths',
        marker=dict(
            size=abs(df[df.columns[-1]].replace(np.nan, 0) / 1000),
            line_color='rgb(40,40,40)',
            line_width=0.5,
            color='crimson')))

    fig5 = go.Figure(data=geoplot)

    fig5.update_layout(
        title_text='Current Cases Bubble Plot (Click on legend to remove each type)',
        showlegend=True,
        font=dict(
            size=9,
            color="#7f7f7f"),
        geo=dict(
            landcolor='rgb(217, 217, 217)',
            scope='world'
        )
    )

    # append all charts to the figures list
    figures = [dict(data=graph_one, layout=layout_one),
               dict(data=graph_two, layout=layout_two),
               fig3, fig4, fig5]

    return figures
