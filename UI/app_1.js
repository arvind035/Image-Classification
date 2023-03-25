$(document).ready(function() {
    $("#submitBtn").on('click', function (e) {
        console.log("submitBtn clicked");	
        $(function(){
            $.ajax({
                type: 'GET',
                // dataType:"jsonp",
                url: "http://127.0.0.1:5000/classify_image",       
                succces: function(data){
                    console.log('success');                    
                }
                
            });
        });
    });
});