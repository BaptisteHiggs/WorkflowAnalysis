//Make the DIV element draggagle:

dragElement(document.getElementsByClassName("circle"));

function dragElement(circleClass) {
  
  alert("hey")
  var elmnt = circleClass[0];
  document.onmousedown = elementDecide;
  
  function elementDecide(e) {
    e = e || window.event;
	
	// Save current mouse location
	var currentMouseX = e.clientX;
	var currentMouseY = e.clientY;

    // Decide which circle is being selected
	for (i = 0; i < circleClass.length; i++) {
	  elmnt = circleClass[i]
	  var distanceX = (elmnt.getAttribute("cx") - (currentMouseX - 8))*(elmnt.getAttribute("cx") - (currentMouseX - 8))
	  var distanceY = (elmnt.getAttribute("cy") - (currentMouseY - 115))*(elmnt.getAttribute("cy") - (currentMouseY - 115))
	  console.log(i)
	  console.log("Distances: (" + distanceX + ", " + distanceY + ")")
	  if (distanceX + distanceY < 1650) {
		console.log(i + " is moving")
	    new dragMouseDown;
		break;
	  }
	}
  }

  function dragMouseDown(e) {
    e = e || window.event;
    // get the mouse cursor position at startup:
    document.onmouseup = closeDragElement;
    // call a function whenever the cursor moves:
    document.onmousemove = elementDrag;
  }

  function elementDrag(e) {
    e = e || window.event;
    // calculate the new cursor position:
    // set the element's new position:

    // elmnt.style.top = (elmnt.offsetTop - pos2) + "px";
    // elmnt.style.left = (elmnt.offsetLeft - pos1) + "px";
	
	elmnt.setAttribute("cx", e.clientX - 8)
	elmnt.setAttribute("cy", e.clientY - 115)
  }

  function closeDragElement(e) {
    e = e || window.event;
    // stop moving when mouse button is released:
	// window.alert((elmnt.attr(cx))
	var diameter = elmnt.getAttribute("r")*2;
	if (((e.clientX - 8) % diameter > 0) || ((e.clientY - 115) % diameter > 0)){
		// move to better spot
		elmnt.setAttribute("cx", (Math.round((e.clientX - 8)/diameter)*diameter));
		elmnt.setAttribute("cy", (Math.round((e.clientY - 115)/diameter)*diameter));
	}
    document.onmouseup = null;
    document.onmousemove = null;
  }
}