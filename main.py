"""
The main Python mpdule that combines cleaner and metrics functions in order to
perform comprehensive analysis
"""

import matplotlib
from matplotlib.dates import MIN_PER_HOUR
from matplotlib.pylab import median
from metrics import average, maximum, standard_deviation
from cleaner import filter_nondigits

import matplotlib.pyplot as plt
heart_rate = median
time = MIN_PER_HOUR
def run(filename: str) -> None:
    """
    Process heart rate data from the specified file, clean it, calculate metrics,
    and save visualizations.

    Args:
        filename (str): The path to the data file (e.g., 'data/phase0.txt').

    Returns:
        float, float, float: You will return the average, max, and standard deviation
    """ 
    data = []
    time = []

    # open file using file I/O and read it into the `data` list
    with open(filename, 'r') as file:
        for line in file:
         heart_rate = line.strip().split()
         data.append(run(heart_rate))
        if ValueError:
         print("skip{line.strip()}")
        if FileNotFoundError:
         print(f"error:file not found{filename}")
    return None
    d = matplotlib.load(plt)
    print(d)

    # Use `filter_nondigits` to clean the data and remove invalid entries, save the output to a new variable
    cleaned_data = filter_nondigits(data)
    if not cleaned_data:
       print("no data after cleaning")

    # plot this data to explore changes in heart rate for this file, save this visualization to the "images" folder
    plt.figure(figsize=(10,5))
    plt.plot(time, cleaned_data)
    plt.title('heart rate data')
    plt.xlabel('time')
    plt.ylabel('heart rate')
    plt.grid()
    plt.savefig("images/heart_rate_plot.png")
    plt.show()
    plt.close

    # calculate the average, maximum, and standard deviation of this file using the functions you've wrote
    avg_hr = average(cleaned_data)
    max_hr = maximum(cleaned_data)
    std_dev_hr = standard_deviation(cleaned_data)

    # return all 3 values
    return avg_hr, max_hr, std_dev_hr


if __name__ == "__main__":
    print(run("data/phase0.txt"))
if __name__:
   run = __name__
   print (f"average heart rate,{average}")
   print (f"maximum heart rate",{maximum})
   print (f"Standard deviation heart rate",{standard_deviation})
  
