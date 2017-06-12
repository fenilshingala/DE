function coll(str) {
	$('#'+str).collapse('toggle');
}

function loadDoc(str) {
	switch(str){
		case "up":url = "updates";break;
		case "sub":url = "submissions";break;
	}
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
			document.getElementById("my_content").innerHTML = this.responseText;
		}
	};
	xhttp.open("GET", url, true);
	xhttp.send();
}