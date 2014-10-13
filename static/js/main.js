function get_ip_loc(){

     var ip = $("#ip_search").val();
     if(ip == undefined || ip == ""){
         alert("ip cann't null");
     }
     $.ajax({
     "url": "api/ip/"+ip,
     "type": "GET",
     "dataType": "json",
     "success": function(data){
         $("#ip_info").html(JSON.stringify(data));
     },
     "error": function(XMLHttpRequest, textStatus, errorThrown){alert(textStatus)}
     });

}
