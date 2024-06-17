# Exercise 3 - Control Regions and Systematic Uncertainties

Launch the `cms_combine` container by typing the following into a terminal on your laptop (or by clicking the play button next to the cms_combine container in the Docker desktop application and using the terminal there).
```sh
docker start -i cms_combine
```

In today's exercise, we are going to use our 4j0b control region that we populated at the end of exercise 2 to constrain our `wjets` process in our 4j2b signal region. Don't worry if you didn't manage to process the samples to create the histograms for the 4j0b region. I have put a `.csv` file  `exercise2solutions/allregions_mbjj.csv` that has both the signal region and control region histograms for you. You'll also find the datacard for the signal region in the same folder: `signalregion_mbjj.txt`. 

## Control region datacard 

First, we need to create a new datacard for our 4j0b control region. This will look very similar to our signal region datacard except that we need to change the name of the channel and point to the right histograms in the file. Copy the text below into a new text file, i've called mine `controlregion_mjjj.txt`

```
imax 1
jmax 4
kmax 0
# -----------------------------------------------------------------------------------------
shapes data_obs controlregion allregions_mbjj.csv controlregion:data:nominal,sum_w:sum_ww
shapes *        controlregion allregions_mbjj.csv controlregion:$PROCESS:nominal,sum_w:sum_ww 
# -----------------------------------------------------------------------------------------
bin         controlregion
observation -1
# -----------------------------------------------------------------------------------------
bin         controlregion controlregion       controlregion      controlregion  controlregion
process     ttbar         single_atop_t_chan  single_top_t_chan  single_top_tW  wjets
process     0             1                   2                  3              4
rate        -1            -1                  -1                 -1             -1
# -----------------------------------------------------------------------------------------
wjets_norm rateParam controlregion wjets 1 [0,5]
```

Notice how the `shapes` lines are now pointing to the `controlregion` histograms in the `allregions_mbjj.csv` file. The names of the channel everywhere has also changed to `controlregion`. This tells combine that this data are independent from the data in our signal region. Finally, the last line of the datacard, 
```
wjets_norm rateParam controlregion wjets 1 [0,5]
```
tells combine to create a parameter called `wjets_norm` that modifies the rate of the `wjets` process in the `controlregion`. By naming this parameter the same as the one in our signal region datacard, this parameter will simultaneously scale the `wjets` process in both regions!

Now we need to create a single datacard that contains the information for both the signal region and the control region. We do not need to do this by hand since the package comes with a tool that does this for us. To create combined datacard, we can run the following, 

```sh
combineCards.py signalregion=signalregion_mbjj.txt controlregion=controlregion_mjjj.txt > combined.txt 
```

Let's look at the resulting datacard (below)
```
Combination of signalregion=signalregion_mbjj.txt  controlregion=controlregion_mjjj.txt
imax 2 number of bins
jmax 4 number of processes minus 1
kmax 0 number of nuisance parameters
----------------------------------------------------------------------------------------------------------------------------------
shapes *              controlregion  allregions_mbjj.csv controlregion:$PROCESS:nominal,sum_w:sum_ww
shapes data_obs       controlregion  allregions_mbjj.csv controlregion:data:nominal,sum_w:sum_ww
shapes *              signalregion   allregions_mbjj.csv signalregion:$PROCESS:nominal,sum_w:sum_ww
shapes data_obs       signalregion   allregions_mbjj.csv signalregion:data:nominal,sum_w:sum_ww
----------------------------------------------------------------------------------------------------------------------------------
bin          signalregion   controlregion
observation  -1             -1           
----------------------------------------------------------------------------------------------------------------------------------
bin          signalregion        signalregion        signalregion        signalregion        signalregion        controlregion       controlregion       controlregion       controlregion       controlregion     
process      ttbar               single_atop_t_chan  single_top_t_chan   single_top_tW       wjets               ttbar               single_atop_t_chan  single_top_t_chan   single_top_tW       wjets             
process      0                   1                   2                   3                   4                   0                   1                   2                   3                   4                 
rate         -1                  -1                  -1                  -1                  -1                  -1                  -1                  -1                  -1                  -1                
----------------------------------------------------------------------------------------------------------------------------------
wjets_norm    rateParam signalregion wjets 1 [0,5]
wjets_norm    rateParam controlregion wjets 1 [0,5]
```

We now see that all of the information has been combined into a single datacard! at the top of the datacard, we see that the datacard is a result of the *combination* of our two original datacards, and the numbers `imax`, `jmax` and `kmax` have automatically been updated for us. 

!!! Warning
    In the combined datacard, both the signal region and control region histograms are taken from the same file `allregions_mbjj.csv`, this is because I have changed the `shape` lines in my signal region datacard to read 
    ```
    shapes data_obs signalregion allregions_mbjj.csv signalregion:data:nominal,sum_w:sum_ww
    shapes *        signalregion allregions_mbjj.csv signalregion:$PROCESS:nominal,sum_w:sum_ww 
    ```
    You do not have to do this if you created the signal region and control region histograms in separate `.csv` files. 

This datacard can now be used as the input to out `combine` commands to perform fits and calculate uncertainties as we did when we only had a single datacard. 

!!! Question 
    Run the fit diagnostics method on the combined datacard to calculate the best fit value for the signal strength parameter `r`. How does this compare to the two results we obtained with a single datacard? Make a plot of the post-fit distributions and the data in the two regions from this new fit. Remember to add the option `-n name` to create a different name for the output file to avoid writing over your original outputs from combine.  

/// details | Show answer
We can run the same commands as before, but this time we provide the combined datacard as the input. For the best fit,
```sh
combine combined.txt -M FitDiagnostics --saveShapes --saveWithUncert -n Combined
```
with the result as, 
```
--- FitDiagnostics ---
Best fit r: 0.917371  -0.00376498/+0.00377766  (68% CL)
```
The result and uncertainty is much closer to the version of the datacard without the freely floating `wjets_norm` parameter. This means we've successfully managed to recover the constraint on the `wjets_norm` parameter by using the data in the 4j0b control region!
You can use the same code from Exercise 2 to plot each of the regions from the result file `fitDiagnosticsCombined.root`
///

## Systematic Uncertainties

In our fits so far, we have assumed that the distributions and rates determined from the simulated events represent perfectly what we would expect to see in data. Of course, reality is never quite that easy and every step of any real data analysis will involve some assumption about how well we can model a particular effect. Each of these assumptions comes with some uncertainty and these uncertainties impact the predicted yields and distributions - we call them "systematic uncertainties". These could range from uncertainties in the theoretical cross-sections used to normalise the samples, uncertainties in the efficiency of the trigger or event selection, energy scale and other calibrations used to reconstruct the particles or even the uncertainty on the integrated luminosity of our data set!

The vast majority of the time spent doing a real LHC data analysis is carefully understanding which uncertainties effect any particular measurement and how large they are. Often, a lot of work is put into reducing these uncertainties (or rather their effect on the measurement) as much as possible to get the best measurements from the data. We don't have time in these exercises to properly calculate the effects of all the different systematic uncertainties that we should consider, but we will take a look at a few simple ones and include them in our analysis. 

### Rate uncertainties 

The simplest form of systematic uncertainties are those that affect the overall predicted rate of a given process. The first one we will look at is the uncertainty in the integrated luminosity. 



 
=== "python"
    ```python
    from root2py import *
    import ROOT
    file   = ROOT.TFile.Open("fitDiagnosticsCombined.root")
    fit_res = convertFitResult(file.Get("fit_s"))
    print(fit_res)
    ```

=== "pyROOT"
    ```python
    import ROOT
    file   = ROOT.TFile.Open("fitDiagnosticsCombined.root")
    fit_res = file.Get("fit_s")
    fit_res.Print()
    ```