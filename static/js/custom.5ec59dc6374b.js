
window.onload = function() {


  $(function(){
    $("#modal_open,.modal_background").click(function () {
      $(".modal_top,.modal_bottom,.modal,.modal_background").fadeToggle( "fast" );
    });
  });

  $(function(){
    $("#hbg_open,.hbg_background").click(function () {
      $(".hbg_body").animate({width:'toggle'},350);
      $(".hbg_background").fadeToggle( "fast" );
    });
  });

  $(function(){
    $("#hl_open,.headlocal_background").click(function () {
      $(".headlocal_body").animate({height:'toggle'},150);
      $(".headlocal_background").fadeToggle( "fast" );
      $(".grobal_hamburger").fadeToggle( "fast" );
    });
  });


}
