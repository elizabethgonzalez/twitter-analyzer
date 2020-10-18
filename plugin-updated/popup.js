document.addEventListener('DOMContentLoaded', function() {
  var exampleButton = document.getElementById('but1');
  exampleButton.addEventListener('click', function() {

    chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
      chrome.tabs.executeScript({
        file: 'parse.js'},
        function(results) {
          document.getElementsByClassName("report")[0].innerHTML = results;
        }
      );
    });
  }, false);
}, false);
