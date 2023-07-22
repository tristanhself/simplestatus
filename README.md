# simplestatus
Simple Status - A Simple HTML Based Status Page Tool

v1.0 - 22/07/2023 - Luke Burling and Tristan Self

A simple HTML based status page tool that allows you as a system administrator to just edit a CSV file and have the tool generate you a pre-formatted HTML status page that you can upload to your favourite website.

The tool uses Python to read the CSV files for the status (of services) and any upcoming maintenance activities, it then renders the page ready for upload.

The tool is intended to be used within a Gitlab CI/CD pipeline and also uses AWS for the publishing of the generated site. It makes use of docker containers to create the environment to run python (to generate the page) and then uses the AWS CLI docker container to upload the content to AWS S3 bucket for publishing via AWS CloudFront.

For installation instructions please see: [Simple Status - A Simple HTML Based Status Page Tool](https://geekmungus.co.uk/?p=3844)
