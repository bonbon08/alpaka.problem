$("#myForm").submit(function (e) {
    document.getElementById('image').style.display = 'block';
    document.getElementById('myForm').style.display = 'none';
    e.preventDefault();
    $.ajax({
        url: '/submit',
        type: 'post',
        data: $('#myForm').serialize(),
        success: function (result) {
            document.getElementById('image').style.display = 'none';
            document.getElementById('myForm').style.display = 'block';
            console.log(result)
            document.querySelector('.result').innerText = result.toString();
        }
    });
});