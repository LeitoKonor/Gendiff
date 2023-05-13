EXTRACT_RESULT = {
    'common': {
        'setting1': 'Value 1',
        'setting2': 200,
        'setting3': True,
        'setting6': {
            'key': 'value',
            'doge': {
                'wow': ''
            }
        }
    },
    'group1': {
        'baz': 'bas',
        'foo': 'bar',
        'nest': {
            'key': 'value'
        }
    },
    'group2': {
        'abc': 12345,
        'deep': {
            'id': 45
        }
    }
}

MAKE_DIFF_RESULT = {
    'common': {
        'status': 'changed',
        'value': {
            'setting4': {
                'status': 'added',
                'value': 'blah blah'
            },
            'setting2': {
                'status': 'deleted',
                'value': 200
            },
            'setting3': {
                'status': 'changed',
                'old_value': True,
                'new_value': None
            },
            'setting1': {
                'status': 'unchanged',
                'value': 'Value 1'
            },
            'follow': {
                'status': 'added',
                'value': False
            },
            'setting5': {
                'status': 'added',
                'value': {
                    'key5': 'value5'
                }
            },
            'setting6': {
                'status': 'changed',
                'value': {
                    'key': {
                        'status': 'unchanged',
                        'value': 'value'
                    },
                    'ops': {
                        'status': 'added',
                        'value': 'vops'
                    },
                    'doge': {
                        'status': 'changed',
                        'value': {
                            'wow': {
                                'status': 'changed',
                                'old_value': '',
                                'new_value': 'so much'
                            }
                        }
                    }
                }
            }
        }
    },
    'group1': {
        'status': 'changed',
        'value': {
            'baz': {
                'status': 'changed',
                'old_value': 'bas',
                'new_value': 'bars'
            },
            'foo': {
                'status': 'unchanged',
                'value': 'bar'
            },
            'nest': {
                'status': 'changed',
                'old_value': {
                    'key': 'value'
                },
                'new_value': 'str'
            }
        }
    },
    'group3': {
        'status': 'added',
        'value': {
            'deep': {
                'id': {
                    'number': 45
                }
            },
            'fee': 100500
        }
    },
    'group2': {
        'status': 'deleted',
        'value': {
            'abc': 12345,
            'deep': {
                'id': 45
            }
        }
    }
}
