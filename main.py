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
    blob = bucket.blob(name+".txt")
    outputfile=blob.open("w")
    read_pdf = PyPDF2.PdfReader(inputfile)
    print("pagecount:"+str(len(read_pdf.pages)))
    for i in range(len(read_pdf.pages)):
        print(i)
        page=read_pdf.pages[i]
        page_content=page.extract_text()
        print(page_content)
        outputfile.write(page_content)
    outputfile.close()
    inputfile.close()
