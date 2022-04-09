var mymap = L.map('mapid').setView([39.46975, -0.37739], 13);

L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
	attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
	maxZoom: 18,
	id: 'mapbox.streets',
	accessToken: 'pk.eyJ1IjoibWVkaW5hem9yaW4iLCJhIjoiY2t5enJsNG5mMHo1NTJ2cXY0cmYzbmwzYSJ9.6B_InBvL-BZnoL_-KyXrPw'
}).addTo(mymap);
console.log('ADDED')
// L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={access_token}', {
//     maxZoom: 18,
//     attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, ' +
//                  '<a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
//                  'Imagery © <a href="http://mapbox.com">Mapbox</a>',
//     id: 'mapbox.streets',
//     accessToken: 'pk.eyJ1IjoibWVkaW5hem9yaW4iLCJhIjoiY2t5enJsNG5mMHo1NTJ2cXY0cmYzbmwzYSJ9.6B_InBvL-BZnoL_-KyXrPw'
// }).addTo(mymap);


var source = new EventSource('/topic/generator');
source.addEventListener('message', function(e){
    console.log('LLEGA EVENTO:')
    // marker = L.marker([39.46975, -0.37739]).addTo(mymap)
    obj = JSON.parse(e.data);
    // console.log(obj);
    for (var key in obj) {
        aux = obj[key]
        console.log(aux)
        // lat = aux["position"]["lat"];
        // long = aux["position"]["lon"];
        // // username = obj["name"];
        // // marker = L.marker([lat,long],).addTo(mymap).bindPopup('Username: <strong>' + username + '</strong>');
        // marker = L.marker([lat,long],).addTo(mymap)
    }


}, false);

// setTimeout(() => {  console.log("World!"); }, 2000);