document.addEventListener('DOMContentLoaded', function() {
    selectStartingMonthTab();

    var classname = document.getElementsByClassName("calendar-booking-empty");
    for (var i = 0; i < classname.length; i++) {
        classname[i].addEventListener('click', showBookingAlert, false);
    }
});


function selectStartingMonthTab() {
    let year=(new Date()).getFullYear();
    let month=(new Date()).getMonth()+1;
    showmonth(year+"-"+month);
}

function showmonth(month) {
  // Hide month info for months not displayed
  var months = document.getElementsByClassName('booking-container'),
      i = months.length;
  while(i--) {
    months[i].style.visibility = "hidden";
    months[i].style.display = "none";
  }

  // Set default (not selected) background to month tabs
  var months = document.getElementsByClassName('month-tab-info'),
      i = months.length;
  while(i--) {
    months[i].style.backgroundColor = "lightgray";
  }

  // Show month data of selected month
  var elem = document.getElementById(month);
  elem.style.visibility = "visible";
  elem.style.display = "grid";

  // Set lightgreen to displayed month
  var elem = document.getElementById("month-tab-"+month);
  elem.style.backgroundColor = "gray";
}

function showTooltip(client) {
      var ev = window.event;
      var posX = ev.clientX;
      var posY = ev.clientY;
      var element = document.elementFromPoint(posX, posY);
      var elem = document.getElementById("tooltip");
      elem.style.top=element.offsetTop+5+'px';
      elem.style.left=posX+10+'px';
      elem.style.visibility = "visible";
      // elem.style.hover='pointer';
      elem.innerHTML="<span class='tooltip-client'>"+client+"</span>";
}

function closeToolTip() {
      var elem = document.getElementById("tooltip");
      elem.style.visibility = "hidden";
}

function showBookingAlert() {
      var ev = window.event;
      var posX = ev.clientX;
      var posY = ev.clientY;
      var element = document.elementFromPoint(posX, posY);
      var elem = document.getElementById("tooltip");

      elem.style.top=element.offsetTop+5+'px';
      elem.style.left=posX+10+'px';
      elem.style.height='100px';
      elem.style.visibility = "visible";

      // elem.style.hover='pointer';


      elem.innerHTML="<div><p class='tooltip-bookit'>Book this room !</p><p class='tooltip-construction'>Under construction.</p></div>";
}
