/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
imsappctrl.controller('menuController', function ($scope) {
//  var imagePath = 'img/list/60.jpeg';
    $scope.Menu = [];
//    for (var i = 0; i < 15; i++) {
    $scope.Menu.push({
//      face: imagePath,
        MenuItem: "Manage Customer",
        Link: "/customer"
    });
    $scope.Menu.push({
//      face: imagePath,
        MenuItem: "Inventory",
        Link: "/inventory"
    });
     $scope.Menu.push({
//      face: imagePath,
        MenuItem: "Manage Order",
        Link: "/order"
    });
    $scope.Menu.push({
//      face: imagePath,
        MenuItem: "Invoice/Billing",
        Link: "/billing"
    });
//    }
});

