// Scripts linked to Base.html of main site.




(function($){
$(document).ready(function(){


// When the user scrolls the page, execute myFunction
window.onscroll = function() {myFunction()};





// Add the sticky class to the navbar when you reach its scroll position. Remove "sticky" when you leave the scroll position
function myFunction() {



    // noinspection JSAnnotator
    $("#navbar").css("top",window.pageYOffset+"px")

}


$("#navbar").menumaker({
    title: "Menu",
    breakpoint: 768,
    format: "multitoggle"
});

$("#navbar").prepend("<div id='menu-line'></div>");

var foundActive = false, activeElement, linePosition = 0, menuLine = $("#navbar #menu-line"), lineWidth, defaultPosition, defaultWidth;


$("#navbar > ul > li").each(function() {
  if ($(this).hasClass('active')) {
    activeElement = $(this);
    foundActive = true;
  }
});

if (foundActive === false) {
  activeElement = $("#navbar > ul > li").parent();
}

defaultWidth ="100%"
lineWidth = activeElement.width();


defaultPosition = linePosition = activeElement.position().left;

menuLine.css("width", lineWidth);
menuLine.css("left", linePosition);

$("#navbar > ul > li").hover(function() {
  activeElement = $(this);
  lineWidth = activeElement.width();
  linePosition = activeElement.position().left;
  menuLine.css("width", lineWidth);
  menuLine.css("left", linePosition);
}, function() {
  menuLine.css("left", defaultPosition);
  menuLine.css("width", defaultWidth);
});

});
})(jQuery);


