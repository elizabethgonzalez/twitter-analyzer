if(document.querySelector('[aria-label="Tweet text"]').style.backgroundColor == "lemonchiffon"){
  document.querySelector('[aria-label="Tweet text"]').style.backgroundColor = "";
  document.querySelector('[data-testid="tweet"]').style.backgroundColor = "";
}
else{
  document.querySelector('[aria-label="Tweet text"]').style.backgroundColor ="lemonchiffon";
  document.querySelector('[data-testid="tweet"]').style.backgroundColor = "LightGreen";
}
