import requests

print("Testing /ask endpoint with authentication...")
print("=" * 50)

# Use the test user we created earlier
login_data = {
    "email": "test@example.com",
    "password": "password123"
}

# Login to get token
response = requests.post("http://127.0.0.1:8000/login", json=login_data)
if response.status_code == 200:
    token = response.json()["access_token"]
    print(f"✅ Logged in successfully")
    
    # Test the /ask endpoint
    ask_data = {
        "message": "What is AI?",
        "system_prompt": "You are a helpful assistant."
    }
    headers = {"Authorization": f"Bearer {token}"}
    
    print("\nSending request to /ask endpoint...")
    response = requests.post("http://127.0.0.1:8000/ask", json=ask_data, headers=headers)
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        print(f"\n✅ Response received!")
        print(f"Response object: {data}")
        print(f"\nActual AI response:")
        print("=" * 50)
        print(data.get('response', 'NO RESPONSE FIELD'))
        print("=" * 50)
    else:
        print(f"❌ Error: {response.text}")
else:
    print(f"❌ Login failed: {response.json()}")
