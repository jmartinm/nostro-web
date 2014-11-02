var map;
var markers = [];

function initialize() {
  var mapOptions = {
    zoom: 12,
    center: new google.maps.LatLng(33.512950, 36.294998)
  };
  map = new google.maps.Map(document.getElementById('map-canvas'),
      mapOptions);

  // // Try HTML5 geolocation
  // if(navigator.geolocation) {
  //   navigator.geolocation.getCurrentPosition(function(position) {
  //     var pos = new google.maps.LatLng(position.coords.latitude,
  //                                      position.coords.longitude);

  //     map.setCenter(pos);
  //   });
  // }
}

google.maps.event.addDomListener(window, 'load', initialize);

function setAllMap(map) {
  for (var i = 0; i < markers.length; i++) {
    markers[i].setMap(map);
  }
}
// Removes the markers from the map, but keeps them in the array.
function clearMarkers() {
  setAllMap(null);
}
// Deletes all markers in the array by removing references to them.
function deleteMarkers() {
  clearMarkers();
  markers = [];
}