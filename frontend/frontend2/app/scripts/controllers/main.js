'use strict';

/**
 * @ngdoc function
 * @name frontend2App.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the frontend2App
 */
angular.module('frontendApp')
  .controller('MainCtrl', function (djangoAuth, $scope) {
      djangoAuth.authenticationStatus(true)
        .then(function() {
          $scope.login_status = true;
        }, function(reason) {
          $scope.login_status = false;
        });

    this.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];
  });
