from app import app

# Expor a aplicação Flask como handler do Vercel
def handler(req, res):
    return app(req, res)