showTime();
function showTime(){
myDate = new Date();
hours = myDate.getHours();
minutes = myDate.getMinutes();
seconds = myDate.getSeconds();
year = myDate.getFullYear();
month = myDate.getMonth() + 1;
day = myDate.getDate();

if (month < 10) month = "0" + month;
if (day < 10) day = "0" + day;
if (hours < 10) hours = "0" + hours;
if (minutes < 10) minutes = "0" + minutes;
if (seconds < 10) seconds = "0" + seconds;


$("#HoraActual").text(day + "/" + month + "/" + year + " " + hours+ ":" +minutes+ ":" +seconds);
setTimeout("showTime()", 1000);
}


