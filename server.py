from flask import Flask, render_template, abort

app = Flask(__name__)

def get_factorial(n):
    if n < 0:
        raise ValueError("Negative numbers do not have a factorial.")
    if n == 0 or n == 1:
        return 1
    return n * get_factorial(n - 1)

@app.route('/<int:n>')
def render_factorial(n):
    try:
        result = get_factorial(n)
        return render_template('factorial.html', number=n, factorial=result)
    except ValueError as e:
        abort(400, str(e))

if __name__ == '__main__':
    app.run(debug=True)