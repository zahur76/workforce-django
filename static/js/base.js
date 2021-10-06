$(document).ready(function(){
    

    $(".login-button").click(function(){ 
        console.log('zahur')       
        $("#loginModal").show();                          
    });

    $(".close").click(function(){        
        $("#loginModal").hide();        
    });
});