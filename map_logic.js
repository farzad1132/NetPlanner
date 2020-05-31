         
// output globals 
var globalVar;
var deletedOldLayers = [];



var tempMarkerlist = [];
function topologyMenuHandler() {

    var pathToIcon = "Icons/blue/server_blue.png"
    var markersGroup = myFeatureGroup;
    var linksGroup = links_groupfeature;
    mymap = MapVar;


    deletedOldLayers = [];
    markers = [];
    tempMarkerlist = [];
    links = [];
    globalVar = [];

    var oldMarkers = [];
    var oldLinks = [];

    featureGroup = new L.featureGroup();
    featureGroup.addTo(mymap);
    featureGroup.on("click", handleMarkerOnClick);

    //turn perivious methods off
    markersGroup.off("click", groupClick);
    linksGroup.off("click", links_click_event);

    markersGroup.on("click", handleMarkerOnClick);

    featureGroup.on("contextmenu", e => deleteOnRightClick(e, featureGroup, markers, links, mymap));

    markersGroup.on("contextmenu", e => deleteOnRightClickOld(e, markersGroup, linksGroup, mymap, featureGroup));
    linksGroup.on("contextmenu", e => deleteOnRightClickOld(e, markersGroup, linksGroup, mymap, featureGroup));

    enableOldMarkerDragging(markersGroup, linksGroup, featureGroup);

    markersGroup.eachLayer(layer => {
        oldMarkers.push({
            "name": getLayerName(layer),
            "location": layer.getLatLng(),
            "layer": layer,
            "data": {},
            "isNew": false
        });
    });

    linksGroup.eachLayer(layer => {
        oldLinks.push({
            "name": getLayerName(layer),
            "start": getMarkerNameByLatLng(layer.getLatLngs()[0], markersGroup),
            "end":  getMarkerNameByLatLng(layer.getLatLngs()[1], markersGroup),
            "startLoc": layer.getLatLngs()[0],
            "endLoc": layer.getLatLngs()[1],
            "layer": layer,
            "data": {},
            "isNew": false
        });
    });

    var addNodeForm = createAddNodeForm(featureGroup, markers, mymap, pathToIcon, oldMarkers);
    var addLinkForm = createAddLinkForm(featureGroup, links, mymap, linksGroup);

    var div = document.createElement("div");
    div.setAttribute("id", "topology-panel");

    var menu = L.control({ position: 'topright' });
    var closeBtn = document.createElement("button");
    closeBtn.setAttribute("class", "mainmap-util-closebtn");
    var addNodeBtn = document.createElement("button");
    addNodeBtn.setAttribute("class", "mainmap-util-btn");
    var addLinkbtn = document.createElement("button");
    addLinkbtn.setAttribute("class", "mainmap-util-btn");
    var doneBtn = document.createElement("button");
    doneBtn.setAttribute("class", "mainmap-util-btn");

    closeBtn.addEventListener("click", e => {

        markers = [];
        tempMarkerlist = [];
        links = [];
        globalVar = [];

        featureGroup.remove();
        closeAllPopups();
        markersGroup.off("click", handleMarkerOnClick);

        markersGroup.eachLayer(layer => {
            layer.dragging.disable();
        });

        markersGroup.off("contextmenu");
        linksGroup.off("contextmenu");

        // restore deleted layers
        restoreDeletedLayers(markersGroup, linksGroup);

        restoreDraggedLayersLocation(oldMarkers, oldLinks);

        restoreOldFeatureGroupEvents(markersGroup, linksGroup);

        div.remove();
    });


    addNodeBtn.addEventListener("click", e => {

        if (document.getElementById("addLinkForm").style.display === "block")
            return;
        document.getElementById("addNodeForm").style.display = "block";
    });

    updateVar = "";

    doneBtn.addEventListener("click", e => {

        // remove new markers drag events
        featureGroup.eachLayer(layer => {
            if (layer instanceof L.Marker)
                layer.dragging.disable();
        });

        markersGroup.eachLayer(layer => {
            layer.dragging.disable();
        });

        featureGroup.off("click", handleMarkerOnClick);

        markersGroup.off("click", handleMarkerOnClick);

        featureGroup.off("contextmenu");
        markersGroup.off("contextmenu");
        linksGroup.off("contextmenu");

        closeAllPopups();

        div.remove();

        // send layers to linksGroup and markersGroup, delete the local featureGroup
        featureGroup.eachLayer(l => {
            if (l instanceof L.Marker) {
                l.addTo(markersGroup);
            }

            else if (l instanceof L.Polyline)
                l.addTo(linksGroup);
        });

        fixMarkersData(markers);

        deletedOldLayers = deletedOldLayers.map(l => getLayerName(l));

        //save changed old layers to markers and links
        saveChangedOldMarkersToMarkers(oldMarkers, markers, deletedOldLayers);
        saveChangedOldLinktoLink(oldLinks, links, deletedOldLayers);

        globalVar = {
            "nodes": markers,
            "links": links
        };

        globalVar = JSON.stringify(globalVar);
        deletedOldLayers = JSON.stringify(deletedOldLayers);

        restoreOldFeatureGroupEvents(markersGroup, linksGroup);
    });

    doneBtn.innerHTML = "Done";
    addNodeBtn.innerHTML = "Add Node";
    closeBtn.innerHTML = "x";
    addLinkbtn.innerHTML = "Add Link"

    addLinkbtn.addEventListener("click", e => {

        if (document.getElementById("addNodeForm").style.display === "block")
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

// check for links connected to marker, also delete the data. - params? - only works for new nodes now
function deleteOnRightClick(event, featureGroup, markers, links, mymap) {
    closeAllPopups();
    tempMarkerlist = [];
    if (event.layer instanceof L.Marker) {
        //delete data, connected links;
        marker = event.layer;
        var connectedLinks = [];
        getConnectedLinks(marker, featureGroup, connectedLinks);
        if (connectedLinks.length == 0) {
            deleteOnRightClickLayer(marker, markers, featureGroup);
        } else {
            popupAlert("Marker cannot be deleted - remove the connected links first.", mymap);
        }
    }

    else if (event.layer instanceof L.Polyline) {
        link = event.layer;
        deleteOnRightClickLayer(link, links, featureGroup);
    }
}

function deleteOnRightClickLayer(layer, list, featureGroup) {
    var name = getLayerName(layer);
    var index = -1;
    list.forEach(l => {
        if (l.name == name) {
            index = list.indexOf(l);
            return;
        }
    });
    list.splice(index, 1);
    featureGroup.removeLayer(layer);
}

function deleteOnRightClickOld(event, markersGroup, linksGroup, mymap, featureGroup) {
    closeAllPopups();
    tempMarkerlist = [];
    if (event.layer instanceof L.Marker) {
        marker = event.layer;
        var connectedLinks = [];
        getConnectedLinks(marker, linksGroup, connectedLinks);
        getConnectedLinks(marker, featureGroup, connectedLinks)
        if (connectedLinks.length == 0) {
            deletedOldLayers.push(marker);
            markersGroup.removeLayer(marker);
        } else {
            popupAlert("Marker cannot be deleted - remove the connected links first.", mymap);
        }
    }

    else if (event.layer instanceof L.Polyline) {
        link = event.layer;
        deletedOldLayers.push(link);
        linksGroup.removeLayer(link);
    }
}

function restoreDeletedLayers(markersGroup, linksGroup) {
    deletedOldLayers.forEach(layer => {
        if (layer instanceof L.Marker)
            markersGroup.addLayer(layer);
        else if (layer instanceof L.Polyline)
            linksGroup.addLayer(layer);
    });
}

function createAddNodeForm(featureGroup, markers, mymap, pathToIcon, oldMarkers) {

    var div = document.createElement("div");
    div.setAttribute("id", "addNodeForm");
    div.setAttribute("class", "vertical");

    var inputParams = {
        "paramNames": ["Node_Name", "ROADM_Type"],
        "paramValues": ["", "Directionless"],
        "paramAllValues": ["", ["Directionless", "CDC"]]
    }

    var nodeParams = createParamsInputs(inputParams.paramNames, inputParams.paramValues);

    var doneBtn = document.createElement("button");
    doneBtn.setAttribute("id", "submitNodeForm");
    doneBtn.setAttribute("class", "mainmap-util-btn");
    doneBtn.innerHTML = "Done";

    var closeBtn = document.createElement("button");
    closeBtn.setAttribute("id", "closeNodeForm");
    closeBtn.setAttribute("class", "mainmap-util-btn");
    closeBtn.innerHTML = "Close";

    closeBtn.addEventListener("click", e => {
        document.getElementById("addNodeForm").style.display = "none";
    });

    doneBtn.addEventListener("click", e => {

        var nodeData;
        var marker;

        //check for input param validity:
        if (!isNameValid(inputParams.paramNames[0], markers) || !isNameValid(inputParams.paramNames[0], oldMarkers)) {
            popupAlert("Invalid Node name", mymap);
            return;
        }

        if (!areNodeParamsValid(inputParams.paramNames[1], inputParams.paramAllValues[1])) {
            popupAlert("Invalid parameter. \n" +
                "ROADM TYPE can have a value of \"Directionless\" or \"CDC\".", mymap);
            return;
        }

        markerName = document.getElementById(inputParams.paramNames[0]).value;

        nodeData = onSubmitForm(inputParams.paramValues, inputParams.paramNames);
        marker = L.marker(mymap.getCenter(), {
            draggable: true,
            icon: createCustomIcon(pathToIcon)
        });

        marker.bindTooltip("<h3>" + markerName + "</h3>");

        featureGroup.addLayer(marker);

        var connectedLinks = [];
        var markerInitLatLng;

        marker.on("dragstart", e => {

            connectedLinks = []
            markerInitLatLng = e.target.getLatLng();
            getConnectedLinks(e.target, featureGroup, connectedLinks);
        });

        marker.on("drag", e => {
            markerInitLatLng = connectLinkToNode(e.target, connectedLinks, markerInitLatLng);
        })

        marker.on("dragend", e => {
            markerInitLatLng = connectLinkToNode(e.target, connectedLinks, markerInitLatLng);
        });


        markers.push({
            "name": markerName,
            "layer": marker,
            "data": nodeData,
            "isNew": true
        });
        div.style.display = "none";
    });

    for (var i = 0; i < nodeParams.length; i++) {
        div.appendChild(nodeParams[i].label);
        div.appendChild(nodeParams[i].param);
    }
    div.appendChild(doneBtn);
    div.appendChild(closeBtn);
    div.style.display = "none";
    return div;
}

function handleMarkerOnClick(event) {

    if (!(event.layer instanceof L.Marker)) {
        return;
    }

    var marker = event.layer;

    var srcNodepopup = L.popup(
        { closeOnClick: false, autoClose: false, offset: new L.Point(1, -15) })
        .setContent("Source Node");
    var destNodepopup = L.popup(
        { closeOnClick: false, autoClose: false, offset: new L.Point(1, -15) })
        .setContent("Destination Node");

    var isSrc = setLinkSrcAndDest(marker);

    if (isSrc) {
        closeAllPopups();
        srcNodepopup.setLatLng(marker.getLatLng()).openOn(mymap);
    } else {
        destNodepopup.setLatLng(marker.getLatLng()).openOn(mymap);
    }

}

function createAddLinkForm(featureGroup, links, mymap, linksGroup) {

    var div = document.createElement("div");
    div.setAttribute("id", "addLinkForm");
    div.setAttribute("class", "vertical");

    var inputParams = {
        "paramValues": ["0.0", "0", "0.2", "0", "1.40E-03", "3.16914E-19"],
        "paramNames": ["Length", "Fiber_Type", "Loss_Coefficient", "Beta", "Gamma", "Dispersion"]
    };

    //create link Params
    linkParams = createParamsInputs(inputParams.paramNames, inputParams.paramValues);

    var doneBtn = document.createElement("button");
    doneBtn.setAttribute("id", "submitLinkForm");
    doneBtn.setAttribute("class", "mainmap-util-btn");
    doneBtn.innerHTML = "Done";

    var closeBtn = document.createElement("button");
    closeBtn.setAttribute("id", "closeLinkForm");
    closeBtn.setAttribute("class", "mainmap-util-btn");
    closeBtn.innerHTML = "Close";

    closeBtn.addEventListener("click", () => {
        document.getElementById("addLinkForm").style.display = "none";
    });

    doneBtn.addEventListener("click", () => {

        var linkData;

        // will uncomment this once I fixed the method
        // var linkValidity = checkLinkValidity(tempMarkerlist, featureGroup);

        // if (!linkValidity.isValid) {
        //     popupAlert(linkValidity.msg, mymap)
        //     return;
        // }

        if (tempMarkerlist.length === 0 || tempMarkerlist[tempMarkerlist.length - 1] == undefined || tempMarkerlist[tempMarkerlist.length - 2] == undefined) {
            popupAlert("No chosen nodes.", mymap);
            return;
        }
        else if (tempMarkerlist.length === 1) {
            popupAlert("Choose a destination node.", mymap);
            return;
        }

        if (tempMarkerlist[tempMarkerlist.length - 1] === tempMarkerlist[tempMarkerlist.length - 2]) {
            popupAlert("Choose a destination node.", mymap);
            return;
        }

        // valid length
        if (!isLengthValid(inputParams.paramNames[0])) {
            popupAlert("Invalid Link Length", mymap);
            return;
        }


        // put this to handle no returning out of the following loop, wtf is wrong with my code?
        var exitVar = false;

        //check the new featuregreoup for a duplicate link
        featureGroup.eachLayer(layer => {
            if (layer instanceof L.Polyline) {
                if (layer.getLatLngs().includes(
                    tempMarkerlist[tempMarkerlist.length - 1].getLatLng())
                    && layer.getLatLngs().includes(
                        tempMarkerlist[tempMarkerlist.length - 2].getLatLng())) {
                    popupAlert("Link already exists.", mymap);
                    exitVar = true;
                    return;
                }
            }

        });


        // check oldFeatureGroup fro a duplicate link
        linksGroup.eachLayer(layer => {
            if (layer instanceof L.Polyline) {
                if (layer.getLatLngs().includes(
                    tempMarkerlist[tempMarkerlist.length - 1].getLatLng())
                    && layer.getLatLngs().includes(
                        tempMarkerlist[tempMarkerlist.length - 2].getLatLng())) {
                    popupAlert("Link already exists.", mymap);
                    exitVar = true;
                    return;
                }
            }
        })

        if (exitVar) {
            return;
        }

        // just to make sure this line does not get executed after returning, js is acting funky again
        // console.log("exec?");

        var startMarker = tempMarkerlist[tempMarkerlist.length - 1];
        var endMarker = tempMarkerlist[tempMarkerlist.length - 2];

        var latlngs = [
            startMarker.getLatLng(),
            endMarker.getLatLng(),
        ];

        var link = L.polyline(latlngs,
            {
                color: 'black',
                opacity: 0.8,
                weight: 3
            }
        );

        closeAllPopups();

        linkName = getLayerName(startMarker) + "-" + getLayerName(endMarker);
        link.bindTooltip("<h3>" + linkName + "</h3>");
        featureGroup.addLayer(link);

        linkData = onSubmitForm(inputParams.paramValues, inputParams.paramNames);

        links.push({
            "name": linkName,
            "start": getLayerName(startMarker),
            "end": getLayerName(endMarker),
            "data": linkData,
            "isNew": true
        });

        div.style.display = "none";

    });

    //add link params list
    for (var i = 0; i < linkParams.length; i++) {
        div.appendChild(linkParams[i].label);
        div.appendChild(linkParams[i].param);
    }
    div.appendChild(doneBtn);
    div.appendChild(closeBtn);

    div.style.display = "none";
    return div;
}

function onSubmitForm(paramValues, paramNames) {

    params = {};

    //set the default value if there is no input
    for (var i = 0; i < paramValues.length; i++) {
        var param = document.getElementById(paramNames[i]).value;
        if (param === "" || param === null)
            param = paramValues[i];
        params[paramNames[i]] = param;
    }
    return params;
}

function isLengthValid(lengthId) {
    length = document.getElementById(lengthId).value;

    if (length == null)
        return false;
    if (isNaN(length))
        return false;

    return true;
}

function isNameValid(nameId, inputList) {

    //also check that the name is not already in the input list

    name = document.getElementById(nameId).value;

    if (name === null || name === "")
        return false;

    for (i = 0; i < inputList.length; i++) {
        if (inputList[i].name.toLowerCase() === name.toLowerCase())
            return false;
    }
    return true;
}

function areNodeParamsValid(paramName, allValues) {

    nodeParam = document.getElementById(paramName);

    if (nodeParam.value === null || nodeParam.value === "") {
        return true;
    }

    for (i = 0; i < allValues.length; i++) {
        if (nodeParam.value.trim() === allValues[i])
            return true;
    }

    return false;

}

function getLayerName(marker) {

    var tooltip = marker["_tooltip"];
    if (tooltip == null || tooltip == undefined) {
        return "no_name";
    }
    x = tooltip["_content"];
    var doc = new DOMParser().parseFromString(x, "text/xml");
    var z = doc.documentElement.textContent;
    NodeName = z.replace(/\s/g, '');
    return NodeName;
}

function popupAlert(msg, mymap) {

    var div = document.createElement("div");
    div.setAttribute("class", "alert");
    var alertTxt = document.createElement("div");
    alertTxt.setAttribute("class", "alert-txt");
    var closeBtn = document.createElement("button");

    alertTxt.innerHTML = msg;
    closeBtn.innerHTML = "x";
    closeBtn.setAttribute("class", "mainmap-util-closebtn");

    closeBtn.addEventListener("click", () => div.remove());

    var alertBox = L.control({ position: 'bottomright' });

    alertBox.onAdd = function (map) {
        div.appendChild(alertTxt);
        div.appendChild(closeBtn);
        return div;
    };

    alertBox.addTo(mymap);
}

function connectLinkToNode(marker, connectedLinks, markerInitLatLng) {

    for (var i = 0; i < connectedLinks.length; i++) {
        var link = connectedLinks[i];
        // console.log("ll" + link.getLatLngs());
        // console.log("ma" + marker.getLatLng());

        var latLngStart = link.getLatLngs()[0];
        var latLngEnd = link.getLatLngs()[1];

        if (latLngEnd.lat == markerInitLatLng.lat && latLngEnd.lng == markerInitLatLng.lng) {

            link.setLatLngs([
                link.getLatLngs()[0],
                marker.getLatLng()
            ]);
        }
        else if (latLngStart.lat == markerInitLatLng.lat && latLngStart.lng == markerInitLatLng.lng) {

            link.setLatLngs([
                marker.getLatLng(),
                link.getLatLngs()[1]
            ]);
        }
    }
    return marker.getLatLng();
}

function getConnectedLinks(marker, featureGroup, connectedLinks) {

    featureGroup.eachLayer(layer => {
        if (layer instanceof L.Polyline) {
            if ( marker.getLatLng().lat == layer.getLatLngs()[0].lat && marker.getLatLng().lng == layer.getLatLngs()[0].lng) {
                connectedLinks.push(layer)
                //console.log("found");
            }
            if ( marker.getLatLng().lat == layer.getLatLngs()[1].lat && marker.getLatLng().lng == layer.getLatLngs()[1].lng) {
                connectedLinks.push(layer)
                //console.log("found");
            } 
        }
    });
}

function setLinkSrcAndDest(marker) {

    if (tempMarkerlist[0] == null) {
        // console.log('srccc   ');
        tempMarkerlist[0] = marker;
        return true;
    } else {
        if (tempMarkerlist[1] == null) {
            // console.log("desttt ");
            tempMarkerlist[1] = marker;
            return false;
        } else {
            // console.log("haha markers go recc recc");
            tempMarkerlist[0] = null;
            tempMarkerlist[1] = null;
            return setLinkSrcAndDest(marker);
        }
    }

}

function createLblTxtFromParamName(paramNames) {

    var lblTxts = [];
    for (var i = 0; i < paramNames.length; i++) {
        var txt = paramNames[i].replace(/_/g, " ");
        txt = txt.concat(": ");
        lblTxts.push(txt);
    }

    return lblTxts;
}

function createParamsInputs(paramNames, paramValues) {

    var paramLblTxts = createLblTxtFromParamName(paramNames);

    var paramElements = [];

    for (var i = 0; i < paramNames.length; i++) {
        var param = document.createElement("input");
        param.setAttribute("id", paramNames[i]);
        param.setAttribute("class", "mainmap-util-input");
        param.setAttribute("type", "text");
        param.placeholder = paramValues[i];

        var paramLbl = document.createElement("label");
        paramLbl.setAttribute("class", "mainmap-util-label");
        paramLbl.innerHTML = paramLblTxts[i];

        paramElements.push({
            "param": param,
            "label": paramLbl
        });
    }

    return paramElements;
}


// not using this now - codes's acting strange
function checkLinkValidity(featureGroup) {

    if (tempMarkerlist.length === 0) {
        return {
            "isValid": false,
            "msg": "No chosen nodes."
        };
    }
    else if (tempMarkerlist.length === 1) {
        return {
            "isValid": false,
            "msg": "Chose a destination node."
        };
    }

    if (tempMarkerlist[tempMarkerlist.length - 1] === tempMarkerlist[tempMarkerlist.length - 2]) {
        return {
            "isValid": false,
            "msg": "Chose a destination node."
        };
    }

    latlngs = [
        tempMarkerlist[tempMarkerlist.length - 1].getLatLng(),
        tempMarkerlist[tempMarkerlist.length - 2].getLatLng(),
    ];

    featureGroup.eachLayer(layer => {
        if (layer instanceof L.Polyline) {
            if (layer.getLatLngs().includes(latlngs[0]) && layer.getLatLngs().includes(latlngs[1])) {
                // console.log("rep", layer.getLatLngs(), latlngs[0], latlngs[1]);
                return {
                    "isValid": false,
                    "msg": "rep"
                };
            }
        }

    });

    return {
        "isValid": true,
        "msg": ""
    };

}

function addLayersToMap(featureGroup, mymap) {

    featureGroup.addTo(mymap);
}

function createCustomIcon(pathToIcon) {

    var myIcon = L.icon({
        iconUrl: pathToIcon,
        iconSize: [30, 30],
        iconAnchor: [20, 30]
    });

    return myIcon;
}

function restoreOldFeatureGroupEvents(markersGroup, linksGroup) {
    markersGroup.on("click", groupClick);
    linksGroup.on("click", links_click_event);
}

function closeAllPopups() {
    mymap.eachLayer(l => {
        // console.log("JOJO");
        if (l instanceof L.Popup) {
            // console.log("KONO DIO DA");
            mymap.removeLayer(l);
        }
    });
}

function fixMarkersData(markers) {
    markers.forEach(marker => {
        marker["location"] = marker["layer"].getLatLng();
        delete marker["layer"];
    });
}

function enableOldMarkerDragging(markersGroup, linksGroup, featureGroup) {

    markersGroup.eachLayer(marker => {
        marker.dragging.enable();
        var connectedLinks = [];
        var markerInitLatLng;

        marker.on("dragstart", e => {

            connectedLinks = []
            markerInitLatLng = e.target.getLatLng();
            getConnectedLinks(e.target, featureGroup, connectedLinks);
            getConnectedLinks(e.target, linksGroup, connectedLinks);
        });

        marker.on("drag", e => {
            markerInitLatLng = connectLinkToNode(e.target, connectedLinks, markerInitLatLng);
        })

        marker.on("dragend", e => {
            markerInitLatLng = connectLinkToNode(e.target, connectedLinks, markerInitLatLng);
        });
    });
}

function restoreDraggedLayersLocation(oldMarkers, oldLinks) {

    oldMarkers.forEach(m => {
        m.layer.setLatLng(m.location);
    });

    oldLinks.forEach(l => {
        l.layer.setLatLngs([
            l.startLoc,
            l.endLoc
        ]);
    });
}

function saveChangedOldMarkersToMarkers(oldMarkers, markers, deletedOldLayers) {
    oldMarkers.forEach(m => {
        if (!(m.location === m.layer.getLatLng()) && !deletedOldLayers.includes(m.name)) {
            m.location = m.layer.getLatLng();
            delete m["layer"];
            markers.push(m);
        }
    });
}

function saveChangedOldLinktoLink(oldLinks, links, deletedOldLayers) {
    oldLinks.forEach(l => {
        if ((!(l.startLoc === l.layer.getLatLngs()[0]) || !(l.endLoc === l.layer.getLatLngs()[1]))
            && !deletedOldLayers.includes(l.name)) {
            delete l["layer"];
            delete l["startLoc"];
            delete l["endLoc"];
            links.push(l);
        }
    });
}

function getMarkerNameByLatLng(latlng, featureGroup){
    var name;
    featureGroup.eachLayer( m => {
        if(m instanceof L.Marker){
            if(latlng === m.getLatLng()){
                name = getLayerName(m);
                return;
            }
        }
    });
    return name;
}