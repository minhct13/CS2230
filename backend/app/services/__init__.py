

import torch
import visen
import py_vncorenlp
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
from transformers import RobertaForSequenceClassification, RobertaConfig, AutoTokenizer
from flask import current_app as app



def load_model(path_model, path_config, nClasses):
    config = RobertaConfig.from_pretrained(
        path_config, from_tf=False,
        num_labels=nClasses,
        output_hidden_states=False)
    model = RobertaForSequenceClassification.from_pretrained(
        path_model, config=config)
    return model




class PhoBERT_API:

    def init_model(self, app):
        self.rdrsegmenter = self.load_rdrsegmenter(save_dir=app.config["SEGMENTER_DIR"])
        self.net = load_model(
            path_model=app.config["NETWORK_PATH"], 
            path_config=app.config["NETWORK_CONF_PATH"],
            nClasses=app.config["NUM_CLASS"])
        self.token_encoder = AutoTokenizer.from_pretrained('vinai/phobert-base')
    
    def load_rdrsegmenter(self, save_dir, annotators=["wseg"]):
        return py_vncorenlp.VnCoreNLP(
        annotators=annotators, 
        save_dir=save_dir
        )
    
    def pre_process(self, sent, token_encoder):
        sent = visen.clean_tone(sent)
        sent = self.rdrsegmenter.word_segment(sent)
        sent = ''.join(sent)
        sent = token_encoder.encode(sent)
        test_ids = pad_sequences(
            [sent],
            maxlen=app.config["MAX_LEN"],
            dtype="long", 
            value=0, 
            truncating="post", 
            padding="post"
            )
        mask = [int(token_id > 0) for token_id in test_ids[-1]]
        return test_ids[-1], mask

    def predict(self, sent, device='cpu'):
        input_ids, input_mask = self.pre_process(sent, self.token_encoder)
        with torch.no_grad():
            b_input_ids, b_input_mask = torch.tensor(np.array([input_ids])).to(device), torch.tensor(np.array([input_mask])).to(device)
            outputs = self.net(b_input_ids, token_type_ids=None, attention_mask=b_input_mask)
            logits = outputs[0]
            logits = logits.detach().cpu().numpy()        
            pred = np.argmax(logits, axis=1)[-1]
        return app.config["INT2LABEL"][pred]
    
model = PhoBERT_API()