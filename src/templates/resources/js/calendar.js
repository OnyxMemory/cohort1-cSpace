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
