args<-commandArgs(TRUE)  
table <- read.table(args[1], header=T, quote="\"")

jpeg('rplot.jpg')
plot (table$x, table$y)
dev.off()
