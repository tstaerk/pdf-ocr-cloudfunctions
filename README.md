# pdf-ocr-cloudfunctions
This will provide you with a Cloud Storage bucket into which you can upload PDFs. They will automatically be converted to txt files and stored under the same name, with .txt appended.

To put this to use:

1. Create a new project in Google Cloud
2. Select project
3. Go to compute engine and activate the API
4. Cloud storage -> create
5. Enter bucket name -> Create -> enforce public access prevention
6. Cloud functions -> create function
7. if being prompted, enable all required APIs
8. give a name to the Cloud Function
9. trigger type: Cloud Storage
10. Bucket: select the bucket you created
11. click grant all
12. click next
13. Enable required APIs
14. select python 3.12
15. insert main.py's and requirements.txt's code
16. click deploy
