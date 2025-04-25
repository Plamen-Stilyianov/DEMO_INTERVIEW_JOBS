def moving_averages():
    numbers = [1, 2, 3, 7, 9]
    window_size = 3

    i = 0
    moving_avg = []
    while i < len(numbers) - window_size + 1:
        this_window = numbers[i: i + window_size]  # get current window

        window_average = sum(this_window) / window_size
        moving_avg.append(window_average)
        i += 1
    return moving_avg


def pd_moving_average():
    import pandas as pd

    numbers = [1, 2, 3, 7, 9]
    window_size = 3

    numbers_series = pd.Series(numbers)
    windows = numbers_series.rolling(window_size)
    moving_averages = windows.mean()

    moving_averages_list = moving_averages.tolist()
    without_nans = moving_averages_list[window_size - 1:]

    return without_nans


if __name__ == '__main__':
    print(moving_averages())
    print(pd_moving_average())
