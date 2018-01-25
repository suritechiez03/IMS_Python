imsappctrl.factory('initService',['$rootScope','$http',function($rootScope,$http){
  var service={};
  service.getInitialSettings = function (){
      $http.get('/mod_auth/accounts/api/getSettings')
      .then(function(data, status, headers, config){
            console.log(headers)
            console.log(status)
           $rootScope.APPLICATION_DATA = data;
      },function(response){
             console.log('Error ' + response.data)
      })

  }
  return service;
}]);
