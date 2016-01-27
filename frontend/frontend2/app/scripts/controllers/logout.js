'use strict';

/**
 * @ngdoc function
 * @name frontendApp.controller:LogoutCtrl
 * @description
 * # LogoutCtrl
 * Controller of the frontendApp
 */
angular.module('frontendApp')
  .controller('LogoutCtrl', function (djangoAuth, $state, $scope) {
    djangoAuth.logout();
    $scope.loggedout=true;
    $state.go('login');
  });
