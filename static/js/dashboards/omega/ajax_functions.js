

function PlotBackTest(data){

    $('#blc-grafica1-0').empty();
    $('#blc-grafica2-0').empty();
    $('#blc-HistWeights-0').empty();


    var data_json = JSON.parse(data);
    var results=data_json['result'];

    $('#blc-grafica1-0').append(results[0]);
    $('#blc-grafica2-0').append(results[1]);
    $('#blc-HistWeights-0').append(results[2]);
    alert("Success")
}
