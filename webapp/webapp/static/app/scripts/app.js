'use strict';

var app = angular
  .module('angApp', ['restangular'], function($interpolateProvider) {
    
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
});

app.controller("matching",function($scope,Restangular){
    
    $scope.$watch(
        function($scope){return $scope.income_date},
        function(newValue, oldValue){
            console.log(newValue);
            console.log(oldValue);
    });
});

