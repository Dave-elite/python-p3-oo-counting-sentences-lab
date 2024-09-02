#!/usr/bin/env python3



class MyString:
    def __init__(self, value=''):
        self._value = ''  # Use an internal variable
        self.value = value

    @property
    def value(self):
        return self._value  # Return the internal variable

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value  # Set the internal variable
        else:
            print('The value must be a string.')
            self._value = ''

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        modified_value = self.value.replace('!', '.').replace('?', '.')
        sentences = modified_value.split('.')
        sentences = [s for s in sentences if s.strip()]
        return len(sentences)
