'use strict';

angular.module('angl.error', ['ngRoute'])

.controller('errorCtrl', ['$scope', 'errorMessage', function($scope, errorMessage) {
    var updateScope = function() {
        $scope.err = errorMessage.data.err;
        $scope.message = errorMessage.data.message;
    };
    errorMessage.setObserver(updateScope);
}])

.factory('errorMessage', function() {
  var data = {err: '', message:''};
  var observerList = [];

  var set = function(err, msg) {
      data.err = err;
      data.message = msg;
      wakeObserver();
  };

  var setObserver = function(callback) {
      observerList.push(callback);
  };

  var wakeObserver = function() {
      angular.forEach(observerList, function(cb) {
          cb();
      });
  };

  return {
      set: set,
      setObserver: setObserver,
      data:data
  }
})

.directive('errorstate', function() {
    return {
        scope: false,
        templateUrl: 'static/partials/error.html'
    }
});

