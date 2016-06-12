document.getElementById("upload_image").onchange = function(e) {
    var longitude, dateStamp, latitude, latRef, longRef;

    EXIF.getData(e.target.files[0], function() {
        var method = 'post';
        var route = '/profile';
        var longitude = EXIF.getTag(this, "GPSLongitude"),
        dateStamp = EXIF.getTag(this, "GPSDateStamp"),
        latitude = EXIF.getTag(this, "GPSLatitude"),
        latRef = EXIF.getTag(this, "GPSLatitudeRef"),
        longRef = EXIF.getTag(this, "GPSLongitudeRef");
        
        $.ajax({
            'url' : route,
            'method': 'POST',
            'datatype' : 'json',
            'data': JSON.stringify({
                "dateStamp": dateStamp,
                "longitude": longitude,
                "latitude" : latitude,
                "latRef"   : latRef,
                "longRef"  : longRef
                }),
            }).done(function(response) {
    	        console.log(response);
            }).fail(function(response) {
                console.log("you did a bad thing");    
            })
        });
}




