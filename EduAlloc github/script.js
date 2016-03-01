$(document).ready(function () {

    $('h3.accordion').click(function () {
        $(this).next().slideToggle();
    }).next().hide();

    var photos = new Array();
    photos[0] = "sadpic1.jpg";
    photos[1] = "sadpic2.jpg";
    photos[2] = "sadpic3.jpg";
	photos[3] = "sadpic4.jpg";
	photos[4] = "sadpic5.jpg";
    var i = 0;
    

  

  
    //the current photos are for test purposes only, once the organization gives me photos for them I will pretty up this div and whatnot
        window.setInterval(function () {

            if (i > photos.length - 1) {
                i = 0;
            }
        
		$('div.pictures').css('background-color', 'black');
        $('div.pictures').css('background-image', 'url(' + photos[i] + ')');
        i++;

    }, 5000);
        

    





});


