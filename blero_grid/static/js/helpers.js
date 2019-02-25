

























/*
    var cols = [

                {% for i in columns %}
                    {column_font: 'Aria', column_content:"column{{ i }}", column_background_color: '#333', column_font_color: '#ddd'},
                {%  endfor %}

    ];



    var cols{{ instance.pk }} = {{ columns }};

    var colHeaders = [];
    var columndata = [];
    for (i = 0; i < cols.length; i ++) {
        colHeaders.push('<label style="background-color: '+cols[i].column_background_color+';color:'+cols[i].column_font_color+'; font:' + cols[i].font + ';">' + cols[i].column_content + '</lable>')
        columndata.push({ data: cols[i].column_content, renderer: cellRenderer, editor: Handsontable.editors.cellEditor })
    }

    console.log(columndata);


    //code for  formatting
    var data{{ instance.pk }} = {{ grid_data }};
    var cols{{ instance.pk }} = {{ columns }};
    var colHeaders{{ instance.pk }} = [];
    for (i = 0; i < cols{{ instance.pk }}.length; i ++) {
        colHeaders{{ instance.pk }}.push('<label style="background-color: '+cols{{ instance.pk }}[i].column_background_color+';color:'+cols{{ instance.pk }}[i].column_font_color+'; font:' + cols{{ instance.pk }}[i].font + ';">' + cols{{ instance.pk }}[i].column_content + '</lable>')
    }
*/
