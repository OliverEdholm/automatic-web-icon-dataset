# Automatic icon dataset

### Summary
Scraping top N websites on the Alexa ranking, downloading all images, filtering based on if the image is a natural photograph or a computer graphic and other smaller sanity checks. All the attributes of every image tag is saved in an adjacent JSON file.

### Running
`python3 -m bin.build_icon_dataset TOP_N OUT_DIRECTORY_PATH N_PROCESSES`

### Ways of determining if an image is a natural photograph or a computer graphic
* Setting a threshold on how many unique colors a very small bilinearly resizes grayscale image has
* Measuring loss after compressing with JPEG, PCA or similar
* ConvNets 

### Relevant papers
#### Creating datasets based on filtering large amounts of websites
* Conceptual Captions: A New Dataset and Challenge for Image Captioning
#### Natural photograph or computer graphic classification
* Distinguishing Computer-generated Graphics from Natural Images Based on Sensor Pattern Noise and Deep Learning
* Distinguishing Computer Graphics from Natural Images Using Convolution Neural Networks
* Distinguishing Computer Graphics from Photographic Images Using Local Binary Patterns

### Author
Oliver Edholm, 17 years old