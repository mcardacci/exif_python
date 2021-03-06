document.getElementById("upload").onchange = function(e) {
	e.preventDefault();
    EXIF.getData(e.target.files[0], function() {
        var method = 'post';
        var route = '/store';
        var longitude = EXIF.getTag(this, "GPSLongitude"),
        dateStamp = EXIF.getTag(this, "GPSDateStamp"),
        latitude = EXIF.getTag(this, "GPSLatitude"),
        latRef = EXIF.getTag(this, "GPSLatitudeRef"),
        longRef = EXIF.getTag(this, "GPSLongitudeRef");
        
        $.ajax({
            'url' : route,
            'method': 'POST',
            'datatype' : 'json',
            'data':{
                "dateStamp": dateStamp,
                "longitude": String(longitude),
                "latitude" : String(latitude),
                "latRef"   : latRef,
                "longRef"  : longRef
                },
        }).done(function(response) {
            console.log('upload successful');
        }).fail(function(response) {
            console.log("you did a bad thing");    
        })
    });
}

