from flask import Flask, request, render_template

import output_generator

app = Flask(__name__,template_folder=(r'C:\Users\srira\OneDrive\Desktop\projects\webscrapping\main\Tempaltes'))

@app.route('/')
def home():
    return render_template('webpage.html')

@app.route('/submit', methods=['POST'])
def submit():
    query = request.form['name']
    o1=output_generator.amazon_find(query.lower())
    o2=output_generator.flipkart_find(query.lower())
    # str1='\n'.join(o1)
    # str2='\n'.join(o2)
    
    return  render_template('dynamic.html',o1=o1,o2=o2)

if __name__ == '__main__':
    app.run(debug=True)
    