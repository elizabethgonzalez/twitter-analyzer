var body = '{"text": "';
var res;

body += document.querySelector('[aria-label="Tweet text"]').innerText;
body += ' "}';
var req = new XMLHttpRequest();
req.open('POST', 'http://127.0.0.1:5000/', true);
req.setRequestHeader('Content-type', 'application/json');
req.onreadystatechange = function() {
  if (req.readyState === 4) {
    res = req.responseText;
    var score = parseFloat(res);
    var color_opt;
    switch(true) {
      case score >= -1 && score < -.5:
        color_opt = "crimson";
        break;
      case score >= -.5 && score < -.2:
        color_opt = "tomato";
        break;
      case score >= -.2 && score < .3:
        color_opt = "lightcyan";
        break;
      case score >= .3 && score < .7:
        color_opt = "lightgreen";
        break;
      case score >= .7 && score <= 1:
        color_opt = "springgreen";
        break;
    }
    document.querySelector('[class="css-1dbjc4n r-1iusvr4 r-16y2uox r-1777fci r-glunga r-1bylmt5 r-13tjlyg r-7qyjyx r-1ftll1t"]').style.backgroundColor = color_opt;
    document.querySelector('[class="css-1dbjc4n r-1iusvr4 r-16y2uox r-1777fci r-glunga r-1bylmt5 r-13tjlyg r-7qyjyx r-1ftll1t"]').style.borderRadius = "10px";
    document.querySelector('[data-testid="toolBar"]').style.backgroundColor = color_opt;
    document.querySelector('[data-testid="toolBar"]').style.borderRadius = "10px";
  }
};
req.send(JSON.stringify(body));
if (res) res;
