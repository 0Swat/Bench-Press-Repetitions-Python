
# Project Title: Impact of 5 Factors on Bench Press Repetitions
## Description

This program simulates the effect of various factors (sleep, previous training, caffeine intake, warm-up, shoulder injury) on the number of repetitions during a strength training session. It generates random data based on these factors and calculates the number of repetitions, then creates plots and histograms for result analysis.

**Note:** The weight and number of repetitions are predefined at 74 kg and 15 repetitions, respectively. The program's code can be modified to simulate with data loaded at runtime.

## Stages  
**Stage 1 - Sleep (Discrete Distribution):**

    Option 1: Chance < 0.25 (Slept less than 6 hours)
    Option 2: Chance 0.25 - 0.50 (Slept between 6-7 hours)
    Option 3: Chance 0.50 - 0.75 (Slept between 8-9 hours)
    Option 4: Chance > 0.75 (Slept more than 9 hours)

**Stage 2 - Previous Training (Discrete Distribution):**

    Option 1: Chance < 0.05 (Trained today or yesterday)
    Option 2: Chance 0.05 - 0.65 (Trained 2 to 3 days ago)
    Option 3: Chance 0.65 - 0.9 (Trained 4 to 7 days ago)
    Option 4: Chance > 0.9 (Trained more than 7 days ago)

**Stage 3 - Caffeine (Discrete Distribution):**

    Option 1: Chance < 0.1 (No caffeine intake before training)
    Option 2: Chance 0.1 - 0.8 (Took 200 mg of caffeine before training)
    Option 3: Chance > 0.8 (Took 400 mg of caffeine before training)

**Stage 4 - Warm-up (Discrete Distribution):**

    Option 1: Chance < 0.1 (No warm-up)
    Option 2: Chance 0.1 - 0.55 (Warm-up between 15 to 30 minutes)
    Option 3: Chance 0.55 - 0.8 (Warm-up between 30 to 45 minutes)
    Option 4: Chance > 0.8 (Warm-up more than 45 minutes)

**Stage 5 - Shoulder Injury (Continuous Distribution):**

    Option 1: Chance < ~0.97 (No shoulder injury)
    Option 2: Chance > ~0.97 (Shoulder injury - termination of bench press)
    Note: The chance of injury may increase if the response at stage 2 or 4 is option 1.

*After running the simulation, the program generates plots and histograms for result analysis.*
## Installation

No specific installation instructions provided. Adjust according to your programming environment and dependencies.
## Usage

Run the program in your preferred development environment. Modify the weight and max repetitions variables if needed to simulate different conditions.
## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
## License

MIT

## Credits

Author: *Oskar Swat*

## Extras

<img src="https://i.imgur.com/wPV1n1c.jpeg" width="1000px"/>

<img src="https://i.imgur.com/gpn3JHo.jpeg" width="1000px"/>



