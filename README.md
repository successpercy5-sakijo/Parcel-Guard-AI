# AI Based Parcel Damage Detection System

## Project Overview

This project proposes an AI-based computer vision system for Takealot to detect and document visible damages to parcel packaging 

## Business Problem

E-commerce businesses process a large number of returns, refunds and replacement requests. When a customer reports that a product arrived damaged it can be difficult to detemine when the damage occured This can create challanges when investigating damage claims and may result in unnecessary refunds, replacements and additional operation costs

## Proposed Solution

We propose an AI powered parcel damage detection system that uses computer vision to analyse images of parcel packaging. The system will classify the parcel as either damaged or intact and access it's condition before parcel is sent out for delivery 

The system will :
- Capture an image of the parcel
- Detect visible external packaging damages
- Classify the parcel as damaged or intact
- Record the parcel condition
- Support the investigation of damage-related returns and refunds

## Proposed Process

The parcel is packaged at the warehouse 
The packaged parcel is placed on a convveyor belt inside the takealot warehouse
As the parcel passes through the scanning area, a camaera captures an image of the parcle
The AI system analyses the image and classifies the parcel as damaged or intact
If the parcel is detected as damaged, it is removed from the normal conveyor flow and sent for staf inspection and repackaging if necessary
If the parcel is detected as intact, it continues through the normal disoatch process

## Dataset

The project will use an imaged based dataset with examples of damaged and intact packaging. The dataset will be used to train and evaluate the computer vision model's ability to identify visible damages to parcel packaging 

## Technologies

- Python
- Computer vision
- Machine learning / Deep learning
- Convolutional Neural Network
- Github


