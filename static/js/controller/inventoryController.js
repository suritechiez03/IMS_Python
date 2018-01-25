imsappctrl.controller('inventoryController',['$location','$scope','initService','inventoryService',function($location,$scope,initService,inventoryService){
    $scope.CategoryList = [];
    $scope.ProductList = [];
    $scope.selectedIndex=0;
    $scope.SAVE_UPDATE_FLAG = 'SAVE';
    $scope.FormCaption = "Manage Products";
    $scope.FormCategoryCaption = "Product Category";
    $scope.selectedcategory = [];
    $scope.selectedproduct = [];

    $scope.clear=function(){
        $scope.Product = {
               ProductCode:'',
               ProductName:'',
               Description:'',
               CategoryCode:'',
               Units:'',
               Size:'',
               MoQ:'',
               HsnSacCode:'',
               Color:'',
               Image:''
        }
        $scope.SAVE_UPDATE_FLAG = 'SAVE';
        $scope.FormCaption = "Add New Product";

    };

    $scope.clearCategory =function(){
        $scope.ProductCategory= {
                CategoryName:'',
                Description:'',
                CategoryID:''
        }
    };

    $scope.init_category= function(){
        $scope.FormCategoryCaption = "Product Category"
        $scope.SAVE_UPDATE_FLAG = 'SAVE';
        $scope.getCategoryList();
    }

    $scope.SaveOrUpdateCategory=function(){
            inventoryService.SaveOrUpdateCategory($scope.ProductCategory)
                $scope.clearCategory();

    };

    $scope.SaveOrUpdateProduct=function(){
            console.log($scope.Product);
            inventoryService.SaveOrUpdateProduct($scope.Product);
            $scope.clear();
            $scope.selectedIndex=0;


    };

    $scope.getCategoryList = function(){
            $scope.CategoryList=[];
            inventoryService.getCategoryList(function(response){
            $scope.CategoryList = response;
            })
    };

    $scope.getProductList = function(){
            $scope.ProductList=[];
            inventoryService.getProductList(function(response){
            $scope.ProductList = response;
            })
    };

    $scope.edit=function(data){
             $scope.Product = data;
             $scope.Product.CategoryCode=data.CategoryCode_id;
             $scope.FormCaption = "Edit Product"
             $scope.SAVE_UPDATE_FLAG = 'UPDATE';
             $scope.selectedIndex=1;

    };
    $scope.edit_category = function(data){
            $scope.clearCategory();
            $scope.ProductCategory.CategoryID = data.id;
            $scope.ProductCategory.CategoryName = data.CategoryName;
            $scope.ProductCategory.Description = data.Description;
            $scope.SAVE_UPDATE_FLAG = 'UPDATE';
    };


    $scope.init_product = function(){
            $scope.FormCaption = "Add New Product"
            $scope.SAVE_UPDATE_FLAG = 'SAVE';
            $scope.getCategoryList();
    };

}])