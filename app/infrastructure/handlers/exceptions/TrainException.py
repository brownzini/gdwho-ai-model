class TrainException:
    
    messages_group = {
        "entries": f"[Entries]: must be between 1 and 100 ",
    }

    @classmethod
    def getDefaultMessage(cls, fieldName: str):
        return cls.messages_group[fieldName]