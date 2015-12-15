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
    'chart.js'
  ])
  .constant('API', 'http://192.168.99.100:81/api/v1')
  .config(function ($stateProvider,$urlRouterProvider,jwtInterceptorProvider,$httpProvider) {
    $urlRouterProvider.otherwise('/');

    jwtInterceptorProvider.tokenGetter = function(store) {
      return store.get('jwt');
    };

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
        url: '/logout',
        controller: function(store, $state) {
          store.remove('jwt');
          $state.go('login');
        }
      });

  })
  .run(function($rootScope, $state, store, jwtHelper) {
    $rootScope.isLoggedIn = function() {
      if (!store.get('jwt') || jwtHelper.isTokenExpired(store.get('jwt'))) {
        return false;
      }
      return true;
    };
    $rootScope.$on('$stateChangeStart', function(e, to) {
      if (to.data && to.data.requiresLogin) {
        if (!store.get('jwt') || jwtHelper.isTokenExpired(store.get('jwt'))) {
          e.preventDefault();
          $state.go('login');
        }
      }
    });
  });
