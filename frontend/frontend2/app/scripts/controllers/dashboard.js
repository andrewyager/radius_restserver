'use strict';

/**
 * @ngdoc function
 * @name frontend2App.controller:DashBoardCtrl
 * @description
 * # MainCtrl
 * Controller of the frontend2App
 */
angular.module('frontendApp')
  .config(function($stateProvider) {
      $stateProvider.state('main.dashboard', {
        url: '/',
        templateUrl: 'views/dashboard.html',
        controller: 'DashBoardCtrl',
        controllerAs: 'main'
      });
  })
  .controller('DashBoardCtrl', function () {

    this.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];
  });
