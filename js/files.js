// jQuery : Keybindings
$(document).keyup(function(e){
  if(e.keyCode === 88) {
    window.location.replace("http://bbs.kyau.net/");
  } else if(e.keyCode === 49) {
    window.location.replace("http://bbs.kyau.net/?megamud");
  } else if(e.keyCode === 50) {
    window.location.replace("http://bbs.kyau.net/?majormud");
  } else if(e.keyCode === 51) {
    window.location.replace("http://bbs.kyau.net/?wgserv");
  }
});
