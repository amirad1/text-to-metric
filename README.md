# Text To Metric with python 
### text to metric is a simple python app that crawl into your text file and exposes every line as a metric for prometheus

## Building the image

docker build . -t textometric

docker tag textometric <your-registry/repo:tag>

docker push <your-registry/repo:tag>

## Deploying the image

