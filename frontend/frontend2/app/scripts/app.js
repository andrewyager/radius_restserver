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
    'djangoRESTAuth',
    'amChartsDirective',
  ])
  .constant('API_BASE', 'http://192.168.99.100:82')
  .constant('API_EXTENSION', '/api/v1')
  .service('urls',function(API_BASE, API_EXTENSION) { this.API = API_BASE + API_EXTENSION;})
  .config(function ($stateProvider,$urlRouterProvider,jwtInterceptorProvider,$httpProvider) {
    $urlRouterProvider.otherwise('/');

    $httpProvider.interceptors.push('jwtInterceptor');

    $stateProvider

      .state('login', {
        url: '/login',
        templateUrl: 'views/login.html',
        resolve: {
            authenticated: function(djangoAuth, $state) {
                return djangoAuth.authenticationStatus(true)
                    .then(function() {
                        console.log('Already logged in!');
                        $state.go('main.dashboard');
                    }, function(reason) {
                        return;
                });
            },
        },
        controller: 'LoginCtrl'
      })
      .state('logout', {
        url: '/logout',
        controller: "LogoutCtrl",
      })

    // Main abstract state
    .state('main', {
        abstract: true,
        templateUrl: "views/main.html",
        resolve: {
            authenticated: function(djangoAuth) {
                return djangoAuth.authenticationStatus(true);
            },
        },
    })

  })
  .run(function($rootScope, djangoAuth, $state, API_BASE) {
        djangoAuth.initialize(API_BASE, false);

      djangoAuth.authenticationStatus(true)
        .then(function() {
          $rootScope.login_status = true;
        }, function(reason) {
          $rootScope.login_status = false;
        });

        $rootScope.$on('$stateChangeError', function (event, toState, toParams, fromState, fromParams, error) {
            if (error === 'UserNotLoggedIn') {
                event.preventDefault();
                console.log(error);
                $state.go('login');
            }
        });

  });
