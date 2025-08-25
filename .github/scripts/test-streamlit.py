#!/usr/bin/env python3

import sys
import requests
import time

def test_streamlit_app():
    """Test if Streamlit app is running and accessible"""
    base_url = "http://localhost:8501"
    max_attempts = 3 
    
    print("🔍 Testing Streamlit app availability...")
    
    # Wait for app to start and test
    for attempt in range(1, max_attempts + 1):
        try:
            print(f"⏳ Attempt {attempt}/{max_attempts}: Checking {base_url}")
            
            response = requests.get(base_url, timeout=5)
            
            if response.status_code == 200:
                print(f"✅ SUCCESS: Streamlit app is running!")
                print(f"   Status Code: {response.status_code}")
                print(f"   Response Length: {len(response.text)} bytes")
                
                # Basic content check
                content = response.text.lower()
                if 'streamlit' in content or 'st-emotion' in content:
                    print("✅ Streamlit content detected in response")
                else:
                    print("⚠️ Warning: No Streamlit indicators found, but app is responding")
                
                return True
            else:
                print(f"❌ Bad status code: {response.status_code}")
                
        except requests.exceptions.ConnectionError:
            print(f"⏳ Connection refused, app might still be starting...")
        except requests.exceptions.Timeout:
            print(f"⏳ Request timeout")
        except Exception as e:
            print(f"❌ Error: {e}")

        time.sleep(5)
    
    print(f"❌ FAILED: App not accessible.")
    return False

if __name__ == "__main__":
    print("🚀 Simple Streamlit E2E Test")
    print("=" * 20)
    
    success = test_streamlit_app()
    
    if success:
        print("\n✅✅✅ Test PASSED!")
        sys.exit(0)
    else:
        print("\n❌❌❌ Test FAILED!")
        sys.exit(1)
