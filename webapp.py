#!/usr/bin/env python
from pathlib import Path

from dash.dependencies import Input, State
from piw import Webapp
from dash import html

from src.ctrls import main_ctrl, input_fields
from src.load import define_inputs
from src.plots.StackedBarPlot import StackedBarPlot
from src.proc import process_inputs
from src.update import update_inputs
from src.utils import load_yaml_config_file


# metadata
metadata = {
    'title': 'Hard-to-electrifiy sectors',
    'abstract': 'Calculating the technoeconomics for the hard-to-electrify sectors (aviation, maritime transport, '
                'cement, primary steel and chemical feedstocks).',
    'about': html.Div([
        html.P('This interactive webapp can be used to inspect data from an accompanying article by the same '
               'authors that studies decarbonisation options of hard-to-electrifiy sectors. Some of the key '
               'assumptions (cost of hydrogen and cost of DAC) can be changed here when producing the stacked-bar '
               'plots.'),
        html.P('Some more explanations on what this work does and how it can be used...'),
        html.P('For more advanced changes and detailed information on the input data and methodology, we encourage '
               'users to inspect the article, its supplement, and the source code written in Python.'),
    ]),
    'authors': [
        {
            'first': 'Clara',
            'last': 'Bachorz',
            'orcid': '0000-0003-1638-4048',
            'affiliation': ['Potsdam Institute for Climate Impact Research, Potsdam, Germany'],
        },
        {
            'first': 'Philipp C.',
            'last': 'Verpoort',
            'orcid': '0000-0003-1319-5006',
            'affiliation': ['Potsdam Institute for Climate Impact Research, Potsdam, Germany'],
        },
        {
            'first': 'Falko',
            'last': 'Ueckerdt',
            'orcid': '0000-0001-5585-030X',
            'affiliation': ['Potsdam Institute for Climate Impact Research, Potsdam, Germany'],
        },
    ],
    'date': '2023-01-09',
    'version': 'v0.1.0',
    'doi': 'TBD',
    'licence': {'name': 'CC BY 4.0', 'link': 'https://creativecommons.org/licenses/by/4.0/'},
    'citeas': 'Bachorz, Clara; Verpoort, Philipp C.; Ueckerdt, Falko (2023): Interactive webapp for techno-economic '
              'analysis of the abatement of hard-to-electrify sectors. V. 0.1.0. GFZ Data Services. '
              'https://doi.org/TBD',
    'reference_citeas': 'Bachorz et al., Mapping the technoeconomic landscape for the hard-to-electrify sectors '
                        '(2024). Working paper in preparation.',
    #'reference_doi': 'TBC',
}


# define webapp
webapp = Webapp(
    piw_id='hard-to-electrify',
    metadata=metadata,
    pages={
        '': 'Simple',
        'advanced': 'Advanced',
    },
    load=[define_inputs],
    ctrls=[main_ctrl],
    generate_args=[
        Input('simple-update', 'n_clicks'),
    ] + [
        State(f"simple-{input_field_id}", 'value')
        for input_field_id in input_fields
    ],
    update=[update_inputs],
    proc=[process_inputs],
    plots=[StackedBarPlot],
    glob_cfg=load_yaml_config_file('global'),
    output=Path(__file__).parent / 'print',
    debug=False,
    input_caching=False,
)


# this will allow running the webapp locally
if __name__ == '__main__':
    webapp.start()
    webapp.run()
