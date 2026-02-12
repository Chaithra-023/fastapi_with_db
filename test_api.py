import requests
import json

# Test 0: Create a user first
print("=" * 50)
print("Test 0: Creating test user")
print("=" * 50)
signup_data = {
    "email": "test@example.com",
    "password": "password123"
}
try:
    response = requests.post("http://127.0.0.1:8000/signup", json=signup_data)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
except Exception as e:
    print(f"Signup Error (user may already exist): {e}")

# Test 1: Check basic endpoint
print("\n" + "=" * 50)
print("Test 1: Testing root endpoint")
print("=" * 50)
try:
    response = requests.get("http://127.0.0.1:8000/")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
except Exception as e:
    print(f"Error: {e}")

# Test 2: Login to get token
print("\n" + "=" * 50)
print("Test 2: Testing login")
print("=" * 50)
login_data = {
    "email": "test@example.com",
    "password": "password123"
}
try:
    response = requests.post("http://127.0.0.1:8000/login", json=login_data)
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        token_data = response.json()
        print(f"Response: {token_data}")
        token = token_data["access_token"]
        print(f"✅ Token obtained: {token[:20]}...")
        
        # Test 3: Test /ask endpoint with authentication
        print("\n" + "=" * 50)
        print("Test 3: Testing /ask endpoint with auth")
        print("=" * 50)
        ask_data = {
            "message": "Hello, this is a test message",
            "system_prompt": "You are a helpful assistant."
        }
        headers = {"Authorization": f"Bearer {token}"}
        try:
            response = requests.post("http://127.0.0.1:8000/ask", json=ask_data, headers=headers)
            print(f"Status: {response.status_code}")
            if response.status_code == 200:
                print(f"Response: {response.json()}")
                print("✅ /ask endpoint working!")
            else:
                print(f"❌ Error Response: {response.text}")
        except Exception as e:
            print(f"❌ Error: {e}")
        
        # Test 4: Test /history endpoint
        print("\n" + "=" * 50)
        print("Test 4: Testing /history endpoint")
        print("=" * 50)
        try:
            response = requests.get("http://127.0.0.1:8000/history", headers=headers)
            print(f"Status: {response.status_code}")
            if response.status_code == 200:
                history = response.json()
                print(f"Response: {history}")
                print(f"✅ History retrieved! Found {len(history)} entries.")
            else:
                print(f"❌ Error Response: {response.text}")
        except Exception as e:
            print(f"❌ Error: {e}")
    else:
        print(f"❌ Login failed: {response.json()}")
except Exception as e:
    print(f"❌ Login Error: {e}")

print("\n" + "=" * 50)
print("Tests completed!")
print("=" * 50)
