$("#myForm").submit(function (e) {
    document.getElementById('image').style.display = 'block';
    e.preventDefault();
    $.ajax({
        url: '/submit',
        type: 'post',
        data: $('#myForm').serialize(),
        success: function (result) {
            document.getElementById('image').style.display = 'none';
            console.log(result)
            document.getElementsByClassName('results').innerText = result.toString();
        }
    });
});