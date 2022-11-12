# Video Assistant for the Visually Impaired 
## Abstract

Visually impaired (VI) individuals all over the world have difficulty navigating their surroundings. Practical assistance systems for scene text recognition (STR) have made it possible for VI persons to receive text information from their surroundings in recent years. The focus of this paper is on recognizing scene text (which includes alpha-numeric characters) from real-time video natural scenes, which is subsequently translated into speech and read out to the VI user. To do this, the performance of two methodologies—a Deep Learning-based end-to-end scene text detection and recognition model called Convolutional Recurrent Neural Network (CRNN) and an independent OCR text detection and recognition model (EasyOCR)—is compared. A collection of scene text images is used to evaluate both models, and the results of their text prediction are recorded. The model that makes the most accurate predictions is then integrated as the recognition model for the real-time video feed. The evaluation revealed that the EasyOCR model was the most accurate at making predictions, therefore it was utilized.

Keywords:
Scene Text Recognition; Real-Time Video Scene Text Recognition; Convolutional Recurrent Neural Network (CRNN); EasyOCR; Text to Speech; Video Assistant; Visually Impaired

## Introduction

Experts use the term "visual impairment" to characterize any vision loss, whether whole or partial blindness, that cannot be corrected with eyeglasses or contact lenses. VI individuals frequently rely on others for information that should have been received via their eyes, and their loss of vision is accompanied by a loss of independence. To meet the needs of the VI community, a text recognition system must be developed that can recognize and extract text from surrounding scenes without the help of others. 

The text written on billboards, buildings, banners, and clothes, is known as scene text i.e., non- document text. Recognizing Scene Text is what is needed for VI users as this is the text in all outdoor areas that they’re unable to navigate. Scene Text Recognition (STR) is more challenging than standard text recognition, which transcribes characters or words from scanned documents, due to a range of issues such as font and colour variations, lighting, distortion, occlusion, low resolution, cluttered background, and so on.

## Aim
The aim of this paper is to accurately detect and recognize scene text from real- time video feed and convert it to audible sound for the VI user. This aim consists of many subparts which include:
* Building a CRNN model and training it on a synthetic word dataset (MJSynth).
* Implementing EasyOCR which is built with Python and Pytorch deep learning.
* Testing both models on a new dataset containing unseen scene text images of Good, Medium and Bad Quality. 
* Evaluating the models based on their results of accurately recognizing the text present in the scene text images dataset.
* The model with the most accurate performance will be singled out as the model to detect scene text from live video feed.
* For the real-time video text recognition, the surrounding digital video from a webcam is transformed into image scene text       frame by frame.
* Scene text image from the video is then fed into the STR model which performs text recognition on the image.
* The model displays the text detection (bounding boxes) and recognition (actual text) on the screen.
* The text recognized is transformed into and made audible for the VI user using python pyttx3.

## Flowchart of Proposed System
<img src="https://user-images.githubusercontent.com/93089387/201490624-809ab00d-b008-414d-a516-9a3c6ad95b98.png" alt="FlowChartHonorsProject-Page-2 drawio (1)" width="500"/>

## Results
### CRNN
#### Good Quality Dataset
<p float="left">
  <img width="300" alt="image" src="https://user-images.githubusercontent.com/93089387/201490847-ca8bc09e-f238-48ea-9171-379320318d93.png">
  <img width="300" alt="image" src="https://user-images.githubusercontent.com/93089387/201491170-0715f3f7-b3db-4192-9df4-e6b03906dbae.png">
</p>


#### Medium Quality Dataset
<p float="left">
  <img width="300" alt="image" src="https://user-images.githubusercontent.com/93089387/201491201-0721de40-cbd5-43c1-b96d-f4c73bf8f329.png">
  <img width="300" alt="image" src="https://user-images.githubusercontent.com/93089387/201491206-10eaac3b-22ec-40fd-a0ef-739895187c1c.png">
</p>

#### Bad Quality Dataset
<p float="left">
  <img width="300" alt="image" src="https://user-images.githubusercontent.com/93089387/201491285-53966040-0f09-4cfc-a03f-97140096fa46.png">
  <img width="300" alt="image" src="https://user-images.githubusercontent.com/93089387/201491292-f1521bc4-671f-4d87-9eb1-66ca4d024f85.png">
</p>


### EasyOCR
#### Good Quality Dataset
<p float="left">
  <img width="300" alt="image" src="https://user-images.githubusercontent.com/93089387/201491328-7543e818-09b8-43f0-beb8-5b09874aa357.png">
 <img width="300" alt="image" src="https://user-images.githubusercontent.com/93089387/201491333-1a45c143-7406-4b09-8b99-7de72b8a393e.png">
</p>


#### Medium Quality Dataset
<p float="left">
 <img width="300" alt="image" src="https://user-images.githubusercontent.com/93089387/201491360-ea55857d-d289-4b66-8f18-d60cf19d59c8.png">
<img width="300" alt="image" src="https://user-images.githubusercontent.com/93089387/201491353-1c0017fb-1496-4b8d-9fee-6e8d011e2b08.png">
</p>

#### Bad Quality Dataset
<p float="left">
  <img width="300" alt="image" src="https://user-images.githubusercontent.com/93089387/201491382-df0ae7e8-d887-403f-8d94-c39ec6722e8b.png">
  <img width="300" alt="image" src="https://user-images.githubusercontent.com/93089387/201491374-b2c877b1-ecfe-4878-b8bc-7b1183fb99ba.png">
</p>

## Real-Time Video Scene Text Recognition
The project's objective of accurately identifying and audibly rendering Scene Text for VI users from Real-Time video feed was accomplished. 
<p float="left">
 <img width="200" alt="image" src="https://user-images.githubusercontent.com/93089387/201491600-42bc2dba-00ed-42b5-8061-a42e52c13d80.png">
 <img width="200" alt="image" src="https://user-images.githubusercontent.com/93089387/201491602-bf52489b-8073-4889-85c3-0dad6e9661b5.png">
 <img width="200" alt="image" src="https://user-images.githubusercontent.com/93089387/201491604-caf69f10-b741-4fd3-b7cd-04e65eab4ee2.png">
</p>

## Conclusion
*	The project's objective of accurately detecting and recognizing Scene Text from Real-Time video feed and rendering it audible for VI users has been achieved. Python's EasyOCR OCR model is used to accomplish this functionality successfully.
*	When compared to a deep learning model with CRNN architecture, which combines CNN and RNN, EasyOCR showed to be the more successful model, leading to the selection of this recognition method.
*	Both the CRNN and EasyOCR models were tested on three datasets containing ten images each which ranged from Bad, Medium, and Good quality.
*	The evaluation of the models led to EasyOCR having an accuracy of 10% on Bad quality Scene Text images, 30% on Medium quality Scene Text Images and 50% on Good quality Scene Text images.
*	These results triumphed over the CRNN model which only accurately recognized text in one image across all three datasets of Scene Text images.
*	Using Python's text-to-speech module, pyttsx3, the Scene Text recognized from Real-Time video was then turned into audible speech for the VI user. 

## Hardware Specifications
Because the use of a GPU significantly reduces the training time for text recognition systems, Google Colab was employed to train the CRNN model. The CRNN and EasyOCR models were both also tested on Google Colab. The deployment of the Real-Time Video Text Recognition was done on the PyCharm IDE as it allows direct access to your machines webcam. Python was used for all programming. The entire software system was written and run on a 128-bit macOS system 11.0.1 (20B29), with 8 GB RAM and an Apple M1 processor, running at 3.2 GHz.


