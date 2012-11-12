started: 12.11.2012

author: Dmitry Khodakov (dmitryhd@gmail.com)

Simple in use frontend for ns-3 experiments to make workflow easier.

Design:

experiment:
  - set of EXPERIMENT_COMMAND_TEMPLATE
  - set of EXPERIMENT_PARAMETERS 
  - set of EXPERIMENT_OUTPUT_FILES
  - to form EXPERIMENT_RUN_COMMAND =  EXPERIMENT_COMMAND_TEMPLATE <-  EXPERIMENT_OUTPUT_FILES <- EXPERIMENT_PARAMETERS
  - set of POSTPROCESSING_COMMAND_TEMPLATE
  - set of POSTPROCESSING_PARAMETERS
  - to form POSTPROCESSING_RUN_COMMAND = POSTPROCESSING_COMMAND_TEMPLATE <- POSTPROCESSING_PARAMETERS <- EXPERIMENT_OUTPUT_FILES

actions:
  - form experiment stored in .py file
  - add any of experiment parameters
  - change any of experiment parameters
  - save history (various experiments)

Usage:

./telexp.py add exp "expname"
./telexp.py exp "expname" set value1 100

