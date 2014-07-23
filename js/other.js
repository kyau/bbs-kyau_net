// jQuery : Toggle plugins tooltip when hovering over server
$(function() {
  $('div#server1').hover(function(){
    $('div#plugins').toggle();
  });
});

// jQuery : Keybindings
$(document).keyup(function(e){
  if(e.keyCode === 88) {
    window.location.replace("http://bbs.kyau.net/");
  }
});
