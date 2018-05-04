imsappctrl.controller('billingController',['$location','$scope','$rootScope','$mdSidenav', '$mdDialog', '$timeout','initService','customerService','inventoryService','ordermgmtService','billingService','alertService',
function($location,$scope,$rootScope,$mdSidenav, $mdDialog, $timeout,initService,customerService,inventoryService,ordermgmtService,billingService,alertService){
       $scope.SelectedProduct = [];
       $scope.selectedIndex = 0;
       $scope.Products = [];
       $scope.ManageInvoice = {products: '',InvoiceType:'',ManageOrder : {OrderDetails:[]}};
       $scope.ManageInvoice.InvoiceType='Invoice'

       $scope.InvoiceTypeList = ('Sales Invoice,Purchase Invoice').split(',').map(function (state) {
                    return {abbrev: state};
                });

       $scope.selected = [];
       $scope.OrderList = [];
       $scope.get_customer_list= function(){
            customerService.getCustomerList(function(response){
                $scope.CustomerList = response;
            });
            $scope.InvoiceTypeChange();


       };
       $scope.get_order_list = function(){
            ordermgmtService.get_order_by_customer($scope.ManageInvoice.Customer,function(response){
                $scope.OrderList=response;
            });
       };
       $scope.init_invoice=function(){
            $scope.get_customer_list();

       };
       $scope.InvoiceTypeChange=function(){
            if($scope.ManageInvoice.InvoiceType ==='Purchase Invoice'){
                $scope.PurchaseInvoice=true;
            }else{
                $scope.PurchaseInvoice=false;
            }
       };
       $scope.getProductList = function(){
            inventoryService.getProductList(function(response){
             $scope.ProductList = response;

            });
             console.log($scope.ProductList);
        };
       $scope.showProduct = function(ev) {
           $scope.getProductList();
           $mdDialog.show({
                          contentElement: '#ProductDialog',
                          parent: angular.element(document.body),
                          targetEvent: ev,
                          clickOutsideToClose: true
                        });

       };
       $scope.showAddInvoiceDetails = function(ev) {
           $mdDialog.show({
                          contentElement: '#AddInvoiceDetails',
                          parent: angular.element(document.body),
                          targetEvent: ev,
                          clickOutsideToClose: true
                        });

       };
       $scope.Remove = function (productIndex) {
                    $scope.ManageInvoice.ManageOrder.OrderDetails.splice(productIndex, 1);
                    $scope.CalcuateCharges();
        };
       $scope.load_order = function(){

       }
       $scope.AddToCart = function(){
         for(var i=0;i< $scope.SelectedProduct.length;i++){
            if ($scope.ManageInvoice.ManageOrder.OrderDetails.indexOf($scope.SelectedProduct[i]) === -1) {
                  $scope.ManageInvoice.ManageOrder.OrderDetails.push($scope.SelectedProduct[i]);
            }else{
                   alertService.showAlert(this, "Info", "Item Already Exists", "OK");
            }
         }
       };
       $scope.updateTotal = function (item) {

            item.TotalAmount = (item.orderQuantity * item.UnitPrice);
            item.TotalAmount = item.TotalAmount - ((item.TotalAmount * item.Discount) / 100);
            item.TotalAmount = $scope.fixedto4digit(item.TotalAmount);
            item.MarginAmt = $scope.fixedto4digit(((item.UnitPrice * item.MarginPrecnt) / 100));
            item.DealerPrice = $scope.fixedto4digit(item.UnitPrice + item.MarginAmt);
            $scope.CalcuateCharges();



       };
        $scope.CalcuateCharges = function () {
                    var grossamt = 0;
                    var CheckTaxAlreadyAdded = 0; //VAT1
                    var totalTax2 = 0;  //VAT 2
                    var roundoff = 0;
                    var finaltax = 0;
                    $scope.DynamicTblGST = [];
                    for (i = 0; i < $scope.ManageInvoice.ManageOrder.OrderDetails.length; i++) {

                        totalTax2 = ($scope.ManageInvoice.ManageOrder.OrderDetails[i].TotalAmount * $scope.ManageInvoice.ManageOrder.OrderDetails[i].Tax) / 100;
                        if ($scope.ManageInvoice.ManageOrder.OrderDetails[i].Tax > 0 && CheckTaxAlreadyAdded !== $scope.ManageInvoice.ManageOrder.OrderDetails[i].Tax) {

                            $scope.DynamicTblGST.push({taxrate: ($scope.ManageInvoice.ManageOrder.OrderDetails[i].Tax / 2), taxprice: (totalTax2 / 2), type: "SGST", tax: $scope.ManageInvoice.ManageOrder.OrderDetails[i].Tax});
                            $scope.DynamicTblGST.push({taxrate: ($scope.ManageInvoice.ManageOrder.OrderDetails[i].Tax / 2), taxprice: (totalTax2 / 2), type: "CGST", tax: $scope.ManageInvoice.ManageOrder.OrderDetails[i].Tax});
                            CheckTaxAlreadyAdded = $scope.ManageInvoice.ManageOrder.OrderDetails[i].Tax;

                        } else
                        {
                            $scope.DynamicTblGST.filter(function (item) {
                                return item.taxrate === $scope.ManageInvoice.ManageOrder.OrderDetails[i].Tax / 2;
                            })
                                    .map(function (item) {
                                        item.taxprice = item.taxprice + (totalTax2 / 2);
                                        return item;
                                    });
                        }
                        grossamt = grossamt + $scope.ManageInvoice.ManageOrder.OrderDetails[i].TotalAmount;
                        finaltax = finaltax + totalTax2; // calculate and add tax for each row
                    }
                    $scope.ManageInvoice.GrossAmount = $scope.fixedto4digit(grossamt);
                    $scope.ManageInvoice.TaxAmount = $scope.fixedto4digit(finaltax);
                    roundoff = parseFloat(grossamt) + parseFloat($scope.ManageInvoice.TaxAmount);
                    $scope.ManageInvoice.RoundOff = $scope.fixedto4digit($scope.fixedto4digit(roundoff) - $scope.fixedto4digit(Math.floor($scope.fixedto4digit(roundoff)))); //(Math.floor(parseFloat(roundoff).toFixed(4)) - parseFloat(roundoff).toFixed(4)).toFixed(4).toString();
                    $scope.ManageInvoice.FinalAmount = $scope.fixedto2digit(Math.floor(parseFloat(roundoff)))
                    if ($scope.ManageInvoice.CrDrNote > 0 || $scope.ManageInvoice.CrDrNote < 0) $scope.ManageInvoice.FinalAmount = $scope.ManageInvoice.FinalAmount - $scope.ManageInvoice.CrDrNote;
        };
        $scope.fixedto4digit = function (i) {

            console.log((+(Math.round(i + "e+4") + "e-4")));
            return (+(Math.round(i + "e+4") + "e-4"));
        };
        $scope.fixedto2digit = function (i) {

            console.log((+(Math.round(i + "e+2") + "e-2")));
            return (+(Math.round(i + "e+2") + "e-2"));
        };
        $scope.SubmitInvoice=function(){
        var invoiceno= ''
            billingService.process_invoice($scope.ManageInvoice,function(response){
            invoiceno=response.data
                   alertService.confirmAlert("Info","Invoice Generated !! " + response.data,"OK","Cancel",function(response){
                      if(response === 'OK'){

                         $scope.get_invoice_pdf(invoiceno)
                         //billingService.get_invoice_pdf(invoiceno,function(response){
                          window.location.reload();
                        // })
                      }
                   });

            });
        };
        $scope.get_invoice_pdf = function(InvoiceNo){
              window.open('/billing/api/get_invoice_pdf?InvoiceNumber='+InvoiceNo,'_blank')
        };
        $scope.fetch_invoice_list_all = function(){
        billingService.fetch_invoice_list_all(function(response){ $scope.invoice_list_all = response.data
            //console.log($scope.invoice_list)
        });

        };
        $scope.GetQuote=function(data){
          var invoice_date = {
                 invoicenumber:"",
                 seller :{
                       name:"",
                       address:"",
                       country:"",
                       gsttin:""
                 },
                 buyer : {
                       name:"",
                       address:"",
                       country:"",
                       gsttin:""
                 },
                 invoice:{
                        invoicenumber:'',
                        invoicedate:"",
                        paymentduedate:"",
                        repname:"",
                        lrnodate:"",
                        deliveryterms:"",
                        frieghtterms:"",
                        transporter:"",
                        esugamano:"",
                        packs:"",
                        roundoff:"",
                        totalamount:""

                 },
                 items:[{

                 }]


          };

        };




}]);