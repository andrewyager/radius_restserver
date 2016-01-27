'use strict';

describe('Check that you can log out when the backend is functioning', function () {

  // load the controller's module
  beforeEach(module('frontendApp'));

  var LogoutCtrl,
    scope,
    $httpBackend,
    $state;

  beforeEach(module("templates")); 

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope, $q, $injector) {
      scope = $rootScope.$new();
      $state = $injector.get('$state');
      spyOn($state, 'go');
      $httpBackend = $injector.get('$httpBackend');
      $httpBackend.when("GET", "http://192.168.99.100:82/rest-auth/user/")
        .respond(200, "");
      $httpBackend.when("POST", "http://192.168.99.100:82/rest-auth/logout/")
        .respond(200, "");
      LogoutCtrl = $controller('LogoutCtrl', {
      $scope: scope
        // place here mocked dependencies
    });
  }));

  it('expect that we have called the login state', function() {
    scope.$digest();
    $httpBackend.flush();
    expect($state.go).toHaveBeenCalledWith('login');
  });
});

describe('Check that you can log out when the backend is partially functioning', function () {

  // load the controller's module
  beforeEach(module('frontendApp'));

  var LogoutCtrl,
    scope,
    $httpBackend,
    $state;

  beforeEach(module("templates")); 

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope, $q, $injector) {
      scope = $rootScope.$new();
      $state = $injector.get('$state');
      spyOn($state, 'go');
      $httpBackend = $injector.get('$httpBackend');
      $httpBackend.when("GET", "http://192.168.99.100:82/rest-auth/user/")
        .respond(403, "");
      $httpBackend.when("POST", "http://192.168.99.100:82/rest-auth/logout/")
        .respond(200, "");
      LogoutCtrl = $controller('LogoutCtrl', {
      $scope: scope
        // place here mocked dependencies
    });
  }));

  it('expect that we have called the login state', function() {
    scope.$digest();
    $httpBackend.flush();
    expect($state.go).toHaveBeenCalledWith('login');
  });
});

describe('Check that you can log out when the backend is not functioning', function () {

  // load the controller's module
  beforeEach(module('frontendApp'));

  var LogoutCtrl,
    scope,
    $httpBackend,
    $state;

  beforeEach(module("templates")); 

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope, $q, $injector) {
      scope = $rootScope.$new();
      $state = $injector.get('$state');
      spyOn($state, 'go');
      $httpBackend = $injector.get('$httpBackend');
      $httpBackend.when("GET", "http://192.168.99.100:82/rest-auth/user/")
        .respond(500, "");
      $httpBackend.when("POST", "http://192.168.99.100:82/rest-auth/logout/")
        .respond(500, "");
      LogoutCtrl = $controller('LogoutCtrl', {
      $scope: scope
        // place here mocked dependencies
    });
  }));

  it('expect that we have called the login state', function() {
    scope.$digest();
    $httpBackend.flush();
    expect($state.go).toHaveBeenCalledWith('login');
  });
});

