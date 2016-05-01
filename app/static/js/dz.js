function allowDrop(event) {
    event.preventDefault();
}

function drop(event) {
    event.preventDefault();
    var $target = $(event.target);
    // console.log($target)
    var method = 'post';
    var route = '/profile';
    $.ajax({
    	'url' : route,
    	'method': 'POST',
    	'datatype' : 'json',
    	'data': JSON.stringify({picture: $target}),
    }).done(function(response) {
    	console.log(response);
    })
    // console.log("It's been dropped!")
    // var data = event.dataTransfer.getData("Text");
    // event.target.appendChild(document.getElementById(data));
    // document.getElementById("demo").innerHTML = "The p element was dropped";
}