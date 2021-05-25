$(document).ready(function(){
    $("form").submit(function(){
        $.ajax({
            method: "POST",
            url:$(this).attr('action'),
            data:$(this).serialize()
        })
        .done(function(response){
            console.log(response)
            $("tbody").append(response);
        })
        return false;
    })

    $(".thumup").on('click', function(){
        let el = $(this).parent().parent().children()[3]; 
        //let currVal = parseInt($(a).text());
        //$(a).text(currVal+1)
        console.log($(this).parent().parent().children()[3])
        console.log($(this).attr('link'))
        $.ajax({
            url:$(this).attr('link')
        })
        .done(function(response){
            //console.log(response);
            //let a = $(this).parent().parent().children()[3];
            //console.log(a);
            $(el).text(response);
        })
        return false;
    })

    $(".thumdown").on('click', function(){
        let el = $(this).parent().parent().children()[3]; 
        //let currVal = parseInt($(a).text());
        //$(a).text(currVal+1)
        console.log($(this).parent().parent().children()[3])
        console.log($(this).attr('link'))
        $.ajax({
            url:$(this).attr('link')
        })
        .done(function(response){
            //console.log(response);
            //let a = $(this).parent().parent().children()[3];
            //console.log(a);
            $(el).text(response);
        })
        return false;
    })

    $(".delete").on('click', function(){
        let el = $(this).parent().parent(); 
        //let currVal = parseInt($(a).text());
        //$(a).text(currVal+1)
        console.log($(this).parent().parent().children()[3])
        console.log($(this).attr('link'))
        $.ajax({
            url:$(this).attr('link')
        })
        .done(function(response){
            //console.log(response);
            //let a = $(this).parent().parent().children()[3];
            //console.log(a);
            $(el).remove();
        })
        return false;
    })
})

