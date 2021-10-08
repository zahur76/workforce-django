$(document).ready(function(){

    // Form set-up  
    $('#id_gender option:first-child').html('Gender');
    $('#id_birth_date').attr('placeholder', 'Birthday'); 
    $('#id_entry_date').attr('placeholder', 'Date of Entry');
    $('#id_termination_date').attr('placeholder', 'Date of termination');    
    $('#id_gender option:first-child').css('display', 'none');  
    $('#id_management_level option:first-child').html('Management Level'); 
    $('#id_management_level option:first-child').css('display', 'none');  

    
    $('#id_gender').click(function(){
        $('#id_gender').css('color', 'black');   
    });

    $('#id_management_level').click(function(){
        $('#id_management_level').css('color', 'black');   
    });

    $('.add_staff-form-input').change(function(){
        console.log('zahur')
        $(this).css('color', 'black');   
    });

    $('#id_gender').css('color', '#aab7c4');
    $('#id_management_level').css('color', '#aab7c4');     

    $('#id_birth_date').change(function(){
        $('#id_birth_date').css('color', 'black');  
    });

    // feature to open upload image button
    $('.upload-image').click(function(){                       
        $('#id_image').click();     
    });

    $('.add_staff-form-input').change(function(){        
        fileInput = $('#id_image').val()         
        filename = fileInput.split('\\')
        console.log(filename)        
        $('.image-filename').html(filename[2]);      
    });
});