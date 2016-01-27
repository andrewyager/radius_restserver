'use strict';

describe('Controller: LogoutCtrl', function () {

  // load the controller's module
  beforeEach(module('frontendApp'));

  var LogoutCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    LogoutCtrl = $controller('LogoutCtrl', {
      $scope: scope
      // place here mocked dependencies
    });
  }));

  it('should indicate in scope logout has been completed', function () {
    expect(scope.loggedout).toBe(true);
  });
});
