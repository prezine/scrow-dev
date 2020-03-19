$('.accordion li').on('click', function (e) {
	e.preventDefault();
	$('.accordion li').removeClass('active');
	$(this).toggleClass('active');
	let type = $(this).data('type');
	if (type == "paying") {
		$("#withdraw").addClass('hide');
		$("#paying").removeClass('hide');
	} else if (type == "withdraw") {
		$("#paying").addClass('hide');
		$("#withdraw").removeClass('hide');
	}
});