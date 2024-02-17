function showMeasurement(){
	var $bust = mysql_real_escape_string($_POST['bust']);
	if ($bust != null) {
		document.getElementById(meas).innerHTML = "Your Bust is $bust <br>";
	}
}