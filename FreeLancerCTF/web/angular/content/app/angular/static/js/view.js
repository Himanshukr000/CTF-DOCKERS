'use strict';

angular.module('angl.view', ['ngRoute', 'angl.error'])
.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/view', {
    templateUrl: 'static/partials/view.html',
    controller: 'viewCtrl'
  })
  .when('/view/:userId', {
    templateUrl: 'static/partials/view.html',
    controller: 'viewCtrl'
  });
}])

.controller('viewCtrl', ['$http','$scope','$location','$routeParams', 'errorMessage', 'checkLogin', function($http,$scope, $location, $routeParams, errorMessage, checkLogin) {
    $scope.search = function(query) {
        if (query != null) {
            $location.path('/view/'+query);
        } else {
            $location.path('/view');
        }
    };

    var viewall = function() {
        $http({
            method:'GET',
            url:'/user/all',
            headers: {
               'Content-Type': 'application/json;charset=utf-8'
            },
        })
        .then(function(resp){
            $scope.userlist = resp.data;
            errorMessage.set('success', resp.data.message);
        },function(error){
            console.log(error);
            errorMessage.set('danger', error.data.message);
        });
    }

    var viewone = function(userId) {
        $http({
            method:'GET',
            url:'/user/' + userId,
            headers: {
               'Content-Type': 'application/json;charset=utf-8'
            },
        })
        .then(function(resp){
            $scope.userlist = [resp.data.user];
            errorMessage.set('success', resp.data.message);
        },function(error){
            console.log(error);
            errorMessage.set('danger', error.data.message);
        });
    }

    checkLogin();
    if (Object.keys($routeParams).length == 0) {
        viewall();
    } else {
        viewone($routeParams.userId);
        $scope.query = parseInt($routeParams.userId);
    }
}]);
