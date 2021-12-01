$(document).ready(function(){

    $(".salary-deletion-modal").click(function(){        
        let deleteSalaryModal = $(this).attr("id").split("-")[4]
        let openDeletionModal = `#delete-salary-modal-${deleteSalaryModal}`
        $(openDeletionModal).show(); 
    })

    $(".view-salary-modal").click(function(){        
        let openSalaryModal = $(this).attr("id").split("-")[4]
        let viewSalaryModal = `#view-salary-modal-${openSalaryModal}`
        $(viewSalaryModal).show();  
    })

    $(".close-button").click(function(){       
        $(".confirm-modal").hide();
        $(".view-modal").hide(); 
    })    

});