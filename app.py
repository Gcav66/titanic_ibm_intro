from flask import Flask, request, redirect, render_template, send_file
import pandas as pd
import os
from model import get_sample_data, get_summary_stats

def create_app():
    app=Flask(__name__)
    app.config['PROPAGATE_EXCEPTIONS'] = True
    return app

app = create_app()

@app.route("/", methods=['GET', 'POST'])
def table():
    template = 'table.html'
    data_df = get_sample_data('train.csv')
    stats_df = get_summary_stats('train.csv')
    return render_template(template, data=data_df.to_html(index=False), summary=stats_df.to_html(index=False))

@app.route("/table-css", methods=['GET', 'POST'])
def table_css():
    template = 'table_css.html'
    data_df = get_sample_data('train.csv')
    stats_df = get_summary_stats('train.csv')
    return render_template(template, data=data_df.to_html(index=False), summary=stats_df.to_html(index=False))

@app.route("/table-css-custom", methods=['GET', 'POST'])
def table_css_custom():
    template = 'table_css_custom.html'
    data_df = get_sample_data('train.csv')
    stats_df = get_summary_stats('train.csv')
    return render_template(template, data=data_df.to_html(index=False), summary=stats_df.to_html(index=False))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host='0.0.0.0', port=int(port), debug=True)