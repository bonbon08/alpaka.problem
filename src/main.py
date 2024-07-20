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
    process_data(search_text, trolling_level)
    return 'Form Submitted'

def process_data(search_text, trolling_level):
    # Process your data here or call other Python scripts
    print(f"Search Text: {search_text}, Trolling Level: {trolling_level}")

if __name__ == '__main__':
    app.run(debug=True)