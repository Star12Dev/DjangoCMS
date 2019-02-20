//this file should hold the ajax functions for interaction in form_addon, dont delete
function GetScrapStatus(data){

    try {
        //Clean Status Container
        $('#blc-ScrapStatus-0').empty();

        //populate grid
        var data_json = JSON.parse(data)


        var district_records = JSON.parse(data_json['district_records']);


        var cols = 0;
        var rows = 0;
        //from dataframe to grid
        for (var row_i in district_records) {


            for (var column_j in district_records[row_i]) {


                window["hot220"].setDataAtCell(rows, cols, district_records[row_i][column_j]);
                cols = cols + 1
            }
            rows = rows + 1;
            cols = 0
        }

        // Update Statis Container
        $('#blc-ScrapStatus-0').append("<div class='container-fluid'><a href=\"#\" class=\"badge badge-success\">Links Read</a></div>")
         $('#blc-ScrapStatus-0').append("<div class='container-fluid'><a href=\"#\" class=\"badge badge-light\">District log last update: "+data_json['district_update']+"</a></div>")
         $('#blc-ScrapStatus-0').append("<div class='container-fluid'><a href=\"#\" class=\"badge badge-light\">Properties log last update: "+data_json['property_update']+"</a></div>")

       //dict_form['property_update'] = stdout.readline


    }
    catch(err){
        $('#blc-ScrapStatus-0').append("<a href=\"#\" class=\"badge badge-danger\">Links not read check logs</a>")
    }

    console.log("GetScrapStatus Success")
}
