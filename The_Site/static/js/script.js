$(document).ready(function(){
	// slider
	$('.slider').slick({
		arrows:true,
		dots:true,
		slidesToShow:1,
		speed:300,
        touchThreshold: 300,
		responsive:[
			{
				breakpoint: 1250,
				settings: {
					arrows:true,
					dots:true,
				}
			},
			{
				breakpoint: 980,
				settings: {
					arrows:false,
					dots:true,
				}
			},
			{
				breakpoint: 550,
				settings: {
					autoplay: true,
					autoplaySpeed: 2000,
					arrows:false,
					dots:false,
				}
			}
		]
	});

	// phone mask
	jQuery(function () {
        $('#phoneNumber').inputmask("+375 (99) 99-99-999");
    });

	$('.test_input').on('keypress', function (event) {
		var regex = new RegExp("^[0-9]+$");
		var key = String.fromCharCode(!event.charCode ? event.which : event.charCode);
		if (!regex.test(key)) {
		   event.preventDefault();
		   return false;
		}
	});

	// form send
	$("#culc-dtn").click(function (){
        var serializedData = $("#culc").serialize();
        $.ajax({
            url: "/culc",
            data: serializedData,
            type: 'post',
            success: function (response){
                $('#amount').text(response.amount);
            }
        })
    });
});

