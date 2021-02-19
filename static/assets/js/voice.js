let isRecording = false;
let recognition;

window.onload = () => {
  window.SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
  recognition = new SpeechRecognition();
  recognition.continuous = true;
  document.getElementById('mic').addEventListener('click', onClickMic);
  recognition.onresult = onSpeech;
}

function onClickMic(event) {
  event.target.classList.toggle('fa-microphone');
  event.target.classList.toggle('fa-microphone-slash');
  
  if (isRecording) {
    recognition.stop();
  } else {
    recognition.start();
  }
  
  isRecording = !isRecording;
}

function onSpeech(event) {
  
  const lastElIndex = event.results.length - 1;
  const text = event.results[lastElIndex][0].transcript;
  // document.getElementById('text').value = text;
  document.getElementById('text').innerText = text;

}