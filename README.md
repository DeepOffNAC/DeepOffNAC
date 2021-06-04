## A Deep Off-Policy Natural Actor-Critic Algorithm

To generate a configuration file for a given algorithm run the following command on write_train_config.py file present in the folder of that algorithm
```bash
python3 write_train_config.py
```
Configuration file can be edited as per the need

Once the configuration file is ready, run the main python code of the algorithm with path to configuration file as command line argument. For example
```bash
python3 NAC_TD0.py train_config.json
```

Configuration files for some of the games with tuned hyperparameters are already present in the repository.
<!---
DeepOffNAC/DeepOffNAC is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->
