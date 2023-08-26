

def test_healthcheck_router(test_app, test_user_headers):
    response = test_app.get(f"/healthcheck", headers=test_user_headers)
    assert response.status_code == 200
