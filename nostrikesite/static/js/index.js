var csrftoken = $.cookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

$( document ).ready(function() {
    $.post("/get_pois/", function(data) {
    	$.each(data, function(index, element) {
    		var parts = element.fields.position.split(/,\s*/);
	    	var myLatlng = new google.maps.LatLng(parts[0], parts[1]);
	    	var data = "Name: {0} <br/>Type: {1} <br/>Website: {2}".format(
	    		element.fields.name,
	    		element.fields.type,
	    		element.fields.website);
    		var infowindow = new google.maps.InfoWindow({
      			content: data
    		});
	    	var marker = new google.maps.Marker({
			    position: myLatlng,
			    map: map,
			    title: element.fields.name
			});
			google.maps.event.addListener(marker, 'click', function() {
      			infowindow.open(map,marker);
    		});

    	})
    });
});