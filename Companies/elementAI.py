# Iris dataset looks like this:
# sepal length (cm), sepal width (cm), petal length (cm), petal width (cm), class
# e.g. (4.9, 3.1, 1.5, 0.1, Iris-setosa)


# Can you help?
# I was given an assignment to provide some stats on the Iris Dataset.
# The dataset contains measurements of three classes of the Iris flower.
# (More info on Iris dataset: https://archive.ics.uci.edu/ml/datasets/iris)

# However,some errors were introduced in the code while I was away.
# I suspect my cat but this is still to be confirmed!

# ------------------------------ !!WARNING!! -----------------------------
# Luckily, the test harness that I had put in place were NOT touched.
# THE TESTS ARE VALID AND COMPLETE!!! (feel free to add more if necessary)
# ------------------------------ !!WARNING!! -----------------------------

# Can you make sure that:
# 1) the following code runs.
# 2) the tests are passing.
# 3) the code follows a pythonic style (naming, formating) and general software development best practices (TDD, DRY, etc.) - don't hesitate to refactor the code if needed!

from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Text
from urllib.request import urlopen
from collections import defaultdict

IRIS_URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"


def run_tests():
    tests = [
        test_loadIris,
        test_split_line,
        test_count_samples_per_class,
        test_compute_avg,
        test_compute_min,
        test_compute_max,
    ]
    for test in tests:
        test()
    print("All tests are passing!")


def loadIris():
    # loads a dataset from a url and returns its non-empty decoded lines
    response = urlopen(IRIS_URL)
    html = response.read().decode("utf-8").split("\n")
    for i in range(len(html) - 1, 0, -1):
        if html[i]:
            break

    return html[:i + 1]


def test_loadIris():
    assert len(loadIris()) == 150


def split_line(line: Any) -> List[Text]:
    result = line.split(",")
    for i in range(len(result)):
        result[i] = result[i].strip()

    return result


def test_split_line():
    assert split_line("a, b, c, d, , f") == ["a", "b", "c", "d", "", "f"]
    assert split_line("a ,b ,c ,d , ,f") == ["a", "b", "c", "d", "", "f"]
    assert split_line("a,b,c,d,,f") == ["a", "b", "c", "d", "", "f"]


# return the count of each classes
def count_samples_per_class(data: List[Text]) -> Dict[Text, int]:
    c = defaultdict(int)
    for line in data:
        c[split_line(line)[4]] += 1

    return c


def test_count_samples_per_class():
    received = count_samples_per_class(loadIris())
    assert received == {"Iris-virginica": 50, "Iris-versicolor": 50, "Iris-setosa": 50}


# compute_avg
def compute_avg(index: int, target_class_name: Optional[Text], data: List[Text]) -> float:
    values = []
    for line in data:
        class_name = split_line(line)[-1]
        if (target_class_name and target_class_name == class_name) \
                or not target_class_name:
            values.append(float.parse(split_line(line)[index]))
    return round(sum(values) / len(values), 2)


def test_compute_avg():
    assert compute_avg(0, "Iris-setosa", loadIris()) == 5.01
    assert compute_avg(1, "Iris-setosa", loadIris()) == 3.42
    assert compute_avg(2, "Iris-setosa", loadIris()) == 1.46
    assert compute_avg(3, "Iris-setosa", loadIris()) == 0.24

    assert compute_avg(0, "Iris-versicolor", loadIris()) == 5.94
    assert compute_avg(1, "Iris-versicolor", loadIris()) == 2.77
    assert compute_avg(2, "Iris-versicolor", loadIris()) == 4.26
    assert compute_avg(3, "Iris-versicolor", loadIris()) == 1.33

    assert compute_avg(0, "Iris-virginica", loadIris()) == 6.59
    assert compute_avg(1, "Iris-virginica", loadIris()) == 2.97
    assert compute_avg(2, "Iris-virginica", loadIris()) == 5.55
    assert compute_avg(3, "Iris-virginica", loadIris()) == 2.03

    assert compute_avg(0, None, loadIris()) == 5.84
    assert compute_avg(1, None, loadIris()) == 3.05
    assert compute_avg(2, None, loadIris()) == 3.76
    assert compute_avg(3, None, loadIris()) == 1.20


def compute_min(index: int, target_class_name: Optional[Text], data: List[Text]) -> float:
    # compute minimum
    values = []
    for line in data:
        class_name = split_line(line)[-1]
        if (target_class_name and target_class_name == class_name) \
                or not target_class_name:
            values.append(float.parse(split_line(line)[index]))
    return round(min(values), 2)


def test_compute_min():
    assert compute_min(0, "Iris-setosa", loadIris()) == 4.30
    assert compute_min(1, "Iris-setosa", loadIris()) == 2.30
    assert compute_min(2, "Iris-setosa", loadIris()) == 1.00
    assert compute_min(3, "Iris-setosa", loadIris()) == 0.10

    assert compute_min(0, "Iris-versicolor", loadIris()) == 4.90
    assert compute_min(1, "Iris-versicolor", loadIris()) == 2.00
    assert compute_min(2, "Iris-versicolor", loadIris()) == 3.00
    assert compute_min(3, "Iris-versicolor", loadIris()) == 1.00

    assert compute_min(0, "Iris-virginica", loadIris()) == 4.90
    assert compute_min(1, "Iris-virginica", loadIris()) == 2.20
    assert compute_min(2, "Iris-virginica", loadIris()) == 4.50
    assert compute_min(3, "Iris-virginica", loadIris()) == 1.40

    assert compute_min(0, None, loadIris()) == 4.30
    assert compute_min(1, None, loadIris()) == 2.00
    assert compute_min(2, None, loadIris()) == 1.00
    assert compute_min(3, None, loadIris()) == 0.10


# compute MAX
def compute_max(index: int, target_class_name: Optional[Text], data: List[Text]) -> float:
    values = []
    for line in data:
        class_name = split_line(line)[-1]
        if (target_class_name and target_class_name == class_name) \
                or not target_class_name:
            values.append(float.parse(split_line(line)[index]))
    return round(max(values), 2)


def test_compute_max():
    assert compute_max(0, "Iris-setosa", loadIris()) == 5.80
    assert compute_max(1, "Iris-setosa", loadIris()) == 4.40
    assert compute_max(2, "Iris-setosa", loadIris()) == 1.90
    assert compute_max(3, "Iris-setosa", loadIris()) == 0.60

    assert compute_max(0, "Iris-versicolor", loadIris()) == 7.00
    assert compute_max(1, "Iris-versicolor", loadIris()) == 3.40
    assert compute_max(2, "Iris-versicolor", loadIris()) == 5.10
    assert compute_max(3, "Iris-versicolor", loadIris()) == 1.80

    assert compute_max(0, "Iris-virginica", loadIris()) == 7.90
    assert compute_max(1, "Iris-virginica", loadIris()) == 3.80
    assert compute_max(2, "Iris-virginica", loadIris()) == 6.90
    assert compute_max(3, "Iris-virginica", loadIris()) == 2.50

    assert compute_max(0, None, loadIris()) == 7.90
    assert compute_max(1, None, loadIris()) == 4.40
    assert compute_max(2, None, loadIris()) == 6.90
    assert compute_max(3, None, loadIris()) == 2.50


run_tests()