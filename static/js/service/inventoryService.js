imsappctrl.factory('inventoryService',['$rootScope','$http','alertService',function($scope,$http,alertService){
   var service={};

        service.getCategoryList= function(callback){
                           $http.get('/inventory/api/get_category_list')
                           .then(function(response){
                                    callback(response.data);
                           },function(response){
                                    alertService.showAlert(null,'Error',response.data,'OK');
                           });

              };
        service.getProductList= function(callback){
                           $http.get('/inventory/api/get_product_list')
                           .then(function(response){
                                    callback(response.data);
                           },function(response){
                                    alertService.showAlert(null,'Error',response.data,'OK');
                           });

              };
        service.SaveOrUpdateCategory=function(data){
                          $http.post('/inventory/api/save_category',data , { headers: { 'contentType':'application/json'}})
                          .then(function(response){
                                alertService.showAlert(null,'Info',response.data,'OK');
                          },function(response){
                                alertService.showAlert(null,'Error',response.data,'OK');
              });
          };
        service.SaveOrUpdateProduct=function(data){
                          $http.post('/inventory/api/save_product',data , { headers: { 'contentType':'application/json'}})
                          .then(function(response){
                                alertService.showAlert(null,'Info',response.data,'OK');
                          },function(response){
                                alertService.showAlert(null,'Error',response.data,'OK');
              });
          };
   return service;
}]);