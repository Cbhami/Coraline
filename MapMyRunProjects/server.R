library(shiny)
library(ggplot2)

# Define server logic required to draw a histogram
shinyServer(
  function(input, output) {
    output$histPlot <- renderPlot({
      # Draw the histogram with the specified bins, input$bins
      ggplot(mtcars, aes(x = ...)) +
        geom_histogram(bins = ...) +  
        labs(x = ...,
             y = ...,
             title = ...
        ) +
        theme(text = element_text(size = 20))
    })
  }
)
