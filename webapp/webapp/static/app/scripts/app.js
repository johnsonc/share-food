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

app.controller("matching",function($scope,Restangular,$cookies,$interval){
    
    var mapping = [];
    mapping['1'] = "pending";
    mapping['2'] = "waiting";
    mapping['3'] = "confirmed";
    mapping['4'] = "accepted";
    mapping['5'] = "assigned";
    mapping['6'] = "notified";
    
    $scope.sendOfferChecked     = true;
    $scope.acceptChecked        = true;
    $scope.assignDriverChecked  = true;
    $scope.notifyChecked        = true;
    $scope.cancelChecked        = true;
    $scope.select = {};
    
    Restangular.all('drivers').getList()
        .then(function(drivers){
            console.log(drivers);
            $scope.drivers = drivers;
    });
    
//    var timer = $interval( function(){
//        if($scope.incomedate){
//            Restangular.all('temporal_matching')
//                .customGET("",{'date':""+$scope.incomedate})
//                .then(function(items){
//                    angular.forEach(items,function(item){
//                        item.status_maped = mapping[item.status];
//                    });
//                $scope.items = items;
//            });
//        }
//    }, 10000);
    
    $scope.$on('$destroy', function() {
          $interval.cancel(timer);
        });
    
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
        $scope.select.offer = {id:item.id};
        $scope.viewDonor = item;
    }
    $scope.viewBenInInfoBox = function(item){
        $scope.viewBen = item;
    }
    
    $scope.sendOffer = function(items){
        angular.forEach(items, function(item){
            $scope.changeStatus(item,2,null);
        });
    }
    
    $scope.accept = function(items){
        angular.forEach(items, function(item){
            $scope.changeStatus(item,4,$scope.picked);
        });
    }
    
    $scope.assignDriver = function(items){
        angular.forEach(items, function(item){
            $scope.changeStatus(item,5,item.driver);
        });
    }
    
    $scope.notify = function(items){
        angular.forEach(items, function(item){
            $scope.changeStatus(item,6,item.driver);
        });
    }
    
    $scope.cancel = function(items){
         angular.forEach(items, function(item){
            $scope.changeStatus(item,1,null);
         });
    }
    
    $scope.sumOf = function(items){
        if(items!=undefined)
            return items.reduce( function(total, item){
                  return total + item.quantity
                }, 0);
        else
            return 0;
    }
    
    $scope.beneficiaryChanged = function(items){
        $scope.sendOfferChecked = false;
        $scope.acceptChecked  = false;
        $scope.assignDriverChecked  = false;
        $scope.notifyChecked  = false;
        $scope.cancelChecked  = false;
        angular.forEach(items,function(item){
            if(item.beneficiary.checked){
                if( item.status != 1 ){
                    $scope.sendOfferChecked = true;
                }
                if( item.status != 3 ){
                    $scope.acceptChecked = true;
                }
                if( item.status != 4 ){
                    $scope.assignDriverChecked = true;
                }
                if($scope.picked==undefined){
                    $scope.assignDriverChecked = true;
                }
                if( item.status != 5 ){
                    $scope.notifyChecked = true;
                }
                if( item.status != 6 ){
                    $scope.cancelChecked = true;
                }
            }
        });
    }
    
    $scope.percentage = function(offer){
        var temp = 0;
        angular.forEach($scope.items, function(item){
            if(item.offer.id == offer.id && item.status>=3 ){
                temp += item.quantity
            }
        });
        var calculation = (temp/offer.estimated_mass) * 100;
        return  calculation;
    }
    
    $scope.changeStatus = function(item,status,driver){
    
        if(item.beneficiary.checked && item.beneficiary.checked == true){
                var temp = {"id": item.id,
                            "date": item.date,
                            "beneficiary_contact_person": item.beneficiary_contact_person,
                            "quantity": item.quantity,
                            "hash": item.hash,
                            "status": status, 
                            "offer": item.offer.id,
                            "driver": driver,
                            "beneficiary": item.beneficiary.id}
                
                Restangular.setDefaultHeaders({"X-CSRFToken": $cookies.get('csrftoken')})
                    .one("temporal_matching_simple",item.id).customPUT(temp)
                    .then(function(resp){
                    });
            }
    }
});



