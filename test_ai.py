import sys
sys.path.append('.')

from utils.ai_response import get_completion

print("Testing AI service...")
print("=" * 50)

try:
    response = get_completion("What is AI?", "You are a helpful assistant.")
    print(f"✅ AI Response received!")
    print(f"Response: {response}")
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
