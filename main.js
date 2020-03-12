

/*
the following codes are to be injected into the html file:
 
inside header: 	

	<!--leaflet.js cdn-->
	<link rel="stylesheet" href="https://unpkg.com/leaflet@1.6.0/dist/leaflet.css"
		integrity="sha512-xwE/Az9zrjBIphAcBb3F6JVqxf46+CDLwfLMHloNu6KEQCAWi6HcDUbeOfBIptF7tcCzusKFjFw2yuvEpDL9wQ=="
        crossorigin="" />
        
	<!-- Make sure you put this AFTER Leaflet's CSS -->
	<script src="https://unpkg.com/leaflet@1.6.0/dist/leaflet.js"
		integrity="sha512-gZwIG9x3wUXg2hdXF6+rVkLF/0Vi9U8D2Ntg4Ga5I5BZpVkVxlJWbSQtXPSiUTtC0TjtGOmxa1AJPuV0CPthew=="
		crossorigin=""></script>

	<link rel="stylesheet" href="style.css" />


inside body:

    <div id="mapid"></div>


    <script src="main.js"></script>
	<script src="https://code.jquery.com/jquery-3.4.1.min.js"
	    integrity="sha256-CSXorXvZcTkaix6Yvo6HppcZGetbYMGWSFlBw8HfCJo=" crossorigin="anonymous"></script>
 */


 
//dummy data
var dummyData = [
    [
        [33.51, 55.68],
        [33.51, 57.68]
    ],
    [
        [32.44, 50.40],
        [30.30, 60.00]
    ],
    [
        [30.51, 55.68],
        [33.51, 57.68]
    ],
    [
        [32.44, 56.40],
        [34.30, 60.00]
    ]
];


//map configs 
popupOptions = {
    maxWidth: "auto"
};

lineOptions = {
    color: 'red'
};


//main map
var mymap = L.map('mapid').setView([33.6, 53.7], 13);

//map tile-layer
L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 6,
    id: 'mapbox/streets-v11',
    // x: 53,
    // y: 33,
    // z: 1,
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'pk.eyJ1IjoicGl0Y2xhaXIiLCJhIjoiY2s3MDZmZGcwMDB1NDNtcDBmZ3pjdWp2NyJ9.MC35oYwFqBb-Zndvv2yiHQ'
}).addTo(mymap);




//mandatory globals, need to be added to the code
var wrapper = document.createElement("div");
var canvas = document.createElement("canvas");
canvas.setAttribute("class", "focusArea");
var displayArea = document.createElement('div');
displayArea.textContent = " ";
displayArea.setAttribute("id", "displayArea");
canvas.height = 50;
canvas.width = 420
wrapper.appendChild(canvas);
wrapper.appendChild(displayArea);



drawLines(dummyData);

createLegend(mymap);

handleMouseOverLines();

/**
 * handles mouse events over the lines
 */
function handleMouseOverLines() {

    canvas.addEventListener("mousemove", showLineNumberInBox);
    canvas.addEventListener("mouseleave", unshowLineNumberInBox);
}

/**
 * addes legend to the given map
 */
function createLegend(mymap) {
    var legend = L.control({ position: 'bottomleft' });
    legend.onAdd = function (map) {
        var div = L.DomUtil.create("div", "legend");
        div.style.backgroundColor = 'WHITE';

        div.innerHTML += '<p>Number of Links<b>: XX</b></p>';
        div.innerHTML += '<p>xxxx  xxxx xxxx<b>: XX</b></p>';

        return div;
    };

    legend.addTo(mymap);
}





/**
 * 
 * @param data: an array of arrays containing two double values
 * 
 * example:
 * var dummyData = [
    [
        [33.51, 55.68],
        [33.51, 57.68]
    ],
    [
        [32.44, 50.40],
        [30.30, 60.00]
    ],
    [
        [30.51, 55.68],
        [33.51, 57.68]
    ],
    [
        [32.44, 56.40],
        [34.30, 60.00]
    ]
];
 */
function drawLines(data) {
    for (var i = 0; i < data.length; i++) {
        var polyline = L.polyline(data[i], lineOptions).addTo(mymap);
        polyline.bindPopup(drawDetailBox, popupOptions);
    }
}

/**
 * draws a popup box with lines inside it.
 * retuns an html element (div)
 */
function drawDetailBox() {

    var h = canvas.height;
    console.log(h);

    var ctx = canvas.getContext("2d");

    for (var i = 1; i <= 100; i++) {

        ctx.beginPath();
        ctx.moveTo(i * 4, 0);
        ctx.lineTo(i * 4, h);
        ctx.lineWidth = 2;
        if (i % 10 == 0)
            ctx.strokeStyle = "blue"
        else
            ctx.strokeStyle = "black";
        ctx.stroke();

    }

    return wrapper;
}


/**
 * adds a number to the bootom of the popup box when mouse is over the corresponding line
 * @param  e: event 
 */
function showLineNumberInBox(e) {
    x = e.clientX;
    y = e.clientY;
    const xOff = e.offsetX;
    if (xOff % 4 <= 2) {
        cursor = parseInt(xOff / 4);
    } else {
        cursor = " ";
    }
    document.getElementById("displayArea").style.display = 'block';
    document.getElementById("displayArea").innerHTML = cursor;
    document.getElementById("displayArea").style.right = x + 'px';
    document.getElementById("displayArea").style.top = y + 'px';
}

/**
 * removes the line number created in method showLineNumberInBox when mouse leaves the line
 */
function unshowLineNumberInBox() {
    document.getElementById("displayArea").style.display = 'none';
    document.getElementById("displayArea").innerHTML = "";
}