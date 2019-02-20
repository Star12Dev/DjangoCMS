// Scripts linked to db_addon


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
var selection_color_data2='#e8e07d';
var selection_color_data1rbg=convertHex(selection_color_data1);
var selection_color_data2rbg=convertHex(selection_color_data2);

var checked_dataframe2 = {}; //new code

var tableId = "table-holder-199"


//right Item Delete

function rightDelete(rItem) {
    

    // add some fancy key handling here?
    var id = rItem;
    var class_parent="";

    if (rItem % 2 == 1)
    {

        class_parent = "even context-frames database_0"

        if (tableId == "table-holder-246") 
        {
            class_parent = "even context-frames database_1"
        }
    }
    else
    {
        class_parent = "odd context-frames database_0"
        if (tableId == "table-holder-246") 
        {
            class_parent = "odd context-frames database_1"
        }
    }

    var classes=class_parent.split(" ");
    var class_list = "";
    for (var i = 0; i < classes.length; i++)
    {
        if (classes[i].length > 0)
        {
            class_list += "."+classes[i];
        }
    }
    

    var active_db=class_list.match(/database_(\d+)/)[1];
    console.log(active_db);
    console.log(checked_dataframe2);
    var checked = false;

    var foundIndex = checked_dataframe2[active_db].findIndex(x => x.id == id);
    //var foundIndex = checked_dataframe2[active_db].findIndex(x.id === id);

    console.log("DEBUG!!"+foundIndex+checked);
    console.log('#' + id+class_list);
    var target_t='#' + id+class_list;

    var column_value=$(target_t).children()[0].textContent;





    if(foundIndex != -1){
        checked_dataframe2[active_db][foundIndex].checked = checked;
        if(checked == false){
            $('#' + id+class_list).css('backgroundColor', '#ffffff');
        }else{
            $('#' + id+class_list).css('backgroundColor', selection_color_data2);
        }

    } else {
        $('#' + id+class_list).css('backgroundColor', selection_color_data2rbg);
        $('.context-menu-item').css('backgroundColor', selection_color_data2rbg);
        $('.context-menu-list').css('backgroundColor', selection_color_data2rbg);
        checked_dataframe2[active_db].push({id:id, checked: checked,column_value:column_value})

    }
    // var tableId = $('#' + id+class_list).closest('table').attr('id');
    var tableHeader = tableId.replace('db-data-table', 'datatable-header');

    var rightSelection = $('#'+tableHeader).find('ul.right-selection')[0];
    $(rightSelection).html('');
    $("#rightDataTable tbody").empty()
    $('#'+tableId).find('tr').not('.group').each(function (index) {
        // if ($(this).css('background-color') == selection_color_data2rbg) {
        //     console.log($(this).find('td').eq(0).text());
        //     // $(rightSelection).append('<li>' + $(this).find('td').eq(0).text() + '</li>');

        //     $('#rightDataTable tbody').append('<tr class="child"><td>' + $(this).find('td').eq(0).text() + '</td>\
        //     <td><a href="javascript:void(0)" class="btn btn-info btn-sm xbtn" href="#" id="right'+$(this).attr('id')+'">' + ' X ' + '</a></td></tr>');
        // }

        var itemColor = $('#' + tableId + ' #' + index).attr('style')

        if (itemColor)
        {
            if (itemColor.substring(22, 25) == "232") {
            // console.log($(this).find('td').eq(0).text());
            // $(leftSelection).append('<li>' + $(this).find('td').eq(0).text() + '</li>');

                $('#rightDataTable tbody').append('<tr class="child"><td>' + $('#' + tableId + ' #' + index)[0].textContent + '</td>\
                <td><a class="btn btn-info btn-sm xbtn" href="#" id="right'+index+'">' + ' X ' + '</a></td></tr>');

            
            }
        }


    });    

    // var classes=class_parent.split(" ");
    // var class_list = "";
    // for (var i = 0; i < classes.length; i++)
    // {
    //     if (classes[i].length > 0)
    //     {
    //         class_list += "."+classes[i];
    //     }
    // }
    // console.log(classes);
    // console.log(rItem);

    // var active_db=class_list.match(/database_(\d+)/)[1];
    // console.log(active_db);
    // console.log(checked_dataframe2);
    // // var checked = e.target.checked;
    // var foundIndex = checked_dataframe2[active_db].findIndex(x => x.id === id);
    // //var foundIndex = checked_dataframe2[active_db].findIndex(x.id === id);

    // // console.log("DEBUG!!"+foundIndex+checked);
    // // console.log('#' + id+class_list);
    // var target_t='#' + id+class_list;

    // var column_value=$(target_t).children()[0].textContent;

    // $('#' + id+class_list).css('backgroundColor', '#ffffff');

    // console.log(active_db)
    // console.log(frontIndex)
    // console.log("---Right-----")
    // checked_dataframe2[active_db][foundIndex].checked = false;


    // // if(foundIndex != -1){
    // //     checked_dataframe2[active_db][foundIndex].checked = checked;
    // //     if(checked == false){
            
    // //     }else{
    // //         $('#' + id+class_list).css('backgroundColor', selection_color_data2);
    // //     }

    // // } else {
    // //     $('#' + id+class_list).css('backgroundColor', selection_color_data2rbg);
    // //     $('.context-menu-item').css('backgroundColor', selection_color_data2rbg);
    // //     $('.context-menu-list').css('backgroundColor', selection_color_data2rbg);
    // //     checked_dataframe2[active_db].push({id:id, checked: checked,column_value:column_value})

    // // }
    // // var tableId = $('#' + id+class_list).closest('table').attr('id');
    // var tableHeader = tableId.replace('db-data-table', 'datatable-header');

    // var rightSelection = $('#'+tableHeader).find('ul.right-selection')[0];
    // $(rightSelection).html('');

    // $('#rightDataTable tbody').empty()

    // $('#'+tableId).find('tr').not('.group').each(function (index) {


    //     // if ($(this).css('background-color') == selection_color_data2rbg) {
    //     //     console.log($(this).find('td').eq(0).text());
    //     //     // $(rightSelection).append('<li>' + $(this).find('td').eq(0).text() + '</li>');

    //     //     $('#rightDataTable tbody').append('<tr class="child"><td>' + $(this).find('td').eq(0).text() + '</td>\
    //     //     <td><a href="javascript:void(0)" class="btn btn-info btn-sm xbtn" href="#" id="right'+$(this).attr('id')+'">' + ' X ' + '</a></td></tr>');
    //     // }

    //     var itemColor = $('#' + tableId + ' #' + index).attr('style')

    //     if (itemColor)
    //     {
    //         if (itemColor.substring(22, 25) == "232") {
    //         // console.log($(this).find('td').eq(0).text());
    //         // $(leftSelection).append('<li>' + $(this).find('td').eq(0).text() + '</li>');

    //             $('#rightDataTable tbody').append('<tr class="child"><td>' + $('#' + tableId + ' #' + index)[0].textContent + '</td>\
    //             <td><a class="btn btn-info btn-sm xbtn" href="#" id="right'+index+'">' + ' X ' + '</a></td></tr>');

            
    //         }
    //     }
    // });

    
}


$(document).ready(function () {

    $(document).ready(function () {
        $('#save_calculate').val(1)
        $('.display.compact.data-table-display.dataTable.no-footer').css('width', '735px');
        $('.dataTables_scrollHead .dataTables_scrollHeadInner').css('width', '735px');
    });




    //----------------------------------Database Add_on Initialize-----------------------------
    //Initialize Database Tables
    var databases_tables = document.querySelectorAll('[id^="database-pluginid"]');

    [].forEach.call(databases_tables, function(li) {
        // create data tables
        var plugin_id =li.textContent;
        var db_table_name="db-data-table-"+plugin_id;
        var col_filter=document.getElementById("database-filtered-column-"+plugin_id).textContent;
        var total_columns=document.getElementById("database-total-columns-"+plugin_id).textContent;

        var replace_col=col_filter.replace("[","");
        replace_col=replace_col.replace("]","");
        console.log(replace_col);
        datatable_filter(db_table_name,replace_col,total_columns);



    });



    // Assign click functions to rows in data tables
    function ColorSelection(e) {




        //dont enter when the table is handsontable
        if ($(this).closest('table').hasClass('htCore')){
            console.log('handsontable');
        }
        else {

            
            console.log("Asd")
            
            if ($(this).closest('tr').attr('class') != 'group') {
                if ($(this).css('background-color') != selection_color_data1rbg) {
                    
                    
                    if ($(this).css('background-color') == selection_color_data2rbg) {
                        
                        var index = checked_dataframe2.map(function (o) {
                            return o.id;
                        }).indexOf($(this).attr('id'));
                        if (checked_dataframe2.hasOwnProperty(index)) checked_dataframe2[index].checked = false;
                    }
                    $(this).css('background-color', selection_color_data1);
                    

                } else {                   


                    $(this).css('background-color', '#ffffff');
                }
            }
            // var tableId = $(this).closest('table').attr('id');
            var tableHeader = tableId.replace('db-data-table', 'datatable-header');

            console.log("Table ID ----" + tableId)


            

            var leftSelection = $('#' + tableHeader).find('ul.left-selection')[0];
            $(leftSelection).html('');
            $("#leftDataTable tbody").empty()
            $('#' + tableId).find('tr').not('.group').each(function (index) {
                var itemColor = $('#' + tableId + ' #' + index).attr('style')                


                if (itemColor)
                {
                    if (itemColor.substring(22, 25) == "159") {
                    // console.log($(this).find('td').eq(0).text());
                    // $(leftSelection).append('<li>' + $(this).find('td').eq(0).text() + '</li>');

                        console.log('#' + tableId + ' -------#' + index)

                        $('#leftDataTable tbody').append('<tr class="child"><td>' + $('#' + tableId + ' #' + index)[0].textContent + '</td>\
                        <td><a class="btn btn-info btn-sm xbtn" href="#" id="left'+index+'">' + ' X ' + '</a></td></tr>');

                    
                    }
                }

                // console.log(itemColor)
                // console.log("-----9-------")
                
                // if ($(this).css('background-color') == selection_color_data1rbg) {
                //     // console.log($(this).find('td').eq(0).text());
                //     // $(leftSelection).append('<li>' + $(this).find('td').eq(0).text() + '</li>');

                //     $('#leftDataTable tbody').append('<tr class="child"><td>' + $(this).find('td').eq(0).text() + '</td>\
                //     <td><a class="btn btn-info btn-sm xbtn" href="#" id="left'+$(this).attr('id')+'">' + ' X ' + '</a></td></tr>');

                    
                // }
            });
            

        }
    }

    function ContextmenuSelection(e) {
        $(this).siblings('.selection_color_data2rbg').removeClass('selection_color_data2rbg')
        $(this).not('.selection_color_data2rbg').addClass('selection_color_data2rbg');
    }

    $("tbody tr").each(function(index){
           $(this).on("click",ColorSelection);
           // $(this).on("contextmenu", ContextmenuSelection)
        });

    

    // Assing Classes to Rows for context menu and create checked_data
        var counter_db=0;
     $( "table[id^='db-data-table']" ).each(function(index) {
            $(this).find("tr").each(function(index){
                $(this).addClass('context-frames '+'database_'+counter_db)
            });
            checked_dataframe2[counter_db]=[];
            counter_db=counter_db+1;

        });



    $("table").on('click', '.xbtn', function(){
        
        var xbtnId = $(this).attr('id').split('t');
        if (xbtnId[0][0] == 'r')
        {
            rightDelete(xbtnId[1]);   
        }
        else
        {
            console.log(xbtnId[1])
            $("#"+tableId+" #"+xbtnId[1]).click();
        }
        
    })

    $("#db_menu li").click(function(s) {
        
        var databaseID = $(this).closest("li").index()
        tableId = "table-holder-199" 

        $("#leftDataTable tbody").empty()
        $("#rightDataTable tbody").empty()  

        if (databaseID == 1)
        {
            var tableHeader = tableId.replace('db-data-table', 'datatable-header');


            
            $('#' + tableId).find('tr').not('.group').each(function (index) {
                // if ($(this).css('background-color') == selection_color_data1rbg) {
                //     // console.log($(this).find('td').eq(0).text());
                //     // $(leftSelection).append('<li>' + $(this).find('td').eq(0).text() + '</li>');

                //     $('#leftDataTable tbody').append('<tr class="child"><td>' + $(this).find('td').eq(0).text() + '</td>\
                //     <td><a class="btn btn-info btn-sm xbtn" href="#" id="left'+$(this).attr('id')+'">' + ' X ' + '</a></td></tr>');

                    
                // }
                // if ($(this).css('background-color') == selection_color_data2rbg) {
                
                //     $('#rightDataTable tbody').append('<tr class="child"><td>' + $(this).find('td').eq(0).text() + '</td>\
                //     <td><a href="javascript:void(0)" class="btn btn-info btn-sm xbtn" href="#" id="right'+$(this).attr('id')+'">' + ' X ' + '</a></td></tr>');
                // }
                var itemColor = $('#' + tableId + ' #' + index).attr('style')

                if (itemColor)
                {
                    if (itemColor.substring(22, 25) == "159") {
                    // console.log($(this).find('td').eq(0).text());
                    // $(leftSelection).append('<li>' + $(this).find('td').eq(0).text() + '</li>');

                        $('#leftDataTable tbody').append('<tr class="child"><td>' + $('#' + tableId + ' #' + index)[0].textContent + '</td>\
                        <td><a class="btn btn-info btn-sm xbtn" href="#" id="left'+index+'">' + ' X ' + '</a></td></tr>');

                    
                    }
                    if (itemColor.substring(22, 25) == "232") {
                    // console.log($(this).find('td').eq(0).text());
                    // $(leftSelection).append('<li>' + $(this).find('td').eq(0).text() + '</li>');

                        $('#rightDataTable tbody').append('<tr class="child"><td>' + $('#' + tableId + ' #' + index)[0].textContent + '</td>\
                        <td><a class="btn btn-info btn-sm xbtn" href="#" id="right'+index+'">' + ' X ' + '</a></td></tr>');

                    
                    }
                }


            });

        }
        else 
        {
            tableId = "table-holder-246"
            var tableHeader = tableId.replace('db-data-table', 'datatable-header');

            console.log(tableId)

            
            $('#' + tableId).find('tr').not('.group').each(function (index) {
                // if ($(this).css('background-color') == selection_color_data1rbg) {
                //     // console.log($(this).find('td').eq(0).text());
                //     // $(leftSelection).append('<li>' + $(this).find('td').eq(0).text() + '</li>');

                //     $('#leftDataTable tbody').append('<tr class="child"><td>' + $(this).find('td').eq(0).text() + '</td>\
                //     <td><a class="btn btn-info btn-sm xbtn" href="#" id="left'+$(this).attr('id')+'">' + ' X ' + '</a></td></tr>');

                    
                // }
                // if ($(this).css('background-color') == selection_color_data2rbg) {
                
                //     $('#rightDataTable tbody').append('<tr class="child"><td>' + $(this).find('td').eq(0).text() + '</td>\
                //     <td><a href="javascript:void(0)" class="btn btn-info btn-sm xbtn" href="#" id="right'+$(this).attr('id')+'">' + ' X ' + '</a></td></tr>');
                // }

                var itemColor = $('#' + tableId + ' #' + index).attr('style')

                if (itemColor)
                {
                    if (itemColor.substring(22, 25) == "159") {
                    // console.log($(this).find('td').eq(0).text());
                    // $(leftSelection).append('<li>' + $(this).find('td').eq(0).text() + '</li>');

                        $('#leftDataTable tbody').append('<tr class="child"><td>' + $('#' + tableId + ' #' + index)[0].textContent + '</td>\
                        <td><a class="btn btn-info btn-sm xbtn" href="#" id="left'+index+'">' + ' X ' + '</a></td></tr>');

                    
                    }
                    if (itemColor.substring(22, 25) == "232") {
                    // console.log($(this).find('td').eq(0).text());
                    // $(leftSelection).append('<li>' + $(this).find('td').eq(0).text() + '</li>');

                        $('#rightDataTable tbody').append('<tr class="child"><td>' + $('#' + tableId + ' #' + index)[0].textContent + '</td>\
                        <td><a class="btn btn-info btn-sm xbtn" href="#" id="right'+index+'">' + ' X ' + '</a></td></tr>');

                    
                    }
                }

            });
        }
        
    })


});





function selectAll(tableId) {
    var tableHeader = tableId.replace('db-data-table', 'datatable-header');
    var btnSelAll = $('#' + tableHeader).find('.btn-select-all');
    var leftSelection = $('#'+tableHeader).find('ul.left-selection')[0];
    var color;
    $(leftSelection).html('');
    if ($(btnSelAll).text() == 'Select All') {
        color = selection_color_data1rbg;
        $(btnSelAll).text('Deselect All');
    }
    else {
        $(btnSelAll).text('Select All')
        $("#leftTBody").empty()
        color = '#fff'
    }   
    

    ('#leftDataTable tbody').empty()
    $('#' + tableId).find('tr').not('.group').each(function (index) {
       if ($(this).css('background-color') !=  selection_color_data2rbg) {
           $(this).css('background-color', color);
       }
       if (color == selection_color_data1rbg) {
           // $(leftSelection).append('<li>' + $(this).find('td').eq(0).text() + '</li>');
           $('#leftDataTable tbody').append('<tr class="child"><td>' + $(this).find('td').eq(0).text() + '</td>\
            <td><a href="javascript:void(0)" class="btn btn-info btn-sm xbtn" href="#" id="left'+$(this).attr('id')+'">' + ' X ' + '</a></td></tr>');           
           
       }
    });
}



//Initialize with filtering of Data Tables
function datatable_filter(db_table_name,filter_row,data_cols) {

    var table_name='#'+db_table_name
    console.log(table_name)

    if (!filter_row){
        console.log("no columen to filter")
        var table = $(table_name).DataTable(
        {

            "fixedHeader":true,
            "scrollY": "400px",
            "scrollX":true,
            "bInfo": false,
            "bLengthChange": false,
            "bPaginate": false,
            "sDom": 'l<"H"Rf>t<"F"ip>',
            "drawCallback": function (settings) {
                var api = this.api();
                var rows = api.rows({page: 'current'}).nodes();

                var last = null;
                var groupadmin = [];
                console.log("ENTERED");



                for (var k = 0; k < groupadmin.length; k++) {
                    // Code added for adding class to sibling elements as "group_<id>"
                    $("#" + groupadmin[k]).nextUntil("#" + groupadmin[k + 1]).addClass(' group_' + groupadmin[k]).addClass('td_row');
                    // Code added for adding Toggle functionality for each group
                    $("#" + groupadmin[k]).click(function () {
                        var gid = $(this).attr("id");
                        $(".group_" + gid).slideToggle(300);
                    });

                }
            },
        }
    );



    }
    else {
        var table = $(table_name).DataTable(
            {

                "fixedHeader": true,
                "scrollY": "400px",
                "scrollX": true,

                "aaSorting": [[filter_row, 'asc']],

                "columnDefs": [
                    {"visible": false, "targets": filter_row}
                ],

                "bInfo": false,
                "bLengthChange": false,
                "bPaginate": false,
                "sDom": 'l<"H"Rf>t<"F"ip>',
                "drawCallback": function (settings) {
                    var api = this.api();
                    var rows = api.rows({page: 'current'}).nodes();

                    var last = null;
                    var groupadmin = [];
                    console.log("ENTERED")

                    api.column(filter_row, {page: 'current'}).data().each(function (group, i) {

                        if (last !== group) {

                            $(rows).eq(i).before(
                                '<tr class="group" id="' + i + '"><td colspan="' + data_cols + '">' + group + '</td></tr>'
                            );
                            groupadmin.push(i);
                            last = group;
                        }
                    });


                    for (var k = 0; k < groupadmin.length; k++) {
                        // Code added for adding class to sibling elements as "group_<id>"
                        $("#" + groupadmin[k]).nextUntil("#" + groupadmin[k + 1]).addClass(' group_' + groupadmin[k]).addClass('td_row');
                        // Code added for adding Toggle functionality for each group
                        $("#" + groupadmin[k]).click(function () {
                            var gid = $(this).attr("id");
                            $(".group_" + gid).slideToggle(300);
                        });

                    }
                },
            }
        );
    }



    $(function() {
        $.contextMenu({
            selector: '.context-frames td',
            callback: function(key, options) {
                alert("Clicked on " + key + " on element " + options.$trigger.attr('id').substr(3));
            },
            items: {
                yesno: {
                    name: "Assing to DataFrame2",
                    type: 'checkbox',

                    selected: false,
                    events: {
                        click: function(e) {
                            console.log(e)

                            // add some fancy key handling here?
                            var id = e.data.$trigger[0].parentElement.id;


                            var class_parent=e.data.$trigger[0].parentElement.className;

                            

                            var classes=class_parent.split(" ");
                            var class_list = "";
                            for (var i = 0; i < classes.length; i++)
                            {
                                if (classes[i].length > 0)
                                {
                                    class_list += "."+classes[i];
                                }
                            }
                            

                            var active_db=class_list.match(/database_(\d+)/)[1];
                            console.log(active_db);
                            console.log(checked_dataframe2);
                            var checked = e.target.checked;

                            var foundIndex = checked_dataframe2[active_db].findIndex(x => x.id === id);
                            //var foundIndex = checked_dataframe2[active_db].findIndex(x.id === id);

                            console.log("DEBUG!!"+foundIndex+checked);
                            console.log('#' + id+class_list);
                            var target_t='#' + id+class_list;

                            var column_value=$(target_t).children()[0].textContent;





                            if(foundIndex != -1){
                                
                                checked_dataframe2[active_db][foundIndex].checked = checked;
                                if(checked == false){
                                    $('#' + id+class_list).css('backgroundColor', '#ffffff');
                                }else{
                                    $('#' + id+class_list).css('backgroundColor', selection_color_data2);
                                }

                            } else {
                                
                                $('#' + id+class_list).css('backgroundColor', selection_color_data2rbg);
                                $('.context-menu-item').css('backgroundColor', selection_color_data2rbg);
                                $('.context-menu-list').css('backgroundColor', selection_color_data2rbg);
                                checked_dataframe2[active_db].push({id:id, checked: checked,column_value:column_value})

                            }
                            // var tableId = $('#' + id+class_list).closest('table').attr('id');
                            var tableHeader = tableId.replace('db-data-table', 'datatable-header');

                            var rightSelection = $('#'+tableHeader).find('ul.right-selection')[0];
                            $(rightSelection).html('');
                            $("#rightDataTable tbody").empty()
                            $('#'+tableId).find('tr').not('.group').each(function (index) {
                                // if ($(this).css('background-color') == selection_color_data2rbg) {
                                //     console.log($(this).find('td').eq(0).text());
                                //     // $(rightSelection).append('<li>' + $(this).find('td').eq(0).text() + '</li>');

                                //     $('#rightDataTable tbody').append('<tr class="child"><td>' + $(this).find('td').eq(0).text() + '</td>\
                                //     <td><a href="javascript:void(0)" class="btn btn-info btn-sm xbtn" href="#" id="right'+$(this).attr('id')+'">' + ' X ' + '</a></td></tr>');
                                // }

                                var itemColor = $('#' + tableId + ' #' + index).attr('style')

                                if (itemColor)
                                {
                                    if (itemColor.substring(22, 25) == "232") {
                                    // console.log($(this).find('td').eq(0).text());
                                    // $(leftSelection).append('<li>' + $(this).find('td').eq(0).text() + '</li>');

                                        $('#rightDataTable tbody').append('<tr class="child"><td>' + $('#' + tableId + ' #' + index)[0].textContent + '</td>\
                                        <td><a class="btn btn-info btn-sm xbtn" href="#" id="right'+index+'">' + ' X ' + '</a></td></tr>');

                                    
                                    }
                                }


                            });                            

                        }
                    }
                }
            },
            events: {
                show: function(opt) {
                    var $this = this;
                    var data =  opt.$trigger[0].parentElement.id;
                    var class_parent=opt.$trigger[0].parentElement.className;
                    var classes=class_parent.split(" ");
                            var class_list = "";
                            for (var i = 0; i < classes.length; i++)
                            {
                            if (classes[i].length > 0)
                            {
                            class_list += "."+classes[i];
                            }
                            }

                    var active_db=class_list.match(/database_(\d+)/)[1];;



                    setTimeout(function () {

                        console.log(checked_dataframe2)
                        if (checked_dataframe2.hasOwnProperty(active_db)) {
                            var result = checked_dataframe2[active_db].filter(function( obj ) {
                                return obj.id == data;
                            });
                            try{
                                $('.context-menu-item > label > input').prop('checked', result[0].checked);
                                if(result[0].checked){
                                    $('.context-menu-item').css('backgroundColor', selection_color_data2rbg);
                                    $('.context-menu-list').css('backgroundColor', selection_color_data2rbg);
                                }else{
                                    $('.context-menu-item').css('backgroundColor', '#ffffff');
                                    $('.context-menu-list').css('backgroundColor', '#ffffff');
                                }
                            }
                            catch (e) {
                                $('.context-menu-item').css('backgroundColor', '#ffffff');
                                $('.context-menu-list').css('backgroundColor', '#ffffff');
                            }
                        }

                    },50);
                }
            }
        });

        $('.context-frames').on('click', function(e){
            console.log('clicked', this);
        })
    });


}


