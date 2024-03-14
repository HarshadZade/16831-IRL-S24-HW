import pandas as pd
import matplotlib.pyplot as plt

# Load CSV files
df_means = pd.read_csv("./data/humanoid-mean.csv")  # Mean returns file
df_std_dev = pd.read_csv("./data/humanoid-std-dev.csv")  # Standard deviations file

# Assuming both dataframes are aligned by the iteration number
# If not, you might need to sort or merge them based on a common 'iteration' column

# Input or define the performance of the expert policy and the behavioral cloning agent
EXPERT_PERFORMANCE = float(input("Enter Expert Policy Performance: "))
BC_AGENT_PERFORMANCE = float(input("Enter Behavioral Cloning Agent Performance: "))

# Plotting DAgger iterations vs mean return with error bars for standard deviation
plt.errorbar(
    df_means["Step"],
    df_means["Value"],
    yerr=df_std_dev["Value"],
    fmt="-o",
    label="DAgger Policy",
)

# Add horizontal lines for the expert and behavioral cloning agent's performance
plt.axhline(y=EXPERT_PERFORMANCE, color="r", linestyle="-", label="Expert Policy")
plt.axhline(
    y=BC_AGENT_PERFORMANCE, color="g", linestyle="-", label="Behavioral Cloning Agent"
)

# Adding titles and labels
plt.title("DAgger Iterations vs Policy Mean Return")
plt.xlabel("DAgger Iteration")
plt.ylabel("Policy Mean Return")
plt.legend()

# Show plot
plt.show()
