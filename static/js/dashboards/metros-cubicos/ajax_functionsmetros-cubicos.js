//this file should hold the ajax functions for interaction in form_addon, dont delete
function MakeAnalysis(data){

    $('#blc-Line_Graph-0').empty();
    $('#blc-Map_Graph-0').empty();

    var data_json = JSON.parse(data);
    var results=data_json['result'];
    var json_data=JSON.parse(results[2]);



     console.log(json_data);
     console.log(Object.keys(json_data).length);
    //update  column values
    var col_names=[];
    for (key in json_data[0]){

        col_names.push(key)
    }
    window["hot204"].updateSettings({
            rowHeaderWidth: 180,
            colHeaders: col_names
        });

    //update cell values
    var counter=0
    for( i=0;i<Object.keys(json_data).length;i++){

        for (key in json_data[i]){

            window["hot204"].setDataAtCell(i,counter,json_data[i][key]);
            counter=counter+1;
        }
        counter=0
    }
    // for (key in json_data[0]){
    //     console.log(json_data[0][key])
    // }
    // var counter=0;
    // for(var key in json_data){
    //
    //     for (column in key){
    //         console.log(key[column]);
    //         //window["hot204"].setDataAtCell(json_data[key][column],counter,'verga');
    //         counter=counter+1;
    //     }
    //     counter=0;
    //}


    $('#blc-Line_Graph-0').append(results[0]);
    $('#blc-Map_Graph-0').append(results[1]);

    alert("Success")
}
