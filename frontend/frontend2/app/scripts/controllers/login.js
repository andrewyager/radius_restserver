'use strict';

/**
 * @ngdoc function
 * @name frontendApp.controller:LoginCtrl
 * @description
 * # LoginCtrl
 * Controller of the frontendApp
 */
angular.module('frontendApp')
  .controller('LoginCtrl', function ($scope, $rootScope, $http, store, $state, API, djangoAuth) {
    $scope.model = {'username':'','password':''};
    $scope.complete = false;
    $scope.login = function(formData){
      $scope.errors = [];
      if(!formData.$invalid){
        djangoAuth.login($scope.model.username, $scope.model.password)
        .then(function(data){
            // success case
            $state.go('home');
        },function(data){
	      $scope.errors = data;
        });
      }
    }
  });

