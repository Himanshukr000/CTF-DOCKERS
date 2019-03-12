'use strict';

angular.module('angl.user', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/user', {
    templateUrl: 'static/partials/user.html',
    controller: 'userCtrl'
  });
}])

.controller('userCtrl', ['$scope','$localStorage',function($scope,$localStorage) {
    $scope.logged_in = false;

    var getUser = function() {
        if ($localStorage.user === undefined) {
            $scope.logged_in = false;
            return;
        }
        $scope.user = $localStorage.user;
        $scope.logged_in = true;
    };

    $scope.$watch(function() {return $localStorage.user}, function() {
        getUser();
    });

    getUser();
}])

.directive('userstate', function() {
    return {
        scope: false,
        templateUrl: 'static/partials/userState.html'
    }
})

.factory('checkLogin', ['$localStorage', '$location', 'errorMessage', function($localStorage, $location, errorMessage) {
    return function() {
        if ($localStorage.user === undefined) {
            console.log($location.path());
            $location.path('/login');
            errorMessage.set('danger', 'You have to be logged in to do that');
        }
    }
}]);
