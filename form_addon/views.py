from collections import OrderedDict

from django.http.response import HttpResponse, JsonResponse
from urllib.parse import parse_qs
from django.core import serializers
from dateutil.parser import parse
from form_addon.models import *
from cms.models import CMSPlugin, Placeholder
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
from importlib import import_module
from dashboards_app.models import Dashboard
import json

# loggin Details#
import logging

# Start Logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# create a file handler
handler = logging.FileHandler('form_addon.log')
handler.setLevel(logging.DEBUG)
# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(handler)



def is_date(string):
    try:
        int(string)
        print('int')
        return False
    except ValueError:
        try:
            if string.find('.') != -1:
                print(string.find('.'))
                return False
            else:
                try:
                    parse(string)
                    print('parse')
                    return True
                except:
                    return False
        except:
            return False




def form_addon(request):
    logger.info("Starting form_addon request of data")


    grid_exist=False
    #Import function from asset
    try:
        form_data = parse_qs(request.POST['form'])
        dashboard_id=json.loads(request.POST['dashboard_id'])
        active_dashboard = Dashboard.objects.get(pk=dashboard_id)
        py_module = import_module('resources.dashboards.' + active_dashboard.slug + '.FormFunctions')
        try:
            grid_data=json.loads(request.POST['grid_data'])
            grid_keys=json.loads(request.POST['grid_keys'])

            grid_data_df = pd.DataFrame(index=grid_keys, columns=range(len(grid_data[0])))
            for counter, i in enumerate(grid_data_df.index):
                grid_data_df.loc[i] = grid_data[counter]

            grid_exist=True

        except Exception as e:
            logger.debug("Grid not read")




    except Exception as e:
        logger.exception('Couldnt import module')



    try:

        if form_data['save_calculate'][0] == '1':  # when value is 1 it means to save the model else backtest
            pass
            #uncomment to activate save/load model
            # ajax_function = form_data['ajax_function'][0]
            # py_function = form_data['py_function'][0]
            # model_name = form_data['model_name'][0]
            # model_comments = form_data['model_comments'][0]
            # button_name = form_data['button_name'][0]
            # form_name = form_data['form_name'][0]
            #
            # if StoreModels.objects.filter(model_name=model_name).exists():
            #     logger.debug('Setting http response to exist')
            #     return HttpResponse('exist')
            # else:
            #     model_save = StoreModels(ajax_function=ajax_function,
            #                              py_function=py_function, model_name=model_name, form_name=form_name,
            #                              model_comments=model_comments, button_name=button_name)
            #
            #     model_save.save()
            #
            # del form_data['ajax_function']
            # del form_data['model_name']
            # del form_data['model_comments']
            # del form_data['save_calculate']
            # del form_data['py_function']
            # del form_data['button_name']
            # del form_data['form_name']
            #
            # unorder_list = []
            #
            # for key, value in form_data.items():
            #     order_key = key.split('-')
            #     logger.info('slkdkljashdjkdhjkasdhkjashdjkash')
            #     logger.info(order_key[0])
            #     logger.info(order_key[1])
            #     unorder_list.append({'order': int(order_key[1]), 'key': order_key[0], 'value': value})
            #
            # order_list = sorted(unorder_list, key=lambda k: k['order'])
            # logger.info(order_list)
            # for i in order_list:
            #     input_name = i['key']
            #     input_value = i['value'][0]
            #     logger.info(input_value)
            #     if input_value == 'on' or input_value == 'off':
            #         input_type = 'checkbox'
            #     elif is_date(input_value):
            #         input_type = 'date'
            #     else:
            #         input_type = 'text'
            #     model_inputs = ModelsInput(model=model_save, input_name=input_name, input_value=input_value,
            #                                input_type=input_type)
            #     model_inputs.save()
            #
            # # logger.info(i)
            #
            # logger.info("#### Model Saved")
            #
            # return HttpResponse('ok')

        elif form_data['save_calculate'][0] == '0':


            if 'model_name' in form_data \
                and 'model_comments' in form_data \
                and 'save_calculate' in form_data:
                del form_data['model_name']
                del form_data['model_comments']
                del form_data['save_calculate']

            py_function = form_data['py_function'][0]
            Form_Dict = OrderedDict()

            for key, value in form_data.items():
                Form_Dict[key] = value[0]

            # method_name = py_function
            # possibles = globals().copy()
            # possibles.update(locals())
            # method = possibles.get(method_name)

            try:
                method = getattr(py_module, py_function)

            except Exception as e:
                logger.exception("Couldnt Import function %s",py_function)

            data_1 = json.loads(request.POST['regressors'])
            data_2 = json.loads(request.POST['target'])

            try:
                dashboard_name = json.loads(request.POST['dashboard_name']).strip().lower()
                dashboard_author = json.loads(request.POST['dashboard_author']).strip().replace(' ', '')
                dashboard_id=json.loads(request.POST['dashboard_id'])
                logger.debug(dashboard_id)

                logfile_name = 'resources/user_logs/' + dashboard_author + dashboard_name.replace(' ','-') +dashboard_id+ '.log'
                logger.debug("sending to log file %s",logfile_name)


            except Exception as e:
                logger.exception("Error extracting log file in FormAddonViews")
                logfile_name = 'form_addon.log'

            logger.info('--- Finishing form_addon request of data')
            logger.debug(data_1)
            if grid_exist==True:
                return JsonResponse(method(Form_Dict, data_1, data_2, logfile_name,grid_data_df.to_json(orient='index')), safe=False)
            else:
                return JsonResponse(method(Form_Dict, data_1, data_2, logfile_name), safe=False)
    except Exception as e:
        logger.exception("error")
