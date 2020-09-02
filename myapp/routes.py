from myapp import app
import json, plotly
from flask import render_template
from wrangling_scripts.create_figures import return_figures
from wrangling_scripts.wrangle_data import *

@app.route('/')
@app.route('/index')
def index():
    """Index page acting as data dashboard in flask application.

    Returns:
        obj: render template used in html.
    """

    figures = return_figures()  # Build figures from data wrangling

    # Plot ids for the html id tag
    ids = ['figure-{}'.format(i) for i, _ in enumerate(figures)]

    # Convert the plotly figures to JSON for javascript in html template
    figures_json = json.dumps(figures, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('index.html',
                           ids=ids,
                           figuresJSON=figures_json,
                           data_set=return_latest_dataset_date())