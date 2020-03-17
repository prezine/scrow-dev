import random
from django.core.cache import cache
from config.app_config import ALPHA_NUM, NUMBERS


class Token:
    def gen_token(self, length=6, ext='int'):
        possibilities = self.token_possibility(ext)
        token = ""
        token_length = length

        for i in range(0, token_length):
            math_random = random.random()
            if math_random < 1:
                math_random = random.uniform(0.1, 0.9)
            token += possibilities[round(math_random * len(possibilities))]

        return token.lower()

    @staticmethod
    def token_possibility(ext):
        if ext == 'alphanum':
            return ALPHA_NUM
        return NUMBERS

    def persist_token(self, token, key, lifetime=180):
        if self.retrieve_token(key):
            self.remove_token(key)

        cache.set(f'token.{key}', token, timeout=lifetime)

    @staticmethod
    def retrieve_token(key):
        return cache.get(f'token.{key}')

    def evaluate_token(self, key, eval_data):
        token = self.retrieve_token(key)

        if token == eval_data:
            return True

        return False

    @staticmethod
    def remove_token(key):
        cache.delete(f'token.{key}')


def generate_invite_token():
    token = Token()
    invite_id = token.gen_token(length=80, ext='alphanum')
    return invite_id
