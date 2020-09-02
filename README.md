# Coronavirus-Web-Dashboard

This repo contains the code for a Python flask application used to create a COVID-19 monitoring dashboard. The app pulls data from the World Health Organistions (WHO) published data sets [here](https://github.com/CSSEGISandData/COVID-19).

The app was then deployed using Heroku.

Data dashboard: https://jacob-covid-dash.herokuapp.com/

![](readme/covid19-dash.gif)

## Repository Structure
- **myapp** - code base for app deployment
- **wrangling_scripts** - Python code to pull data, wrangle data and create visualisations.

## 1. Introduction

This is the code deployed on heroku to create a web dash board to report the latest COVID-19 statistics in the current pandemic. It is based on a Python Flask App Pulling Data from John Hopkins CSSE and plotting using the plotly module to facilitate interactive.

## 2. Functionality
Click on legend to reformat graph and plot selected datasets. The visualisations are created from Plotly allowing interactive graphing.

## 3. Data Discussion
This is pulled from John Hopkins Github page (here) and at the time of creation updated daily from the World Health Organistions (WHO) published data sets. This includes some region data that is cleaned up in the code to just base the figures on countries instead of regions.


