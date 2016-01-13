'use strict';

/**
 * @ngdoc overview
 * @name frontend2App
 * @description
 * # frontend2App
 *
 * Main module of the application.
 */
angular
  .module('frontendApp', [
    'ngAnimate',
    'ngCookies',
    'ngMessages',
    'ngResource',
    'ui.router',
    'ngSanitize',
    'ngTouch',
    'angular-jwt',
    'angular-storage',
    'chart.js',
    'djangoRESTAuth'
  ])
  .constant('API', 'http://192.168.99.100:81/api/v1')
  .config(function ($stateProvider,$urlRouterProvider,jwtInterceptorProvider,$httpProvider) {
    $urlRouterProvider.otherwise('/');

    $httpProvider.interceptors.push('jwtInterceptor');

    $stateProvider
      .state('home', {
        url: '/',
        templateUrl: 'views/main.html',
        controller: 'MainCtrl',
        controllerAs: 'main'
      })
      .state('login', {
        url: '/login',
        templateUrl: 'views/login.html',
        controller: 'LoginCtrl'
      })
      .state('logout', {
        controller: "LogoutCtrl",
      })

  })
  .run(function($rootScope, djangoAuth) {
      djangoAuth.initialize('//192.168.99.100:81', false);
  });
