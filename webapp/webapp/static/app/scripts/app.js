'use strict';

angular.module('angApp.directives',[]);

var app = angular
  .module('angApp', ['restangular', 'angApp.directives', 'ngCookies'], function($interpolateProvider) {
//    'restangular'
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
});

app.config(function(RestangularProvider) {
    RestangularProvider.setBaseUrl('/api');

});

app.filter('uniqueOffer', function() {
   return function(collection, keyname) {
      var output = [], 
          keys = [];

      angular.forEach(collection, function(item) {
          var key = item.offer[keyname];
          if(keys.indexOf(key) === -1) {
              keys.push(key);
              output.push(item);
          }
      });

      return output;
   };
});

app.controller("matching",function($scope,Restangular,$cookies){
    
    var mapping = [];
    mapping['1'] = "pending";
    mapping['2'] = "waiting";
    mapping['3'] = "confirmed";
    mapping['4'] = "accepted";
    mapping['5'] = "assigned";
    mapping['6'] = "notified";
    
    $scope.$watch(
        function($scope){return $scope.incomedate},
        function(newValue, oldValue){
            if(newValue!=oldValue)
                $scope.getList(newValue);
    });
    
    $scope.getList = function(in_date){
        var temp_matching = Restangular.all('temporal_matching');
        
        temp_matching.customGET("",{'date':""+in_date}).then(function(items){
                angular.forEach(items,function(item){
                    item.status_maped = mapping[item.status];
                });
                $scope.items = items;
            });
    }
    $scope.viewDonorInInfoBox = function(item){
        $scope.viewDonor = item;
    }
    $scope.viewBenInInfoBox = function(item){
        $scope.viewBen = item;
    }
    
    $scope.sendOffer = function(items){
//       operator klika „Send offer” i do zaznaczonych beneficjentów wysyłany jest mail z propozycją przyjęcia dotacji, 
//	     status beneficjenta zmienia się z „pending” na „waiting".
        
        angular.forEach(items, function(item){
            item.status = 2;
            if(item.beneficiary.checked && item.beneficiary.checked == true){
                var temp = {"id": item.id,
                            "date": item.date,
                            "beneficiary_contact_person": item.beneficiary_contact_person,
                            "quantity": item.quantity,
                            "status": 2, //<-- status changed
                            "offer": item.offer.id,
                            "beneficiary": item.beneficiary.id}
                
                Restangular.setDefaultHeaders({"X-CSRFToken": $cookies.get('csrftoken')})
                    .one("temporal_matching_simple",item.id).customPUT(temp)
                    .then(function(resp){
                    });
            }
        });
        $scope.getList($scope.incomedate);
    }
    
    $scope.accept = function(items){
        console.log("accept");
    }
    
    $scope.assignDriver = function(items){
        console.log("assignDriver");
    }
    
    $scope.notify = function(items){
        console.log("notify");
    }
    
    $scope.cancel = function(items){
        console.log("cancel");
    }
    
    $scope.sumOf = function(items){
        if(items!=undefined)
            return items.reduce( function(total, item){
                  return total + item.beneficiary.num_meals
                }, 0);
        else
            return 0;
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
        template: '<th>[[status]]</th>'
      };
});


