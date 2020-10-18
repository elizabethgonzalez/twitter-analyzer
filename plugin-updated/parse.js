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
  }
};
req.send(JSON.stringify(body));
if (res) res;
