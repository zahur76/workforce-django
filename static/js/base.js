$(document).ready(function(){    
    $(".login-button").click(function(){             
        $("#loginModal").show();                          
    });

    $(".close").click(function(){        
        $("#loginModal").hide();        
    });

    /* Function to clear flash messages after 3's*/  
    setTimeout(function(){
        $(".flash-message").hide("slow");
    }, 3000 ); // 5 secs

    /* Allow password to become visible*/ 
    $("body").on('click', '.eye-icon', function() {
        $(this).toggleClass("fa-eye fa-eye-slash");
        input = $("#password");
        if (input.attr("type") === "password") {
          input.attr("type", "text");
        } else {
          input.attr("type", "password");
        }
    });

    $(".dropdown").click(function(){        
        $("#drop-down").show();
        $("#drop-down").addClass('open');
        console.log($("#drop-down").attr("style"))             
    });        
    
    var drop_modal = document.getElementById('drop-down');
    window.onclick = function(event) {
        if (event.target == drop_modal) {     
           drop_modal.style.display = "none";     
         }   
     }          
});
