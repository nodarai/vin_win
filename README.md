# Vin-Win

Check if given users won the national [StopCov lottery](https://stopcov.lotto.ge/).

The list of users must be provided in `vin.json`. The example of content can be found in `vin-example.json`.

## Running the script

1. Clone the project and its sub-modules:

    ```bash
    git clone --recurse-submodules git@github.com:nodarai/vin_win.git
    cd vin_win
    ```

2. Create a `.env` file with MagtiFun user and password. Example file: `.env.example`.

3. The recommended way to run the project is with [Pipenv](https://pipenv.org):

    ```bash
    pipenv install # install dependencies
    pipenv run python main.py
    ```