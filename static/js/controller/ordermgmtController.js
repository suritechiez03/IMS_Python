imsappctrl.controller('ordermgmtController',['$location','$scope','$rootScope','$mdSidenav', '$mdDialog', '$timeout','initService','customerService','inventoryService','ordermgmtService','alertService',
function($location,$scope,$rootScope,$mdSidenav, $mdDialog, $timeout,initService,customerService,inventoryService,ordermgmtService,alertService){
    $scope.selectedIndex=0;
    $scope.ProductList=[];
    $scope.searchTerm='';
    $scope.selected=[];
    $scope.selectedproductlist=[];
    $scope.Order = { OrderDetails:[] , CustomerType :'' ,CustomerNumber:'',OrderDate:'',Comments:'' }
    $scope.clearSearchTerm = function () {
             $scope.searchTerm = '';
    };
    $scope.init_order_management=function(){
         customerService.getCustomerList(function(response){
             $scope.CustomerList = response;
          });

         inventoryService.getProductList(function(response){
            $scope.ProductList = response;
          })
    };

    $scope.AddtoCart = function (product, qty) {
        console.log(product);
        product.orderQuantity = qty;
        if ($scope.selectedproductlist.indexOf(product) === -1){
                    $scope.selectedproductlist.push(product);
                    $scope.orderQuantity = 0;
        }else{
            alertService.showAlert(this,"","Item Already Exists","OK");
        }
        console.log($scope.selectedproductlist);
    };
    $scope.Save_Order = function(){
        $scope.Order.Comments=""
        $scope.Order.OrderDetails = $scope.selectedproductlist;
        console.log($scope.Order)
        ordermgmtService.save_order($scope.Order)

    };
    $scope.get_order_list = function(){
        ordermgmtService.get_order_list(function(response){
        console.log(response)
        $scope.OrderList = response;
        });
    };
    $scope.showOrderDetails = function(data) {
        $scope.Order.OrderDate = new Date(data.OrderRaisedDate);
        $scope.Order.CustomerNumber = data.CustomerNumber;
        for(i=0;i<data.OrderDetails.length;i++){
            $scope.selectedproductlist.push({OrderNumber:data.OrderDetails[i].OrderNumber_id,ProductCode:data.OrderDetails[i].ProductDetails[0].ProductCode,ProductName:data.OrderDetails[i].ProductDetails[0].ProductName,orderQuantity:data.OrderDetails[i].OrderQty})
        }
        $scope.selectedIndex=0;

    };
    $scope.removeProduct= function (item){
        console.log(item);
        ordermgmtService.remove_product(item, function(response){
             var index = $scope.selectedproductlist.indexOf(item);
             $scope.selectedproductlist.splice(index, 1);
        });
    };

}])