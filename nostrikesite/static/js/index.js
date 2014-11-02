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

var color_map = {
    verified : "d8444f",
    nonverified : "47aedb"
};

function fill_gmap(data) {
    $.each(data, function(index, element) {
            var pinColor;
            if (element.fields.verified) {
                pinColor = color_map["verified"];
            }
            else {
                pinColor = color_map["nonverified"];   
            }
            var pinImage = new google.maps.MarkerImage("http://chart.apis.google.com/chart?chst=d_map_pin_letter&chld=%E2%80%A2|" + pinColor,
            new google.maps.Size(21, 34),
            new google.maps.Point(0,0),
            new google.maps.Point(10, 34));
            var pinShadow = new google.maps.MarkerImage("http://chart.apis.google.com/chart?chst=d_map_pin_shadow",
            new google.maps.Size(40, 37),
            new google.maps.Point(0, 0),
            new google.maps.Point(12, 35));
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
                title: element.fields.name,
                icon: pinImage,
                shadow: pinShadow
            });
            markers.push(marker)
            google.maps.event.addListener(marker, 'click', function() {
                infowindow.open(map,marker);
            });

        })

}

$( document ).ready(function() {
    var req_data = {};
    $.post("/get_pois/", function(data) {
    	fill_gmap(data);
    });
    
    $('select[name=verified],select[name=type]').on("change", function(){
        var name = $(this).attr("name");

        req_data[name] = $(this).val();
        $.post("/get_pois/", req_data, function(data) {
            deleteMarkers();
            fill_gmap(data);
        });
    })

});