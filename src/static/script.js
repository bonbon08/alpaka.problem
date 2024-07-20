$("#myForm").submit(function (e) {
    e.preventDefault();
    $.ajax({
        url: '/submit',
        type: 'post',
        data: $('#myForm').serialize(),
        success: function () {
            alert("worked");
        }
    });
});