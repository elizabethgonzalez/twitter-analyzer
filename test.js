document.addEventListener('DOMContentLoaded', function() {
  var exampleButton = document.getElementById('example');
  exampleButton.addEventListener('click', function() {
    chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
      var body = '{"text": "';
      document.querySelector('[aria-label="Tweet text"]').style.backgroundColor="red";
      body += ' 1testing"}'
      var req = new XMLHttpRequest();
      req.open('POST', 'http://127.0.0.1:5000/', true);
      req.setRequestHeader('Content-type', 'application/json');
      req.onreadystatechange = function() {
        if (req.readyState === 4) {
          document.getElementById('results').innerHTML = req.responseText;
        }
      };
      req.send(body);

    });
  }, false);
}, false);
