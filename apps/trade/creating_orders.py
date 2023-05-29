import random
from pulp import LpProblem, LpMaximize, LpVariable, value, PulpError

from .service import Result


def generate_random_prices(num_orders: int, min_price: float, max_price: float):

    try:
        random_prices = []
        for _ in range(num_orders):
            random_value = random.uniform(min_price, max_price)
            random_prices.append(random_value)

        random_prices.sort(reverse=True)
        return Result.success(status=True, data=random_prices)
    except Exception as e:
        return Result.fail(status=False, message=str(e))


# Using Linear Programming techniques to find the right proportion of value to
# fit the constraints
def generate_orders(prices: list, max_volume: float,
                    amount_dif: float):
    try:
        problem = LpProblem("Linear Programming Problem", LpMaximize)

        num_orders = len(prices)

        # generating coefficients to optimize the linear function
        coefficients = []
        for j in range(num_orders):
            variable = LpVariable(f"order_{j + 1}", lowBound=0)
            coefficients.append(variable)

        problem += sum([prices[i] * coefficients[i] for i in range(num_orders)]) == max_volume

        # adding constraints considering amountDif
        for j in range(1, num_orders):
            problem += prices[0] * coefficients[0] <= amount_dif * j + prices[j] * coefficients[j]

        for j in range(num_orders - 1):
            problem += prices[j] * coefficients[j] <= amount_dif + prices[j + 1] * coefficients[j + 1]

        problem.solve()

        return Result.success(status=True, data=[value(variable) for variable in coefficients])

    except PulpError as e:
        return Result.fail(status=False, message=str(e))