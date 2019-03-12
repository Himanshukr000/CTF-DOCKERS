'use strict';

angular.module('angl.edit', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/edit', {
    templateUrl: 'static/partials/edit.html',
    controller: 'editCtrl'
  });
}])

.controller('editCtrl', ['$http','$scope','$location','$localStorage','errorMessage', 'checkLogin', function($http,$scope,$location,$localStorage,errorMessage, checkLogin) {
    $scope.edit = function(user) {
        $http({
            method:'POST',
            url:'/user/edit',
            headers: {
               'Content-Type': 'application/json;charset=utf-8'
            },
            data:user
        })
        .then(function(resp){
            $localStorage.user = resp.data.user;
            errorMessage.set('success', resp.data.message);
        },function(error){
            console.log(error);
            errorMessage.set('danger', error.data.message);
        });
    }
    checkLogin();
    $scope.user = angular.copy($localStorage.user);
    delete $scope.user.password;
    delete $scope.user.role;
    delete $scope.user.id;
}]);
