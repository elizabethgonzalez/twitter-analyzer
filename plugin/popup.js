document.addEventListener('DOMContentLoaded', function() {
  var exampleButton = document.getElementById('example');
  exampleButton.addEventListener('click', function() {

    chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
      chrome.tabs.executeScript({
        file: 'toggle.js'}
      );
    });
  }, false);
}, false);
