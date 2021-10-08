$(document).ready(function(){

    // Placeholders for add staff form    
    $('#id_gender option:first-child').html('Gender');    
    $('#id_gender option:first-child').css('display', 'none');  
    $('#id_management_level option:first-child').html('Management Level'); 
    $('#id_management_level option:first-child').css('display', 'none');  

    
    $('#id_gender').change(function(){
        $('#id_gender').css('color', 'black');   
    });

    $('.add_staff-form-input').change(function(){
        $(this).css('color', 'black');   
    });

    // feature to open upload image button
    $('.upload-image').click(function(){
        console.log('zahur')               
        $('#id_image').click();     
    });

    $('.add_staff-form-input').change(function(){        
        fileInput = $('#id_image').val()         
        filename = fileInput.split('\\')
        console.log(filename)        
        $('.image-filename').html(filename[2]);      
    });
});