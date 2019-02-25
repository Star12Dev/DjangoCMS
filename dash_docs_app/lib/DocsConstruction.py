
from dash_docs_app.models import DashDoc
from dash_docs_app.models import DocumentedModel

#check if all the plugins from dashboard excist in the document
from cms.models import CMSPlugin
from cms.models import Placeholder
from django.test.client import RequestFactory
from django.contrib.admin import AdminSite
from django.contrib.auth.models import User
from cms.api import add_plugin
from db_addon.models import DBPlugin,DBPlugin_individual
from form_addon.models import FormPlugin,FormInputs


#loggin Details#
import logging
#Start Logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# create a file handler
handler = logging.FileHandler('dash_docs.log')
handler.setLevel(logging.DEBUG)
# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(handler)



def CreateLinkList(link_text,link_id,level=0):

    if level==0:
        text_value='<a href="#'+str(link_id)+'"><p class="main_list"> <i class ="fas fa-angle-right"> '+link_text+'</i></p></a>'
    if level==1:
        text_value = '<a href="#' + str(
            link_id) + '"><p class="main_list_1"> <i class ="fas fa-angle-right"> ' + link_text + '</i></p></a>'



    logger.debug(text_value)

    return text_value

def CreateContentText(header_id,header_text,body_text=''):
    text_value='<div class="body_container"><h2 id="'+str(header_id)+'" class="plugin_header">'+header_text+'</h2>'
    text_value+='<br>'
    text_value+=body_text+'</div>'
    return text_value


def CreateFormAddinDoc(content_plugin,doc_sidebar_placehoder,doc_content_placeholder,language):
    form_plugin = FormPlugin.objects.get(cmsplugin_ptr_id=content_plugin.id)
    logger.debug(form_plugin.form_name)
    holder_plugin = add_plugin(doc_sidebar_placehoder, 'TextPlugin', language,
                               body=CreateLinkList('Form: ' + str(form_plugin.form_name), content_plugin.id,0))

    logger.debug(form_plugin)
    form_inputs = FormInputs.objects.filter(id_fr=form_plugin)
    # loop throught inputs to create boddy:
    body_content = '<div class="form_inputs">Inputs:</div><div class="inputs_details">'
    for i_f in form_inputs:
        body_content += '<p><b>' + i_f.input_name + ' </b><i>' + i_f.input_type + '</i></p>'

    body_content += '</div><p> Edit Form Documentation ... </p>'

    holder_plguin_content = add_plugin(doc_content_placeholder, 'TextPlugin', language,
                                       body=CreateContentText(content_plugin.id,'Form: '+ str(form_plugin.form_name),
                                                              body_content))

    return holder_plugin

def CreateDBIndivAddinDoc(side_plugin,doc_sidebar_placehoder,doc_content_placeholder,language):
    db_plugin = DBPlugin_individual.objects.get(cmsplugin_ptr_id=side_plugin.id)
    logger.debug(db_plugin.database_name)
    holder_plugin = add_plugin(doc_sidebar_placehoder, 'TextPlugin', language,
                               body=CreateLinkList('Database: ' + str(db_plugin.database_name), side_plugin.id,1))

    logger.debug(db_plugin)
    body_content = '<div class="form_inputs">Database Details:</div><div class="inputs_details">'
    #container details
    filter_column=str(db_plugin.database_filter_column)

    body_content += '<p><b> Database table name: </b><i>' + db_plugin.database_table_name + '</i></p>'
    body_content += '<p><b> Database table filtered by: </b><i>' +filter_column + '</i></p>'

    body_content += '</div><p> Edit Database Documentation ... </p>'

    holder_plguin_content=add_plugin(doc_content_placeholder, 'TextPlugin', language,
                                       body=CreateContentText(side_plugin.id, "Database: "+str(db_plugin.database_name),
                                                              body_content))


    return holder_plugin

def BuildDoc(self):

    # check if dashdoc excist if not create it.
    try:
        active_dashboard=self.get_object()

        if DashDoc.objects.filter(dashboard_id=active_dashboard).count()==0:


            logger.info(active_dashboard.id)
            new_doc=DashDoc(dashboard_id=active_dashboard)
            new_doc.save()
            logger.info("dashboard created for %s", active_dashboard.slug)

        sidebar_plugins_documented=False
        content_pluings_documented=False

        PLUGIN_DOCUMENTATION=['DBPlugin','DBPlugin_individual','FormsPlugin','BleroContainerPlugin']



        #Get Active Plugins

        side_bar_placerholder_id=active_dashboard.sidebar_content.id
        content_placeholder_id=active_dashboard.content.id
        side_bar_plugins=CMSPlugin.objects.filter(placeholder_id=side_bar_placerholder_id)
        content_plugins=CMSPlugin.objects.filter(placeholder_id=content_placeholder_id)
        #plugins to include documentation

        doc_content_plugins=[plugin for plugin in content_plugins if plugin.plugin_type in PLUGIN_DOCUMENTATION ]
        doc_side_bar_plugins=[plugin for plugin in side_bar_plugins if plugin.plugin_type in PLUGIN_DOCUMENTATION ]



        #Get Placeholder ids from doc page
        active_doc=DashDoc.objects.get(dashboard_id=active_dashboard)
        doc_sidebar_placeholder_id=active_doc.sidebar_content_id
        doc_content_placeholder_id=active_doc.dash_docs_content_id

        #Create TextPlugins for each of the plugins
        doc_content_placeholder = Placeholder.objects.get(id=doc_content_placeholder_id)
        doc_sidebar_placehoder=Placeholder.objects.get(id=doc_sidebar_placeholder_id)
        language = 'en'
        #start on plugins on the sidebar
    except Exception as e:
        logger.exception("SDF")



    try:

        for side_plugin in doc_side_bar_plugins:

            #check if plugin is documentes
            try:
                DocumentedModel.objects.get(parent_plugin=side_plugin)
                logger.debug('Documentation for this plugin already exist %s',side_plugin)
            except DocumentedModel.DoesNotExist:

                #dashboard_not documented_then document
                #check if it is Database individual


                if side_plugin.plugin_type=="DBPlugin":
                    holder_plguin_content = add_plugin(doc_content_placeholder, 'TextPlugin', language,
                                                       body=CreateContentText(side_plugin.id,'Databases'))
                    holder_plugin = add_plugin(doc_sidebar_placehoder, 'TextPlugin', language, body=CreateLinkList('Databases',side_plugin.id))

                    logger.debug('Pluggin DBPLugin added to documentation')


                if side_plugin.plugin_type=="DBPlugin_individual":
                    holder_plugin = CreateDBIndivAddinDoc(side_plugin, doc_sidebar_placehoder, doc_content_placeholder,
                                                       language)


                documented_model = DocumentedModel(parent_plugin=side_plugin,holder_plugin=holder_plugin)
                documented_model.save()
                logger.debug('Plugin Documented %s',side_plugin)

        sidebar_plugins_documented=True

    except Exception as e:
        logger.exception("error while trying to document side bar plugins")

    try:

        for content_plugin in doc_content_plugins:

            #check if plugin is documented
            try:
                DocumentedModel.objects.get(parent_plugin=content_plugin)
                logger.debug('Documentation for this content plugin already exist %s',content_plugin)
            except DocumentedModel.DoesNotExist:

                if content_plugin.plugin_type == "FormsPlugin":

                    holder_plugin=CreateFormAddinDoc(content_plugin,doc_sidebar_placehoder,doc_content_placeholder,language)


                documented_model = DocumentedModel(parent_plugin=content_plugin, holder_plugin=holder_plugin)
                documented_model.save()
                logger.debug('Plugin Documented %s', content_plugin)


    except Exception as e:
        logger.exception("error while trying to document content plugins")



    return sidebar_plugins_documented,content_pluings_documented
