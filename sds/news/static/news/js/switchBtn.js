$(window).keyup(function (e) {
	var target = $(".button-eco input:focus");
	if (e.keyCode == 9 && $(target).length) {
		$(target).parent().addClass("focused");
		
	}
});

$(".button-eco input").focusout(function () {
	$(this).parent().removeClass("focused");
});

function get_cookie(cookie_name) {
	var results = document.cookie.match(
		"(^|;) ?" + cookie_name + "=([^;]*)(;|$)"
	);

	if (results) return unescape(results[2]);
	else return null;
}

function checkBox(){
	var eco = get_cookie("eco")
	if (eco == "true"){
		document.getElementById("checkboxEco").checked = true
	}
	else{
		document.getElementById("checkboxEco").checked = false
	}
}
checkBox()