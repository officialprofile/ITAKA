library(dplyr)

data = read.csv('raw_data.txt', sep = ';', header = F)
colnames(data) = c('Imie i nazwisko', 'Wiek obecny', 'Data zaginiecia', 'Wiek', 'Wzrost', 
                   'Kolor oczu', 'Znaki szczegolne', 'Ostatnie miejsce pobytu', 'Kraj')

data$`Wiek obecny`      <- sapply(data$`Wiek obecny`, function(x) {as.numeric(strsplit(x, ' ')[[1]][2])})
data$Wiek               <- sapply(data$Wiek, function(x) {as.numeric(strsplit(x, ' ')[[1]][2])})
data$Wzrost             <- sapply(data$Wzrost, function(x) {as.numeric(strsplit(x, ' ')[[1]][1])})
data$`Data zaginiecia`  <- sapply(data$`Data zaginiecia`, function(x) {as.Date(x, fromat = "%Y/%m/%d")})
data$`Plec`             <- sapply(data$`Imie i nazwisko`, function(x) {ifelse(strsplit(x, ' ')[[1]][1] == 'Zaginiony:', 'M', 'K')})
data$`Nazwisko`         <- sapply(data$`Imie i nazwisko`, function(x) {y = strsplit(x, ' ')[[1]]; y[length(y)]})
data$`Imie`             <- sapply(data$`Imie i nazwisko`, function(x) {strsplit(x, ' ')[[1]][2]})
