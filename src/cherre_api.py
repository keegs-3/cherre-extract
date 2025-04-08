def run_query(query, variables=None):
    headers = get_auth_header()
    headers["Content-Type"] = "application/json"

    payload = {"query": query}
    if variables:
        payload["variables"] = variables

    response = requests.post(CHERRE_URL, json=payload, headers=headers)
    response.raise_for_status()

    data = response.json()
    if "errors" in data:
        raise Exception(f"GraphQL error: {data['errors']}")
    return data.get("data", {})
