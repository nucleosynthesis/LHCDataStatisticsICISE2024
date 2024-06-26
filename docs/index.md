---
hide:
 - toc
---

# INTRODUCTION

This is the webpage for the lecture series on Data Analysis and Statistics at the LHC. In these pages, you can find links to the lectures as well as exercises for you to explore a typical data analysis at CMS. 
You should be familiar with simple programming in Python, however, the examples should give you enough information to produce the desired output even if you don't know much Python. 

There are four sets of exercises in these pages that you can find under the Exercises tab, one for each day of the course. You should read through the information given and copy code/commands where prompted into your own terminal or notebook. 

!!! Question
    Throughout the exercises, there will be questions in a green box like this that contains a challenge for you to try on your own. Below, there will be a solution in a blue box for you to check against your own answer or in case you get really stuck. Please do try on your own before revealing the solution. 

<details>
<summary><b>Show answer</b></summary>
The answer will be shown here
</details>

!!! tip "Challenge"
    If you are feeling especially confident, you can have a go at extra challenges that I have put in these turquoise boxes. I won't provide a solution for these challenges, but you don't need to complete them to progress through the other exercises. 

!!! Warning 
    Sometimes, there will be some technical or conceptual hurdle that requires a bit of careful thought to work around. I have tried to point these out to you in orange boxes like this one to help avoid any major road blocks. 

Throughout the exercise, you will see code blocks like the ones below. Those that are labelled as **Text only** are either output from some command or they are text that you can copy (eg Datacards), 

```
This is just simple text
```

Those labeled with **Bash**, indicate commands that can be typed into your Terminal and executed there, 
```sh
echo "Hello! I am in a bash terminal"
```

and those with **Python** as the label indicate python code that can be run inside a Jupyter notebook
```python
# This is python code
def printHello():
	print("Hello!")
printHello()
```

For all of these, there is a copy icon in the top right that you can use to copy the entire contents of the block. 

## Getting started (Pre-Course)

We are going to need some software for the exercises. All of the software required is available pre-packaged in container images that you can run using Docker! Head over to the [Getting Started](https://nucleosynthesis.github.io/LHCDataStatisticsICISE2024/setup/) pages now to install Docker and obtain the relevant images. This can take some time so please do this **before** the start of the lecture course. 

## Useful Links 

You can find more useful information about the software we will be using below 

  * [Docker](https://www.docker.com/): Docker is a desktop client for running the container images that we will be using for these exercises.  
  * [CMS Open Data](https://cms-opendata-guide.web.cern.ch/): The CMS Collaboration regularly releases open datasets for public use. This link is the CMS Open Data Guide
  * [Combine](https://cms-analysis.github.io/HiggsAnalysis-CombinedLimit/v9.2.X/): The Combine tool is the main statistical analysis software package used by the CMS Collaboration. It is based on the ROOT/RooFit software packages, however for these exercises, you do not need to be an expert user of these packages. 


## About the Author

[Dr. Nicholas Wardle](https://www.imperial.ac.uk/people/n.wardle09/) is a lecturer in Physics at Imperial College London. He is also a member of the CMS Collaboration and his research is focused on statistical methods for data analysis and searches for BSM physics through precision measurements of Higgs boson properties. 
