from app.services import *

def test_usec1():
    services = Services()
    result = services.findsenses('animals')
    for line in result.senses:
        assert (type(line)) == Senses
        assert line.surface == 'animals'
        assert type(line.sense) == int
        assert type(line.definition) == list

def test_usec1many():
    service = Services()
    searches = ['afternoon', 'beauty', 'animals', 'bed', 'diamonds', 'forget', 'inexorable', 'nails', 'radiant', 'sky',
                'toys', 'young']
    results = []
    for search in searches:
        results.append(service.findsenses(search))
    assert len(results) == len(searches) #We are expecting at least some words to return with multiple senses.
    distinctsenses = []
    for result in results:
        for i, line in enumerate(result.senses):
            assert line.surface in searches
            distinctsenses.append((line.sense, line.surface, line.definition))
    assert len(distinctsenses) > len(searches) #We should have more senses than words
    assert distinctsenses[3] == (0, 'beauty', [('gazed', 1), ('entranced', 1), ('cavern', 1), ('creation', 1), ('gathered', 1), ('centre', 1), ('harmony', 1), ('loveliness', 1), ('person', 1), ('ancient', 1), ('strength', 1)])
