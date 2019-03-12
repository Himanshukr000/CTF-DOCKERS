'use strict';

angular.module('angl', [
  'ngRoute',
  'angl.home',
  'angl.login',
  'angl.logout',
  'angl.create',
  'angl.edit',
  'angl.user',
  'angl.view',
  'angl.error',
  'angl.flag',
  'ngStorage'
])

.config(['$locationProvider', '$routeProvider', function($locationProvider, $routeProvider) {
    $locationProvider.hashPrefix('!');
//  $routeProvider.otherwise({redirectTo: '/home'});
}]);
