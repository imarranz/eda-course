# EDA_Course


## Exploratory Data Analysis Course

## Table of Content

  * data: A csv file with data.
    * 2018\_Central\_Park\_Squirrel\_Census\_-\_Squirrel\_Data.csv
  * documents: pdf files 
  * images: images for presentation
    * Data_in_Support_of_Enhancing_Metabolomics_Research_Through_Data_Mining.pdf
    * Robinson-icebreaker.pdf
  * ipynb: Jupyter notebbok and slides
    * presentation.ipynb
    * presentation_slides.html
  * notes: 
    * nbconvert.txt: command to generate the html slides
  * scripts: Python scripts and R scripts
    * dataframe\_outlier\_pca.py
    * dataframe\_outlier.py
    * distances.py
    * heterocedasticidad\_no\_normalidad.py
    * heterocedasticidad.py
    * mahalanobis\_example\_01.py
    * mahalanobis\_example\_02.py
    * pca.py
    * qqplot.py
    * tboxcox.R  

### Generate Slides

```
jupyter nbconvert presentation.ipynb --to slides --reveal-prefix reveal.js --no-prompt --SlidesExporter.reveal_theme=white --SlidesExporter.reveal_transition=slide --TagRemovePreprocessor.remove_input_tags={\"hide\"}
```

### Git Clone

How to access the course via git

```
git clone https://github.com/imarranz/EDA_Course.git
```

How to acces the course via web

https://github.com/imarranz/EDA_Course
