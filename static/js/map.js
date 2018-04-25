// The example code provided.
// Access token now loaded from server env.
// Add each state as a layer on line 40.
// Submit form data and use results as fill opacity line 79-102.

var map = new mapboxgl.Map({
  container: 'map',
  maxZoom: 5.5,
  minZoom: 1.8,
  style: 'mapbox://styles/mapbox/light-v9',
  center: [-115.36957574368233, 50.732480262447524],
  zoom: 2.850019725398168
});

map.on('load', function () {

  var layers = map.getStyle().layers;

  // Find the index of the first symbol layer in the map style
  var firstSymbolId;
  for (var i = 0; i < layers.length; i++) {
      if (layers[i].type === 'symbol') {
          firstSymbolId = layers[i].id;
          break;
      }
  }

  var statesLayer = map.addLayer({
    'id': 'us-states',
    'type': 'fill',
    'source': {
      type: 'geojson',
      data: statesData
    },
    'paint': {
      'fill-color': '#db600f',
      'fill-opacity': 0.01
    }
  }, firstSymbolId);

  statesData['features'].forEach(function(feature) {
    map.addLayer({
      'id': feature['id'],
      'type': 'fill',
      'source': {
        'type': 'geojson',
        'data': {
          'type': 'Feature',
          'geometry': feature['geometry']
        }
      },
      'layout': {},
      'paint': {
        'fill-color': '#db600f',
        'fill-opacity': 0.01
      }
    });
  })
});

map.on('click', 'us-states', function(e) {
  var coordinates = almostFlatten(e.features[0].geometry.coordinates);
  var bounds = new mapboxgl.LngLatBounds(coordinates[0], coordinates[0]);
  coordinates.forEach(function(coord) {
    bounds.extend(coord);
  })

  map.fitBounds(bounds, { padding: 100 });
});


function almostFlatten(arr) {
  return arr.reduce(function (flat, toFlatten) {
    return flat.concat(Array.isArray(toFlatten[0]) ? almostFlatten(toFlatten) : [toFlatten]);
  }, []);
}


function fillOpacity(data) {
  // takes states and count json from disaster helper/server/page
  var totalCounts = data['total'];
  var states = data['counts'];
  // for each state, divides count by total records
  for (var state in states) {
    if (states.hasOwnProperty(state)) {
      var opacity = states[state] / totalCounts;
      // match state up with state shape
      // use the ratio as fill opacity
      map.setPaintProperty(state, 'fill-opacity', opacity)
    }
  }
}


$('form').on('submit', function(e) {
  e.preventDefault();
  $.post('/filters.json', {
    'fd': $('input[name="from_date"]').val(),
    'td': $('input[name="to_date"]').val(),
    'disasters': $('select[name="disasters"]').val()
  }, fillOpacity);
});
