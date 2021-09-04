function checkWidgetToDisplay()
{
    alert("Now slide down!");
    var meteo = document.getElementById("option1");
    var bourse = document.getElementById("option3");
    var trex = document.getElementById("option4");
    var restaurant = document.getElementById("option5");
    var foot = document.getElementById("option6");
    var reddit = document.getElementById("option8");
    var calculator = document.getElementById("option9");
//    var youtube = document.getElementById("option10");

    //METEO WIDGET
    if (meteo.checked == true)
	visibilite("id_div_1");
    else
	unvisibilite("id_div_1");
    //MAPS WIDGET
    //BOURSE WIDGET
    if (bourse.checked == true)
	visibilite("id_div_3");
    else
	unvisibilite("id_div_3");
    //YOUTUBE WIDGET
    if (trex.checked == true)
	visibilite("id_div_4");
    else
	unvisibilite("id_div_4");
    //RESTAURANT WIDGET
    if (restaurant.checked == true)
	visibilite("id_div_5");
    else
	unvisibilite("id_div_5");
    //FOOTBALL WIDGET
    if (foot.checked == true)
	visibilite("id_div_6");
    else
	unvisibilite("id_div_6");
    //FOOTBALL WIDGET
    //REDDIT WIDGET
    if (reddit.checked == true)
	visibilite("id_div_8");
    else
    unvisibilite("id_div_8");
    if (calculator.checked == true)
	visibilite("id_div_9");
    else
    unvisibilite("id_div_9");
//    if (youtube.checked == true)
//	visibilite("id_div_10");
//    else
//    unvisibilite("id_div_10");
}

function visibilite(thingId)
{
    var targetElement = document.getElementById(thingId);
    targetElement.style.display = "";
}

function unvisibilite(thingId) {
    var targetElement = document.getElementById(thingId);
    targetElement.style.display = "none";
}

function sendConfirmgoogle(google)
{
    var profile = google.getBasicProfile();
    var mail = profile.getEmail();
    alert(mail);
}

function sendConfirm()
{
    var dest = document.getElementById("mail").value;
    alert(dest);
}
