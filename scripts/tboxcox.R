tboxcox <- function(X = X, lambda = seq(-5, 5, 0.1), plot.it = FALSE) {
  X <- X[!is.na(X)]
  
  if (length(X)>=3) {
    CORXY <- c()
    for (i in lambda) {
      if (i == 0) {
        Y <- log(X)
      } else {
        Y <- (X^i - 1) / i
      }
      
      XN <- qqnorm(Y, plot.it = FALSE)
      CORXY <- c(CORXY, cor.test(XN$x,XN$y)$estimate)
    }
    
    bestlambda <- lambda[which.max(CORXY)]
  } else {
    bestlambda <- numeric(0)
    CORXY <- rep(0, length(lambda))
  }
  
  if (length(bestlambda)==0) {
    bestlambda <- 1
    correlacion <- format(max(0, na.rm = TRUE),digits = 3)
  } else {
    correlacion <- format(max(CORXY, na.rm = TRUE), digits = 3)
  }
  
  if (bestlambda == 0) {
    Y <- log(X)
  } else {
    Y <- (X^bestlambda - 1) / bestlambda
  }
  
  
  if (plot.it) {
    
    hist(X, main = "Original Data", col = "red", xlab = "", 
         cex.axis = 0.7, yaxt = "n")
    axis(2, las = 2, cex.axis = 0.7)
    
    plot(lambda,CORXY, type = "l", main = "Box-Cox Normality Plot Y", lwd = 2,
         ylim = c(0,1), xlim = c(min(lambda),max(lambda)),
         xlab = substitute(
           paste(lambda, ": ", bl, "    ",Correlation,": ",mc,sep=""),
           list(bl = bestlambda, mc = correlacion)),
         ylab = "Correlation Coefficient",
         cex.axis = 0.7, yaxt = "n")
    axis(2, las = 2, cex.axis = 0.7)
    abline(v = bestlambda)
    
    
    hist(Y, main = "Transformed Data", 
         col = "green4", 
         xlab = "", 
         cex.axis = 0.7, 
         yaxt = "n")
    axis(2, las = 2, cex.axis = 0.7)
    
    qqx <- qqnorm(X, plot.it = FALSE)
    qqy <- qqnorm(Y, plot.it = FALSE)
    
    qqnorm(Y, cex.axis = 0.7,
           xlim = range(c(qqx$x,qqy$x)),
           ylim = range(c(qqx$y,qqy$y)),                        
           main = "Normal Q-Q Plot", 
           pch = 16,
           col = "green4",
           cex = 1.5, yaxt = "n")
    axis(2, las = 2, cex.axis = 0.7)    
    qqline(Y, col = "green4")    
    points(qqx$x, qqx$y, pch = 16, col = "red", cex = 1.5)
    qqline(X, col = "red")
    
    legend(x = "topleft",
           legend = c("Original Data", "Transformed Data"),
           bty = "n",
           pch = c(16,16),
           col = c("red","green4"),
           cex = 0.8)
  }
  return(list(X = X, 
              Y = Y, 
              bestlambda = bestlambda, 
              lambda = lambda, 
              cor = CORXY))
}
