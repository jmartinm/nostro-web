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

var infowindow;

function get_gmap_infobox(element) {
    var infoBox = document.createElement('div');
    infoBox.className = "safe-location";
    if(element.fields.verified) infoBox.className += " verified";
    else infoBox.className += " not_verified";
    var infoBox_header = document.createElement('div');
    infoBox_header.className = "infoBox_header";
    infoBox_header.innerHTML = "{0}".format(element.fields.name);
    infoBox.appendChild(infoBox_header);

    var infoBox_type = document.createElement('div');
    infoBox_type.className = "infoBox_type";
    infoBox_type.innerHTML = element.fields.type.substr(0,1);
    infoBox.appendChild(infoBox_type);

    var infoBox_endorse = document.createElement('div');
    infoBox_endorse.className = "infoBox_endorse";
    infoBox_endorse.innerHTML = "Endorse!";
    infoBox.appendChild(infoBox_endorse);

    var infoBox_endorse_count = document.createElement('div');
    infoBox_endorse_count.className = "infoBox_endorse_count";
    infoBox_endorse_count.innerHTML = element.fields.public_endorsment + " persons have endorsed this location!";
    infoBox.appendChild(infoBox_endorse_count);

    var infoBox_verification = document.createElement('div');
    infoBox_verification.className = "infoBox_verification";
    if(element.fields.verified) {
        infoBox_verification.innerHTML = "Signed and verified by ThePortOfLife";
        infoBox_verification.innerHTML += " on " + element.fields.verified_date + "</b>";
    } else {
        infoBox_verification.innerHTML = "This site has not yet been verified by an organization!";
    }
    infoBox.appendChild(infoBox_verification);

    var infoBox_content = document.createElement('div');
    infoBox_content.className = "infoBox_content";
    var latitude = Number(element.fields.position.split(/,\s*/)[0]).toFixed(3);
    var longitude = Number(element.fields.position.split(/,\s*/)[1]).toFixed(3);
    infoBox_content.innerHTML = "Name: {0} <br/>Type: {1} <br/>Website: <a href={2}>{2}</a><br/>Location: {3} {4}, {5} {6}".format(
        element.fields.name,
        element.fields.type,
        element.fields.website,
        Math.abs(latitude), latitude>0?"N":"S",
        Math.abs(longitude), longitude>0?"E":"W" );
    infoBox.appendChild(infoBox_content);

    return new InfoBox({
        content: infoBox,
            boxStyle: {
                background: "url('http://google-maps-utility-library-v3.googlecode.com/svn/trunk/infobox/examples/tipbox.gif') no-repeat"
            }
        });
}

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
            var marker = new google.maps.Marker({
                position: myLatlng,
                map: map,
                title: element.fields.name,
                icon: pinImage,
                shadow: pinShadow
            });
            marker.ib = infowindow;
            // infowindow.isOpen = false;
            markers.push(marker)
            google.maps.event.addListener(marker, 'click', function() {
                // if(infowindow.isOpen){ infowindow.close(); infowindow.isOpen = false; }
                // else { infowindow.open(map,marker); infowindow.isOpen = true; }
                if (infowindow) infowindow.close();
                infowindow = get_gmap_infobox(element);
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
