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
  .controller('StatsCtrl', function (urls, $http, $scope, $timeout, $q) {
  $scope.dataFromPromise = function() {
        var deferred = $q.defer();
        $http({
            url: urls.API +'/userdata.json/',
            method: 'GET'
        }).then(function(datapoints) {
            deferred.resolve(datapoints.data);
        }, function(error) {
            deferred.reject(error);
        });

        return deferred.promise;
    };

    this.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];


    $scope.amChartOptions = $timeout(function() {
        return {
            type: "serial",
            pathToImages: 'https://cdnjs.cloudflare.com/ajax/libs/amcharts/3.13.0/images/',
            theme: "light",
            marginRight: 80,
            valueAxes: [{
                title: "Bandwidth used",
                position: "left"
            }],
            data: $scope.dataFromPromise(),
            graphs: [{
                valueAxis: "v1",
                bullet: "round",
                bulletBorderThickness: 1,
                hideBulletsCount: 30,
                title: "download",
                valueField: "datain",
                fillAlphas: 0.0,
                type: "smoothedLine",
                lineColor: "#FF2600",
                useLineColorForBulletBorder: true,
            }, 
            {
                valueAxis: "v2",
                bullet: "round",
                bulletBorderThickness: 1,
                hideBulletsCount: 30,
                title: "upload",
                valueField: "dataout",
                fillAlphas: 0.0,
                type: "smoothedLine",
                lineColor: "#3484CA",
                useLineColorForBulletBorder: true,
            },
            {
                valueAxis: "v3",
                bullet: "round",
                bulletBorderThickness: 1,
                hideBulletsCount: 30,
                title: "total",
                valueField: "totaldata",
                fillAlphas: 0.1,
                type: "smoothedLine",
                lineColor: "#5ACE69",
                useLineColorForBulletBorder: true,
            }
            ],
            chartScrollbar: {
                graph: "g1",
                oppositeAxis: false,
                offset:30,
                scrollbarHeight: 80,
                backgroundAlpha: 0,
                selectedBackgroundAlpha: 0.1,
                selectedBackgroundColor: "#888888",
                graphFillAlpha: 0,
                graphLineAlpha: 0.5,
                selectedGraphFillAlpha: 0,
                selectedGraphLineAlpha: 1,
                autoGridCount:true,
                color:"#AAAAAA"
            },
            chartCursor: {
                valueLineEnabled: true,
                valueLineBalloonEnabled: true,
                cursorAlpha:1,
                cursorColor:"#258cbb",
                limitToGraph:"g1",
                valueLineAlpha:0.2
            },
            categoryField: "date",
            categoryAxis: {
                dashLength: 1,
                minorGridEnabled: true,
                minPeriod: "mm",
                parseDates: true,
                dateFormats: {period:'mm',format:'JJ:NN'},
                categoryFunction: function (cvalue, dataitem, ref) {
                    console.log('categoryFunction:');
                    console.log(cvalue);
                    console.log(dataitem);
                    console.log(ref);
                    var date_split = dataitem.date.split("-");
                    var DateNew = new Date(date_split[0], date_split[1], date_split[2], dataitem.data_hour, 0, 0, 0);
                    console.log(DateNew);
                    return DateNew;
                },
            },
            legend: {
                align: "left",
                equalWidths: false,
                periodValueText: "[[value.sum]]GB",
                valueAlign: "left",
                valueText: "[[value]]([[percents]]%)",
                valueWidth: 100
            },
            creditsPosition: "top-left",
        }

    }, 1000);


  });
