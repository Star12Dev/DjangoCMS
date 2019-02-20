//link to ajax functions from dashboards.


var imported = document.createElement('script');
imported.src = '/static/js/dashboards/omega/ajax_functions.js';
document.head.appendChild(imported);

var imported = document.createElement('script');
imported.src = '/static/js/dashboards/portfolio-creator/ajax_functionsportfolio-creator.js';
document.head.appendChild(imported);

var imported = document.createElement('script');
imported.src = '/static/js/dashboards/metros-cubicos/ajax_functionsmetros-cubicos.js';
document.head.appendChild(imported);

var imported = document.createElement('script');
imported.src = '/static/js/dashboards/contacts/ajax_functionscontacts.js';
document.head.appendChild(imported);

var imported = document.createElement('script');
imported.src = '/static/js/dashboards/metros-cubicos-scrap-monitor/ajax_functionsmetros-cubicos-scrap-monitor.js';
document.head.appendChild(imported);

var imported = document.createElement('script');
imported.src = '/static/js/dashboards/swap-pricer/ajax_functionsswap-pricer.js';
document.head.appendChild(imported);

console.log(imported.src)



function convertHex(hex){
    hex = hex.replace('#','');
    r = parseInt(hex.substring(0,2), 16);
    g = parseInt(hex.substring(2,4), 16);
    b = parseInt(hex.substring(4,6), 16);
    //Look for spaces !!!!
    result = 'rgb('+r+', '+g+', '+b+')';
    return result;
}

var selection_color_data1='#9fd9ea';
var selection_color_data2='#e8e07d'
var selection_color_data1rbg=convertHex(selection_color_data1);
var selection_color_data2rbg=convertHex(selection_color_data2);



function submit_form(csrf_token, form, dataframe1, dataframe2) {
    var form_data = form.closest("form").serialize();


    for (var input in form.closest("form")[0]){

        try{
            input_name=form.closest("form")[0][input].name;
            if(input_name=='form_instance'){

                var form_instance=form.closest("form")[0][input].value
            }
                //Get child grid
                var hot_id=$('#form-child-container-'+form_instance).find("div[id^='hot']").attr('id');
                var grid_data= window[hot_id].getData();
                var grid_keys=window[hot_id].getRowHeader();
        }
        catch(err){
            console.log('No Grid ')
            var grid_data=[];
            var grid_keys=[];
        }

    }





//this function creates the ajax post  of the form addon
    console.log(JSON.stringify(grid_data))
    console.log(JSON.stringify(grid_keys))

    $.ajax({
        type: "POST",
        url: "/form-addon/",
        data: {
            csrfmiddlewaretoken: csrf_token,
            form: form_data,
            target: JSON.stringify(dataframe2), //new code
            regressors: JSON.stringify(dataframe1), //new code
            dashboard_name:JSON.stringify($("#dashboard_title_value").text()),
            dashboard_author:JSON.stringify($("#dashboard_author_value").text()),
            dashboard_id:JSON.stringify($("#dashboard_id_value").text()),
            grid_data:JSON.stringify(grid_data),
            grid_keys:JSON.stringify(grid_keys),

        },
        success: function (data) {


            var data_json = JSON.parse(data);
            console.log("ENTER!!");
            console.log(data_json);

            window[data_json['ajax_function']](data);


            /*
            if(data.split('<!')[0]=='ok'){
                alert('Model Saved')
            }else if(data.split('<!')[0]=='exist'){
                alert('Model Name Exist!')
            }
            else{
                var data_json = JSON.parse(data);
                console.log("ENTER!!");
                console.log(data_json);
                window[data_json['ajax_function']](data); //if you want to pass arguments to the function
                //window[data_json['ajax_function']]();
                // if(data_json['ajax_function'] === 'function1'){
                //     function1();
                // }else if(data_json['ajax_function'] === 'function2'){
                //     function2()
                // }
                // Object.keys(data_json).forEach(function(key) {
                //     $('#append_form_div').append(key + " " + data_json[key] + " ")
                // });
            }

            */
        },
        error: function (x, t, m) {
            console.log("error on AJAX");

            alert("error"+m);


        }
    });
}



// Controlling functions for submit of the form Addon.

    $('.show_model').click(function () {

        $('#save_calculate').val(1);
    });
    $('#calculate').click(function () {
        $('#save_calculate').val(0);
    });


    $('.submit_form_addon').on('click', '.submit_form', function () {
        $('input[type="search"]').val('').keyup();
        var dataframe1 = {};
        var dataframe2 = {};



        // look for all Database tables and get what it is selected on each one


        var counter_db=0;
        $( "table[id^='db-data-table']" ).each(function(index) {

            // Get DataFrame 1 Values
            dataframe1[counter_db]=[];
            dataframe2[counter_db]=[];
            $(this).find("tr").each(function(index){
                if($(this).css('background-color') === selection_color_data1rbg){
                //dataframe1[counter_db].push($(this).attr('id'));
                dataframe1[counter_db].push($(this).children()[0].textContent);
                }
            });


            //Get DataFrame Values
            for(var i=0; i<checked_dataframe2[counter_db].length; i++){
                if(checked_dataframe2[counter_db][i].checked){

                dataframe2[counter_db].push(checked_dataframe2[counter_db][i].column_value);


                }
                }





            counter_db=counter_db+1;
        });




        console.log(dataframe1);
        console.log(dataframe2);

        ;






        submit_form(token, $(this), dataframe1, dataframe2);
    });

    // $('.submit_form_addon').on('click', '.show_model', function () {
    //     // document.getElementById("save_model_div").style.display = "block";
    //     if($(this).siblings(".save_model_div").css('display')=='block'){
    //         $(this).siblings(".save_model_div").css('display', 'none');
    //     }else{
    //         $(this).siblings(".save_model_div").css('display', 'block');
    //     }
    //
    //
    // });
 //------------------------------------------END NEW CODE-------------------------------------------------






