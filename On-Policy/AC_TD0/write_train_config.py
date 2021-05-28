import json

dictionary = {}
dictionary['env'] = "CartPole-v1"
dictionary['gamma'] = 0.99
dictionary['iterations'] = 1000
dictionary['episode_length'] = None
dictionary['numpy_seed'] = 1
dictionary['environment_seed'] = 1
dictionary['pytorch_seed'] = 1
dictionary['render'] = False
dictionary['rewards_path'] = 'cartpole_rewards.json'
dictionary['record'] = False
dictionary['recording_path'] = 'cartpole_recording/'
dictionary['recording_frequency'] = 10
dictionary['actor'] = {}
dictionary['actor']['hidden_layer_neurons'] = [16]
dictionary['actor']['learning_rate'] = 0.001
dictionary['actor']['load'] = False
dictionary['actor']['load_path'] = 'model/actor_final.pkl'
dictionary['actor']['initial_save_path'] = 'model/actor_initial.pkl'
dictionary['actor']['final_save_path'] = 'model/actor_final.pkl'
dictionary['critic'] = {}
dictionary['critic']['hidden_layer_neurons'] = [64,64]
dictionary['critic']['learning_rate'] = 0.005
dictionary['critic']['load'] = False
dictionary['critic']['load_path'] = 'model/critic_final.pkl'
dictionary['critic']['initial_save_path'] = 'model/critic_initial.pkl'
dictionary['critic']['final_save_path'] = 'model/critic_final.pkl'
dictionary['learning_rate_scheduler'] = {}
dictionary['learning_rate_scheduler']['required'] = True
dictionary['learning_rate_scheduler']['schedule'] = [[(400,500),{'lr_A':0.000001,'lr_C':0.000001}]]


with open('train_config.json', 'w') as fp:
    json.dump(dictionary, fp, indent=4)