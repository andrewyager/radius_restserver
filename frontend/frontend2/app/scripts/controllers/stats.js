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
    $scope.usageperiod = {};
    $scope.quotaDataForGraph = function() {
        var data = [];
        data[0] = {
            "category": "This Period",
            "total_data": 0,
            "remaining_data": 0,
            "fill-color": "#FFFFFF"
        };
        var percentage, color, used_data, td, rd;
        if ($scope.usageperiod.current && $scope.quota) {
            used_data = $scope.usageperiod.current.total/1024/1024/1024;
            percentage = used_data/$scope.quota;
            if (percentage<0.8) {
                color = "#008000";
            } else if (percentage < 1.0) {
                color = "#ff8000";
            } else {
                color = "#cb1919";
            }
            td = used_data.toFixed(3);
            rd = $scope.quota - td;
            if (percentage<0.02) {
                td = (0.02*rd).toFixed(3);
                rd = rd - td;
            }
            if (rd<0) {
                rd = 0;
            }
            data[0] = {
                "category": "This Period",
                "total_data": td,
                "remaining_data": rd,
                "fill-color": color
            };
            data[1] = {
                "category": "Last Period",
                "total_data": 0,
                "remaining_data": 0,
                "fill-color": "#000000"
            };
        }
        if ($scope.usageperiod.previous) {
            used_data = $scope.usageperiod.previous.total/1024/1024/1024;
            percentage = used_data/$scope.quota;
            if (percentage<0.8) {
                color = "#008000";
            } else if (percentage < 1.0) {
                color = "#ff8000";
            } else {
                color = "#cb1919";
            }
            td = used_data.toFixed(3);
            rd = $scope.quota - td;
            if (rd<0) {
                rd = 0;
            }
            data[1] = {
                "category": "Last Period",
                "total_data": td,
                "remaining_data": rd,
                "fill-color": color
            };
        }
        return data;
    };

    $scope.quotaGraph = $timeout(function() {
        return {
            "type": "serial",
            "categoryField": "category",
            data: $scope.quotaDataForGraph(),
            "rotate": true,
            "startDuration": 1,
            "theme": "light",
            "graphs": [
                {
                    "fillAlphas": 1,
                    "fillColorsField": "fill-color",
                    "gapPeriod": 0,
                    "id": "used_data",
                    "lineThickness": 0,
                    "type": "column",
                    "valueField": "total_data",
                    "showBalloon": true,
                    "valueAxis": "DataUsage",
                    "title": "Consumed Data"
                },
                {
                    "fillAlphas": 0.8,
                    "fillColors": "#BBBBBB",
                    "id": "remaining_data",
                    "type": "column",
                    "lineThickness": 0,
                    "valueAxis": "DataUsage",
                    "showBalloon": false,
                    "valueField": "remaining_data",
                    "title": "Remaining Data"
                }
            ],
            "valueAxes": [
                {
                    "id": "DataUsage",
                    "minimum": 0,
                    "stackType": "100%",
                    "labelsEnabled": false
                }
            ]
        };
    }, 0);

    $scope.loadData = function(params) {
        $http({
            url: urls.API + '/userquota.json/',
            method: 'GET',
            params: params
        }).success(function(quotalist) {
            if (quotalist.length>0) {
                $scope.quota = quotalist[0].quota/1024/1024/1024;
            } else {
                $scope.quota = "500GB";
            }
        }).error(function() {
            $scope.quota = "Unknown";
        });
        // get billing info
        $http({
            url: urls.API + '/userbilling.json/',
            method: 'GET',
            params: params
        }).success(function(billingdata) {
            if (billingdata.length>0) {
                $scope.anniversary = billingdata[0].anniversary_day;
                $scope.excessaction = billingdata[0].action;
                $scope.service_status = billingdata[0].status;
                $scope.username = billingdata[0].username;
                if ($scope.excessaction === "shape" && $scope.service_status === "exceed") {
                    $scope.status = "shaped";
                } else {
                    $scope.status = "not shaped";
                }
                // get data for this period
                $http({
                    url: urls.API + '/quotausage.json/',
                    method: 'GET',
                    params: params
                }).success(function(usage) {
                    if (usage.total) {
                        $scope.usageperiod.current = usage;
                    } else {
                        $scope.usageperiod.current = {
                            total_out:0,
                            total_in:0,
                            total:0
                        };
                    }
                    var data=$scope.quotaDataForGraph();
                    $scope.$broadcast('amCharts.updateData', data, 'quotaGraphChart');
                }).error(function() {
                    $scope.anniversary = "Unknown";
                    $scope.excessaction = "shape";
                });

                $http({
                    url: urls.API + '/quotausage/'+$scope.username+'/1.json/',
                    method: 'GET',
                    params: params
                }).success(function(usage) {
                    if (usage.total) {
                        $scope.usageperiod.previous = usage;
                        var data=$scope.quotaDataForGraph();
                        $scope.$broadcast('amCharts.updateData', data, 'quotaGraphChart');
                    }
                });
            } else {
                $scope.anniversary = "1";
                $scope.excessaction = "charge excess";
                $scope.service_status = "normal";
            }
        }).error(function() {
            $scope.anniversary = "Unknown";
            $scope.excessaction = "shape";
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
                useLineColorForBulletBorder: true,
            }],
            chartScrollbar: {
                graph: "g1",
                oppositeAxis: false,
                offset: 30,
                scrollbarHeight: 25,
                backgroundAlpha: 0,
                selectedBackgroundAlpha: 0.1,
                graphFillAlpha: 0,
                graphLineAlpha: 0.5,
                selectedGraphFillAlpha: 0,
                selectedGraphLineAlpha: 1,
                autoGridCount: true,
            },
            chartCursor: {
                valueLineEnabled: true,
                valueLineBalloonEnabled: true,
                cursorAlpha: 1,
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