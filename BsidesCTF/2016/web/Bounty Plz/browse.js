var mainLoopId = setInterval(function(){
  var casper = require('casper').create();

  casper.start('http://localhost:10000/', function() {
    this.fill('form[action="/login"]', { user: 'admin', password: 'NBcO5i5xe0TjI8wq' }, true);
  });

  casper.thenOpen('http://localhost:10000/admin/report', function() {
  });

  casper.thenOpen('http://localhost:10000/admin/clear', function() {
  });

  casper.run(function () {
    this.echo("Checked for bugs @ " + Date());
  });
}, 20000);
