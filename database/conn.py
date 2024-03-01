import os
from supabase import create_client, Client

# url: str = os.environ.get("https://jjhcgfkksochzqcqnbvo.supabase.co")
# key: str = os.environ.get("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImpqaGNnZmtrc29jaHpxY3FuYnZvIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcwNzQ2OTczOCwiZXhwIjoyMDIzMDQ1NzM4fQ.38NmKB5_K6t-1squH4HuhP1G5pQdThGBNYUzewSN7As")
# supabase: Client = create_client(url, key)

url = "https://jjhcgfkksochzqcqnbvo.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImpqaGNnZmtrc29jaHpxY3FuYnZvIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcwNzQ2OTczOCwiZXhwIjoyMDIzMDQ1NzM4fQ.38NmKB5_K6t-1squH4HuhP1G5pQdThGBNYUzewSN7As"

supabase: Client = create_client(url, key)
