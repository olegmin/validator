"""
    Модуль с полезными утилитами
"""


class Company:

    def __init__(self, data):
        self.values = data

    def __getitem__(self, key):
        if key == "":
            return None
        elif "." not in key:
            return self.values[key]
        else:
            items_list = key.split('.')
            return self.recursive_value(self.values, items_list)

    def recursive_value(self, dct, items_list):
        if len(items_list) > 1:
            item = items_list.pop(0)
            return self.recursive_value(dct[item], items_list)
        else:
            return dct[items_list[0]]


class ValidationRules:

    def __init__(self, company):
        self.company = company
        self.global_rules = None

    def validate(self, r):
        self.global_rules = r
        return self.analize_rule('rule_1')

    def analize_rule(self, rule_name):
        rule = self.global_rules[rule_name]
        if self.cond(rule['if']):
            return self.exec(rule['then'])
        else:
            return self.exec(rule['else'])

    def cond(self, options):
        method_name = options.pop('cond')
        return getattr(self, method_name)(options)

    def exec(self, options):
        type = options.pop('type')
        if type == 'rule':
            return self.analize_rule(options['name'])
        else:
            return getattr(self, type)(options)

    def greater_then_on_equal_to(self, options):
        company_value = self.company[options['field']]
        return company_value >= options['value']

    def range(self, options):
        company_value = self.company[options['field']]
        return options['min'] < company_value < options['max']

    def equal(self, options):
        company_value = self.company[options['field']]
        return options['value'] == company_value

    def result(self, options):
        return options