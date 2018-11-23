$(document).ready(function(){
    $('[data-toggle="tooltip"]').tooltip();
});

var ipaWords = document.querySelectorAll('.ipa-word a span');

ipaWords.forEach(function (ipaWord) {

    var sound = new Howl({
        src: ['/static/audios/' + ipaWord.textContent + '.mp3']
    });

    ipaWord.addEventListener('click', function (evt) {
        evt.preventDefault();
        sound.play();
    })
});