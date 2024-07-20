from flask import Flask, render_template, request
from gpt import get_ai_return
app = Flask(__name__)

@app.route('/')
def index():
    # Serve your HTML file
    return render_template('test.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Extract data from form
    search_text = request.form['search']
    trolling_level = request.form['trolling']
    # Here you can call any function and pass the extracted data
    process_data(int(int(trolling_level) / 10), search_text)
    return 'Form Submitted'

def process_data(search_text, trolling_level):
    
    print(f"Search Text: {search_text}, Trolling Level: {trolling_level}")
    result = get_ai_return(search_text, trolling_level)
    print(result)

if __name__ == '__main__':
    app.run(debug=True)