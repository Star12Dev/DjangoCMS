import pandas as pd
import numpy as np
import plotly.graph_objs as go


from plotly import tools
from plotly.offline.offline import _plot_html
import plotly.plotly as plotly



def CreateTraces(Data, y_axis, ColorScale):
    n_lines = 0
    Traces = []
    for column in Data.columns:
        x_index = Data[column][Data[column].notnull()].index
        y_values = Data[column][Data[column].notnull()].values
        Strategy_trace = go.Scatter(
            x=x_index,
            y=y_values,
            name=Data.columns[n_lines],
            yaxis=y_axis,
            line=dict(color=ColorScale[n_lines % len(ColorScale)])
        )
        n_lines = n_lines + 1
        Traces.append(Strategy_trace)

    return Traces


def CreateSource(Data, source, increase=0):
    return dict(
        x=max(Data.index),
        y=min(Data.min(axis=0)) + increase,
        xref='x',
        yref='y',
        text=source,
        showarrow=False,
        arrowhead=7
    )


def CreateSubtitle(subtitle):
    return dict(xref='paper', yref='paper', x=0, y=1.01, xanchor='left',
                yanchor='bottom',
                text=subtitle,
                font=dict(family='Lora',
                          size=14,
                          color='rgb(105,105,105)'),
                showarrow=False)


def CreateTitle(Title, color_t):
    return dict(xref='paper', yref='paper', x=0, y=1.05, xanchor='left',
                yanchor='bottom',
                text=Title,
                font=dict(family='Lora',
                          size=20,
                          color=color_t),
                showarrow=False)

def GenerateLinePlotData(Data):
    ColorScale = ['rgb(255,0,0)', 'rgb(255,255,0']
    Traces = CreateTraces(Data, 'y1', ColorScale)

    annotations = []
    # add Title
    annotations.append(CreateTitle("Test Chart", ColorScale[0]))
    layout=go.Layout()
    layout['annotations'] = annotations

    fig = go.Figure(data=Traces, layout=layout)
    return fig


def CreateLineFigure_simple(Data, ChartTitle, ColorScale, source, Y_Range_Opt=False, subtitle=''):
    # Data: DataFrame with column names and one index, the function will
    # return a pltly figure with the desired color scale, title
    # subtitle and source

    Traces = CreateTraces(Data, 'y1', ColorScale)
    # create layout
    annotiations = []
    # add Title
    annotiations.append(CreateTitle(ChartTitle, ColorScale[0]))

    # add Subtitle
    annotiations.append(CreateSubtitle(subtitle))

    # add source
    annotiations.append(CreateSource(Data, source))

    if Y_Range_Opt == False:
        layout = go.Layout(legend=dict(orientation="h"))
    else:
        layout = go.Layout(
            yaxis=dict(
                range=[Y_Range_Opt[0], Y_Range_Opt[1]]
            )

        )

    layout['annotations'] = annotiations
    fig = go.Figure(data=Traces, layout=layout)
    return fig


def PortfolioWeightsGraph(Data, ChartTitle, ColorScale, source, Y_Range_Opt=False, subtitle=''):
    # Delete Columns with 0s
    Data = Data.loc[:, (Data != 0).any(axis=0)]
    Data = Data.reindex(Data.mean().sort_values().index, axis=1).copy()
    Cumul = Data.copy()
    for i in reversed(range(len(Data.columns))):
        cumsum = Data[Data.columns[i]]
        for j in range(i):
            cumsum = Cumul[Data.columns[j]].values + cumsum

        Cumul[Data.columns[j]] = cumsum

    Traces = []
    colors = 0
    for column in Cumul.columns:

        TempPD = Cumul[column][Data[column] > 0]
        TempPD_Vals = Data[column][Data[column] > 0]
        hover = TempPD_Vals.apply(lambda x: "{:.2f}%".format(x * 100))

        if np.mean(TempPD_Vals) > .05:
            trace_temp = go.Scatter(
                x=TempPD.index,
                y=TempPD.values,
                text=hover,
                hoverinfo='name+x+text',
                mode='lines',
                connectgaps=True,
                name=column,
                line=dict(color=ColorScale[colors % len(ColorScale)]),

            )
            colors = colors + 1
            Traces.append(trace_temp)

    # create layout
    annotiations = []
    # add Title
    annotiations.append(CreateTitle(ChartTitle, ColorScale[-1]))

    # add Subtitle
    annotiations.append(CreateSubtitle(subtitle))

    # add source
    annotiations.append(CreateSource(Data, source))

    if Y_Range_Opt == False:
        layout = go.Layout(legend=dict(orientation="h"))
    else:
        layout = go.Layout(
            yaxis=dict(
                range=[Y_Range_Opt[0], Y_Range_Opt[1]]
            )

        )

    layout['annotations'] = annotiations
    fig = go.Figure(data=Traces, layout=layout)
    return fig


def GenerateBoxPlotData(Data, ChartTitle, ColorScale, source, Y_Range_Opt=False, subtitle=''):
    TimeDataFrame = Data
    # create layout
    annotiations = []
    # add Title
    annotiations.append(CreateTitle(ChartTitle, ColorScale[0]))

    # add Subtitle
    annotiations.append(CreateSubtitle(subtitle))

    # add source
    annotiations.append(CreateSource(Data, source))

    # Create a trace
    traces = []
    color_s = 0
    for t_series in TimeDataFrame.columns:
        Temp_Trace = go.Box(

            y=TimeDataFrame[t_series],
            name=t_series,
            boxpoints='all',
            marker=dict(
                color=ColorScale[color_s % len(ColorScale)],
            )

        )
        traces.append(Temp_Trace)
        color_s = color_s + 1

    layout = go.Layout(legend=dict(orientation="h"))
    layout['annotations'] = annotiations
    fig = go.Figure(data=traces, layout=layout)

    return fig

