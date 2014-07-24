// jQuery : Keybindings
$(document).keyup(function(e){
  if(e.keyCode === 69) {
    window.location.replace("http://bbs.kyau.net/?enter");
  } else if(e.keyCode === 72) {
    window.location.replace("http://kyau.net/wiki/Category:MajorMUD");
  } else if(e.keyCode === 65) {
    window.location.replace("http://bbs.kyau.net/?about");
  } else if(e.keyCode === 67) {
    window.location.replace("http://bbs.kyau.net/?cap");
  } else if(e.keyCode === 68) {
    window.location.replace("http://bbs.kyau.net/?files");
  } else if(e.keyCode === 83) {
    window.location.replace("http://bbs.kyau.net/?gossip");
  } else if(e.keyCode === 82) {
    window.location.replace("http://bbs.kyau.net/?rules");
  } else if(e.keyCode === 84) {
    window.location.replace("http://bbs.kyau.net/?top");
  } else if(e.keyCode === 71) {
    window.location.replace("http://bbs.kyau.net/?topgang");
  } else if(e.keyCode === 87) {
    window.location.replace("http://bbs.kyau.net/?who");
  } else if(e.keyCode === 49) {
    window.location.replace("http://bbs.kyau.net/?realm");
  } else if(e.keyCode === 191) {
    $('div#help').toggle();
  } else if(e.keyCode === 27) {
    $('div#help').css('display','none');
  }
});
