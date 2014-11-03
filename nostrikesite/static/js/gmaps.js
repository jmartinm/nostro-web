var map;
var markers = [];

//Set up the custom styles for the map. I've created two styles so the map can switch between them depending on the zoom level. i.e. there is far less detail when the map is zoomed out.
//First, we read in the data describing style.
var style_nostro = [ { "stylers": [ { "saturation": -85 } ] },
{ "featureType": "water", "stylers": [ { "color": "#00a1ff" }, 
{ "lightness": 78 } ] },
{ "elementType": "labels.icon", "stylers": [ { "visibility": "off" } ] } ];


//Opening the option for a map to be adapted in the future
var style_nostro_zoomed = [ { "stylers": [ { "saturation": -85 } ] },
{ "featureType": "water", "stylers": [ { "color": "#00a1ff" }, 
{ "lightness": 78 } ] },
{ "elementType": "labels.icon", "stylers": [ { "visibility": "off" } ] } ];

function initialize() {
  //The degree to which the map is zoomed in. This can range from 0 (least zoomed) to 21 and above (most zoomed).
  var nostroMapZoom = 6;
  //The max and min zoom levels that are allowed.
  var nostroMapZoomMax = 16;
  var nostroMapZoomMin = 4;

  var mapOptions = {
    zoom: 12,
    center: new google.maps.LatLng(33.512950, 36.294998),
    maxZoom:nostroMapZoomMax,
    minZoom:nostroMapZoomMin,
    //Turn off the map controls as we will be adding our own later.
    panControl: false,
    mapTypeControl: false,
    mapTypeControlOptions: {
      mapTypeIds: [ 'map_styles_nostro', 'map_styles_nostro_zoomed']
    }
  };

  map = new google.maps.Map(document.getElementById('map-canvas'),
      mapOptions);

   //Then we use this data to create the styles. 
  var styled_nostro = new google.maps.StyledMapType(style_nostro, {name: "nostro style"});
  var styled_nostro_zoomed = new google.maps.StyledMapType(style_nostro_zoomed, {name: "nostro style zoomed"});

  //Assigning the two map styles defined above to the map.
  map.mapTypes.set('map_styles_nostro', styled_nostro);
  map.mapTypes.set('map_styles_nostro_zoomed', styled_nostro_zoomed);
  //Setting the one of the styles to display as default as the map loads.
  map.setMapTypeId('map_styles_nostro');


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