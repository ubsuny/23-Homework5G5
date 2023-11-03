# Homework Task

**Take the FFT of the CO2/methane data of the most recent monthly average CO2 data of any of the the stations listed in (https://www.esrl.noaa.gov/gmd/dv/data/index.php?category=Greenhouse%2BGases&parameter_name=Carbon%2BDioxide&frequency=Monthly%2BAverages))**.

In particular fullfill three tasks (one for each group member):

**Task 1:**
- Write a function that calculates the actual frequency in useful units.
- Determine the frequency (ideally with a function) of the peak(s).

**Task 2:**
Use some combination of waveform modification (which may include padding, windowing, taking the FFT, manipulating the waveforms, inverse FFT, and undoing the window+padding), to do the following:
- Clean up either high or low frequency noise (depends on your data) in the time domain by zeroing the appropriate waveform coefficients in the frequency domain.
- Plot both the "raw" and "cleaned" spectra in the time domain.

**Task 3:**
- Write the documentation
- Reuse github actions for linting and unit tests
- write unit tests for Task1 and Task 2
  
---

For this you have to complete the following steps:

- Discuss with the other groups using issues which station data you will use. Each group should use a different one.
- Discuss in this repository using issues who will do which task (specified above)
- Discuss who should be the main responsible for the repository (the one that can accept merge requests, let me know in discord so I can adjust rights)
- Discuss and generate milestone for your project to optimize the timeline of your project
- Discuss and generate labels for your issues
- Fork this repository
- Merge the necessary fies from the original homework project into your fork
- commit
- create merge requests for your work

Also use discord for discussing solutions to any issues popping up.

## Grading

| Homework Points                  |                |              |            |
| -------------------------------- | -------------- | ------------ | ---------- |
|                                  |                |              |            |
| Interaction on own project       |                |              |            |
| Category                         | min per person | point factor | max points |
| Commits                          | 6              | 1            | 6          |
| Merge requests                   | 3              | 1            | 3          |
| Merge Accepted                   | 1              | 1            | 1          |
| Branches                         | 2              | 0.5          | 1          |
| Issues                           | 10             | 0.5          | 5          |
| Closed Issues                    | 5              | 0.2          | 1          |
| \# Conversations                 | 30             | 0.2          | 6          |
|                                  |                |              |            |
| Total                            |                |              | 23         |
|                                  |                |              |            |
| Shared project points            |                |              |            |
| \# Label                         | 5              | 0.2          | 1          |
| \# Milestones                    | 2              | 1            | 2          |
| \# Tags                          | 0              | 1            | 0          |
|                                  |                |              |            |
| Total                            | 7              |              | 5          |
|                                  |                |              |            |
|                                  |                |              |            |
| Interaction on others project(s) |                |              |            |
| Category                         | min per person | point factor | max points |
| Commits                          | 3              | 1            | 3          |
| Branches                         | 1              | 0.5          | 0.5        |
| Issues                           | 9              | 0.5          | 4.5        |
| \# Conversations                 | 15             | 0.2          | 3          |
|                                  |                |              |            |
| Total                            | 22             |              | 11         |
|                                  |                |              |            |
| Result                           |                |              |            |
| Task completion                  | 5              | 1            | 5          |
|                                  |                |              |            |
| Sum                              |                |              | 42         |
