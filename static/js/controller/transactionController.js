imsappctrl.controller('transactionController',['$location','$scope','$rootScope','$mdSidenav', '$mdDialog', '$timeout','initService','customerService','inventoryService','ordermgmtService','billingService','alertService',
function($location,$scope,$rootScope,$mdSidenav, $mdDialog, $timeout,initService,customerService,inventoryService,ordermgmtService,billingService,alertService){
    $scope.searchInvoice = ''
    $scope.SelectedInvoice=[]
    $scope.ManageTransaction ={ Invoice:[] };
    $scope.invoice_list = [];
    $scope.PaymentMethodOptions = ('Cash Cheque Card').split(' ').map(function (state) {
                         return {abbrev: state};
                     });
    $scope.init = function (){

    };
    $scope.load_invoice = function(){
        billingService.get_invoice_list(function(response){
            $scope.invoice_list = response.data
            console.log($scope.invoice_list)
        });
         $mdDialog.show({
                          contentElement: '#InvoiceList',
                          parent: angular.element(document.body),
                          targetEvent: null,
                          clickOutsideToClose: true
                        });
    };
    $scope.load_InvoiceDetails = function (){
        $scope.ClearFields();
        $scope.ManageTransaction.Invoice = $scope.SelectedInvoice;
        $scope.ManageTransaction.InvoiceNumber = $scope.SelectedInvoice[0].InvoiceNumber;
        $scope.ManageTransaction.AmountToBePaid =$scope.SelectedInvoice[0].BalanceAmount;


    };
    $scope.process = function(){
                	if(parseFloat($scope.ManageTransaction.TransactionAmount) > ($scope.ManageTransaction.AmountToBePaid)){
                		alertService.showAlert(this,"Info","Transaction amount cannot be greater than "+$scope.ManageTransaction.AmountToBePaid ,"Ok");
                	}else{
                	billingService.ProcessPayment($scope.ManageTransaction,function(response){

                			 alertService.confirmAlert("Info","Payment Successful " + response.data,"OK ","Print Receipt",function(response){
                                  if(response === 'OK'){
                                     //window.open('/billing/api/get_invoice_pdf?InvoiceNumber='+invoiceno,'_blank')
                                     //billingService.get_invoice_pdf(invoiceno,function(response){
                                      window.location.reload();
                                    // })
                                  }else{
                                      //window.open('/billing/api/get_invoice_pdf?InvoiceNumber='+invoiceno,'_blank')
                                  }   window.location.reload();
                               });
                	});
                }
     };
     $scope.ClearFields = function(){
        $scope.ManageTransaction.AmountToBePaid=0;
        $scope.ManageTransaction.Invoice='';
        $scope.ManageTransaction.InvoiceNumber='';
        $scope.ManageTransaction.PaymentMethod=''
        $scope.ManageTransaction.Description=''
     };

}]);