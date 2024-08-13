from transformers import AutoModelForCausalLM, AutoTokenizer, logging
import torch
import os



class UseModels:

    def __init__(self):
        logging.set_verbosity_error()
        logging.set_verbosity_error()

    def setMemory(self, size):
        self.memory=[]
        self.MEMORY_SIZE = size
        self.memory.append("Hi I'm Nemo, you can talk with me.")

    def createModelAndTokenizer(self, model_name):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)

        # return self.model, self.tokenizer

    """ Save Model"""
    def saveModel(self, path):
        self.model.save_pretrained(path)

    """Save Tokenizer"""
    def saveTokenizer(self, path):
        self.tokenizer.save_pretrained(path)


    """Get model and tokenizer from saved"""
    def getModelFromSaved(self, str):
        self.model=AutoModelForCausalLM.from_pretrained(str)

    def getTokenizerFromSaved(self, str):
        self.tokenizer=AutoTokenizer.from_pretrained(str)


    """Get Model"""
    def getModel(self,model_name, save_name, path):
        if(os.path.exists(path+ save_name + "-model")):
            return AutoModelForCausalLM.from_pretrained(path + "/" + save_name + "-model")
        else:
            return AutoModelForCausalLM.from_pretrained(model_name)

    """Get Tokenizer"""
    def getTokenizer(self, model_name, save_name, path):
        if (os.path.exists(path + "/" + save_name + "-tokenizer")):
            return AutoTokenizer.from_pretrained(path + "/" + save_name + "-tokenizer")
        else:
            return AutoTokenizer.from_pretrained(model_name)

    def updateMemory(self, convo):
        # add to history
        if (len(self.memory) >= self.MEMORY_SIZE * 2):
            self.memory.pop(0)
            self.memory.pop(0)

        self.memory.append(convo)
        self.memory.append((self.tokenizer.eos_token))

        return "".join(self.memory)


    def inference(self, prompt):

        # add input to memory
        input_withContext = self.updateMemory(prompt)
        # print("memory >> ", input_withContext)

        # tokenize
        prompt_input_ids = self.tokenizer.encode(input_withContext, return_tensors='pt')

        # generate response
        response = self.model.generate(
            prompt_input_ids,
            max_new_tokens=50,
            num_beams=3,
            # pad_token_id= self.tokenizer.eos_token,
            early_stopping=True)

        # decode the response
        output = self.tokenizer.decode(response[0])

        output.split(self.tokenizer.eos_token)
        reply = output.split(self.tokenizer.eos_token)[-2]

        # add output to memory
        # print("memory o>> ", self.updateMemory(reply))

        return reply





