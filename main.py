from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Manoj GitOps Live - AWS EKS</title>
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
                    padding: 45px 55px;
                    border-radius: 24px;
                    box-shadow: 0 20px 45px rgba(0, 0, 0, 0.6);
                    backdrop-filter: blur(14px);
                    text-align: center;
                    border: 2px solid #00e5ff;
                    max-width: 650px;
                }
                h1 { font-size: 2.5rem; margin-bottom: 12px; color: #ffffff; }
                p { font-size: 1.15rem; color: #00e5ff; line-height: 1.6; }
                .badges {
                    display: flex;
                    gap: 12px;
                    justify-content: center;
                    margin-top: 25px;
                }
                .badge {
                    padding: 10px 20px;
                    border-radius: 30px;
                    font-size: 0.95rem;
                    font-weight: bold;
                    letter-spacing: 0.5px;
                }
                .badge-v3 { background: #ff007f; color: white; }
                .badge-gitops { background: #00e676; color: #000; }
                .badge-probes { background: #7c4dff; color: white; }
            </style>
        </head>
        <body>
            <div class="card">
                <h1>Hello from Flask on Kubernetes! 🚀</h1>
                <p>⚡ Powered by AWS EKS, GitHub Actions CI/CD & ArgoCD GitOps ⚡</p>
                <div class="badges">
                    <span class="badge badge-v3">Version 3.0</span>
                    <span class="badge badge-gitops">4 Pods Scaled</span>
                    <span class="badge badge-probes">Probes Active 💚</span>
                </div>
            </div>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
