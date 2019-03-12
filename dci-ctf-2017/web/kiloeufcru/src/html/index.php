<?php

require_once "config.php";

?>
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8"/>
    <title>Facts</title>
    <style>
     p {
         font-size: 40px;
     }
    </style>
  </head>
  <body>

    <img alt="" src="http://www.bikingbeatscancer.org/wp-content/uploads/2015/12/advice_didyouknow_en.png"/>

    <div>
      <a href="#" data-q="<?= sign("1") ?>">Fact 1</a>
      <a href="#" data-q="<?= sign("2") ?>">Fact 2</a>
      <a href="#" data-q="<?= sign("3") ?>">Fact 3</a>
      <a href="#" data-q="<?= sign("4") ?>">Fact 4</a>
      <a href="#" data-q="<?= sign("5") ?>">Fact 5</a>
    </div>

    <p id="quote"></p>

    <script>
     var quote = document.querySelector('#quote');

     function handleClick() {
         fetch('/api.php?q=' + escape(this.getAttribute('data-q'))).then(function(res) {
             return res.json();
         }).then(function(data) {
             quote.innerHTML = data['text'];
         });
     }

     document.querySelectorAll('a[data-q]').forEach(function(a) {
         a.onclick = handleClick;
     });


     fetch('/.git/refs/heads/master').then((x) => x.text()).then(function(version) {
         document.querySelector('#version').innerHTML += (`<small>Version ${version.slice(0,3).split('').join('.')}</small>`);
     });

    </script>

    <div id="version"></div>

  </body>
</html>
