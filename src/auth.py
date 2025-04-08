def get_auth_header():
    token = os.getenv("CHERRE_API_KEY")
    if not token:
        raise ValueError("CHERRE_API_KEY not found in environment variables.")
    return {"Authorization": token}
