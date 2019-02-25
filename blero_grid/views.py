
from blero_grid.models import *
from django.http.response import HttpResponse, JsonResponse
from urllib.parse import parse_qs
from django.views.decorators.csrf import csrf_exempt

# loggin Details#
import logging

# Start Logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# create a file handler
handler = logging.FileHandler('blero_grid.log')
handler.setLevel(logging.DEBUG)
# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(handler)



@csrf_exempt
def save_grid(request):

    try:


        # change label to is edited



        row_values=request.POST.getlist('row_values[]')
        col_values=request.POST.getlist('col_values[]')
        model_id=request.POST['model_id']
        n_rows=len(row_values)
        n_columns=len(col_values)
        grid_values=[request.POST.getlist('grid_values['+str(i)+'][]') for i in range(n_rows)]



        #change edited to model
        active_grid=BleroGrid.objects.get(pk=model_id)
        active_grid.content_edited=True
        active_grid.save()

        #get cell values
        #GridCells
        for row in range(n_rows):

            for column in range(n_columns):


                #update Cell
                cell_value=grid_values[row][column]
                if cell_value !='':
                    temp_cell, created = GridCells.objects.update_or_create(model=active_grid,row_number= row, column_number= column,
                                                                            defaults={
                                                                                'content_edited': True,
                                                                                'cell_content': cell_value,
                                                                            }
                                                                            )

                    temp_cell.refresh_from_db()


    except Exception as e:
        logger.exception("error from ajax")

    return JsonResponse("ok", safe=False)
