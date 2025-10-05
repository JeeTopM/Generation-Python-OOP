'''
Класс Config
Реализуйте класс Config, который соответствует шаблону синглтон и описывает конфигурационный объект
    с фиксированными параметрами. При создании экземпляра класс не должен принимать никаких аргументов.
При первом вызове класса Config должен создаваться и возвращаться экземпляр этого класса,
    а при последующих вызовах должен возвращаться экземпляр, созданный при первом вызове.
Экземпляр класса Config должен иметь четыре атрибута:
    program_name — атрибут со строковым значением GenerationPy
    environment — атрибут со строковым значением release
    loglevel — атрибут со строковым значением verbose
    version — атрибут со строковым значением 1.0.0
'''


class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
            cls._instance.program_name = 'GenerationPy'
            cls._instance.environment = 'release'
            cls._instance.loglevel = 'verbose'
            cls._instance.version = '1.0.0'
        return cls._instance


# test 1
config = Config()

print(config.program_name)
print(config.environment)
print(config.loglevel)
print(config.version)
'''GenerationPy
release
verbose
1.0.0'''
# test 2
config1 = Config()
config2 = Config()
config3 = Config()

print(config1 is config2)
print(config1 is config3)
'''True
True'''
