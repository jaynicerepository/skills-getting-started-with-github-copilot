"""
Backend FastAPI tests using pytest and the AAA (Arrange-Act-Assert) pattern.
"""

def test_get_activities(client):
    # Arrange
    # (client fixture provides a fresh TestClient)

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_signup_success(client):
    # Arrange
    email = "testuser1@example.com"
    activity = "Basketball"

    # Act
    response = client.post(f"/activities/{activity}/signup", params={"email": email})

    # Assert
    assert response.status_code == 200
    assert "Signed up" in response.json().get("message", "")

def test_signup_duplicate(client):
    # Arrange
    email = "testuser2@example.com"
    activity = "Basketball"
    client.post(f"/activities/{activity}/signup", params={"email": email})

    # Act
    response = client.post(f"/activities/{activity}/signup", params={"email": email})

    # Assert
    assert response.status_code == 400
    assert "already signed up" in response.json().get("detail", "")

def test_signup_nonexistent_activity(client):
    # Arrange
    email = "testuser3@example.com"
    activity = "NonexistentActivity"

    # Act
    response = client.post(f"/activities/{activity}/signup", params={"email": email})

    # Assert
    assert response.status_code == 404
    assert "not found" in response.json().get("detail", "")
