import functions_framework
import PyPDF2
from google.cloud import storage

# Triggered by a change in a storage bucket
@functions_framework.cloud_event
def hello_gcs(cloud_event):
    data = cloud_event.data

    event_id = cloud_event["id"]
    event_type = cloud_event["type"]

    bucket = data["bucket"]
    name = data["name"]
    metageneration = data["metageneration"]
    timeCreated = data["timeCreated"]
    updated = data["updated"]

    print(f"Event ID: {event_id}")
    print(f"Event type: {event_type}")
    print(f"Bucket: {bucket}")
    print(f"File: {name}")
    print(f"Metageneration: {metageneration}")
    print(f"Created: {timeCreated}")
    print(f"Updated: {updated}")


    storage_client = storage.Client()
    bucket=storage_client.bucket(bucket)
    blob = bucket.blob(name)
    with blob.open("rb") as f:
        read_pdf = PyPDF2.PdfReader(f)
        page=read_pdf.pages[0]
        page_content=page.extract_text()
        print(page_content)
    print("still here")
