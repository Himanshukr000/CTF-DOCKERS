'use strict';

angular.module('angl.flag', ['ngRoute', 'angl.error'])
.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/flag', {
    templateUrl: 'static/partials/flag.html',
    controller: 'flagCtrl'
  })
}])

.controller('flagCtrl', ['$http', 'errorMessage', function($http, errorMessage) {
    $http({
        method:'GET',
        url:'/flag',
        headers: {
            'Content-Type': 'application/json;charset=utf-8'
        },
    })
    .then(function(resp){
        errorMessage.set('success', resp.data.message);
    },function(error){
        console.log(error);
        errorMessage.set('danger', error.data.message);
    });
}]);
