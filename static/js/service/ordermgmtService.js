imsappctrl.factory('ordermgmtService',['$rootScope','$http','alertService',function($scope,$http,alertService){
   var service={};
   service.save_order = function(data){
         $http.post('/order/api/save_order',data , { headers: { 'contentType':'application/json'}})
                          .then(function(response){
                                alertService.showAlert(null,'Info',response.data,'OK');
                          },function(response){
                                alertService.showAlert(null,'Error',response.data,'OK');
              });
   };
   service.get_order_list = function(callback){
         $http.get('/order/api/get_order_list')
                           .then(function(response){
                                    callback(response.data);
                           },function(response){
                                    alertService.showAlert(null,'Error',response.data,'OK');
                           });
   };
   service.get_order_by_customer = function(data,callback){
         $http.post('/order/api/get_order_by_customer',data, { headers: { 'contentType':'application/json'}})
                           .then(function(response){
                                    callback(response.data);
                           },function(response){
                                    alertService.showAlert(null,'Error',response.data,'OK');
                           });
   };
   service.remove_product = function(data, callback){
         $http.post('/order/api/remove_product', data, { headers: { 'contentType':'application/json'}})
                            .then(function(response){
                                  alertService.showAlert(null,'info',response.data,'OK')
                                  callback(response);
                            },function(response){
                                  alertService.showAlert(null,'info',response.data,'OK')
                            });
   };

   return service;


}]);