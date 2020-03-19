

/*
the following codes are to be injected into the html file:
 
inside header: 	

	<link rel="stylesheet" href="MainMap_style.css" />


inside body:

    <div id="MapVar"></div>

*/


//mandatory globals, need to be added to the code
var wrapper = document.createElement("div");
var canvas = document.createElement("canvas");
canvas.setAttribute("class", "focusArea");
var displayArea = document.createElement('div');
// displayArea.textContent = " ";
displayArea.setAttribute("id", "displayArea");
displayArea.innerHTML = "Wavelength Number: ";
canvas.height = 50;
canvas.width = 420
wrapper.appendChild(canvas);
wrapper.appendChild(displayArea);



drawLines(event, handleMouseOverLines);

createLegend(MapVar);



/**
 * handles mouse events over the lines
 */
function handleMouseOverLines(lambdaList) {

    canvas.addEventListener("mousemove", e => showLineNumberInBox(e, lambdaList));
    canvas.addEventListener("mouseleave", unshowLineNumberInBox);
}



/**
 * addes legend to the given map
 */
function createLegend(MapVar) {
    var legend = L.control({ position: 'bottomleft' });
    legend.onAdd = function (map) {
        var div = L.DomUtil.create("div", "legend");
        div.style.backgroundColor = 'WHITE';

        div.innerHTML += '<p>Number of Links<b>: XX</b></p>';
        div.innerHTML += '<p>xxxx  xxxx xxxx<b>: XX</b></p>';

        return div;
    };

    legend.addTo(MapVar);
}





/**
 * 
 * @param data: an array of arrays containing two double values
 * 

 */
function drawLines(layer, lambdaList, callback) {

    popupOptions = {
        maxWidth: "auto"
    };

    layer.bindPopup(drawDetailBox(lambdaList), popupOptions)
    
    callback(lambdaList)

}

/**
 * draws a popup box with lines inside it.
 * retuns an html element (div)
 */
function drawDetailBox(lambdaList) {

    var h = canvas.height;
    console.log(h);

    var ctx = canvas.getContext("2d");

    for (var i = 1; i <= 100; i++) {

        ctx.beginPath();
        ctx.moveTo(i * 4, 0);
        ctx.lineTo(i * 4, h);
        ctx.lineWidth = 2;
        if (lambdaList.includes(i))
            ctx.strokeStyle = "black"
        else
            ctx.strokeStyle = "gray";
        ctx.stroke();

    }

    return wrapper;
}


/**
 * adds a number to the bootom of the popup box when mouse is over the corresponding line
 * @param  e: event 
 */
function showLineNumberInBox(e, LambdaLsit) {
    x = e.clientX;
    y = e.clientY;
    var lineNum = 0;
    const xOff = e.offsetX;
    if (xOff % 4 <= 2) {
        cursor = " ";
        lineNum = parseInt(xOff / 4);
        if(lambdaList.includes(lineNum)){
            cursor = lineNum;
        }
    } else {
        cursor = " ";
    }
    document.getElementById("displayArea").style.display = 'block';
    document.getElementById("displayArea").innerHTML = 'Wavelength Number: '+ cursor;
    document.getElementById("displayArea").style.right = x + 'px';
    document.getElementById("displayArea").style.top = y + 'px';
}

/**
 * removes the line number created in method showLineNumberInBox when mouse leaves the line
 */
function unshowLineNumberInBox() {
    document.getElementById("displayArea").innerHTML = "Wavelength Number: ";
}