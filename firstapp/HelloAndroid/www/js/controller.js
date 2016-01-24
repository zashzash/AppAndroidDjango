angular.module('ionicApp', ['ionic'])

.controller('MyCtrl', function($scope,$ionicPopup) {
  
  $scope.data = {
    showDelete: false
  };
  
  $scope.view = function(item) {
    alert('Title: ' + item.title + ' Description: ' + item.description + ' Author: ' + item.author);
  };
  
   // An alert dialog
  $scope.showAlert = function(item) {
   var alertPopup = $ionicPopup.alert({
     title: item.title,
     template: item.description,
   });

   alertPopup.then(function(res) {
     console.log(item.author);
   });
 };
  
  $scope.share = function(item) {
    alert('Share Item: ' + item.id);
  };
  
  $scope.moveItem = function(item, fromIndex, toIndex) {
    $scope.items.splice(fromIndex, 1);
    $scope.items.splice(toIndex, 0, item);
  };
  
  $scope.onItemDelete = function(item) {
    $scope.items.splice($scope.items.indexOf(item), 1);
};

  //$scope.items = json_decode(file_get_contents('http://127.0.0.1:8000/api/question/'));
  $scope.items = [{"title":"What is it?","description":"This is..... stupid question","author":1},{"title":"The BUG?","description":"this is the bug question","author":1}];
  
});

