let speechRec;

function setup() { 
  noCanvas();
  var foo = new p5.Speech(); // speech synthesis object
//  foo.speak('hi there'); // say something 
  speechRec = new p5.SpeechRec(gotSpeech);
  //let continuous = true;
  //let interimResults = true;
  //speechRec.start(continuous, interimResults);
  speechRec.start();
  
  function gotSpeech(speech) {
    
 //     foo.speak(speech.text);
    // if (speechRec.resultValue){
    //   createP(speechRec.resultString)
    // }
    console.log(speechRec);
    //print(speech.text);
	}
  
} 