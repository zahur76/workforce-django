$(document).ready(function(){

    // Form set-up  
    $('#id_gender option:first-child').html('Gender');
    $('#id_birth_date').attr('placeholder', 'Birthday'); 
    $('#id_entry_date').attr('placeholder', 'Date of Entry');
    $('#id_termination_date').attr('placeholder', 'Date of termination');    
    $('#id_gender option:first-child').css('display', 'none');  
    $('#id_management_level option:first-child').html('Management Level'); 
    $('#id_management_level option:first-child').css('display', 'none');
        
    $('#id_start_date').attr('placeholder', 'Start date');
    $('#id_end_date').attr('placeholder', 'End_date');
    
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
    
    // change colour of dropdown menu selected items
    let gender = $('#id_gender').val();
    if(gender!=""){
        $('#id_gender').css('color', 'black');
    }
    let level = $('#id_management_level').val();
    if(level!=""){
        $('#id_management_level').css('color', 'black');
    }

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

    // open delete modal    
    $('.open-modal').click(function(){
        openModal = $(this).attr("id");
        requiredModal = 'delete' + openModal.split('open')[1];
        $("#" + requiredModal).show();        
    })

    $('.close-modal').click(function(){
        $('.confirm-modal').hide();
    })   
    
    
    // Sick leave charts 

    $(".close-data").hide();
    $('.close-data').click(function(){
        console.log('zahur')
        $('#myChart').hide();
        $(".close-data").hide();
    }) 
    
    form = $('#data-year')
    $('#data-year').change(function(){
       form.submit();
    });

    let dataYear = $('#data-year').attr('placeholder');    
    $('#data-year option:selected').html(dataYear);

    $('.show-data').click(function(){
        $(".close-data").show();
        $('#myChart').show();        
        let month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', "Sep", 'Oct', 'Nov', "Dec"];        
        let days = [sickData['Jan'], sickData['Feb'], sickData['Mar'], sickData['Apr'], sickData['May'], sickData['Jun'], sickData['Jul'], sickData['Aug'], sickData['Sep'], sickData['Oct'], sickData['Nov'], sickData['Dec']]
        let barColors = [];
        for (let i=0; i<=month.length; i++){
            barColors.push("blue"); 
        }               
        new Chart("myChart", {
            type: "bar",
            data: {
              labels: month,
              datasets: [{
                backgroundColor: barColors,
                data: days
              }]
            },
            options: {
              legend: {display: false},
              title: {
                display: true,
                text: "Sick Leave 2021"
              }
            }
        });

    })      
});