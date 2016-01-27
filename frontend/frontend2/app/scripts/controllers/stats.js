'use strict';
/**
 * @ngdoc function
 * @name frontend2App.controller:AboutCtrl
 * @description
 * # AboutCtrl
 * Controller of the frontend2App
 */
angular.module('frontendApp').config(function($stateProvider) {
    $stateProvider.state('main.stats', {
        url: '/stats',
        templateUrl: 'views/stats.html',
        controller: 'StatsCtrl',
        controllerAs: 'stats',
    });
}).controller('StatsCtrl', function(urls, $http, $scope, $timeout, $q, $state, $filter) {
    // Today
    $scope.dateCurrent = new Date();
    $scope.dateCurrent = $filter('date')($scope.dateCurrent, 'yyyy-MM-dd');
    // Yesterday
    $scope.dateYesterday = new Date();
    $scope.dateYesterday.setDate($scope.dateYesterday.getDate() - 1);
    $scope.dateYesterday = $filter('date')($scope.dateYesterday, 'yyyy-MM-dd');
    // First day of this month
    $scope.firstDayThisMonth = new Date();
    $scope.firstDayThisMonth = new Date($scope.firstDayThisMonth.getFullYear(), $scope.firstDayThisMonth.getMonth(), 1);
    $scope.firstDayThisMonth = $filter('date')($scope.firstDayThisMonth, 'yyyy-MM-dd');
    // First day of last month
    $scope.firstDayLastMonth = new Date();
    $scope.firstDayLastMonth = new Date($scope.firstDayLastMonth.getFullYear(), $scope.firstDayLastMonth.getMonth() - 1, 1);
    $scope.firstDayLastMonth = $filter('date')($scope.firstDayLastMonth, 'yyyy-MM-dd');
    // Date 7 days ago
    $scope.date7DaysAgo = new Date();
    $scope.date7DaysAgo.setDate($scope.date7DaysAgo.getDate() - 7);
    $scope.date7DaysAgo = $filter('date')($scope.date7DaysAgo, 'yyyy-MM-dd');
    //$scope.date_range = {fromdate: $scope.firstDayThisMonth, todate: $scope.dateCurrent};
    $scope.period_select_items = [{
        id: 1,
        label: 'Current Month',
        date_range: {
            fromdate: $scope.firstDayThisMonth,
            todate: $scope.dateCurrent
        },
    }, {
        id: 2,
        label: 'Previous Month',
        date_range: {
            fromdate: $scope.firstDayLastMonth,
            todate: $scope.firstDayThisMonth
        },
    }, {
        id: 3,
        label: 'Last 7 days',
        date_range: {
            fromdate: $scope.date7DaysAgo,
            todate: $scope.dateCurrent
        },
    }, {
        id: 4,
        label: 'Last day',
        date_range: {
            fromdate: $scope.dateYesterday,
            todate: $scope.dateCurrent
        },
    }, ];
    $scope.period_select_change = function() {
        console.log('period_select_change selected: ' + $scope.period_select.date_range.fromdate);
        $scope.date_range = $scope.period_select.date_range;
        $scope.dataFromPromise($scope.date_range).then(function(data) {
            $scope.$broadcast('amCharts.updateData', data, 'myFirstChart');
        }, function(reason) {
            console.log('Chart update failed: ' + reason);
        });
    };
    $scope.dataFromPromise = function(params) {
        var deferred = $q.defer();
        $http({
            url: urls.API + '/userdata.json/',
            method: 'GET',
            params: params
        }).then(function(datapoints) {
            deferred.resolve(datapoints.data);
        }, function(error) {
            deferred.reject(error);
        });
        return deferred.promise;
    };
    $scope.amChartOptions = $timeout(function() {
        return {
            type: "serial",
            pathToImages: 'bower_components/amcharts/dist/amcharts/images/',
            theme: "light",
            marginTop: 10,
            marginRight: 40,
            valueAxes: [{
                title: "Data used",
                position: "left"
            }],
            data: $scope.dataFromPromise($scope.date_range),
            graphs: [{
                valueAxis: "v1",
                bullet: "round",
                bulletBorderThickness: 1,
                hideBulletsCount: 30,
                title: "upload",
                valueField: "datain",
                fillAlphas: 0.0,
                type: "smoothedLine",
                lineColor: "#FF2600",
                useLineColorForBulletBorder: true,
            }, {
                valueAxis: "v2",
                bullet: "round",
                bulletBorderThickness: 1,
                hideBulletsCount: 30,
                title: "download",
                valueField: "dataout",
                fillAlphas: 0.0,
                type: "smoothedLine",
                lineColor: "#3484CA",
                useLineColorForBulletBorder: true,
            }, {
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
            }],
            chartScrollbar: {
                graph: "g1",
                oppositeAxis: false,
                offset: 30,
                scrollbarHeight: 25,
                backgroundAlpha: 0,
                selectedBackgroundAlpha: 0.1,
                selectedBackgroundColor: "#888888",
                graphFillAlpha: 0,
                graphLineAlpha: 0.5,
                selectedGraphFillAlpha: 0,
                selectedGraphLineAlpha: 1,
                autoGridCount: true,
                color: "#AAAAAA"
            },
            chartCursor: {
                valueLineEnabled: true,
                valueLineBalloonEnabled: true,
                cursorAlpha: 1,
                cursorColor: "#258cbb",
                limitToGraph: "g1",
                valueLineAlpha: 0.2
            },
            categoryField: "date",
            categoryAxis: {
                dashLength: 1,
                minorGridEnabled: true,
                minPeriod: "mm",
                parseDates: true,
                dateFormats: {
                    period: 'mm',
                    format: 'JJ:NN'
                },
                categoryFunction: function(cvalue, dataitem) {
                    var date_split = dataitem.date.split("-");
                    var DateNew = new Date(date_split[0], date_split[1] - 1, date_split[2], dataitem.data_hour, 0, 0, 0);
                    return DateNew;
                },
            },
            legend: {
                align: "left",
                equalWidths: false,
                periodValueText: "[[value.sum]]Bytes",
                valueAlign: "left",
                valueText: "[[value]]([[percents]]%)",
                valueWidth: 100
            },
            prefixesOfBigNumbers: [{
                "number": 1024,
                "prefix": "k"
            }, {
                "number": 1048576,
                "prefix": "M"
            }, {
                "number": 1073741824,
                "prefix": "G"
            }, {
                "number": 1099511627776,
                "prefix": "T"
            }, ],
            usePrefixes: true,
            creditsPosition: "top-left",
            export: {
                "enabled": true
            }
        };
    }, 0);
});