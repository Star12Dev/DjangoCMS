from django.http import HttpResponse
from django.template import loader
from django.template.context import RequestContext

from dash_docs_app.models import DashDoc
from dashboards_app.models import Dashboard

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

def index(request):

    template = loader.get_template('dash_docs_app/base.html')
    context = {
        'test_context': '56',
    }
    return HttpResponse(template.render(context, request))

def dashboard_doc_view(request,dashboard_id):
    template=loader.get_template('dash_docs_app/doc_detail.html')

    dashboard_parent=Dashboard.objects.get(id=dashboard_id)
    logger.debug(type(dashboard_parent))
    dash_doc=DashDoc.objects.get(dashboard_id=dashboard_parent)
    logger.debug(type(dash_doc))

    if not dash_doc:
        doc_exist=False
        logger.debug('doc not excist')
    else:
        doc_exist=True
        dashboard_title=Dashboard.objects.filter(id=dashboard_id)[0].title

        #get Parent Model title




    context = {
        'doc_exist':doc_exist,
        'dashboard_id': dashboard_id,
        'dashboard_title':dashboard_title,
        'instance':dash_doc,
    }
    return HttpResponse(template.render(context, request))


