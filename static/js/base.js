$(document).ready(function(){
    
    $(".login-button").click(function(){ 
        console.log('zahur')       
        $("#loginModal").show();                          
    });

    $(".close").click(function(){        
        $("#loginModal").hide();        
    });

    /* Function to clear flash messages after 3's*/  
    setTimeout(function(){
        $(".flash-message").hide("slow");
    }, 3000 ); // 5 secs
    
});