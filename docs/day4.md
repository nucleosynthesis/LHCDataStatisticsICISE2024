#Information for signal search 
 events = NanoEventsFactory.from_root(
    "root://eospublic.cern.ch//eos/opendata/cms/derived-data/POET/23-Jul-22/RunIIFall15MiniAODv2_TprimeTprime_M-1200_TuneCUETP8M1_13TeV-madgraph-pythia8_flat/5A744C3D-EA4C-4C35-9738-BF878E063562_flat.root",
    , schemaclass=AGCSchema, treepath='events').events()

filter_eff = 1 
xsex = 0.0118 # pb for 1200 GeV Tprime 
nevts_blah = 253993


obsbins=np.arange(500,2050,80)

lumi uncertainty in 2015 - 2.2% 