from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/biography')
def biography():
    return render_template('biography.html')

@app.route('/oteche')
def oteche():
    return render_template('otechestvennie.html')

@app.route('/zarubej')
def zarubej():
    return render_template('zarubejnie.html')


@app.route('/lebedev')
def lebedev():
    return render_template('bio_lebedev.html')

@app.route('/ershov')
def ershov():
    return render_template('bio_ershov.html')

@app.route('/lyapunov')
def lyapunov():
    return render_template('bio_lyapunov.html')
@app.route('/gavrilov')
def gavrilov():
    return render_template('bio_gavr.html')
@app.route('/brus')
def brus():
    return render_template('bio_brus.html')
@app.route('/bruk')
def bruk():
    return render_template('bio_bruk.html')


@app.route('/tiuring')
def tiuring():
    return render_template('bio_tiuring.html')

@app.route('/bebidj')
def bebidj():
    return render_template('bio_bebidj.html')

@app.route('/neyman')
def neyman():
    return render_template('bio_neyman.html')


@app.route('/inter')
def inter():
    return render_template('inter.html')

@app.route('/check')
def check():
    return render_template('prover.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')


if __name__ == '__main__':
    app.run(debug=True)



