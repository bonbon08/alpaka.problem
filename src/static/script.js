$("#myForm").submit(function (e) {
    e.preventDefault();
    fetch('/submit', {
        method: 'POST',
        body: $('#myForm').serialize()
    })
    .then(response => response.json())
    .then(data => {
        // Update the 'results' div with the result
        document.getElementById('results').innerText = data.result;
    })
    .catch(error => console.error('Error:', error));

});