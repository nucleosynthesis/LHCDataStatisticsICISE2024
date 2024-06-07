!!! tip "Challenge" 
    In the online documentation, on [Goodness of fit tests](https://cms-analysis.github.io/HiggsAnalysis-CombinedLimit/latest/part3/commonstatsmethods/#goodness-of-fit-tests), you can find instructions for calculating $p$-values using toys rather than relying on asymptotic methods. Calculate the $p$-values for the two cases using the saturated algorithm.


#Information for signal search 
 events = NanoEventsFactory.from_root(
    'root://eospublic.cern.ch//eos/opendata/cms/derived-data/POET/23-Jul-22/RunIIFall15MiniAODv2_TprimeTprime_M-700_TuneCUETP8M1_13TeV-madgraph-pythia8_flat/D0C3325F-026B-4069-87AA-F0815FE788DB_flat.root'
    , schemaclass=AGCSchema, treepath='events').events()

filter_eff = 1 
xsex = 0.455 # pb for 700 GeV Tprime 
nevts_blah = 253993