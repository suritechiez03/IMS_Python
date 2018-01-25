imsappctrl.controller('customerController',['$location','$scope','initService','customerService',function($location,$scope,initService,customerService){

    $scope.selectedIndex=0;
    $scope.SAVE_UPDATE_FLAG = 'SAVE';
    $scope.FormCaption='New Customer';
    $scope.CustomerTypeList=['Dealer','Supplier','Customer','Authorizer','Partner']
    $scope.CustomerList = [] ;
    $scope.Clear=function(){
    $scope.Customer = {
          CustomerID:'',
          CustomerNumber:'',
          CustomerName:'',
          CustomerType:'',
          TinNumber:'',
          PanNumber:'',
          CstNumber:'',
          GstNumber:'',
          CompanyEmail:'',
          CompanyWebsite:'',
          CompanyAddress:'',
          PhoneNumber:'',
          Address_Id:''

    }
    $scope.FormCaption='New Customer'
    }
    $scope.SaveOrUpdate=function(){

          customerService.saveorupdate($scope.Customer);
          $scope.GetCustomerList();
          $scope.SAVE_UPDATE_FLAG='SAVE'
          $scope.selectedIndex=0;

          $scope.Clear();

    };
    $scope.GetCustomerList=function(){
          customerService.getCustomerList(function(response){
          $scope.CustomerList = response;
          });
    };
    $scope.editCustomer= function(data){
          $scope.Clear();
          $scope.SAVE_UPDATE_FLAG='UPDATE'
          $scope.Customer.CustomerID = data.CustomerID;
          $scope.Customer.CustomerNumber = data.CustomerNumber;
          $scope.Customer.CustomerName = data.CustomerName;
          $scope.Customer.CustomerType = data.CustomerType;
          $scope.Customer.TinNumber = data.TinNumber;
          $scope.Customer.PanNumber = data.PanNumber;
          $scope.Customer.CstNumber = data.CstNumber;
          $scope.Customer.GstNumber = data.GstNumber;
          $scope.Customer.CompanyWebsite = data.customeraddress__WebSite;
          $scope.Customer.CompanyEmail = data.customeraddress__Email;
          $scope.Customer.PhoneNumber = data.customeraddress__PhoneNumber;
          $scope.Customer.CompanyAddress = data.customeraddress__Address;
          $scope.Customer.Address_Id = data.customeraddress__id;
          $scope.selectedIndex=1;
          $scope.FormCaption='Edit Customer Info';
    }


}]);