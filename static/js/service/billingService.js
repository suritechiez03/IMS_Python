imsappctrl.factory('billingService',['$rootScope','$http','alertService',function($scope,$http,alertService){
   var service={};

   service.process_invoice = function(data,callback){
         $http.post('/billing/api/process_invoice',data , { headers: { 'contentType':'application/json'}})
                          .then(function(response){
                                callback(response)
                          },function(response){
                                alertService.showAlert(null,'Error',response.data,'OK');
              });
   };
   service.validate_invoice = function(invoice,callback){
         $http.post('/billing/api/validate_invoice',invoice , {headers : {'contentType' : 'application/json'}})
                           .then(function(response){
                                callback(response)
                           },function(response){
                                alertService.showAlert(null,'Error',response.data,'OK');
                           });
   };
   service.get_invoice_list = function (callback){
         $http.get('/billing/api/get_invoice_list', {headers : {'contentType' : 'application/json'}})
                           .then(function(response){
                                callback(response)
                           },function(response){
                                alertService.showAlert(null,'Error',response.data,'OK');
                           });
   };
   service.fetch_invoice_list_all = function (callback){
         $http.get('/billing/api/fetch_invoice_list_all', {headers : {'contentType' : 'application/json'}})
                           .then(function(response){
                                callback(response)
                           },function(response){
                                alertService.showAlert(null,'Error',response.data,'OK');
                           });
   };
   service.ProcessPayment = function(invoice,callback){
         $http.post('/billing/api/process_payment',invoice , {headers : {'contentType' : 'application/json'}})
                           .then(function(response){
                                callback(response)
                           },function(response){
                                alertService.showAlert(null,'Error',response.data,'OK');
                           });
   };
   service.get_invoice_pdf = function (invoiceno,callback){

         $http.get('/billing/api/get_invoice_pdf?InvoiceNumber='+invoiceno, {headers : {'contentType' : 'application/pdf'}})
                           .then(function(response){
                                callback(response)
                           },function(response){
                                alertService.showAlert(null,'Error',response.data,'OK');
                           });
   };
   return service;
   }]);