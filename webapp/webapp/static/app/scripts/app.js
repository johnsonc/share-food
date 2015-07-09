angular.module('angapp', ['restangular', 'leaflet-directive', 'ngCookies'])

.config(function($interpolateProvider) {
//    'restangular'
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
})

.config(function(RestangularProvider) {
    RestangularProvider.setBaseUrl('/api');
})

.filter('uniqueOffer', function() {
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
})

.controller("matching",['$scope','Restangular','$interval','$cookies','$q',
    function($scope,Restangular,$interval,$cookies,$q){ 
    
    angular.extend($scope, {
        center: {
            lat: 44.097,
            lng: -79.552,
            zoom: 7
        },
        defaults: {
            scrollWheelZoom: false
        },
        markers: {},
        paths: {}
    });
    $scope.mapopened = false;
                               
    var mapping = [];
    mapping['1'] = "pending";
    mapping['2'] = "waiting";
    mapping['3'] = "confirmed";
    mapping['4'] = "accepted";
    mapping['5'] = "assigned";
    mapping['6'] = "notified";
    mapping['7'] = "expired";
    mapping['8'] = "canceled";
    
    $scope.sendOfferChecked     = true;
    $scope.acceptChecked        = true;
    $scope.assignDriverChecked  = true;
    $scope.notifyChecked        = true;
    $scope.cancelChecked        = true;
    $scope.select = {};
    
    Restangular.all('drivers').getList()
        .then(function(drivers){
            $scope.drivers = drivers;
    });
    
    var link = 0;
    
    var timer = $interval( function(){
        var myEl = angular.element( document.querySelector( '#id_date' ) );
        $scope.incomedate = myEl[0].value;
    }, 1000);    
    
    $scope.$on('$destroy', function() {
          $interval.cancel(timer);
        });
    
    $scope.$watch(
        function($scope){return $scope.incomedate},
        function(newValue, oldValue){
            if(newValue!=oldValue)
                $scope.getList(newValue);
    });  

    $scope.$watchCollection("filtItems",
         function( newValue, oldValue ) {
            $scope.map($scope.filtItems);
        } );
        
    
    $scope.getList = function(in_date){
        var temp_matching = Restangular.all('temporal_matching');
        if(in_date.length>8)
        temp_matching.customGET("",{'date':""+in_date}).then(function(items){
                angular.forEach(items,function(item){
                    item.status_maped = mapping[item.status];
                });
                $scope.items = items;
                $scope.select.offer = {};
            });
    }
    
    
    $scope.map = function(items){
        
        var map_ben = [];
        var map_don = [];
        var lines = [];
        var map_points = {};
        var promises = [];
        
        var getLatLong = function(location){
            var temp = location.substring(7, location.length - 1);
            return temp.split(" ");    
        }
        
        var getLocation = function(user_id,type,status,name){
            var defer = $q.defer();
            Restangular.all('organization').customGET("",{'user':user_id}).then(function(obj){
                
                var item = obj[0];
                var temp_lat = Number(parseFloat(getLatLong(item.location)[1]).toFixed(3));
                var temp_lng = Number(parseFloat(getLatLong(item.location)[0]).toFixed(3));
                if(type=="donor"){
                    map_points['d'+item.id]= { 
                                    lat: temp_lat ,
                                    lng: temp_lng ,
                                    message: name,
                                    icon:{
                                        type: 'awesomeMarker',
                                        icon: 'tag',
                                        markerColor: 'red'
                                        }
                                    }
                } else {
                    map_points['b'+item.id]= { 
                                    lat: temp_lat,
                                    lng: temp_lng,
                                    message: name,
                                    icon:{
                                        type: 'awesomeMarker',
                                        icon: 'cog',
                                        markerColor: (status >= 3 ? "green" : "red")
                                        }
                                    }
                }
                defer.resolve();
            });
            return defer.promise;
        }    
        
        var createLine = function(us_id1,us_id2,index){
            var defer = $q.defer();
            Restangular.all('organization').customGET("",{'user':us_id1}).then(function(obj){
                var item = obj[0];
                var us1_lat = Number(parseFloat(getLatLong(item.location)[1]).toFixed(3));
                var us1_lng = Number(parseFloat(getLatLong(item.location)[0]).toFixed(3));
                Restangular.all('organization').customGET("",{'user':us_id2}).then(function(obj){
                    var item = obj[0];
                    var us2_lat = Number(parseFloat(getLatLong(item.location)[1]).toFixed(3));
                    var us2_lng = Number(parseFloat(getLatLong(item.location)[0]).toFixed(3));
                    
                    lines[index] = {
                        color: 'green',
                        weight: 2,
                        latlngs: [
                            { lat: us1_lat, lng: us1_lng },
                            { lat: us2_lat, lng: us2_lng }
                        ]
                    }
                    defer.resolve(); 
                });
            });
            return defer.promise;
        }    
        
        if($scope.mapopened){
            angular.forEach(items,function(item){
                if(item.status>=0){
                    if(map_ben.indexOf(item.beneficiary.user)== -1){
                        map_ben.push(item.beneficiary.user);
                        promises.push(getLocation(item.beneficiary.user,"beneficiary",item.status,item.beneficiary_contact_person));
                    }
                }
                if(map_don.indexOf(item.offer.donor)== -1){
                    map_don.push(item.offer.donor);
                    promises.push(
                        getLocation(item.offer.donor,"donor",item.status,item.offer.name));
                    }
                if( item.status>=3){
                    createLine(item.beneficiary.user, item.offer.donor,item.id);
                }
                
            });
            $q.all(promises).then(function(){
                angular.extend($scope, {
                    markers: map_points,
                    paths: lines
                });
            });
        }
    }
    
    $scope.viewDonorInInfoBox = function(item){
        $scope.select.offer = {id:item.id};
        $scope.viewDonor = item;
        item.showcolor = true;
        angular.forEach($scope.items,function(obj){
            if(obj.offer.id != item.id){
                obj.offer.showcolor = false;                
            }
        })
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
    
    $scope.assignDriver = function(items, driver){
        angular.forEach(items, function(item){
            $scope.changeStatus(item,5,driver);
        });
    }
    
    $scope.notify = function(items){
        angular.forEach(items, function(item){
            $scope.changeStatus(item,6,item.driver);
        });
    }
    
    $scope.cancel = function(items){
         angular.forEach(items, function(item){
            $scope.changeStatus(item,8,null);
         });
    }
    
    $scope.sumOf = function(items){
        if(items!=undefined)
            return items.reduce( function(total, item){
                  return total + Number(item.quantity)
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
                temp += Number(item.quantity)
            }
        });
        var calculation = (temp/Number(offer.estimated_mass)) * 100;
        return  calculation;
    }
    
    $scope.changeStatus = function(item,status,driver){
        if(item.beneficiary.checked && item.beneficiary.checked == true){
            var temp = {
                    "id": item.id,
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
                    item.status_maped = mapping[resp.status];
                    item.status = resp.status;
//                    item.driver = resp.driver;

                    $scope.beneficiaryChanged($scope.items);
                },
                function(response) {
                    console.log("Error with status code", response.status);
                });
            }
    }
    
    $scope.saveQuantity = function(item){
        var temp = {
            "id": item.id,
            "date": item.date,
            "beneficiary_contact_person": item.beneficiary_contact_person,
            "quantity": item.quantity,
            "hash": item.hash,
            "status": item.status, 
            "offer": item.offer.id,
            "driver": item.driver,
            "beneficiary": item.beneficiary.id}
                
        Restangular.setDefaultHeaders({"X-CSRFToken": $cookies.get('csrftoken')})
            .one("temporal_matching_simple",item.id).customPUT(temp)
            .then(function(resp){
            });
    }
    
    
}]);



