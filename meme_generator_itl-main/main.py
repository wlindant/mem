from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Pobranie wybranego obrazu
        selected_image = request.form.get('image-selector')

        # Zadanie #2. Pobranie tekstu
        text_top = request.form.get('textTop')
        text_bottom = request.form.get('textBottom')

        # Zadanie #3. Pobranie pozycji tekstu
        text_top_y = request.form.get('textTop_y')
        text_bottom_y = request.form.get('textBottom_y')

        # Zadanie #3. Pobranie koloru tekstu
        selected_color = request.form.get('color-selector')

        return render_template('index.html', 
                               selected_image=selected_image, 
                               text_top=text_top,
                               text_bottom=text_bottom,
                               text_top_y=text_top_y,
                               text_bottom_y=text_bottom_y,
                               selected_color=selected_color
                               )
    else:
        # Domyślne wyświetlenie pierwszego obrazu
        return render_template('index.html', selected_image='logo.svg')

@app.route('/static/img/<path:path>')
def serve_images(path):
    return send_from_directory('static/img', path)

app.run(debug=True)