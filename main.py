from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Flask on AWS EKS - GitOps</title>
            <style>
                body {
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
                    color: white;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                }
                .card {
                    background: rgba(255, 255, 255, 0.08);
                    padding: 40px 50px;
                    border-radius: 20px;
                    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.5);
                    backdrop-filter: blur(10px);
                    text-align: center;
                    border: 1px solid rgba(255, 255, 255, 0.15);
                    max-width: 600px;
                }
                h1 { font-size: 2.4rem; margin-bottom: 12px; color: #ffffff; }
                p { font-size: 1.15rem; color: #00e5ff; line-height: 1.6; }
                .badges {
                    display: flex;
                    gap: 10px;
                    justify-content: center;
                    margin-top: 25px;
                }
                .badge {
                    padding: 8px 18px;
                    border-radius: 30px;
                    font-size: 0.9rem;
                    font-weight: bold;
                    letter-spacing: 0.5px;
                }
                .badge-v2 { background: #ff007f; color: white; }
                .badge-gitops { background: #00c853; color: white; }
            </style>
        </head>
        <body>
            <div class="card">
                <h1>Hello from Flask on Kubernetes! 🚀</h1>
                <p>⚡ Powered by AWS EKS, GitHub Actions CI/CD & ArgoCD GitOps ⚡</p>
                <div class="badges">
                    <span class="badge badge-v2">Version 2.0</span>
                    <span class="badge badge-gitops">GitOps Live</span>
                </div>
            </div>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
