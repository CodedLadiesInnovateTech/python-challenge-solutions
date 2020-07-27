import matplotlib.pylot as pylot
import tkinter

# nums = [2, 6, 9, 0, 4, 5]
# bins

def histogram(number, bins):
    for let in nums:
        try:
            nums = list(map(float, nums))
            plt.title("Histogram")
            plt.xlabel("Value")
            plt.ylabel("Frequency")
            plt.show()
            plt.close("all")
        except:
            print("Please input numbers only")

nums = input("Enter numbers: ").split(",")
bins = int(input("Enter bins: "))
histogram(number, bins)