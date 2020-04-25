/**
 *copy all the function into your code, but you only need to call this one.
 * @param {*} mymap map variable
 * @param {*} dataVar : the return value is stored in this
 */

function addNodeToMainMap(mymap, dataVar) {

    var markers = [];
    var links = [];

    var markerList = [];

    featureGroup = L.featureGroup();
    console.log(featureGroup);
    featureGroup.addTo(mymap);

    var addNodeForm = createAddNodeForm(featureGroup, markers, markerList, mymap);
    var addLinkForm = createAddLinkForm(featureGroup, links, markerList, mymap);

    var div = document.createElement("div");

    var menu = L.control({ position: 'topright' });
    var closeBtn = document.createElement("button");
    closeBtn.setAttribute("class", "mainmap-util-btn");
    var addNodeBtn = document.createElement("button");
    addNodeBtn.setAttribute("class", "mainmap-util-btn");
    var addLinkbtn = document.createElement("button");
    addLinkbtn.setAttribute("class", "mainmap-util-btn");
    var doneBtn = document.createElement("button");
    doneBtn.setAttribute("class", "mainmap-util-btn");


    closeBtn.addEventListener("click", e => {

        markers = [];
        markerList = [];
        links = [];
        featureGroup.remove();

        div.remove();
    });


    addNodeBtn.addEventListener("click", e => {

        if( document.getElementById("addLinkForm").style.display === "block")
            return;
        document.getElementById("addNodeForm").style.display = "block";
    });



    doneBtn.addEventListener("click", e => {
        // sendBack = true;
        //set marker coords and data to some variable
        featureGroup.eachLayer(layer => {
            if (layer instanceof L.Marker)
                layer.dragging.disable();
        });

        div.remove();
        console.log(markers);
        console.log(links);
        dataVar = {
            "nodes": markers,
            "links": links,
            "featureGroup": featureGroup
        }
    });


    doneBtn.innerHTML = "Done!";
    addNodeBtn.innerHTML = "Add Node";
    closeBtn.innerHTML = "x";
    addLinkbtn.innerHTML = "Add Link"

    addLinkbtn.addEventListener("click", e => {

        // console.log(markerList);
        if( document.getElementById("addNodeForm").style.display === "block")
            return;
        document.getElementById("addLinkForm").style.display = "block";

    });

    menu.onAdd = function (map) {

        div.appendChild(doneBtn);
        div.appendChild(addLinkbtn);
        div.appendChild(addNodeBtn);
        div.appendChild(closeBtn);
        div.appendChild(addNodeForm);
        div.appendChild(addLinkForm);

        return div;
    };

    menu.addTo(mymap);

}


function createAddNodeForm(featureGroup, markers, markerList, mymap) {

    var div = document.createElement("div");
    div.setAttribute("id", "addNodeForm");
    div.setAttribute("class", "vertical");

    var nodeParam1 = document.createElement("input");
    nodeParam1.setAttribute("id", "nodeParam1");
    nodeParam1.setAttribute("class", "mainmap-util-input");
    nodeParam1.value = "param1-node";
    nodeParam1.placeholder = "param1-node";
    nodeParam1.setAttribute("type", "text");

    var nodeParam2 = document.createElement("input");
    nodeParam2.setAttribute("id", "nodeParam2");
    nodeParam2.setAttribute("class", "mainmap-util-input");
    nodeParam2.value = "param2-node";
    nodeParam2.placeholder = "param2-node";
    nodeParam2.setAttribute("type", "text");

    var doneBtn = document.createElement("button");
    doneBtn.setAttribute("id", "submitNodeForm");
    doneBtn.setAttribute("class", "mainmap-util-btn");
    doneBtn.innerHTML = "Done!";

    var closeBtn = document.createElement("button");
    closeBtn.setAttribute("id", "closeNodeForm");
    closeBtn.setAttribute("class", "mainmap-util-btn");
    closeBtn.innerHTML = "X";

    closeBtn.addEventListener("click", e => {
        console.log(featureGroup);
        document.getElementById("addNodeForm").style.display = "none";
    });

    doneBtn.addEventListener("click", e => {

        var nodeData;
        var marker;

        var srcNodepopup = L.popup({ autoClose: false }).setContent("Source Node");
        var destNodepopup = L.popup({ autoClose: false }).setContent("Destination Node");
        // destNodepopup.setLatLng([33.51, 57.68]).openOn(mymap);

        console.log("llll");
        nodeData = onSubmitNodeForm();
        marker = L.marker(mymap.getCenter(), { draggable: true });

        marker.on("click", e => {
            console.log(e.target);
            markerList.push(e.target);
            // var isSrc = setLinkSrcAndDest(markerList, marker);
            // if (isSrc) srcNodepopup.setLatLng(e.target.getLatLng()).openOn(mymap);
            // else destNodepopup.setLatLng(e.target.getLatLng()).openOn(mymap);
        });


        var connectedLinks = [];
        var markerInitLatLng;

        marker.on("dragstart", e => {

            connectedLinks = []
            // console.log(e.target.getLatLng());
            markerInitLatLng = e.target.getLatLng();

            getConnectedLinks(e.target, featureGroup, connectedLinks);
        });

        marker.on("drag", e => {

            console.log(e.target.getLatLng());
            markerInitLatLng = connectLinkToNode(e.target, connectedLinks, markerInitLatLng);
        })

        marker.on("dragend", e => {

            markerInitLatLng = connectLinkToNode(e.target, connectedLinks, markerInitLatLng);
        });

        featureGroup.addLayer(marker);
        markers.push({
            "node": marker,
            "nodeData": nodeData
        });
        // console.log(markers);
        div.style.display = "none";
    });


    div.appendChild(nodeParam1);
    div.appendChild(nodeParam2);
    div.appendChild(doneBtn);
    div.appendChild(closeBtn);
    div.style.display = "none";
    return div;
}

function onSubmitNodeForm() {

    return {
        "param1": document.getElementById("nodeParam1").value,
        "param2": document.getElementById("nodeParam2").value

    };
}

function createAddLinkForm(featureGroup, links, markerList, mymap) {

    var div = document.createElement("div");
    div.setAttribute("id", "addLinkForm");
    div.setAttribute("class", "vertical");

    var linkParam1 = document.createElement("input");
    linkParam1.setAttribute("id", "linkParam1");
    linkParam1.setAttribute("class", "mainmap-util-input");
    linkParam1.value = "param1-link";
    linkParam1.placeholder = "param1-link";
    linkParam1.setAttribute("type", "text");

    var linkParam2 = document.createElement("input");
    linkParam2.setAttribute("id", "linkParam2");
    linkParam2.setAttribute("class", "mainmap-util-input");
    linkParam2.value = "param2-link";
    linkParam2.placeholder = "param2-link";
    linkParam2.setAttribute("type", "text");


    var doneBtn = document.createElement("button");
    doneBtn.setAttribute("id", "submitLinkForm");
    doneBtn.setAttribute("class", "mainmap-util-btn");
    doneBtn.innerHTML = "Done!";

    var closeBtn = document.createElement("button");
    closeBtn.setAttribute("id", "closeLinkForm");
    closeBtn.setAttribute("class", "mainmap-util-btn");
    closeBtn.innerHTML = "X";

    closeBtn.addEventListener("click", () => {
        document.getElementById("addLinkForm").style.display = "none";
    });

    doneBtn.addEventListener("click", () => {

        var linkData;

        if (markerList.length < 2) {
            popupAlert("choose 2 nodes", mymap);
            return;
        }

        if(markerList[markerList.length - 1] === markerList[markerList.length - 2]){
            popupAlert("choose a destination node", mymap);
            return;
        }

        latlngs = [
            markerList[markerList.length - 1].getLatLng(),
            markerList[markerList.length - 2].getLatLng(),
        ];
        // console.log(latlngs);

        var link = L.polyline(latlngs, { color: 'red' });
        featureGroup.addLayer(link);

        linkData = onSubmitLinkForm();

        links.push({
            "link": link,
            "linkData": linkData
        });

        // console.log(links);
        div.style.display = "none";

    });

    div.appendChild(linkParam1);
    div.appendChild(linkParam2);
    div.appendChild(doneBtn);
    div.appendChild(closeBtn);

    div.style.display = "none";
    return div;
}


function onSubmitLinkForm() {
    return {
        "param1": document.getElementById("linkParam1").value,
        "param2": document.getElementById("linkParam2").value
    };
}


function popupAlert(msg, mymap) {

    var div = document.createElement("div");
    div.setAttribute("class", "alert horizontal");
    var alertTxt = document.createElement("h5");
    var closeBtn = document.createElement("button");

    alertTxt.innerHTML = msg;
    closeBtn.innerHTML = "X";
    closeBtn.setAttribute("class", "mainmap-util-btn");

    closeBtn.addEventListener("click", () => div.remove());

    var alertBox = L.control({ position: 'bottomright' });

    alertBox.onAdd = function (map) {
        div.appendChild(alertTxt);
        div.appendChild(closeBtn);
        return div;
    };

    alertBox.addTo(mymap);
    console.log(msg);
}


function connectLinkToNode(marker, connectedLinks, markerInitLatLng) {

    for (var i = 0; i < connectedLinks.length; i++) {
        var link = connectedLinks[i];
        console.log("ll" + link.getLatLngs());
        console.log("ma" + marker.getLatLng());

        var latLngStart = link._latlngs[0];
        var latLngEnd = link._latlngs[1];

        if (latLngEnd == markerInitLatLng) {

            console.log("ee");
            link.setLatLngs([
                link.getLatLngs()[0],
                marker.getLatLng()
            ]);
        }
        else if (latLngStart == markerInitLatLng) {

            console.log("ss");
            link.setLatLngs([
                marker.getLatLng(),
                link.getLatLngs()[1]
            ]);
        }
    }
    console.log("init " + markerInitLatLng);
    return marker.getLatLng();


}

function getConnectedLinks(marker, featureGroup, connectedLinks) {

    featureGroup.eachLayer(layer => {
        if (layer instanceof L.Polyline) {

            console.log(layer._latlngs);
            if (layer._latlngs.includes(marker.getLatLng())) {
                console.log("layer" + layer._latlngs);
                connectedLinks.push(layer)
            }
        }

    });
}

function setLinkSrcAndDest(markerList, marker) {

    var isSrc = true;

    if (markerList[0] == null) {
        if(markerList[0] === marker)
            return;
        markerList.splice(0, 0, marker);
        console.log("src n");
    }
    else if (markerList[1] == null) {
        if(markerList[1] === marker)
            return;
        markerList.splice(1, 0, marker);
        isSrc = false;
        console.log("des n");
    }
    else {
        markerList.splice(0, 0, marker);
        markerList.splice(1, 0, null);
        console.log("b fu");
    }

    return isSrc;
}