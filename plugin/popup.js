document.addEventListener('DOMContentLoaded', function() {
  var exampleButton = document.getElementById('example');
  exampleButton.addEventListener('click', function() {

    chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
      chrome.tabs.executeScript(
        tabs[0].id, {code: 'if(document.body.style.backgroundColor == "red"){document.body.style.backgroundColor = "";}else{document.body.style.backgroundColor ="red";}'}
      );
    });
  }, false);
}, false);
