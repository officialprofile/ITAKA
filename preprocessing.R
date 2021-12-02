library(dplyr)
library(readr)
library(lubridate)

data = read.csv('raw_data.txt', sep = '|', header = F)
colnames(data) = c('name', 'current_age', 'date_of_missing', 'age', 'height', 
                   'eye_color', 'distinctive_signs', 'last_place', 'country')

data$current_age        <- sapply(data$current_age, function(x) {as.numeric(strsplit(x, ' ')[[1]][2])})
data$age                <- sapply(data$age, function(x) {as.numeric(strsplit(x, ' ')[[1]][2])})
data$height             <- sapply(data$height, function(x) {as.numeric(strsplit(x, ' ')[[1]][1])})

data$gender             <- sapply(data$name, function(x) {ifelse(strsplit(x, ' ')[[1]][1] == 'Zaginiony:', 'M', 'F')})
data$last_name          <- sapply(data$name, function(x) {y = strsplit(x, ' ')[[1]]; y[length(y)]})
data$first_name         <- sapply(data$name, function(x) {strsplit(x, ' ')[[1]][2]})

data$year               <- sapply(data$date_of_missing, function(x) {year(x)})
data$month              <- sapply(data$date_of_missing, function(x) {month(x)})
data$day                <- sapply(data$date_of_missing, function(x) {day(x)})
data$week               <- sapply(data$date_of_missing, function(x) {week(x)})
data$day_of_week        <- sapply(data$date_of_missing, function(x) {wday(x)})


data <- data[, c('first_name', 'last_name', 'gender', 'age', 'current_age', 'height', 'eye_color', 
                 'last_place', 'country', 'date_of_missing', 'year', 'month', 'week',
                 'day', 'day_of_week', 'distinctive_signs')]

write.csv(data, 'data.csv', row.names = F, sep = "|")
