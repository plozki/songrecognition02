
function recorder(){
    const uploadURL = "/home"

    let constraintObj = {
        audio: true,
        video: false
    };


    //handle older browsers that might implement getUserMedia in some way
    if (navigator.mediaDevices === undefined) {
        navigator.mediaDevices = {};
        navigator.mediaDevices.getUserMedia = function(constraintObj) {
            let getUserMedia = navigator.webkitGetUserMedia || navigator.mozGetUserMedia;
            if (!getUserMedia) {
                return Promise.reject(new Error('getUserMedia is not implemented in this browser'));
            }
            return new Promise(function(resolve, reject) {
                getUserMedia.call(navigator, constraintObj, resolve, reject);
            });
        }
    }else{
        navigator.mediaDevices.enumerateDevices()
        .then(devices => {
            devices.forEach(device=>{
                console.log(device.kind.toUpperCase(), device.label);
                //, device.deviceId
            })
        })
        .catch(err=>{
            console.log(err.name, err.message);
        })
    }

    navigator.mediaDevices.getUserMedia(constraintObj)
    .then(function(mediaStreamObj) {

        let start = document.getElementById('btnStart');
        let stop = document.getElementById('btnStop');
        let audioSave = document.getElementById('audio2');
        let mediaRecorder = new MediaRecorder(mediaStreamObj);
        let chunks = [];

        start.addEventListener('click', (ev)=>{
            mediaRecorder.start();
            console.log(mediaRecorder.state);
        });
        stop.addEventListener('click', (ev)=>{
            mediaRecorder.stop();
            console.log(mediaRecorder.state);
        });
        mediaRecorder.ondataavailable = function(ev) {
            chunks.push(ev.data);
        }
        mediaRecorder.onstop = (ev)=>{
            let blob = new Blob(chunks, { 'type' : 'audio/wav' });
            console.log("we are live");
            //sending the blob to the server
            const xhr = new XMLHttpRequest()
            const data = new FormData()
            data.append('audio_file', blob, 'my blob');


            chunks = [];
            let audioURL = window.URL.createObjectURL(blob);
            audioSave.src = audioURL;
            // data.append('audio_src', audioURL);
            xhr.open('POST', uploadURL)
            xhr.send(data)

            // var a = document.createElement('a');
            // a.href = "/result";
            // document.body.appendChild(a);






        }
    }).catch(function(err) {
        console.log(err.name, err.message);
    });


    /*********************************
    getUserMedia returns a Promise
    resolve - returns a MediaStream Object
    reject returns one of the following errors
    AbortError - generic unknown cause
    NotAllowedError (SecurityError) - user rejected permissions
    NotFoundError - missing media track
    NotReadableError - user permissions given but hardware/OS error
    OverconstrainedError - constraint video settings preventing
    TypeError - audio: false, video: false
    *********************************/


}
