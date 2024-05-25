# pdf-ocr-cloudfunctions
This will provide you with a Cloud Storage bucket into which you can upload PDFs. They will automatically be converted to txt files and stored under the same name, with .txt appended.

To put this to use:

1. Create a new project in Google Cloud
2. Select project
3. Go to compute engine and activate the API
4. Cloud storage -> create
5. Create -> enforce public access prevention
6. Cloud functions -> create function
7. give it a name
8. trigger type: Cloud Storage
9. Bucket: select the bucket you created
10. click grant all
11. click next
12. Enable required APIs
13. select python 3.12
14. insert main.py's and requirements.txt's code
15. click deploy
