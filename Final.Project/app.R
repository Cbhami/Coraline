#
# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#

# UI starter code
url <- "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DV0151EN-SkillsNetwork/labs/module_4/starter_code/ui.R"
download.file(url, destfile = "ui.R")

# Server starter code
url <- "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DV0151EN-SkillsNetwork/labs/module_4/starter_code/server.R"
download.file(url, destfile = "server.R")

# Dataset
url <- "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DV0151EN-SkillsNetwork/labs/module_4/starter_code/adult.csv"
download.file(url, destfile = "adult.csv")

library(shiny)

# Define UI for application that draws a histogram
ui <- fluidPage(
  fluidRow(
    column(width = 4),
    column(width = 8)
  ),
  fluidRow(column(width = 12))
  )

fluidRow(
  column(width = 4,
         wellPanel(
           selectInput(...),
           radioButtons(...))
  ),
  column(width = 8, plotOutput('p1'))
)

df_country <- reactive({
  adult %>% filter(native_country == input$country)
})

    # Application title
titlePanel("Old Faithful Geyser Data"),

    # Sidebar with a slider input for number of bins 
    sidebarLayout(
        sidebarPanel(
            sliderInput("bins",
                        "Number of bins:",
                        min = 1,
                        max = 50,
                        value = 30)
        ),

        # Show a plot of the generated distribution
        mainPanel(
           plotOutput("distPlot")
        )
    )
)

# Define server logic required to draw a histogram
server <- function(input, output) {

    output$distPlot <- renderPlot({
        # generate bins based on input$bins from ui.R
        x    <- faithful[, 2]
        bins <- seq(min(x), max(x), length.out = input$bins + 1)

        # draw the histogram with the specified number of bins
        hist(x, breaks = bins, col = 'darkgray', border = 'white')
    })
}

# Run the application 
shinyApp(ui = ui, server = server)
