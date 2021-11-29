$(document).ready(function(){

    $(".salary-deletion-modal").click(function(){        
        let deleteSalaryModal = $(this).attr("id").split("-")[4]
        let openDeletionMOdal = `#delete-salary-modal-${deleteSalaryModal}`
        $(openDeletionMOdal).show(); 
    })


    $(".close-button").click(function(){       
        $(".confirm-modal").hide(); 
    })    

});