# -*- coding: utf-8 -*-

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from dashboards_app.models import Dashboard
from cms.models import CMSPlugin
from django.contrib import admin

from db_addon.models import *
from . import models
from importlib import import_module


import csv
import os

import datetime

from django.shortcuts import render
from db_addon.models import *
import pandas as pd
import sqlite3


# loggin Details#
import logging
#Start Logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# create a file handler
handler = logging.FileHandler('database_addon.log')
handler.setLevel(logging.DEBUG)
# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(handler)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def CreateHTMLTable(df, id):

    try:
        records = len(df.index)
        
        html = '<div class="my-out">\
                    <div>\
                        <table border="1">\
                            <thead>\
                                <tr>\
                                <th>Selected</th>\
                                <th>Remove</th> </tr>\
                            </thead>\
                        </table>\
                    </div>\
                    <div class="my-oneline">\
                        <table id="leftDataTable" class="table table-striped table-bordered">\
                            <thead>\
                            </thead>\
                            <tbody id="leftTBody"> \
                            </tbody>\
                        </table>\
                    </div>\
                </div>'

        html += '<div class="my-out">\
                    <div>\
                        <table border="1">\
                            <thead>\
                                <tr>\
                                <th>Selected</th>\
                                <th>Remove</th> </tr>\
                            </thead>\
                        </table>\
                    </div>\
                    <div class="my-oneline">\
                        <table id="rightDataTable" class="table table-striped table-bordered">\
                            <thead>\
                            </thead>\
                            <tbody id="rightTBody"> \
                            </tbody>\
                        </table>\
                    </div>\
                </div>'

        # html += '<table id="leftDataTable" class="table table-striped table-bordered my-oneline my-cur">\
        #     <thead>\
        #         <tr>\
        #             <th>Selected</th>\
        #             <th>Remove</th> </tr>\
        #     </thead>\
        #     <tbody> \
        #     </tbody>'
        
        html += '<div id="datatable-header-'+str(id)+'" style="display: inline-block;width:100%;">'

        # html += '<div class="dt-buttons"><button class="btn btn-primary btn-select-all" onclick="selectAll(\'db-data-' \
        #       'table-' + str(id) + '\')">Select All</button></div><div class="clearfix"><ul class="left-selection">' \
        #                            '</ul><ul class="right-selection"></ul></div></div>'

        html += '<div class="dt-buttons"><button class="btn btn-primary btn-select-all my-selectAll" onclick="selectAll(\'db-data-' \
              'table-' + str(id) + '\')">Select All</button></div></div>'

        html += '<table id="db-data-table-'+str(id)+'" class="display compact data-table-display" width="100%" >'

        html += '<thead><tr>'
        for col in df.columns:

           html += '<th>'+col+'</th>'

        html += '</tr></thead><tbody>'

        for row in range(records):
            html += '<tr id=' + str(row) + '>'
            for col in df.columns:
                html += '<td>' + str(df[col].iloc[row]) + '</td>'
            html += '</tr>'

        html += '</tbody></table>'
    except Exception as e:
        logger.exception('Error Creting Table')

    return html


class DBPlugin_individual(CMSPluginBase):
    model = DBPlugin_individual
    name = "Add Database"
    render_template = "db_addon/detail_dbplugin.html"




    def render(self, context, instance, placeholder):
        logger.info('##############Connecting to DB ...')

        try:

            # Include DB
            try:
                database_name = instance.database_name

                try:
                    table_name = instance.database_table_name
                except:
                    logger.error("DB couldnt find table with name ", instance.database_table_name)
            except:
                logger.error("DB not found ", instance.database_table_name)

            database = os.path.join(BASE_DIR, 'resources/DB/' + database_name + '.db')

            conn = sqlite3.connect(database)
            logger.info("Connected To Database %s", database_name)
            c = conn.cursor()

            c.execute('SELECT * FROM {tn}'. \
                      format(tn=table_name, ))
            all_rows = c.fetchall()
            c.execute('PRAGMA table_info({tn})'. \
                      format(tn=table_name, ))

            list_col = c.fetchall()
            col_names = [col[1] for col in list_col]
            query_df = pd.DataFrame(all_rows, columns=col_names)
            conn.close()

            logger.info("Data Extracted and Transformed by ", instance.database_py_function)




            try:
                # ToDo Transform Queried DF using the desired python function
                active_plugin= CMSPlugin.objects.get(pk=instance.cmsplugin_ptr_id)
                dashboard=Dashboard.objects.get(sidebar_content_id=active_plugin.placeholder_id)
                dash_slug=dashboard.slug
                dash_author=dashboard.author
                dash_author=dash_author.name.replace(" ","")

                try:


                    py_module = import_module('resources.dashboards.' + dash_slug + '.FormFunctions')
                    py_function = instance.database_py_function
                    method = getattr(py_module, py_function)
                    modified_df=method(query_df.copy(),dash_author,dashboard.id)


                    logger.info("Database filtered by function")
                except Exception as e:
                    logger.exception('Couldnt import module')
                    modified_df=query_df

                # sort by column

                try:
                    filter = instance.database_filter_column
                    modified_df = modified_df.sort_values(filter)

                    filtered_column = modified_df.columns.get_indexer([filter])
                    logger.info("DataBase sorted by %s ", filter)
                    logger.debug(filtered_column)
                except Exception as e:
                    logger.exception("Couldnt find column %s to sort", filter)
                    filtered_column = []



                sc = CreateHTMLTable(modified_df,instance.cmsplugin_ptr_id)
            except:
                logger.info("Data Frame couldnt be transformed to Data Table ")



            logger.info("DataBase %s read succesfully ", database)
        except Exception as e:
            logger.exception("DataBase %s was not read ", database)
            sc=[]
            filtered_column=[]
            query_df=pd.DataFrame()



        context.update({
            'instance': instance,
            'data_table': sc,
            'filtered_column': filtered_column,
            'total_columns': len(query_df.columns),
        })



        return context


class DBPlugin(CMSPluginBase):
    model = DBPlugin
    name = 'Add Databases to Navigation Bar'
    render_template = "db_addon/base_dbplugin.html"
    allow_children = True
    child_classes = ['DBPlugin_individual']

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,

        })

        return context





plugin_pool.register_plugin(DBPlugin)
plugin_pool.register_plugin(DBPlugin_individual)
