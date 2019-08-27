# Convert-h5-to-tflite

This script converts a h5 model to tflite model, which can be used to run on android devices.

STEPS ON HOW TO DO SO:

#1. 
Replace data directory folder path 

    train_data_dir = '/home/garima/Music/dogs-vs-cats/trainnew'
    validation_data_dir = '/home/garima/Music/dogs-vs-cats/testnew'

2.Create your own model or load pre-trained ones.

3. Save the model after training.

4. Call TocoConverter to convert the newly created h5 file, via this command:
   converter = tf.lite.TocoConverter.from_keras_model_file('/home/garima/Music/dogs-vs-cats/models/fromsiraj.h5')

5. Done!
