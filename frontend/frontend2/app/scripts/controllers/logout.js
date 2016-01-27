'use strict';

/**
 * @ngdoc function
 * @name frontendApp.controller:LogoutCtrl
 * @description
 * # LogoutCtrl
 * Controller of the frontendApp
 */
angular.module('frontendApp')
  .controller('LogoutCtrl', function (djangoAuth, $state) {
    djangoAuth.logout().then(function() {
	    $state.go('login');
    });
  });
