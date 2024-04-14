
# Tournament Management System

This repository contains a Python script (`SwissPairing.py`) that implements a tournament management system. The system handles team pairings, match simulations, score updates, and rating adjustments based on match outcomes.

## Features

- **Team Pairings**: The system pairs teams for matches, ensuring fair matchups and minimizing repeat pairings.
- **Match Simulation**: Simulates matches between paired teams using a random probability model based on their ratings.
- **Score and Rating Updates**: Updates scores and ratings of teams based on match results.
- **Constraints Handling**: Applies constraints to keep team ratings within specified upper and lower limits.
- **Bye Team Handling**: Manages teams with byes by adjusting their ratings and scores appropriately.

## Setup

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/Tournament-management.git
   ```

2. Install the required dependencies. Ensure you have Python and pip installed. Run:

   ```bash
   pip install pandas
   ```

3. Prepare the team data:

   - Create a CSV file named `data.csv` containing team information such as Team Name, Rating, and Language of Code.
   - Ensure the CSV file is structured with appropriate columns and data types.

## Usage

1. Run the script `SwissPairing.py`:

   ```bash
   python SwissPairing.py
   ```

2. The script will load the team data from `data.csv`, perform team pairings, simulate matches, and update scores and ratings accordingly.

3. Monitor the output to see match results, updated scores, and ratings for teams.

## Limitations

- **Trade-off between Uniqueness and Similar Ratings**: Due to the algorithm's emphasis on unique pairings and fair matches, occasional repeat matchups may occur, affecting approximately 8-9 matches out of a total of 240 matches played.

## Contributing

Contributions to improve the system's functionality, efficiency, or documentation are welcome. Please follow the standard GitHub workflow:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-improvement`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push your changes to the branch (`git push origin feature-improvement`).
5. Create a new Pull Request.

## License

This project is licensed under the [MIT License](LICENSE.md).

---
