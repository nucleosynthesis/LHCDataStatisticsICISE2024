# Exercise 1 - Datasets, Selections and Histograms

For the exercises, we will use a simplified version of a [CMS analysis](https://link.springer.com/content/pdf/10.1007/JHEP09(2017)051.pdf) to measure the production cross-section of top-quark / anti-top-quark pairs - $\sigma_{tt}$ - in proton-proton collisions at a centre of mass energy of 13 TeV. We will be using real data from the CMS experiment, taken in 2015 during Run 2 of the LHC. The code is based on the CMS open data workshop linked [here](https://cms-opendata-workshop.github.io/workshopwhepp-lesson-ttbarljetsanalysis/), which you can read through if you are interested. 

The image below is a Feynman diagram of the process we are interested in measuring, namely $t\bar{t}\rightarrow (bW^{+})(bW^{-})\rightarrow bq\bar{q}bl^{-}\bar{\nu}_{l}$ - the lepton+jets final state. 

![TT lepton + jets Feynman Diagram](images/ttbar_diagram.png)

In our example, we will focus on the case where the lepton $l$ is an electron or muon.  In the CMS detector, these leptons are extremely well measured and are very good for "triggering" the events that we are interested in. Looking at the final state, we would also expect to see 4 hadronic jets, two of which will be $b-$jets, and missing transverse momentum from the neutrino which isn't detected.   