function SubForm (){
    $.ajax({
        url: '/submit',
        type: 'post',
        data: $('#myForm').serialize(),
        success: function(){
            alert("worked");
        }
    });
}