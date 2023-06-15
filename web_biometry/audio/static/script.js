navigator.mediaDevices.getUserMedia({ audio: true})
        .then(stream => {
        const mediaRecorder = new MediaRecorder(stream);

        document.querySelector('#start').addEventListener('click', function(){
        mediaRecorder.start();
        });
    var audioChunks = [];
    mediaRecorder.addEventListener("dataavailable",function(event) {
        audioChunks.push(event.data);
    });

    mediaRecorder.addEventListener("stop", async function() {
        const audioBlob = new Blob(audioChunks, {
            type: 'audio/wav'
        });
        const audioUrl = URL.createObjectURL(audioBlob);
        var audio = document.createElement('audio');
        audio.src = audioUrl;
        audio.controls = true;
        audio.autoplay = true;
        document.querySelector('#audio').appendChild(audio);

        let fd = new FormData();
        fd.append('voice', audioBlob);
        let promise = await fetch('', {
            method: 'POST',
            body: fd});
        console.log(123);

        audioChunks = [];
});
    document.querySelector('#stop').addEventListener('click', function(){
        mediaRecorder.stop();
    });
});