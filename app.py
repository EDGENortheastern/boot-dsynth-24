from flask import Flask, render_template, request, redirect, url_for
from helpers.generate_linear import generate_equation

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def show_equation():
    if request.method == 'POST':
        # Get the user's answer and the correct solution
        user_answer = int(request.form['user_answer'])
        correct_solution = int(request.form['correct_solution'])

        # Check if the user's answer is correct
        if user_answer == correct_solution:
            feedback = "Correct! Well done."
        else:
            feedback = f"Incorrect. The correct answer was {correct_solution}."

        # Redirect after handling POST, passing feedback as a query parameter
        return redirect(url_for('show_equation', feedback=feedback))

    # On GET request, generate a new equation
    equation, solution = generate_equation()

    # Get feedback if any exists in the URL parameters
    feedback = request.args.get('feedback')

    return render_template('index.html', equation=equation, solution=solution, feedback=feedback)

if __name__ == '__main__':
    app.run(debug=True)
