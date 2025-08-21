



from flask import Flask, render_template_string
import os

app = Flask(__name__)

HTML = '''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hola Mundo Docker</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background: linear-gradient(135deg, #6dd5ed, #2193b0);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .card {
            box-shadow: 0 4px 24px rgba(0,0,0,0.15);
            border-radius: 1rem;
        }
        .logo {
            width: 80px;
            margin-bottom: 1rem;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-md-6">
                <div class="card p-4 text-center">
                    <img src="https://cdn-icons-png.flaticon.com/512/5968/5968705.png" class="logo" alt="Flask Logo">
                    <h1 class="mb-3">Hola Mundo</h1>
                    <p class="lead">desde <b>Flask + Docker + GitHub Actions + Render</b></p>
                    <hr>
                    <p class="mb-0">ITLA | Renny Báez <span class="badge bg-primary">2021-0441</span></p>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
'''

@app.get("/")
def hello():
    return render_template_string(HTML)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
