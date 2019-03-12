'use strict';

angular.module('angl.create', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/create', {
    templateUrl: 'static/partials/create.html',
    controller: 'createCtrl'
  });
}])

.controller('createCtrl', ['$http','$scope','errorMessage', function($http,$scope, errorMessage) {
    $scope.test = "lmao"
    $scope.create = function(user) {
        $http({
            method:'POST',
            url:'/user/create',
            headers: {
               'Content-Type': 'application/json;charset=utf-8'
            },
            data:user
        })
        .then(function(resp){
            console.log(resp);
            errorMessage.set('success', resp.data.message);
        },function(error){
            console.log(error);
            errorMessage.set('danger', error.data.message);
        });
    }
}]);
