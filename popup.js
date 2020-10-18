document.addEventListener('DOMContentLoaded', function() {
  var exampleButton = document.getElementById('example');
  exampleButton.addEventListener('click', function() {

    chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
      chrome.tabs.executeScript({
        file: 'parse.js'},
        function(results) {
          if (results)
            {document.getElementById('results').innerHTML = results;}
          else {
              document.getElementById('results').innerHTML = "something happened";
            }

        }
      );
    });
  }, false);
}, false);
