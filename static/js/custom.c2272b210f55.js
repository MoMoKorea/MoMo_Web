
window.onload = function {
  $(function(){
    $("#modal_open,#modal_close,.modal_background").click(function () {
      $(".modal_top,.modal_background").fadeToggle( "fast" );
    });
  });
}
