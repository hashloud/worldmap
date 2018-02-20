function makeRequest( url ){
    $.ajax({
        url: url,
        dataType: 'json',
        success: function(persons){
            $("div.person").removeClass("person");
            for (var i = 0, len = persons.person.length; i < len; i++) {
                var person = persons.person[i];
                var x = person.point.x;
                var y = person.point.y;
                var row = $("div.row")[ y ];
                var field = $(row.children[ x ]);
                field.addClass( "person" )
            }
        },
        error: function(err){
            //alert( "Error: " + err );
        }
    });
}
