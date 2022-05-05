$(function () {
	
    var location =  document.location.pathname;
 
    $('.nav__right a').each(function () {
		
        var link = $(this).attr('href');
 
        if (location == link) {
            $(this).addClass('active__header');
        }

		// переписать этот if
		if (document.location.pathname.split('/')[1] == 'post'){
			$('.nav__right a:first').addClass('active__header');
		}
    });
});


$(function () {
	
    var location =  document.location.pathname;
 
    $('.footer__nav__right a').each(function () {
		
        var link = $(this).attr('href');
 
        if (location == link) {
			console.log("check")
            $(this).addClass('active__footer');
        }
    });
});