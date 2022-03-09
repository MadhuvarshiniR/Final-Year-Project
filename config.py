import os
MODEL_CONFIGS = {
    # dataset:[model location,training dataset,testing data]
    "CUSTOM_DATA": [os.getcwd()+"\\"+r"models\custom_model.h5",
                    os.getcwd()+"\\"+r"gestures\custom\train", os.getcwd()+"\\"+r"gestures\custom\test"],

    "ASL": [os.getcwd()+"\\"+r"models\ASL_model.h5",
            os.getcwd()+"\\"+r"gestures\ASL\train", os.getcwd()+"\\"+r"gestures\ASL\train"]
}
