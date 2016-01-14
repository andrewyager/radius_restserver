'use strict';

/**
 * @ngdoc function
 * @name frontend2App.controller:AboutCtrl
 * @description
 * # AboutCtrl
 * Controller of the frontend2App
 */
angular.module('frontendApp')
  .config(function($stateProvider) {
	  $stateProvider.state('main.stats', {
	    url: '/stats',
	    templateUrl: 'views/stats.html',
	    controller: 'StatsCtrl',
	    controllerAs: 'stats',
	  });
  })
  .controller('StatsCtrl', function (urls, $http, $scope) {
  	$scope.response = null;
  	$scope.data = [];
  	$scope.series = [];
  	$scope.labels= [];
  	$scope.tdata = 0;
    $http({
        url: urls.API +'/userdata.json/',
        method: 'GET'
    }).then(function(datapoints) {
        $scope.labels = [];
        $scope.series = ['Data Up', 'Data Down', 'Total Data'];
        var dataup = [];
        var datadown = [];
        var totaldata = [];
        var days = {};
        for (var i = 0; i < datapoints.data.length; i++) {
            if (!days[datapoints.data[i].date]) {
                days[datapoints.data[i].date] = {
                    date: datapoints.data[i].date,
                    datain: 0,
                    dataout: 0,
                    totaldata: 0
                };
            }
            days[datapoints.data[i].date].datain += Math.round(datapoints.data[i].datain/1024/1024,2);
            days[datapoints.data[i].date].dataout += Math.round(datapoints.data[i].dataout/1024/1024,2);
            days[datapoints.data[i].date].totaldata += Math.round(datapoints.data[i].totaldata/1024/1024,2);
        }
        var tdata = 0;
        for (var key in days) {
            $scope.labels.push(days[key].date);
            dataup.push(days[key].datain);
            datadown.push(days[key].dataout);
            totaldata.push(days[key].totaldata);
            tdata += days[key].totaldata;
        }
        $scope.days = days;
        $scope.data.push(
            dataup,
            datadown,
            totaldata
        );
        $scope.tdata = tdata;
    }, function(error) {
        $scope.response = error.data;
    });

    this.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];
  });
