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

    print("in hello_gcs")


    storage_client = storage.Client()
    bucket=storage_client.bucket(bucket)
    blob = bucket.blob(name)
    inputfile=blob.open("rb")
    read_pdf = PyPDF2.PdfReader(inputfile)
    page=read_pdf.pages[0]
    page_content=page.extract_text()
    print(page_content)
    blob = bucket.blob(name+".txt")
    outputfile=blob.open("w")
    outputfile.write(page_content)
    outputfile.close()
    inputfile.close()
