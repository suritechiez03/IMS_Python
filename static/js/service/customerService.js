imsappctrl.factory('customerService',['$rootScope','$http','alertService',function($scope,$http,alertService){
   var service={};

          service.saveorupdate=function(data){
                      $http.post('api/save_customer_info',data , { headers: { 'contentType':'application/json'}})
                      .then(function(response){
                            alertService.showAlert(null,'Info',response.data,'OK');
                      },function(response){
                            alertService.showAlert(null,'Error',response.data,'OK');
                      });
          };
          service.getCustomerList= function(callback){
                       $http.get('api/get_customer_list')
                       .then(function(response){
                                callback(response.data);
                       },function(response){
                                alertService.showAlert(null,'Error',response.data,'OK');
                       });

          };

  return service;
  }]);