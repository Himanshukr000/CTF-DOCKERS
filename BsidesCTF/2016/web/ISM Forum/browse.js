var mainLoopId = setInterval(function(){
  var casper = require('casper').create();

  casper.start('http://localhost:5001/', function() {
    this.fill('form[action="/login"]', { user: 'admin', password: '0mHYA8ZI0GsiCmot' }, true);
  });

  casper.thenOpen('http://localhost:5001/c54c497c-38b6-408a-a597-5aa25bd0bd88', function() {
  });

  casper.run(function () {
    this.echo("Checked for images @ " + Date());
  });
}, 30000);
