

$( "#form" ).submit(function( event ) {
   event.preventDefault();
  console.log("form submitted!")  // sanity check
  console.log( $( "#form" ).serialize() );
  create();
  
});




function create() {
    console.log("create  is working!") // sanity check

    //TODO: Get data from form 
    var d = "first_name='prueba name'";
   
    $.ajax([{
    	url : "create/",
    	type: "POST",
    	data: { param : d },

    	success : function(json){
    		console.log('consulta ')
    	},
    	error : function(xhr, errmsg, err){
    		console.log (errmsg);
    		console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
    	}
    }]);
};

