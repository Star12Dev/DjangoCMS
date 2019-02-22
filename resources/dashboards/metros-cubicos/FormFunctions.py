#this file should hold the functions that can be selected in each dashboard, do not delete or rename this file
import pandas as pd
import numpy as np
import os
import inspect
from os.path import normpath, basename
from cms.models import CMSPlugin
import sqlite3
import sqlalchemy as sqla

from resources.dashboards.omega import GraphicsFunctions as GF
from plotly.offline import download_plotlyjs, plot
import json
import plotly.graph_objs as go

from resources.Blero.helpers import SetUserLog

#ColorScale = ['#1d284b', '#22fefe', '#b34f8e', '#505759', '#007096', '#006A8E', '#00617F', '#005670']
ColorScale=['#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4', '#46f0f0', '#f032e6', '#bcf60c',
            '#fabebe', '#008080', '#e6beff','#9a6324', '#fffac8', '#800000', '#aaffc3', '#808000', '#ffd8b1',
            '#000075', '#808080',]
##########Database Function################
def RemoveColumns(columns_to_remove, data):
    new_data = data.drop(columns=columns_to_remove)
    return new_data


def GetBuyProperties(data,dash_author,dash_id):
    BASE_DIR =os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    logfile_name=os.path.join('resources/user_logs/' +dash_author+ basename(normpath(BASE_DIR)) +str(dash_id)+ '.log')

    logger = SetUserLog(logfile_name)

    buy_sell = 'buy'
    new_data = data[data.price_type == buy_sell]
    columns_to_remove = ['date_data', 'link', 'ad_name', 'price_currency', 'ppsm', 'land_m2', 'price_type', 'price',
                         'sqm', 'rooms', 'address', 'seller']
    new_data = RemoveColumns(columns_to_remove, new_data.copy())
    new_data=new_data.groupby(['state','district']).count().reset_index()
    new_data=new_data[['district','state']]

    #group by District


    logger.info('Data trasnformed and filtered for prices')




    return new_data

##########Form Functions################

def SliceByColumn(column_name, data):
    # Slice by column to plot
    new_columns = [column_name + x for x in data[column_name].unique()]
    new_data = pd.DataFrame(columns=new_columns, index=data.index)

    for x in data[column_name].unique():
        df_slice = data[data[column_name] == x]['price']
        new_data[column_name + x] = df_slice
    new_data.index = data.sqm


    return new_data


def ExtractDataByState(data,logger):

    try:
        database = '/app/resources/DB/MetrosCubicos.db'
        conn = sqlite3.connect(database)
        table_name = 'clean_apartments_data'


        engine = sqla.create_engine('sqlite:///'+database)
        districts=list(set(data))
        districts=['"'+x+'"' for x in districts]
        query=""" SELECT * from {tn} WHERE district in ({dist})""".\
            format(tn=table_name,dist=','.join(districts))
        properties=pd.read_sql_query(query, engine)

        conn.close()
    except Exception as e:
        logger.exception("Couldnt Extract Data from DB")

    return properties

def GeneratePropertiesLine(properties,min_sqm,max_sqm,min_price,logger):
    chart_data = properties.copy()
    currency = 'MXN'
    chart_data = chart_data[chart_data.sqm > min_sqm]
    chart_data = chart_data[chart_data.sqm < max_sqm]
    chart_data = chart_data[chart_data.price_currency == currency]
    chart_data = chart_data[chart_data.price > min_price]
    mean_ppsm = chart_data.ppsm.mean()

    # slice by column
    column_name = 'seller'
    data = chart_data.copy()

    new_data = SliceByColumn(column_name, data.copy())

    new_data['Mean Price by sqm'] = new_data.index * mean_ppsm



    title = 'Properties prices sliced by  ' +column_name
    source = 'Source: Metros Cubicos'
    new_data.columns=[x.replace('sellerInmobiliaria','').replace('- Inmuebles','') for x in new_data.columns]
    fig=GF.CreateLineFigure_simple(new_data,title, ColorScale,source)

    def resize_graph(figure):

        figure.layout.width = 900
        figure.layout.height = 650
        figure.layout.margin.pad = 1
        figure.layout.margin.t = 50
        figure.layout.margin.b = 50
        return figure

    fig=resize_graph(fig)
    fig.layout.legend["orientation"]='v'
    fig.layout.xaxis['title']='Square Meters'
    fig.layout.yaxis['title'] = 'Price $'
    fig.layout.xaxis['showticklabels'] = True

    fig.data[-1].line['color']='#1d284b'

    # chart specifics
    uniques = data[column_name].unique().size
    for i in range(uniques):
        fig.data[i].mode = 'markers'

    fig.data[i + 1].mode = 'lines'
    div_line = plot(fig, include_plotlyjs=True, output_type='div')

    return div_line


def CreateMapChart(properties, mapbox_access_token,logger):
    data = []
    for i in properties.index:
        lat = [str(properties.loc[i].lat)]
        lng = [str(properties.loc[i].lng)]
        name = properties.loc[i].address
        temp_trace = go.Scattermapbox(
            lat=lat,
            lon=lng,
            mode='markers',
            marker=dict(
                size=14
            ),
            text=name,
        )

        data.append(temp_trace)

    layout = go.Layout(
        autosize=True,
        hovermode='closest',
        mapbox=dict(
            accesstoken=mapbox_access_token,
            bearing=0,
            style='streets',
            center=dict(
                lat=19.4284141802915,
                lon=-99.15993981970851,
            ),
            pitch=0,
            zoom=10
        ),
    )

    fig = dict(data=data, layout=layout)

    def resize_graph(figure):
        figure['layout'].width = 900
        figure['layout'].height = 650
        figure['layout'].margin.pad = 1
        figure['layout'].margin.t = 50
        figure['layout'].margin.b = 50
        return figure

    fig=resize_graph(fig)
    fig['layout'].showlegend=False

    div_map = plot(fig, include_plotlyjs=False, output_type='div')

    return div_map


def CheckIfNumber(string):
    flag = False
    try:
        string_list = string.split()
        for x in string_list:
            y = x.replace(",", "")
            if str.isdigit(y):
                flag = True
    except:
        pass
    return flag
def ExtractPropertiesAddresses(properties,logger):

    address_flag=properties.address.apply(CheckIfNumber)
    target_properties=properties[address_flag]
    args=target_properties.address.values.tolist()

    try:
        database = '/app/resources/DB/MetrosCubicos.db'
        conn = sqlite3.connect(database)
        table_name = 'addresses'


        engine = sqla.create_engine('sqlite:///'+database)
        addresses = ['"' + x + '"' for x in args]

        query="""select * from {tn} where address in ({seq}) """.\
            format(tn=table_name, seq=','.join(addresses))
        addresses_pd=pd.read_sql_query(query, engine)

        conn.close()

        target_properties=target_properties.merge(addresses_pd,on='address',how='left')


        #get only properties that can have an address
        target_properties=target_properties[target_properties.lng!='']
        target_properties=target_properties.dropna()




    except Exception as e:
        target_properties = []
        logger.exception("Couldnt Extract Addresses")

    return target_properties


def AnalyzeProperties(dict_form,data_1,data_2,logfile_name):
    # first step to interact with Blero is to  initialize the logger file.
    logger=SetUserLog(logfile_name)
    logger.info("---------Starting Property Analysis---------")
    mapbox_access_token = "pk.eyJ1IjoiamFsYXRvcnJzMSIsImEiOiJjam9ubHJuazExZGhvM3BwY3F3emZzcXU2In0.dUN0mrjFZ-OVUFts2rdRzg"

    min_sqm=float([ v for k,v in dict_form.items() if 'Min SQM' in k][0])
    min_price =float( [v for k, v in dict_form.items() if 'Min Price' in k][0])
    max_sqm=float([v for k, v in dict_form.items() if 'Max SQM' in k][0])


    try:


        #Get Lines and average Price
        properties=ExtractDataByState(data_1['0'], logger)
        line_div=GeneratePropertiesLine(properties,min_sqm,max_sqm,min_price,logger)

        #get Map Values
        properties_to_map=ExtractPropertiesAddresses(properties,logger)
        if len(properties_to_map.index)<10:
            logger.debug(len(properties_to_map.index))
            map_div=CreateMapChart(properties_to_map,mapbox_access_token,logger)
           
        else:
            map_div='<p> to many properties for API </p>'


        #Get data for grid
        columns_to_remove = ['date_data', 'price_type', 'price','land_m2', 'google_json', 'lat', 'lng']
        properties_to_grid = RemoveColumns(columns_to_remove, properties_to_map.copy())

        dict_form.update({'result':[line_div,map_div,properties_to_grid.to_json(orient='index')]})
        logger.info("-------------Analysis Finished-------------")

    except Exception as e:
        logger.exception("Analysis not performed")


    return json.dumps(dict_form)



