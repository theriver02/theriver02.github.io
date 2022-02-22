$(document).ready(function(){
	//==============================================================================


	/*==============================================================================
	jQuery events
	==============================================================================*/

	// Change wrapper and <li> color on wrapper dblclick
	jQuery("body").on("dblclick", ".wrapper", function() {
		jQuery(this).css("background-color", "white");
		jQuery("li").css("background-color", "yellow");
	});

	jQuery("body").on("click", ".icon", function() {
		jQuery("header li").toggleClass("visible");

	});




	//==============================================================================
});
