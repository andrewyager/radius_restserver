'use strict';

/**
 * @ngdoc function
 * @name frontendApp.controller:LoginCtrl
 * @description
 * # LoginCtrl
 * Controller of the frontendApp
 */
angular.module('frontendApp')
  .controller('LoginCtrl', function ($scope, $rootScope, $http, store, $state, API) {
	$scope.user = {};
	$scope.login = function() {
	    $http({
	      url: API+'/token/',
	      method: 'POST',
	      data: $scope.user
	    }).then(function(response) {
	      // jscs:disable requireCamelCaseOrUpperCaseIdentifiers
	      store.set('jwt', response.data.token);
	      $rootScope.user = $scope.user.username;
	      $state.go('about');
	    }, function(error) {
	      window.alert(error.data);
	    });
	  };
  });