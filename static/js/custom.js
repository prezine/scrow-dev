// Enable Toggle Switches
$(".nav-item").on('click', function (e) {
	e.preventDefault();
	$(".element-box").addClass('hide');
	var href = $(this).find('a.nav-link').attr('href').replace('#','');
	document.title = "Scrow — "+ $(this).find('a.nav-link').data('title');
	$("#"+href).removeClass('hide');
});

// Fetch Json
$(document).ready(function() {
	$.getJSON('./app/helpers/banks.json', function(data) {
		var html = '';
		$.each(data, function(index, value) {
			html += '<option value="'+ value +'">'+ value +'</option>';
		});
		$('select.bank').html(html);
	});
});

// On boarding ...
introJs().start();
introJs(".introduction").start();