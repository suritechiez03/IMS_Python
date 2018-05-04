imsappctrl.factory('customerService',['$rootScope','$http','alertService',function($scope,$http,alertService){
   var service={};

          service.saveorupdate=function(data,callback){
                      $http.post('/customer/api/save_customer_info',data , { headers: { 'contentType':'application/json'}})
                      .then(function(response){
                           callback(response)

                      },function(response){
                            alertService.showAlert(null,'Error',response.data,'OK');
                      });
          };
          service.getCustomerList= function(callback){
                       $http.get('/customer/api/get_customer_list')
                       .then(function(response){
                                callback(response.data);
                       },function(response){
                                alertService.showAlert(null,'Error',response.data,'OK');
                       });

          };

  return service;
  }]);