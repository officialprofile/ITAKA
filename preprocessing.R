library(dplyr)
library(lubridate)

data = read.csv('raw_data.txt', sep = ';', header = F)
colnames(data) = c('Imie i nazwisko', 'Wiek obecny', 'Data zaginiecia', 'Wiek', 'Wzrost', 
                   'Kolor oczu', 'Znaki szczegolne', 'Ostatnie miejsce pobytu', 'Kraj')

data$`Wiek obecny`      <- sapply(data$`Wiek obecny`, function(x) {as.numeric(strsplit(x, ' ')[[1]][2])})
data$Wiek               <- sapply(data$Wiek, function(x) {as.numeric(strsplit(x, ' ')[[1]][2])})
data$Wzrost             <- sapply(data$Wzrost, function(x) {as.numeric(strsplit(x, ' ')[[1]][1])})

data$`Plec`             <- sapply(data$`Imie i nazwisko`, function(x) {ifelse(strsplit(x, ' ')[[1]][1] == 'Zaginiony:', 'M', 'K')})
data$`Nazwisko`         <- sapply(data$`Imie i nazwisko`, function(x) {y = strsplit(x, ' ')[[1]]; y[length(y)]})
data$`Imie`             <- sapply(data$`Imie i nazwisko`, function(x) {strsplit(x, ' ')[[1]][2]})

data$Rok                <- sapply(data$`Data zaginiecia`, function(x) {year(x)})
data$Miesiac            <- sapply(data$`Data zaginiecia`, function(x) {month(x)})
data$Dzien              <- sapply(data$`Data zaginiecia`, function(x) {day(x)})
data$`Dzien tygodnia`   <- sapply(data$`Data zaginiecia`, function(x) {wday(x)})


data <- data[, c('Imie', 'Nazwisko', 'Plec', 'Wiek', 'Wiek obecny', 'Wzrost', 'Kolor oczu', 
                 'Ostatnie miejsce pobytu', 'Kraj', 'Data zaginiecia', 'Rok', 'Miesiac', 
                 'Dzien', 'Dzien tygodnia', 'Znaki szczegolne')]

write.csv(data, 'data.csv', row.names = F)
