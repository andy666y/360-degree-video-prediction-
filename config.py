# configurations
from easydict import EasyDict as edict
__C = edict()
cfg = __C

__C.training_epochs = 30 #300
# DataIO
__C.use_xyz = True
__C.use_phi_theta = False
__C.use_yaw_pitch_roll = False
__C.use_cos_sin = False
__C.process_in_seconds = True
__C.batch_size = 32
__C.fps = 30


__C.include_own_history = True
__C.own_history_only = True

if __C.process_in_seconds:
    __C.predict_len = 10 #predict the future len
    __C.running_length = 10 #history in seconds
    __C.predict_step = 10 #predict n seconds during testing
else:
    __C.predict_len = 10 #predict the future frames
    __C.running_length = 10
    __C.predict_step = 10

__C.OUTPUT_DIR = './model/'

__C.fix_target_user = False
__C.target_uer_ID = None
__C.use_more_video = True #train on multiple videos except test_video_ind
__C.test_video_ind = None#3#8

__C.add_residual_link = False
__C.has_reconstruct_loss = False
__C.stuff_zero = False
__C.stuff_last = False
__C.change_xyz2xxxyyyzzz = False #the same for fc-lstm



__C.concat_state = False

# __C.LEARNING_RATE = 0.001
__C.LEARNING_RATE = 1e-5
__C.lr_epoch_step = 10
__C.clip_gradient = True
__C.pop_alpha = 0.5
__C.add_xyz_sum1 = False

__C.use_CNN_data_format = False
__C.use_convLSTM_data_format = True
__C.use_decoder = False



__C.shuffle_data = False
__C.stateful_across_batch = False

__C.dropout_rate = 0.3
__C.conv_kernel_size = 5

__C.predict_mean_var = True
__C.sample_and_refeed = True
__C.use_GMM = True #using mixture density output layer


#__C.input_mean_var = False
__C.input_mean_var = True
__C.teacher_forcing = False
__C.use_one_hot = False  
    

__C.predict_eos = False
__C.use_residual_input = True #step difference 
__C.normalize_residual = False
__C.subsample_datadb = False
__C.berrnoulli_loss_weight = 10

__C.use_mixed_dataset = False #Tsinghua+icme_saliency
__C.use_overlapping_chunks = True
if __C.use_overlapping_chunks:
    if __C.process_in_seconds:    
        __C.data_chunk_stride=10  # 1 second
    else:   
        __C.data_chunk_stride=1 # 10 frame
else:
    if __C.process_in_seconds:
        __C.data_chunk_stride=__C.running_length*__C.fps
    else:
        __C.data_chunk_stride=__C.running_length


__C.linear_mode = None # 'presistence'
if __C.linear_mode!=None:
    __C.linear_mode_residual = True


__C.need_split = False
__C.dilation_rate = 1 #for convlstm

__C.use_saliency = False


__C.cut_data_head = False
