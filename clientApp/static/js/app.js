
$( "#form_contact" ).submit(function( event ) {
  event.preventDefault();
  console.log( $( this ).serialize() );
});
