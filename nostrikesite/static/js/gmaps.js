var map;

function initialize() {
  var mapOptions = {
    zoom: 10,
    center: new google.maps.LatLng(46.201228, 6.139797)
  };
  map = new google.maps.Map(document.getElementById('map-canvas'),
      mapOptions);

  // Try HTML5 geolocation
  if(navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
      var pos = new google.maps.LatLng(position.coords.latitude,
                                       position.coords.longitude);

      map.setCenter(pos);
    });
  }
}

google.maps.event.addDomListener(window, 'load', initialize);