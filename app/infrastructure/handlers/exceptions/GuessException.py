class GuessException:
    
    messages_group = {
        "input": f"[Input]: must be between 3 and 100 ",
        "data": f"[Data]: must be between 3 and 100 ",
    }

    @classmethod
    def getDefaultMessage(cls, fieldName: str):
        return cls.messages_group[fieldName]