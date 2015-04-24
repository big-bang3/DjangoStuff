

var MyApp = angular.module('myapp', []);
var my_app = angular.module('myapp').config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
});
MyApp.controller('msg_l',function msg_l($scope,$http){ 
  function call_req(){$http.get(window.location.href+"/aj_req").success(
                    function(data,status,headers,config){ $scope.sh=false;$scope.l_msg=data;
                                                      }
                    )}
  function ang_msg(){$http.get("http://172.16.2.197:8000/project1/").success(
                    function(data,status,headers,config){
                      
                     $scope.unread=data[0];$scope.online=data[1];$scope.offline=data[2];
                        }
                    );}
 
  call_req(); ang_msg();

  setInterval(call_req,3000);
  setInterval(ang_msg,5000);
  

})

$(document).ready(function(){


  aj2();
  $('#send_msg').keydown(function(event){
      if(event.which == 13 && !event.shiftKey) {$('#subit').submit();return false;}
       $('#b1').load(function(){
                      var textarea = document.getElementById('b1');
                      textarea.scrollTop = textarea.scrollHeight;   window.alert("fvff");         
                          });
  });
/*function escapeHtml(text) {
  var map = {
    '&': '&amp;',
    '<': '&lt;',
    '>': '&gt;',
    '"': '&quot;',
    "'": '&#039;',
    '`': '<br>'
  };

  return text.replace(/[&<>"'`]/g, function(m) { return map[m]; });
}
*/
/*
function aj(){

$.ajax({
url:window.location.href+"/aj_req",
dataType:"json",
method:"GET",
success:function(data){
                $("#try_ajax").html(escapeHtml(data.data1));
            }
});



}
*/
function aj2(){
$.ajax({
        url : "http://172.16.2.197:8000/project1/check_msg",
        method : "GET",
        dataType:"json",
        success:function(y){ 
          if(y.y1){
        $("#try2").html(y.y1);
}
        }


});



}
var bec = setInterval(aj2,5000);
//var abc=setInterval(aj,4000);




});
/*
setInterval(function(){
var xmlhttp;

if (window.XMLHttpRequest)
  {// code for IE7+, Firefox, Chrome, Opera, Safari
  xmlhttp=new XMLHttpRequest();
  }
else
  {// code for IE6, IE5
  xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
  }
xmlhttp.onreadystatechange=function()
  {
  if (xmlhttp.readyState==4 && xmlhttp.status==200)
    {
    document.getElementById("try_ajax").innerHTML=xmlhttp.responseText;}
  }
xmlhttp.open("GET",window.location.href+"/aj_req",true);
xmlhttp.send();
},3000);*/
