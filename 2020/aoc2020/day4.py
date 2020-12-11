import re


def match_date(x, date_min, date_max):
    pattern = re.compile(r'^(\d{4})$')
    match = re.findall(pattern, x)
    if len(match) == 1:
        if (int(x) >= date_min) & (int(x) <= date_max):
            return True
    return False

def match_size(x):
    thresh = {
        'cm': (150, 193),
        'in': (59, 76)
    }
    pattern = re.compile(r'^(\d+)(cm|in)$')
    matches = re.findall(pattern, x)
    if len(matches) == 1:
        size, size_unit = matches[0]
        return (int(size) >= thresh[size_unit][0]) & (int(size) <= thresh[size_unit][1])
    return False


def match_pattern(x, pattern):
    pattern = re.compile(pattern)
    matches = re.findall(pattern, x)
    if len(matches) == 1:
        return True
    return False


REQUIRED_FIELDS = {
    "byr": lambda x: match_date(x, 1920, 2002),
    "iyr": lambda x: match_date(x, 2010, 2020),
    "eyr": lambda x: match_date(x, 2020, 2030),
    "hgt": match_size,
    "hcl": lambda x: match_pattern(x, r'^#([0-9a-f]{6})$'),
    "ecl": lambda x: match_pattern(x, r'^(amb|blu|brn|gry|grn|hzl|oth)$'),
    "pid": lambda x: match_pattern(x, r'^([0-9]{9})$')
}

OPTIONAL_FIELDS = [
    "cid"
]


def _get_passports_with_required_fields(input_path):
    inputs = "".join(open(input_path).readlines())
    passports_str = [t.replace('\n', ' ') for t in inputs.split('\n\n')]
    pattern = re.compile(r'(\w{3}):([\w#]+)')
    invalid_passports = []
    valid_passports = []
    for passport_str in passports_str:
        this_passport = dict(re.findall(pattern, passport_str))
        this_passport_fields = list(this_passport.keys())
        missing_fields = [f for f in REQUIRED_FIELDS if f not in this_passport_fields]
        if len(missing_fields) > 0:
            invalid_passports.append(this_passport)
        else:
            valid_passports.append(this_passport)
    return valid_passports


def run1(input_path):
    return len(_get_passports_with_required_fields(input_path))

def run2(input_path):
    valid_passports = []
    for passport in _get_passports_with_required_fields(input_path):
        valid_fields = 0
        for field, field_rule in REQUIRED_FIELDS.items():
            if field_rule(passport[field]):
                valid_fields += 1
        if valid_fields == len(REQUIRED_FIELDS):
            valid_passports.append(passport)
    return len(valid_passports)



if __name__ == '__main__':
    path = 'inputs/day4.txt'
    print(run1(path))
    print(run2(path))
