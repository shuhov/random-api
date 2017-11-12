
# our base image
FROM python:2.7.14-onbuild

# specify the port number the container should expose
EXPOSE 5000

# run the application
CMD ["sh", "./run.sh"]
