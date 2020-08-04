function playAudio(){
    var audio = "/poewit_web/static/src/img/PoEWitPronunciation.m4a"
    var sound = new Audio(audio);
    sound.play();
}

(function (){
    var anchor=document.querySelectorAll("[data-mimetype='application/pdf']");
    for(var i = 0; i < anchor.length; i++){ 
        anchor[i].innerHTML="Download PDF";
    };
})();