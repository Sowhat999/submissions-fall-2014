var mouseX, mouseY;
var thluffyX, thluffyY;
thluffyX=Math.random() * (window.innerWidth-500);
thluffyY=Math.random()* (window.innerHeight-220);
var thluffy = document.getElementById("thluffy");
console.log(thluffyX)
document.getElementById("thluffy").style.left=thluffyX+"px";
document.getElementById("thluffy").style.top=thluffyY+"px";
var playing= true;
var play = function(e) {
		var audio =document.getElementById('javert_loud');
		var distance =Math.sqrt(Math.pow(mouseX-(thluffyX+250),2)+Math.pow(mouseY-(thluffyY+110),2));
		if (distance >500)
			audio.volume=.05;
		else if (distance >400)
			audio.volume=.2;
		else if (distance >300)
			audio.volume=.5;
		else if (distance >200)
			audio.volume=.8;
		else
			audio.volume=1;
		audio.play();
		//console.log(distance);
		if (playing){
			myevent = setTimeout(play,300);
		}
	}

window.addEventListener('mousemove', function(e) {
		mouseX = e.pageX;
		mouseY = e.pageY;
});



var done=function(){
	playing=false;
	var audio =document.getElementById('donotforget');
	audio.play();
	thluffy.style.opacity=1;


	
}

thluffy.addEventListener('click',done);
var myevent;
myevent = setTimeout(play,200);