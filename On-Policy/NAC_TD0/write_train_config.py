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
dictionary['advantage_critic'] = {}
dictionary['advantage_critic']['learning_rate'] = 0.001
dictionary['advantage_critic']['load'] = False
dictionary['advantage_critic']['load_path'] = 'model/a_critic_final.pkl'
dictionary['advantage_critic']['initial_save_path'] = 'model/a_critic_initial.pkl'
dictionary['advantage_critic']['final_save_path'] = 'model/a_critic_final.pkl'
dictionary['value_critic'] = {}
dictionary['value_critic']['hidden_layer_neurons'] = [64,64]
dictionary['value_critic']['learning_rate'] = 0.01
dictionary['value_critic']['load'] = False
dictionary['value_critic']['load_path'] = 'model/v_critic_final.pkl'
dictionary['value_critic']['initial_save_path'] = 'model/v_critic_initial.pkl'
dictionary['value_critic']['final_save_path'] = 'model/v_critic_final.pkl'
dictionary['learning_rate_scheduler'] = {}
dictionary['learning_rate_scheduler']['required'] = True
dictionary['learning_rate_scheduler']['schedule'] = [[(499,500),{'lr_A':0.00001,'lr_A_C':0.00001,'lr_V_C':0.00001}]]


with open('train_config.json', 'w') as fp:
    json.dump(dictionary, fp, indent=4)