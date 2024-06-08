# filename: plot_stock_gains.py
import matplotlib.pyplot as plt

# Stock gains YTD for NVIDIA and TSLA
stocks = ['NVIDIA', 'TSLA']
ytd_gains = [0.15, 0.25]  # Sample data for demonstration

plt.figure(figsize=(10, 6))
plt.bar(stocks, ytd_gains, color=['blue', 'green'])
plt.xlabel('Stocks')
plt.ylabel('YTD Gain')
plt.title('Stock Gain YTD for NVIDIA and TSLA (2024)')
plt.ylim(0, max(ytd_gains) + 0.1)

plt.savefig('ytd_stock_gains.png')
plt.show()