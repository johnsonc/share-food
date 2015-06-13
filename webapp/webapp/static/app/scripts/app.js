'use strict';

angular.module('angApp.directives',[]);

var app = angular
  .module('angApp', ['restangular','angApp.directives'], function($interpolateProvider) {
//    'restangular'
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
});

app.config(function(RestangularProvider) {
    RestangularProvider.setBaseUrl('/api');

});

app.controller("matching",function($scope,Restangular){
    
    var temp_matching = Restangular.all('temporal_matching');
    
    $scope.$watch(
        function($scope){return $scope.incomedate},
        function(newValue, oldValue){
            temp_matching.customGET("",{'date':""+newValue}).then(function(items){
                $scope.items = items;
                console.log(items);
            });
    });
    
    $scope.getList = function(in_date){
        console.log("$scope.getList");
    }
    $scope.viewDonorInInfoBox = function(item){
        $scope.viewDonor = item;
    }
    $scope.viewBenInInfoBox = function(item){
        $scope.viewBen = item;
    }
});

angular.module('angApp.directives')
    .directive('st', function() {
      return {
        restrict: 'E',
        replace: true,
        scope: {
          stat: '='
        },
        link: function(scope, element, attrs) {
            attrs.$observe('stat', function(st) {
                scope.status = st.status;
                console.log(st);
            });
            
        },
        template: '<th>[[stat.status]]</th>'
      };
});

