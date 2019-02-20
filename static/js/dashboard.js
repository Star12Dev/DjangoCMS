//-------------------------------------------Reshaping addons-----------------------------------------------------

function SavePlugin(plugin,plugin_type){

    var pk = plugin.attr('id');
    if (plugin_type == 'FormLabel' || plugin_type == 'FormInput' || plugin_type == 'FormBtn') {
        pk = plugin.attr('data-id');
    }
    var top = plugin.css('top');
    var left = plugin.css('left');
    var width = plugin_type == 'FormInput' ? plugin.find('input').css('width') : plugin.css('width') ;
    var height = plugin_type == 'FormInput'? plugin.find('input').css('height') : plugin.css('height');
    var data = {
        'pk': pk,
        'top': top,
        'left': left,
        'width': width,
        'height': height
    };

    $.ajax({
        url: '/plugin_position/'+plugin_type+'/',
        type: 'post',
        data: data,
        success: function (data) {
            console.log(data['status']);
        },
        error: function () {
            console.log('Couldnt Save Plugins!');
        }
    });

}

function RestorePlugin(plugin,plugin_type){
    var pk = plugin_type == 'FormLabel' || plugin_type == 'FormInput' || plugin_type == 'FormBtn' ? plugin.attr('data-id') : plugin.attr('id');
    var data = {
        'pk': pk
    };

    $.ajax({
        url: '/plugin_position/'+plugin_type+'/',
        type: 'get',
        data: data,
        success: function (data) {
            console.log(data['status']);
        },
        error: function () {
            console.log('Couldnt restore plugins!');
        }
    });

}


$('#save_view').click(function () {
    var classList = $('.submit_form_addon');
    // classList.push($('.blero-container-wrapper'));
    $.each(classList, function(index, item) {
        SavePlugin($(this),'FormPlugin')
    });
    classList= $('.blero-container-wrapper');
    $.each(classList, function(index, item) {
        SavePlugin($(this),'BleroContainer')
    });

    classList= $('.terminal_holder');
    $.each(classList, function(index, item) {
        console.log($(this))
        SavePlugin($(this),'LogTerminal')
    });

    classList = $('.form-element-container').not('.btn-container');
    $.each(classList, function(index, item) {
        console.log($(this))
        SavePlugin($(this),'FormInput')
    });

    classList = $('.form-element-container.btn-container');
    $.each(classList, function(index, item) {
        console.log($(this))
        SavePlugin($(this),'FormBtn')
    });

    classList = $('.form-element-label');
    $.each(classList, function(index, item) {
        console.log($(this))
        SavePlugin($(this),'FormLabel')
    });

    classList = $('.blero-grid-wrapper');
    $.each(classList, function(index, item) {
        console.log($(this))
        SavePlugin($(this),'BleroGrid')
    });

    classList = $('.task-holder');
    $.each(classList, function(index, item) {
        console.log($(this))
        SavePlugin($(this),'TaskHolder')
    });

})
$('#restore_view').click(function () {
    var classList = $('.submit_form_addon');
    $.each(classList, function(index, item) {
        RestorePlugin($(this),'FormPlugin');

    });

    classList = $('.blero-container-wrapper');
    $.each(classList, function(index, item) {
        RestorePlugin($(this),'BleroContainer');

    });

    classList = $('.terminal_holder');
    $.each(classList, function(index, item) {
        RestorePlugin($(this),'LogTerminal');
    });

    classList = $('.form-element-container').not('.btn-container');
    $.each(classList, function(index, item) {
        RestorePlugin($(this),'FormInput')
    });

    classList = $('.form-element-container.btn-container');
    $.each(classList, function(index, item) {
        RestorePlugin($(this),'FormBtn')
    });

    classList = $('.form-element-label');
    $.each(classList, function(index, item) {
        RestorePlugin($(this),'FormLabel')
    });

    classList = $('.blero-grid-wrapper');
    $.each(classList, function(index, item) {
        RestorePlugin($(this),'BleroGrid')
    });

    classList = $('.task-holder');
    $.each(classList, function(index, item) {
        RestorePlugin($(this),'TaskHolder')
    });

});


$('#btn_edit_mode').click(function () {
   $('.edit-mode.hide').removeClass('hide');
   $('.exit-mode').not('.hide').addClass('hide');

   $( ".blero-container-wrapper" ).draggable('enable').resizable('enable');

   $( ".submit_form_addon" ).draggable('enable').resizable('enable');

   $( ".terminal_holder" ).draggable('enable').resizable('enable');

   $( ".form-element-container" ).draggable('enable').resizable('enable');

   $( ".form-element-label" ).draggable('enable').resizable('enable');

   $( ".blero-grid-wrapper" ).draggable('enable').resizable('enable');

   $( ".task-holder" ).draggable('enable').resizable('enable');

});

$('#btn_exit_mode').click(function () {
   $('.exit-mode.hide').removeClass('hide');
   $('.edit-mode').not('.hide').addClass('hide');

   $( ".blero-container-wrapper" ).draggable('disable').resizable('disable');

   $( ".submit_form_addon" ).draggable('disable').resizable('disable');

   $( ".terminal_holder" ).draggable('disable').resizable('disable');

   $( ".form-element-container" ).draggable('disable').resizable('disable');

   $( ".form-element-label" ).draggable('disable').resizable('disable');

   $( ".blero-grid-wrapper" ).draggable('disable').resizable('disable');


   $( ".task-holder" ).draggable('disable').resizable('disable');

});



$(document).ready(function () {

    $('#btn_exit_mode').click();
});








