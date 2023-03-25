la <- read.csv("LADataAFter2010.csv", header = TRUE)
head(la)

# plot to show the trend of median housing price in LA over time
plot(x = la$months, y = la$price, xlab = "Number of Months Since January 2010", 
     ylab = "Median Prices of Houses in Los Angeles", main = "Price Over Time for Los Angeles Houses", 
     col = c("red", "darkblue")[as.integer(factor(la$time > 30))],
     cex = 1, pch = 19)
legend(x = -1, y = 9e+05, legend = c("Avg. Time on Market <30 Days", "Avg. Time on Market >30 Days"), 
       pch = 19, col = c("red", "darkblue"), bty = "n")

# transformed data scatterplot to create linear relationship
plot(x = la$months, y = sqrt(la$price), xlab = "Number of Months Since January 2010", 
     ylab = "Square Root of Median Prices of Houses in Los Angeles", 
     main = "Price Over Time for Los Angeles Houses (Transformed)", 
     cex = 1, pch = 19)

# linear model for square root of price vs. time
model_months <- lm(sqrt(price) ~ months, data = la)
summary(model_months)
plot(model_months)

# what the model predicts for our data
price_predictions <- (predict(model_months, data.frame("months" = 1:156)))^2

# plot of the difference between the model's prediction and the actual data
plot(x = 1:156, y = change, cex = 1, pch = 19, 
     ylab = "Difference in Prediction and Actual Median Price", xaxt = "n", 
     col = c("red", "darkblue")[as.integer(factor(abs(change) < 50000))])
legend(x = -5, y = 155000, legend = c(">50000", "<50000"), 
       pch = 19, col = c("red", "darkblue"), bty = "n")

# predicting the median price of LA homes for each month in 2023
predict_2023 <- data.frame("months" = 157:168)
predict(model_months, predict_2023)

