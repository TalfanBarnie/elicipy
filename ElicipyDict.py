elicitation_name = 'test'

# datarepo can be 'local' or 'github'
datarepo = 'local'

# if datarepo is 'github' you need user and token to access it
# user = ''
# github_token = ''

# folder or repository with data
Repository = 'createWebform'

output_dir = 'OUTPUT'

# comment if there is ony one language
#language = 'ITA'

analysis = True
target = True

target_list = [2,3]
seed_list = [1,2]

n_sample = 5000
n_bins = 10

# hist_type: 'bar' or 'step'
hist_type = 'bar'

# EW_flag (equal weights):
# 0 - no EW
# 1 - EW 
EW_flag = 1

# ERF_flag: 
# 0 - no ERF
# 1 - ERF original 
# 2 - ERF modified
ERF_flag = 1

# 
Cooke_flag = 1

# parameters for Cooke

# significance level (this value cannot be higher than the
# highest calibration score of the pool of experts)
alpha = 0.05  

# overshoot for intrinsic range
overshoot = 0.1  

# global cal_power
# this value should be between [0.1, 1]. The default is 1.
cal_power = 1  


