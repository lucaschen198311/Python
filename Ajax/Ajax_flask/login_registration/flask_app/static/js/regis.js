$(document).ready(function(){
    $("#email").keyup(function(){
        let data = $(".regist").serialize();
        $.ajax({
            url:"/email_check",
            method: "POST",
            data: data
        })
        .done(function(res){
            $(".emailMsg").html(res)
        })
    })
})