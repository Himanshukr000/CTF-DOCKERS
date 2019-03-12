'use strict';

angular.module('angl.login', ['ngRoute'])
.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/login', {
    templateUrl: 'static/partials/login.html',
    controller: 'loginCtrl'
  });
}])

.controller('loginCtrl', ['$http','$scope','$localStorage','$location', 'errorMessage', 'checkLogin', function($http,$scope,$localStorage, $location, errorMessage, checkLogin) {
    $scope.test = "lmao";
    $scope.login = function(user) {
        $http({
            method:'POST',
            url:'/user/login',
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
    var checkLogin = function() {
        if ($localStorage.user !== undefined) {
            $location.path('/logout');
        }
    };
    checkLogin();
}]);

angular.module('angl.logout', ['ngRoute'])
.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/logout', {
    templateUrl: 'static/partials/logout.html',
    controller: 'logoutCtrl'
  });
}])

.controller('logoutCtrl', ['$http','$scope','$localStorage','$location', 'errorMessage', 'checkLogin', function($http,$scope,$localStorage, $location, errorMessage, checkLogin) {
    $scope.logout = function(user) {
        $http({
            method:'GET',
            url:'/user/logout',
        })
        .then(function(resp){
            $localStorage.user = undefined;
            errorMessage.set('success', resp.data.message);
        },function(error){
            console.log(error);
            errorMessage.set('danger', error.data.message);
        });
    }
    checkLogin();
}]);
