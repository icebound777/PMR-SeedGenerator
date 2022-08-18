class KeyValuePair:
   def __init__(self, key, value) -> None:
      self.key = key
      self.value = value

   def __eq__(self, obj):
      raise Exception(f"Invalid comparison of KeyValuePair was attempted between {self} and {obj}")
      
   def __lt__(self, obj):
      raise Exception(f"Invalid comparison of KeyValuePair was attempted between {self} and {obj}")
      
   def __le__(self, obj):
      raise Exception(f"Invalid comparison of KeyValuePair was attempted between {self} and {obj}")
      
   def __ne__(self, obj):
      raise Exception(f"Invalid comparison of KeyValuePair was attempted between {self} and {obj}")
      
   def __gt__(self, obj):
      raise Exception(f"Invalid comparison of KeyValuePair was attempted between {self} and {obj}")
      
   def __ge__(self, obj):
      raise Exception(f"Invalid comparison of KeyValuePair was attempted between {self} and {obj}")

   def __bool__(self):
      raise Exception(f"Invalid boolean evaluation of KeyValuePair was attempted with {self}")
      
      